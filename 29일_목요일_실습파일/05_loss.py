"""실습 05: 정답 인덱스와 logits로 손실을 계산합니다."""
import torch
from torch import nn

# logits: 모델이 출력한 가공되지 않은 예측값(점수)입니다. 
# 크기는 (2, 2)로, 2개의 데이터 샘플이 있고 각각 2개의 클래스(선택지)에 대한 점수를 가집니다.
logits = torch.tensor([[2.0, 0.0], [0.0, 2.0]])

# target: 각 데이터의 실제 정답 클래스 번호(인덱스)입니다.
# 정수형(torch.long)이어야 하며, 첫 번째 샘플의 정답은 0번 클래스, 두 번째 샘플의 정답은 1번 클래스임을 의미합니다.
target = torch.tensor([0, 1], dtype=torch.long)

# [수정] 손실 함수 객체를 생성할 때는 인자를 넣지 않고 빈 괄호()로 선언합니다.
loss_fn = nn.CrossEntropyLoss()

# loss_fn에 logits와 target을 순서대로 넣어 loss를 계산하세요.
# logits에 softmax를 먼저 적용하지 마세요.
# >>> B05
# TODO B05: 위 요구사항을 읽고 이 블록을 완성하세요.
# 생성된 loss_fn 손실 함수 객체에 모델의 예측값(logits)과 정답(target)을 순서대로 입력하여 최종 손실을 구합니다.
# PyTorch의 CrossEntropyLoss는 내부에서 자동으로 Softmax 연산을 수행하므로, 사용자가 미리 적용하면 안 됩니다.
loss = loss_fn(logits, target)
# <<< B05

# 출력 결과 확인
print("logits:", tuple(logits.shape))                  # 출력: (2, 2)
print("target:", tuple(target.shape), target.dtype)    # 출력: (2,) torch.int64
print("loss:", round(loss.item(), 6))                  # 정답과 예측이 매우 잘 맞아떨어지므로 낮은 손실 값(약 0.126928)이 출력됩니다.

""" 출력 결과 값
cpu = _conversion_method_template(device=torch.device("cpu"))
logits: (2, 2)
target: (2,) torch.int64
loss: 0.126928 """