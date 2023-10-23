import torch
from  transformers import AutoModel
import tempfile
from pathlib import Path

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

checkpoint = "adept/fuyu-8b"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"{device=}")
model = AutoModel.from_pretrained(checkpoint).to(device)
print_model_stats(model)