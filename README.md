# RIFE CLI Tool

RIFE 비디오 보간(Video Interpolation) 도구를 위한 커맨드 라인 인터페이스입니다.

## Installation

```bash
# Conda 환경 생성
conda create -n RIFE python=3.8
conda activate RIFE

# 필요한 패키지 설치
conda install numpy==1.19.5
conda install pytorch torchvision cpuonly -c pytorch
conda install opencv
conda install -c conda-forge scikit-video
conda install scipy pillow tqdm
conda install lapack
