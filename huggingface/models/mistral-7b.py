from transformers import pipeline

pipe = pipeline("text-generation", model="mistralai/Mistral-7B-v0.1")

print(pipe("I like to eat pizza because it is"))

