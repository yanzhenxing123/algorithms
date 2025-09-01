import re
import sys
import json
import os
from typing import List, Dict, Tuple


def parse_textgrid_ultimate(content: str) -> Tuple[List[str], List[str]]:
    """
    终极版本的TextGrid解析
    只提取每个item的第一个intervals内容
    """
    lines = content.split('\n')

    speaker1_texts = []
    speaker2_texts = []
    current_speaker = None
    in_interval = False
    current_text = None

    def clean_text(text: str) -> str:
        """清理文本内容"""
        if not text:
            return ""
        
        # 移除转义字符和特殊标记
        text = text.replace('\\n', '').replace('\\"', '"').strip('"')
        text = text.replace("<anchor_1>", "").replace("<wfzx>", "")
        
        # 如果整个文本就是沉默标记，则返回沉默标记
        if text.lower() in ["<sil>", "<wfzx>"]:
            return text.lower()
        
        # 移除文本中的沉默标记
        text = text.replace("<sil>", "").replace("<wfzx>", "")
        
        return text.strip()

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
                text = clean_text(match.group(1))
                
                # 将文本按说话人分类存储
                if current_speaker == "1":
                    speaker1_texts.append(text)
                elif current_speaker == "2":
                    speaker2_texts.append(text)

                in_interval = False
                current_text = None

    return speaker1_texts, speaker2_texts


def create_alternating_conversation_ultimate(speaker1_texts: List[str], speaker2_texts: List[str]) -> List[Dict]:
    """
    创建交替的对话JSON，并检查说话次数是否相等
    """
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
            "speaker": "1", 
            "text": speaker1_texts[i]
        })

        # 添加speaker2的文本
        result.append({
            "speaker": "2", 
            "text": speaker2_texts[i]
        })

    return result


def postprocess_conversation_ultimate(conversation: List[Dict]) -> List[Dict]:
    """
    终极版本的后处理对话数据，确保严格的1->2->1交替格式
    """
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
            # 两个说话者都在说话，需要特殊处理
            # 这里我们需要确保交替格式，所以只能选择一个说话者
            # 根据当前processed列表的最后一个说话者来决定
            
            if not processed:
                # 第一个轮次，选择有内容的说话者
                if turn1["text"] and not turn2["text"]:
                    processed.append({
                        "speaker": "1",
                        "text": turn1["text"]
                    })
                elif turn2["text"] and not turn1["text"]:
                    processed.append({
                        "speaker": "2",
                        "text": turn2["text"]
                    })
                elif turn1["text"] and turn2["text"]:
                    # 两个都有内容，先添加speaker1
                    processed.append({
                        "speaker": "1",
                        "text": turn1["text"]
                    })
            else:
                # 根据上一个说话者来决定
                last_speaker = processed[-1]["speaker"]
                if last_speaker == "1":
                    # 上一个说话者是1，这次应该是2
                    if turn2["text"]:
                        processed.append({
                            "speaker": "2",
                            "text": turn2["text"]
                        })
                else:
                    # 上一个说话者是2，这次应该是1
                    if turn1["text"]:
                        processed.append({
                            "speaker": "1",
                            "text": turn1["text"]
                        })
            
            i += 2

    return processed


def process_textgrid_file_ultimate(file_path: str, output_dir: str) -> List[Dict]:
    """
    终极版本的TextGrid文件处理
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"文件不存在: {file_path}")
        
        print(f"开始处理文件: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 解析TextGrid文件
        speaker1_texts, speaker2_texts = parse_textgrid_ultimate(content)

        # 创建交替对话
        conversation = create_alternating_conversation_ultimate(speaker1_texts, speaker2_texts)
        
        # 后处理
        conversation = postprocess_conversation_ultimate(conversation)
        
        # 创建输出目录
        os.makedirs(output_dir, exist_ok=True)

        # 生成输出文件名
        input_filename = os.path.basename(file_path)
        output_filename = os.path.splitext(input_filename)[0] + '_ultimate.json'
        output_path = os.path.join(output_dir, output_filename)

        # 保存JSON到文件
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(conversation, f, ensure_ascii=False, indent=4)

        print(f"处理完成: {input_filename}")
        print(f"speaker1说话次数: {len(speaker1_texts)}")
        print(f"speaker2说话次数: {len(speaker2_texts)}")
        print(f"生成的对话轮次: {len(conversation)}")
        print(f"结果已保存到: {output_path}")

        # 验证交替格式
        validate_alternating_format_ultimate(conversation)

        return conversation

    except Exception as e:
        print(f"处理文件时出错: {e}")
        return []


def validate_alternating_format_ultimate(conversation: List[Dict]):
    """验证对话格式是否为交替的"""
    if not conversation:
        return
    
    print("\n=== 格式验证 ===")
    print("前10个对话轮次:")
    
    for i, turn in enumerate(conversation[:10]):
        print(f"{i+1:2d}. Speaker{turn['speaker']}: {turn['text'][:50]}...")
    
    # 检查交替性
    errors = []
    for i in range(1, len(conversation)):
        if conversation[i]["speaker"] == conversation[i-1]["speaker"]:
            errors.append(f"位置{i}: 连续两个Speaker{conversation[i]['speaker']}")
    
    if errors:
        print(f"\n⚠️  发现{len(errors)}个格式错误:")
        for error in errors[:5]:  # 只显示前5个错误
            print(f"   {error}")
    else:
        print(f"\n✅ 格式正确: 所有{len(conversation)}个轮次都是交替的")


def main():
    """主函数"""
    file_path = "./202412-boke-part3-denoise_02.TextGrid"
    output_dir = "./output"
    
    result = process_textgrid_file_ultimate(file_path, output_dir)
    
    if result:
        print(f"\n✅ 处理成功！生成了{len(result)}个对话轮次")
    else:
        print("❌ 处理失败")


if __name__ == "__main__":
    main()
