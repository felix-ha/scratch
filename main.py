import torch
import logging
logging.basicConfig(level=logging.INFO)
# transformers.logging.set_verbosity_info()

from transformers import AutoTokenizer, AutoModel, AutoModelForSequenceClassification


def run():
    checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
    tokenizer = AutoTokenizer.from_pretrained(checkpoint)

    raw_inputs = [
    "I've been waiting for a HuggingFace course my whole life.",
    "I hate this so much!",
]
    inputs = tokenizer(raw_inputs, padding=True, truncation=True, return_tensors="pt")
    logging.info(f'{inputs}')

    checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
    model = AutoModel.from_pretrained(checkpoint)
    outputs = model(**inputs)
    logging.info('Head of base model')
    logging.info(f'{outputs.last_hidden_state.shape}')


    checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
    model = AutoModelForSequenceClassification.from_pretrained(checkpoint)
    outputs = model(**inputs)
    logging.info('Head for seq classification')
    logging.info(f'{outputs.logits.shape}')
    logging.info(f'{outputs.logits}')

    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    logging.info(f'{predictions}')

    logging.info(f'{model.config.id2label}')


if __name__ == "__main__":
    logging.info(f'{torch.cuda.is_available()=}')
    logging.info(f'{torch.cuda.device_count()=}')
    logging.info(f'{torch.cuda.current_device()=}')
    logging.info(f'{torch.cuda.device(0)=}')
    logging.info(f'{torch.cuda.get_device_name(0)=}')
    run()
    
    