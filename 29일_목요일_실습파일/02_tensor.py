"""실습 02: 값뿐 아니라 shape·dtype·device를 같이 확인합니다."""
import torch

# 1. 0차원 텐서 (스칼라, Scalar) 생성
# 하나의 단일 상숫값입니다. 대괄호 없이 숫자만 넣었으므로 차원이 없어 shape가 ()로 출력됩니다.
scalar = torch.tensor(3.0)

# 2. 1차원 텐서 (벡터, Vector) 생성
# 숫자들이 한 줄로 나열된 형태입니다. 데이터가 3개 들어있으므로 1차원 형태인 (3,)으로 출력됩니다.
vector = torch.tensor([1.0, 2.0, 3.0])

# [[1.0, 2.0], [3.0, 4.0]]을 torch.float32의 2차원 Tensor matrix로 만드세요.
# 자료를 CPU로 옮기는 코드는 제공되어 있습니다.
# >>> B02
# 해설 B02: 아래 구현은 위 요구사항을 충족하는 정답 예시입니다.
# 대괄호를 이중([[ ]])으로 사용하여 가로 2개, 세로 2개 세트인 '2차원 행렬(Matrix)'을 생성합니다.
# dtype=torch.float32를 명시하여 32비트 실수형 데이터 타입으로 고정합니다.
matrix = torch.tensor([[1.0, 2.0], [3.0, 4.0]], dtype=torch.float32)
# <<< B02

# .to("cpu") 함수를 사용하여 생성된 행렬 데이터를 확실하게 CPU 연산 장치 메모리로 이동시킵니다.
matrix = matrix.to("cpu")

# 3. 각 텐서의 정보 확인 및 출력
# tuple(tensor.shape): 텐서의 크기/형태를 파이썬의 기본 튜플 형식으로 변환합니다.
# tensor.dtype: 데이터의 종류(예: 32비트 실수형, 64비트 정수형 등)를 나타냅니다.
# tensor.device: 해당 텐서가 현재 어떤 장치(CPU 또는 GPU/CUDA)에 올라가 연산 중인지 보여줍니다.
print("스칼라:", tuple(scalar.shape), scalar.dtype, scalar.device)
print("벡터:", tuple(vector.shape), vector.dtype, vector.device)
print("행렬:", tuple(matrix.shape), matrix.dtype, matrix.device)

# .tolist() 함수를 사용하여 PyTorch 텐서 객체를 파이썬이 다루기 쉬운 기본 중첩 리스트 구조로 변환하여 출력합니다.
print("행렬 값:", matrix.tolist())

""" 출력 결과 값
cpu = _conversion_method_template(device=torch.device("cpu"))
스칼라: () torch.float32 cpu
벡터: (3,) torch.float32 cpu
행렬: (4,) torch.float32 cpu
행렬 값: [1.0, 2.0], 3.0, 4.0] """