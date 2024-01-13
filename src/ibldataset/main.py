from .codemodel import make_processing
from .psuedodata import data_to_string
import json
from datasets import load_dataset, DatasetDict


def make_dataset(num_data):
    dataset = []
    for j in range(num_data):
        processing = make_processing()
        str_data = data_to_string(processing)
        data = {}
        data['instruction'] = str_data
        data['output'] = processing
        data['index'] = j
        data['category'] = 'regression'
        dataset.append(data)

    #dataset = {key: [dic[key] for dic in dataset] for key in dataset[0]}
    #dataset = Dataset.from_dict(dataset)
    return dataset


def preserve_dataset(dataset, path):
    with open(path, 'w', encoding='utf-8') as file:
        for record in dataset:
            json_record = json.dumps(record, ensure_ascii=False)
            file.write(json_record + '\n')
    return


def upload_dataset(train_path, test_path, dataset_name):
    train_dataset = load_dataset("json", data_files = train_path)
    test_dataset = load_dataset("json", data_files = test_path)
    dataset_dict = DatasetDict({
        'train': train_dataset['train'],
        'test': test_dataset['train']
        })
    dataset_dict.push_to_hub(f"fuyu-quant/{dataset_name}")
    return


def download_dataset(data_name):
    dataset = load_dataset(f"fuyu-quant/{data_name}", split='train')
    return dataset
