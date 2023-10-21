FROM huggingface/transformers-pytorch-gpu

WORKDIR /app

COPY . . 

ENTRYPOINT [ "python", "main.py" ]
