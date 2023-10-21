#!/bin/bash


# ==================================================================
# Initial setup
# ------------------------------------------------------------------

    # Set ENV variables
    export APT_INSTALL="apt-get install -y --no-install-recommends"
    export PIP_INSTALL="python -m pip --no-cache-dir install --upgrade"
    export GIT_CLONE="git clone --depth 10"

    # Update apt
    sudo apt update


# ==================================================================
# Tools
# ------------------------------------------------------------------

    DEBIAN_FRONTEND=noninteractive \
    sudo $APT_INSTALL \
        gcc \
        make \
        pkg-config \
        apt-transport-https \
        build-essential \
        apt-utils \
        ca-certificates \
        wget \
        rsync \
        git \
        vim \
        mlocate \
        libssl-dev \
        curl \
        openssh-client \
        unzip \
        unrar \
        zip \
        awscli \
        csvkit \
        emacs \
        joe \
        jq \
        dialog \
        man-db \
        manpages \
        manpages-dev \
        manpages-posix \
        manpages-posix-dev \
        nano \
        iputils-ping \
        sudo \
        ffmpeg \
        libsm6 \
        libxext6 \
        libboost-all-dev

# ==================================================================
# Python
# ------------------------------------------------------------------

    #Based on https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa

    # Adding repository for python3.11
    DEBIAN_FRONTEND=noninteractive \
    sudo $APT_INSTALL software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa -y

    # Installing python3.11
    DEBIAN_FRONTEND=noninteractive sudo $APT_INSTALL \
    python3.11 \
    python3.11-dev \
    python3.11-venv \
    python3-distutils-extra

    # Add symlink so python and python3 commands use same python3.9 executable
    sudo ln -s /usr/bin/python3.11 /usr/local/bin/python3
    sudo ln -s /usr/bin/python3.11 /usr/local/bin/python

    # Installing pip
    curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11
    export PATH=$PATH:/home/paperspace/.local/bin

    python3.11 -m pip install --upgrade pip


# ==================================================================
# Installing CUDA packages (CUDA Toolkit 11.7.1 & CUDNN 8.5.0)
# ------------------------------------------------------------------

    # Based on https://developer.nvidia.com/cuda-toolkit-archive
    # Based on https://developer.nvidia.com/rdp/cudnn-archive

    wget https://developer.download.nvidia.com/compute/cuda/11.7.1/local_installers/cuda_11.7.1_515.65.01_linux.run
    sudo sh cuda_11.7.1_515.65.01_linux.run --silent --toolkit
    export PATH=$PATH:/usr/local/cuda-11.7/bin
    export LD_LIBRARY_PATH=/usr/local/cuda-11.7/lib64
    rm cuda_11.7.1_515.65.01_linux.run

    wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
    sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
    sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub
    sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"
    sudo $APT_INSTALL libcudnn8=8.5.0.*-1+cuda11.7
    sudo $APT_INSTALL libcudnn8-dev=8.5.0.*-1+cuda11.7


# ==================================================================
# PyTorch
# ------------------------------------------------------------------

    # Based on https://pytorch.org/get-started/locally/

    $PIP_INSTALL torch==2.1.0 torchvision==0.13.1 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu116
        

# ==================================================================
# JAX
# ------------------------------------------------------------------

    # Based on https://github.com/google/jax#pip-installation-gpu-cuda

    $PIP_INSTALL "jax[cuda11_cudnn82]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html


# ==================================================================
# TensorFlow
# ------------------------------------------------------------------

    # Based on https://www.tensorflow.org/install/pip

    # export LD_LIBRARY_PATH=${HOME}/anaconda3/lib
    $PIP_INSTALL tensorflow==2.9.2


# ==================================================================
# Hugging Face
# ------------------------------------------------------------------
    
    # Based on https://huggingface.co/docs/transformers/installation
    # Based on https://huggingface.co/docs/datasets/installation

    $PIP_INSTALL transformers==4.34.1 datasets==2.14.5


# ==================================================================
# JupyterLab
# ------------------------------------------------------------------

    # Based on https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html#pip

    $PIP_INSTALL jupyterlab==3.4.6


# ==================================================================
# Additional Python Packages
# ------------------------------------------------------------------

    $PIP_INSTALL \
        numpy==1.23.2 \
        scipy==1.9.1 \
        pandas==1.4.4 \
        cloudpickle==2.1.0 \
        scikit-image==0.19.3 \
        scikit-learn==1.1.2 \
        matplotlib==3.5.3 \
        ipython==8.5.0 \
        ipykernel==6.15.2 \
        ipywidgets==8.0.2 \
        cython==0.29.32 \
        tqdm==4.64.1 \
        gdown==4.5.1 \
        xgboost==1.6.2 \
        pillow==9.2.0 \
        seaborn==0.12.0 \
        sqlalchemy==1.4.40 \
        spacy==3.4.1 \
        nltk==3.7 \
        boto3==1.24.66 \
        tabulate==0.8.10 \
        future==0.18.2 \
        gradient==2.0.6 \
        jsonify==0.5 \
        opencv-python==4.6.0.66 \
        pyyaml==5.4.1 \
        sentence-transformers==2.2.2 \
        wandb==0.13.4


# ==================================================================
# Installing JRE and JDK
# ------------------------------------------------------------------

    sudo $APT_INSTALL default-jre
    sudo $APT_INSTALL default-jdk


# ==================================================================
# CMake
# ------------------------------------------------------------------

    sudo $GIT_CLONE https://github.com/Kitware/CMake ~/cmake
    cd ~/cmake
    sudo ./bootstrap
    sudo make -j"$(nproc)" install


# ==================================================================
# Config & Cleanup
# ------------------------------------------------------------------

    echo "export PATH=${PATH}" >> ~/.bashrc
    echo "export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}" >> ~/.bashrc