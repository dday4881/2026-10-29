"""실습 06: 작은 정상 자료로 학습 순서만 익힙니다. 여기는 train 오차 확인용입니다."""
import torch
from torch import nn

# 일관된 초기 가중치 생성을 위해 시드를 42로 고정합니다.
torch.manual_seed(42)

# X (입력 데이터): 2개의 특징을 가진 8개의 데이터 샘플 (크기: 8x2)
X = torch.tensor([[-2., -1.], [-1., -1.], [-1., 0.], [0., -1.],
                  [1., 0.], [0., 1.], [1., 1.], [2., 1.]])

# y (실제 정답): 각 샘플의 정답 클래스 인덱스 (0 또는 1)
y = torch.tensor([0, 0, 0, 0, 1, 1, 1, 1], dtype=torch.long) 

# 이전 실습 04에서 다뤘던 2 -> 8 -> 2 신경망 모델 구조를 정의합니다.
model = nn.Sequential(nn.Linear(2, 8), nn.ReLU(), nn.Linear(8, 2))

# 분류 문제를 위한 교차 엔트로피 손실 함수를 준비합니다.
loss_fn = nn.CrossEntropyLoss()

# 옵티마이저(최적화 도구): 확률적 경사하강법(SGD)을 사용하며, 학습률(lr)은 0.1로 설정합니다.
# model.parameters()를 전달하여 모델 안의 가중치와 편향들을 관리하게 만듭니다.
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

# 학습을 시작하기 전, 아무것도 모르는 초기 상태 모델의 손실(오차) 값을 확인합니다.
print("학습 전 loss:", round(loss_fn(model(X), y).item(), 6))

# 모델을 '학습 모드'로 전환합니다. (드롭아웃이나 배치 정규화 같은 기법들이 학습용으로 켜집니다.)
model.train()

# ----------------- 딥러닝 핵심 학습 루프 (80번 반복) -----------------
for epoch in range(80):
    # [1단계] 지난 반복(Epoch)에서 계산되었던 기울기(Gradient)들을 0으로 깨끗이 초기화합니다.
    # 초기화하지 않으면 이번 기울기가 지난 기울기와 더해져 엉뚱한 방향으로 학습됩니다.
    optimizer.zero_grad()
    
    # [2단계] 순전파(Forward): 현재 모델에 입력 데이터 X를 넣어 예측값을 구하고 손실 함수로 오차를 계산합니다.
    loss = loss_fn(model(X), y)
    
    # 현재 loss의 gradient를 계산하세요.
    # 파라미터 값은 아직 바뀌지 않으며 .grad에 기울기가 들어갑니다.
    # >>> B06
    # TODO B06: 위 요구사항을 읽고 이 블록을 완성하세요.
    # [3단계] 역전파(Backward): 오차(loss)를 바탕으로 각 가중치들이 얼마나 수정되어야 하는지 기울기(미분값)를 계산합니다.
    loss.backward() 
    # <<< B06
    
    # 현재 gradient를 사용해 파라미터를 한 번 갱신하세요.
    # optimizer의 step 메서드를 호출합니다.
    # >>> B07
    # TODO B07: 위 요구사항을 읽고 이 블록을 완성하세요.
    # [4단계] 가중치 업데이트(Step): [3단계]에서 계산된 기울기와 학습률(0.1)을 바탕으로 모델의 진짜 가중치(파라미터)들을 드디어 한 걸음 수정합니다.
    optimizer.step() 
    # <<< B07

    # 1. zero_grad -> 2. forward -> 3. loss -> 4. backward -> 5. step 순서 잊지 말기!
# ------------------------------------------------------------------

# 모델을 '평가/추론 모드'로 전환합니다.
model.eval()

# 가중치를 업데이트할 필요가 없는 추론 단계이므로 오토그라드(기울기 추적 엔진)를 꺼서 메모리를 아끼고 속도를 높입니다.
with torch.no_grad():
    logits = model(X) # 학습이 완료된 모델로 최종 예측값(원시 점수)을 뽑아냅니다.
    
    # 학습 후 오차가 얼마나 줄어들었는지 확인합니다. (0.473 -> 0.106으로 감소)
    print("학습 후 loss:", round(loss_fn(logits, y).item(), 6))
    
    # .argmax(dim=1)은 2개의 클래스 점수 중 더 높은 점수를 가진 인덱스(0 또는 1)를 선택합니다.
    # 실제 정답 y와 비교하여 맞으면 True(1.0), 틀리면 False(0.0)로 바꾼 후 평균(.mean)을 내어 정확도를 구합니다.
    print("train 정확도:", round((logits.argmax(dim=1) == y).float().mean().item(), 4))

print("주의: 위 정확도는 학습한 8건의 결과이며 새로운 자료의 성능이 아닙니다.")

""" 출력 결과 물
cpu = _conversion_method_template(device=torch.device("cpu"))
학습 전 loss: 0.473224
학습 후 loss: 0.106799
train 정확도: 1.0
주의: 위 정확도는 학습한 8건의 결과이며 새로운 자료의 성능이 아닙니다. """