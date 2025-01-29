from transformers import pipeline

path = "./local_model"

inputs = [
    "I've been waiting for a HuggingFace course my whole life.",
    "I hate this so much!",
]
classifier = pipeline(task="sentiment-analysis", model=path, device=0)
ouput = classifier(inputs=inputs)
print(ouput)
