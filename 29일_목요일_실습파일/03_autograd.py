# """실습 03: x=3에서 y=x²+2x+1과 기울기를 계산합니다."""
# import torch
# x = torch.tensor(3.0, requires_grad=True)
# # y = x² + 2x + 1을 Tensor 연산으로 작성하세요.
# # x를 Python 숫자로 바꾸지 마세요. 계산 그래프가 이어져 있어야 합니다.
# # >>> B03
# # TODO B03: 위 요구사항을 읽고 이 블록을 완성하세요.
# y = x + 0
# # <<< B03
# # backward는 y 값을 바꾸지 않고 x.grad에 기울기를 계산합니다.
# y.backward()
# print("y:", y.item())
# print("dy/dx:", x.grad.item())


"""실습 03: x=3에서 y=x²+2x+1과 기울기를 계산합니다."""
import torch

# x = 3.0 이라는 값을 가진 텐서를 생성합니다.
# requires_grad=True는 이 변수(x)를 바탕으로 계산된 식들의 미분값(기울기)을 자동으로 추적하겠다는 의미입니다.
x = torch.tensor(3.0, requires_grad=True)

# y = x² + 2x + 1을 Tensor 연산으로 작성하세요.
# x를 Python 숫자로 바꾸지 마세요. 계산 그래프가 이어져 있어야 합니다.
# >>> B03
# TODO B03: 위 요구사항을 읽고 이 블록을 완성하세요.
# x**2는 x의 제곱을 의미하며, PyTorch의 연산 그래프를 유지하면서 수식을 완성합니다.
y = x**2 + 2*x + 1
# <<< B03

# backward() 함수는 y에서 출발하여 x까지 거꾸로 거슬러 올라가며 미분(오차역전파)을 수행합니다.
# 이 연산을 거치면 x.grad 변수에 dy/dx(기울기) 값이 자동으로 저장됩니다.
y.backward()

# [오류 해결] x.grad는 함수가 아니라 '텐서 변수'이므로 소괄호()를 붙이면 안 됩니다.
# x.grad에 저장된 미분값 텐서를 확인하는 올바른 문법입니다.
x.grad  

# .item()은 텐서 안에 들어있는 단 하나의 숫자를 파이썬의 일반 숫자(Float) 타입으로 꺼내오는 함수입니다.
print("y:", y.item())          # x=3 일 때 y = 3² + 2(3) + 1 = 16.0 출력
print("dy/dx:", x.grad.item()) # y를 x로 미분하면 2x + 2 이므로, x=3 일 때 기울기인 8.0 출력

"""출력 결과 값 
cpu = _conversion_method_template(device=torch.device("cpu"))
y: 16.0
dy/dx: 8.0 """