
# conda 패키지관리자 자체 업데이트
(VirtualEnv) > conda update -n base conda

# 설치된 파이썬 패키지를 모두 최신 버전으로 업데이트
(VirtualEnv) > conda update -all

# 텐서플로 설치 (AVX 지원하지 않는 CPU)
(VirtualEnv) > pip install tensorflow==1.4.0     

# 탠서플로 1.9.0 버전부터는 콘다를 사용하여 텐서플로 설치 권장
(VirtualEnv) > conda install tensorflow
