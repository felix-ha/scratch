from transformers import pipeline
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"{device=}")

pipe = pipeline("text-generation", model="mistralai/Mistral-7B-v0.1", device=device)

print(pipe("I like to eat pizza because it is"))

