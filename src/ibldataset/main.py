from .codemodel import make_processing
from .psuedodata import data_to_string
from datasets import Dataset, DatasetDict


def make_dataset():
    dataset = []
    for j in range(3000):
        processing = make_processing()
        str_data = data_to_string(processing)
        data = {}
        data['instruction'] = str_data
        data['output'] = processing
        data['index'] = j
        data['category'] = 'regression'
        dataset.append(data)

    dataset = {key: [dic[key] for dic in dataset] for key in dataset[0]}
    dataset = Dataset.from_dict(dataset)
    return dataset


def make_dataset_dict():
    train_dataset = make_dataset()
    test_dataset = make_dataset()

    dataset_dict = DatasetDict({
        'train': train_dataset,
        'test': test_dataset
    })
    return dataset_dict
