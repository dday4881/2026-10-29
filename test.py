# import torch

# print("PyTorch:", torch.__version__)
# print("빌드 CUDA:", torch.version.cuda)
# print("CUDA 사용 가능:", torch.cuda.is_available())

# if torch.cuda.is_available():
# print("GPU:", torch.cuda.get_device_name(0))
# props = torch.cuda.get_device_properties(0)
# print("VRAM(GB):", round(props.total_memory / 1024**3, 1))

# import torch
# x = torch.tensor([[1.0, 2.0],
# [3.0, 4.0]],
# dtype=torch.float32)
# y = torch.tensor([0, 1], dtype=torch.long)
# print(x)
# print(x.shape, x.dtype, x.device)
# print(y.shape, y.dtype)

# import torch
# a = torch.randn(2, 3)
# b = torch.zeros(2, 3)
# c = torch.ones(2, 3, dtype=torch.float32)
# print(a.shape)
# print(b.sum().item())
# print(c.mean().item())

# import torch
# from torch import nn
# device = torch.device(
# "cuda" if torch.cuda.is_available() else "cpu"
# )
# X = torch.randn(4, 2).to(device)
# model = nn.Linear(2, 1).to(device)
# output = model(X)
# print(device)
# print(X.device, output.device)

# # model.to(device)
# # Tensor.to(device)
# # 모델과입력이같은장치여야한다.
# # .to()는 원본과 다른 Tensor를 반환할 수
# # 있으므로결과를다시변수에저장한다