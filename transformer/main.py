import torch
import torch.nn.functional as F

# Example input: batch size = 1, sequence length = 3, embedding dimension = 4
# This is input data for a single sequence with 3 tokens,
# each represented by a 4-dimensional embedding.
x = torch.rand(1, 3, 4)

W_q = torch.rand(4, 4)
W_k = torch.rand(4, 4)
W_v = torch.rand(4, 4)

Q = torch.matmul(x, W_q)
K = torch.matmul(x, W_k)
V = torch.matmul(x, W_v)

scores = torch.matmul(Q, K.transpose(-2, -1)) / (4 ** 0.5)

attention_weights = F.softmax(scores, dim=-1)

output = torch.matmul(attention_weights, V)

print("Attention Weights:\n", attention_weights)
print("Output Shape:", output.shape)
