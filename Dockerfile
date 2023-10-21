FROM huggingface/transformers-pytorch-gpu

WORKDIR /app

COPY . . 

ENTRYPOINT [ "/bin/python3", "main.py" ]
