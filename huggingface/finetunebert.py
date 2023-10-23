from pathlib import Path
import tempfile
from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModel,
    AutoModelForSequenceClassification,
    DataCollatorWithPadding,
    Trainer,
    TrainingArguments
    )
import torch

def compute_size(model):
    state_dict = model.state_dict()
    with tempfile.TemporaryDirectory() as tempdir:
        tmp_path = Path(tempdir).joinpath("model.pt")
        torch.save(state_dict, tmp_path)
        size_mb = tmp_path.stat().st_size / (1024 * 1024)
    return size_mb

def print_model_stats(model):
    print(
        f"{model.__class__.__name__} has {sum(p.numel() for p in model.parameters() if p.requires_grad):,} parameters"
    )
    print(f'{compute_size(model)=}')

checkpoint = "distilbert-base-uncased"

emotions = load_dataset("dair-ai/emotion")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"{device=}")




print(emotions['train'].features)


print(emotions["train"][0:10])

tokenizer = AutoTokenizer.from_pretrained(checkpoint)

def tokenize(batch):
  return tokenizer(batch["text"], padding=True, truncation=True)

print(tokenize(emotions["train"][:2]))

emotions_encoded = emotions.map(tokenize, batched=True, batch_size=None)

emotions_encoded

"""Vanilla Model head"""

model = AutoModel.from_pretrained(checkpoint).to(device)

print_model_stats(model)

raw_inputs = [
    "Hi this is a test",
    "This too",
]

inputs = tokenizer(raw_inputs, padding=True, truncation=True, return_tensors="pt")

inputs = {k:v.to(device) for k,v in inputs.items()}
with torch.no_grad():
  outputs = model(**inputs)

print(outputs.last_hidden_state.shape)

"""Training Classification Head"""

num_labels = 6
model = (AutoModelForSequenceClassification.from_pretrained(checkpoint, num_labels=num_labels).to(device))

with torch.no_grad():
  outputs = model(**inputs)

print(outputs.logits.shape)
print(outputs)

"""Training"""

from sklearn.metrics import accuracy_score, f1_score
def compute_metrics(pred):
  labels = pred.label_ids
  preds = pred.predictions.argmax(-1)
  f1 = f1_score(labels, preds, average="weighted")
  acc = accuracy_score(labels, preds)
  return {"accuracy": acc, "f1": f1}

batch_size = 64
logging_steps = len(emotions_encoded["train"]) // batch_size
model_name = f"{checkpoint}-finetuned-emotion"
training_args = TrainingArguments(output_dir=model_name,
        num_train_epochs=2,
        learning_rate=2e-5,
        per_device_train_batch_size=batch_size,
        per_device_eval_batch_size=batch_size,
        weight_decay=0.01,
        evaluation_strategy="epoch",
        disable_tqdm=False,
        logging_steps=logging_steps,
        log_level="error")

trainer = Trainer(model=model, args=training_args,
    compute_metrics=compute_metrics,
    train_dataset=emotions_encoded["train"],
    eval_dataset=emotions_encoded["validation"],
    tokenizer=tokenizer)

trainer.train()

preds_output = trainer.predict(emotions_encoded["validation"])
preds_output.metrics

