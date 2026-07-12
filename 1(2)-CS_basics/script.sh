#!/bin/bash

# anaconda(또는 miniconda)가 존재하지 않을 경우 설치해주세요!
if ! command -v conda &> /dev/null
then
    echo "[INFO] Miniconda를 설치합니다."
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
    bash miniconda.sh -b -p $HOME/miniconda3
    rm miniconda.sh
    
    export PATH="$HOME/miniconda3/bin:$PATH"
    source "$HOME/miniconda3/etc/profile.d/conda.sh"
    conda init bash
else
    echo "[INFO] 이미 설치되어 있습니다."
    export PATH="$HOME/miniconda3/bin:$PATH"
    export PATH="$HOME/anaconda3/bin:$PATH"
fi

# 환경 활성화 기본 설정 
if [ -f "$HOME/miniconda3/etc/profile.d/conda.sh" ]; then
    source "$HOME/miniconda3/etc/profile.d/conda.sh"
elif [ -f "$HOME/anaconda3/etc/profile.d/conda.sh" ]; then
    source "$HOME/anaconda3/etc/profile.d/conda.sh"
elif command -v conda &> /dev/null; then
    source "$(conda info --base)/etc/profile.d/conda.sh"
fi

# 'myenv' 가상환경이 없으면 생성
if ! conda info --envs | grep -q "myenv"; then
    echo "[INFO] myenv 가상환경을 생성합니다..."
    conda create -n myenv python=3.10 -y
fi

# 가상환경 활성화
echo "[INFO] myenv 가상환경을 활성화합니다..."
conda activate myenv

## 건드리지 마세요! ##
python_env=$(python -c "import sys; print(sys.prefix)")
if [[ "$python_env" == *"/envs/myenv"* ]]; then
    echo "[INFO] 가상환경 활성화: 성공"
else
    echo "[INFO] 가상환경 활성화: 실패"
    exit 1 
fi

# 필요한 패키지 설치
echo "[INFO] mypy 패키지를 설치합니다..."
pip install mypy

# Submission 폴더 파일 실행 위치 보정
if [[ "$PWD" == */submission ]]; then
    cd ..
fi


mkdir -p output

# submission 폴더의 파이썬 파일들을 순회하며 실행
for file in submission/*.py; do
    [ -e "$file" ] || continue
    
    filename=$(basename "$file")
    
    
    pure_num=$(echo "$filename" | grep -oE '[0-9]+' | tail -n 1)
    
    
    if [ -f "input/${pure_num}_input" ]; then
        echo "[INFO] ${filename} 파일 실행 중... (입력: input/${pure_num}_input)"
        python "$file" < "input/${pure_num}_input" > "output/${pure_num}_output"
    fi
done

# mypy 테스트 수행 및 로그 자동 저장
echo "[INFO] mypy 테스트를 수행하고 로그를 저장합니다..."
mypy submission/*.py > mypy_log.txt 2>&1 || true

# 현재 가상환경 정보를 conda.yml 파일로 저장
echo "[INFO] 가상환경 정보를 conda.yml로 내보냅니다..."
conda env export > conda.yml

# 가상환경 비활성화
conda deactivate
