"""
@Author: yanzx
@Time: 2025/9/4 17:56 
@Description: 
"""
import numpy as np

def softmax(logits):
    exp_logits = np.exp(logits)
    return exp_logits / np.sum(exp_logits)


def compute_logprobs(logits):
    # Compute the softmax probabilities
    probabilities = softmax(logits)
    # Compute the log-probabilities
    logprobs = np.log(probabilities)
    return probabilities, logprobs


# 示例模型生成函数
def generate_with_logprobs(model, initial_context, max_length):
    context = initial_context
    generated_tokens = []
    all_logprobs = []

    for _ in range(max_length):
        logits = model.predict_next_token_logits(context)  # 模拟预测logits
        probabilities, logprobs = compute_logprobs(logits)

        # 根据概率采样下一个token
        next_token = np.random.choice(len(logits), p=probabilities)
        generated_tokens.append(next_token)
        all_logprobs.append(logprobs[next_token])

        # 更新上下文
        context.append(next_token)

        # 假设生成结束标识符
        if next_token == model.end_token:
            break

    return generated_tokens, all_logprobs


class DummyModel:
    end_token = -1  # 假设的结束标志

    def predict_next_token_logits(self, context):
        # 返回一个虚拟的 logits 序列
        return np.random.randn(10)  # 假设有10个可能token


# 运行生成过程
model = DummyModel()
initial_context = []
generated_tokens, logprobs = generate_with_logprobs(model, initial_context, max_length=5)

print("Generated tokens: ", generated_tokens)
print("Log-probs: ", logprobs)