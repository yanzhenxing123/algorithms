import re
import sys
import json
import os


def postprocess_conversation(conversation):
    """后处理对话数据，按时间状态处理，保证输出1->2->1交替"""
    if not conversation:
        return []

    processed = []
    i = 0
    n = len(conversation)

    # 确保数据是成对的
    if n % 2 != 0:
        print("警告: 数据不是成对出现的!")
        return conversation

    # 按时间状态处理（每两行为一个时间状态）
    while i < n:
        # 获取当前时间状态的两个说话者
        turn1 = conversation[i]  # speaker 1
        turn2 = conversation[i + 1]  # speaker 2

        # 检查是否两个都沉默，如果是则跳过整个时间状态
        if (turn1["text"].lower() in ["sil", "<sil>", "<wfzx>"] and
                turn2["text"].lower() in ["sil", "<sil>", "<wfzx>"]):
            i += 2  # 跳过这个时间状态
            continue

        # 检查speaker1是否沉默
        if turn1["text"].lower() in ["sil", "<sil>", "<wfzx>"]:
            # speaker1沉默，收集连续的时间状态中speaker2的说话内容
            speaker2_texts = []
            if turn2["text"].lower() not in ["sil", "<sil>", "<wfzx>"]:
                speaker2_texts.append(turn2["text"])

            j = i + 2
            # 继续查找后续连续的时间状态中speaker1仍然沉默的情况
            while j < n:
                next_turn1 = conversation[j]
                next_turn2 = conversation[j + 1]

                # 如果speaker1仍然沉默，收集speaker2的非沉默内容
                if next_turn1["text"].lower() in ["sil", "<sil>", "<wfzx>"]:
                    if next_turn2["text"].lower() not in ["sil", "<sil>", "<wfzx>"]:
                        speaker2_texts.append(next_turn2["text"])
                    j += 2
                else:
                    break

            # 添加合并后的speaker2内容
            if speaker2_texts:
                processed.append({
                    "speaker": "2",
                    "text": "".join(speaker2_texts)
                })

            i = j  # 跳到下一个需要处理的时间状态

        # 检查speaker2是否沉默
        elif turn2["text"].lower() in ["sil", "<sil>", "<wfzx>"]:
            # speaker2沉默，收集连续的时间状态中speaker1的说话内容
            speaker1_texts = []
            if turn1["text"].lower() not in ["sil", "<sil>", "<wfzx>"]:
                speaker1_texts.append(turn1["text"])

            j = i + 2
            # 继续查找后续连续的时间状态中speaker2仍然沉默的情况
            while j < n:
                next_turn1 = conversation[j]
                next_turn2 = conversation[j + 1]

                # 如果speaker2仍然沉默，收集speaker1的非沉默内容
                if next_turn2["text"].lower() in ["sil", "<sil>", "<wfzx>"]:
                    if next_turn1["text"].lower() not in ["sil", "<sil>", "<wfzx>"]:
                        speaker1_texts.append(next_turn1["text"])
                    j += 2
                else:
                    break

            # 添加合并后的speaker1内容
            if speaker1_texts:
                processed.append({
                    "speaker": "1",
                    "text": "".join(speaker1_texts)
                })

            i = j  # 跳到下一个需要处理的时间状态

        else:
            # 两个说话者都在说话，正常添加
            processed.append(turn1)
            processed.append(turn2)
            i += 2

    return processed


def parse_textgrid_simple(content):
    """简化解析，只提取每个item的第一个intervals内容"""
    lines = content.split('\n')

    result = []
    speaker1_texts = []
    speaker2_texts = []
    current_speaker = None
    in_interval = False
    current_text = None

    for line in lines:
        line = line.strip()

        # 检测item开始
        if 'item [' in line and ']:' in line:
            match = re.search(r'item \[(\d+)\]', line)
            if match:
                current_speaker = match.group(1)

        # 检测intervals开始
        elif 'intervals [' in line and ']:' in line:
            in_interval = True
            current_text = None

        # 提取text
        elif 'text =' in line and in_interval:
            match = re.search(r'text = "(.*)"', line)
            if match:
                text = match.group(1).replace('\\n', '').strip()
                text = text.replace('\\"', '"').strip('"').replace("<anchor_1>", "")
                if text != "<sil>":
                    text = text.replace("<sil>", "")
                current_text = text

                # 将文本按说话人分类存储
                if current_speaker == "1" and current_text:
                    speaker1_texts.append(current_text)
                elif current_speaker == "2" and current_text:
                    speaker2_texts.append(current_text)

                in_interval = False
                current_text = None

    return speaker1_texts, speaker2_texts


def create_alternating_conversation(speaker1_texts, speaker2_texts):
    """创建交替的对话JSON，并检查说话次数是否相等"""
    # 检查说话次数是否相等
    if len(speaker1_texts) != len(speaker2_texts):
        print(f"警告: speaker1说话次数({len(speaker1_texts)})与speaker2说话次数({len(speaker2_texts)})不相等！")
        min_length = min(len(speaker1_texts), len(speaker2_texts))
        speaker1_texts = speaker1_texts[:min_length]
        speaker2_texts = speaker2_texts[:min_length]

    result = []
    for i in range(len(speaker1_texts)):
        # 添加speaker1的文本
        result.append({
            "speaker": "1", "text": speaker1_texts[i]
        })

        # 添加speaker2的文本
        result.append({
            "speaker": "2", "text": speaker2_texts[i]
        })

    return result


def process_textgrid_file_simple(file_path, output_dir):
    """处理TextGrid文件并保存结果到指定目录"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 解析TextGrid文件
        speaker1_texts, speaker2_texts = parse_textgrid_simple(content)

        conversation = create_alternating_conversation(speaker1_texts, speaker2_texts)
        conversation = postprocess_conversation(conversation)
        os.makedirs(output_dir, exist_ok=True)

        # 生成输出文件名
        input_filename = os.path.basename(file_path)
        output_filename = os.path.splitext(input_filename)[0] + '.json'
        output_path = os.path.join(output_dir, output_filename)

        # 保存JSON到文件
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(conversation, f, ensure_ascii=False, indent=4)

        print(f"处理完成: {input_filename}")
        print(f"speaker1说话次数: {len(speaker1_texts)}")
        print(f"speaker2说话次数: {len(speaker2_texts)}")
        print(f"生成的对话轮次: {len(conversation)}")
        print(f"结果已保存到: {output_path}")

        return conversation

    except Exception as e:
        print(f"处理文件时出错: {e}")
        return []


file_path = "./202412-boke-part3-denoise_02.TextGrid"
output_dir = "./output"

result = process_textgrid_file_simple(file_path, output_dir)