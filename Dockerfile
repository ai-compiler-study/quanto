FROM nvcr.io/nvidia/pytorch:24.06-py3

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y libgl1 libglib2.0-0 wget git git-lfs python3-pip python-is-python3 libcairo2-dev pkg-config python3-dev tzdata && \
    rm -rf /var/lib/apt/lists/*

RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.5/zsh-in-docker.sh)" -- \
    -t robbyrussell

# Install dependencies
RUN apt-get install -y build-essential cmake git pkg-config libjpeg-dev \
    libtiff5-dev libpng-dev libavcodec-dev libavformat-dev \
    libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev \
    libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev \
    libatlas-base-dev gfortran ffmpeg libmagickwand-dev

RUN apt install python3-tk libaio-dev -y

RUN pip install -U opencv-python-headless diffusers transformers onnx_graphsurgeon gpustat \
    accelerate ipdb fire seaborn loguru deepspeed timm dynaconf datasets cached_path b2sdk imagesize ujson \
    "torchmetrics[image]" open_clip_torch image-reward openai-clip image-reward deepspeed webdataset wandb \
    omegaconf pytorch-lightning==1.8.3.post0 albumentations==1.3.0 scikit-image clean-fid 

RUN pip install hydra-core --upgrade --pre
RUN pip install optimum-quanto sentencepiece protobuf seaborn matplotlib ftfy "numpy<1.26.4"
