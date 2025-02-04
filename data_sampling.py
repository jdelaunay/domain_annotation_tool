import json
from random import sample

if __name__ == "__main__":
    with open("./data/cleaned_data_with_llama_domains.json", "r") as file:
        dataset = [json.loads(line) for line in file]
    sample_ds = sample(dataset, 100)
    print(sample_ds)
    with open("data/sample.json", "w") as outfile:
        json.dump(sample_ds, outfile)
