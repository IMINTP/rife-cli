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
```

## Usage

```
python cli_rife.py
```

# 입력
1. 비디오 파일 경로 입력
* 예: /Users/username/videos/input.mp4

2. Interpolation 배수 입력
* 1: 2배 프레임 생성
* 2: 4배 프레임 생성
* 3: 8배 프레임 생성


# 출력
* 처리된 비디오는 입력 비디오와 같은 디렉토리에 저장됩니다
* 출력 파일명: [원본파일명]_[배수]X_[fps]fps.mp4
* 예시) input.mp4를 2배 보간 처리한 경우: input_2X_60fps.mp4

## Requirements
* Python 3.8 이하
