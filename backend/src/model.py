import torch
from transformers import AutoModel, AutoTokenizer
import numpy as np


tokenizer = AutoTokenizer.from_pretrained('../token')
model = AutoModel.from_pretrained('../model') 


def get_embedding(text):
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        embeddings = model(**inputs).last_hidden_state.mean(dim=1)
    return embeddings.numpy()
