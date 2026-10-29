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

'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

T = int(input())  # 채점 로봇이 주는 전체 문제 개수(예: 3 또는 8)를 받아 저장합니다.

# T(8)부터 시작해서, -1 미만(즉 0)까지, -1씩 줄어들면서 반복해라!
for test_case in range(T, -1, -1): # 1번부터 T번까지 차례대로 돌리는 표준 형태입니다.
    # ---------------------------------------------
    # 3단계: 이 안쪽에 '한 개의 문제를 푸는 로직'을 작성합니다.
    # ---------------------------------------------
    # 예시 구조 (반복문 안쪽)
    # 정답을 계산하는 코드들을 여기에 구현하신 뒤...
    
    print(test_case, end = " ")


# 1. 숫자를 3개 넣을 때: range(시작, 끝, 규칙)
# • 첫 번째 -1 (끝 번호): "-1 직전(즉, 0)까지만 가라!" [1]
# • 두 번째 -1 (규칙/증감): "1씩 줄어들면서 가라!" [1]
# • 결과: 8부터 시작해서 1씩 줄어들며 0까지 잘 내려갑니다. (8 7 6 ... 0) [1]


# 2. 호기심에 1개를 지워서 숫자를 2개만 넣었을 때: range(시작, 끝)

# 여기서 맨 뒤의 -1을 지우면 숫자가 2개(T, -1)가 되죠? 그러면 컴퓨터는 마지막 숫자를 '규칙'이 아니라 '끝 번호'로 생각하고, '규칙'은 자동으로 +1(1씩 더하기)로 정해버립니다. [1]
# • 즉, range(8, -1)은 "8부터 시작해서 -1 직전까지 가는데, 1씩 더하면서 가라!"라는 뜻이 됩니다. [1]
# • 컴퓨터의 멘붕: '아니, 8에서 숫자를 더해가며 커져야 하는데 어떻게 -1로 가라는 거지?' [1]
# • 결과: 컴퓨터가 시작하자마자 갈 수 없다고 판단해서 아무 숫자도 꺼내지 않고 반복문을 끝내버린 것입니다. [1]
