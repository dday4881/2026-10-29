"""실습 01: 설치된 PyTorch와 CUDA 노출을 확인합니다. GPU가 없어도 CPU로 진행합니다."""
import torch  # PyTorch 라이브러리를 불러옵니다.

# 1. 설치된 PyTorch의 버전을 출력합니다.
print("PyTorch:", torch.__version__)

# 2. PyTorch가 어떤 버전의 CUDA(NVIDIA GPU 가속 도구) 기반으로 빌드되었는지 확인합니다.
print("PyTorch CUDA 빌드:", torch.version.cuda)

# 3. 현재 컴퓨터 환경에서 GPU(CUDA)를 실제로 사용할 수 있는 상태인지 확인합니다. (True/False)
print("CUDA 사용 가능:", torch.cuda.is_available())

# GPU 함수는 사용 가능한 경우에만 호출합니다. 드라이버 번호는 터미널 nvidia-smi에서 별도로 기록합니다.
if torch.cuda.is_available():
    # 사용 가능한 GPU가 있다면, 0번 장치(첫 번째 GPU)의 모델명을 출력합니다.
    print("GPU:", torch.cuda.get_device_name(0))
    
    # 0번 GPU의 전체 메모리(VRAM) 크기를 바이트(Byte) 단위에서 GiB 단위로 변환하고 소수점 둘째 자리까지 반올림하여 출력합니다.
    # (1024**3은 바이트를 기가바이트로 바꾸는 연산입니다.)
    print("VRAM GiB:", round(torch.cuda.get_device_properties(0).total_memory / 1024**3, 2))
else:
    # GPU를 사용할 수 없는 환경(또는 세팅)일 때 출력됩니다.
    print("GPU: 이번 실행에서는 사용하지 않음")

# 현재 연산이 수행되는 기본 장치가 CPU임을 안내합니다.
print("이 단계의 연산 장치: cpu")

# 정상 숫자 1.0, 2.0을 담은 Tensor를 sample에 저장하세요.
# 아래 덧셈 결과가 [2.0, 3.0]이면 계산 환경이 준비된 것입니다.
# >>> B01
# TODO B01: 위 요구사항을 읽고 이 블록을 완성하세요.
# 실수형 데이터 1.0과 2.0을 가지는 PyTorch의 기본 배열 형태인 '텐서(Tensor)' 객체를 생성합니다.
sample = torch.tensor([1.0, 2.0])
# <<< B01

# 생성한 텐서의 모든 요소에 각각 1을 더한 뒤([2.0, 3.0]), 이를 파이썬의 기본 리스트(List) 구조로 변환하여 출력합니다.
print("덧셈:", (sample + 1).tolist())

""" 출력 결과 물
cpu = _conversion_method_template(device=torch.device("cpu"))
PyTorch: 2.14.0+cu130
PyTorch CUDA 빌드: 13.0
CUDA 사용 가능: True
GPU: NVIDIA GeForce RTX 5080 Laptop GPU
VRAM GiB: 15.92
이 단계의 연산 장치: cpu
덧셈: [2.0, 3.0] """