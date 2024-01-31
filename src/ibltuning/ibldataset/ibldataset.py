import json
from datasets import load_dataset, DatasetDict
import os
import random
from tqdm import tqdm
from .codemodel.restrict_linear import restrict_linear_dataset
from .codemodel.restrict_branch import restrict_branch_dataset
from .codemodel.branch import branch_dataset
from .codemodel.linear import linear_dataset

def _make_dataset(num_data, mode, num_rows, generated_coefficients):
    dataset = []

    for j in tqdm(range(num_data)):
        if mode == 'linear':
            processing, str_data = linear_dataset(num_rows)
        elif mode == 'restrict_linear':
            processing, str_data, _ = restrict_linear_dataset(num_rows)
        elif mode == 'branch':
            processing, str_data = branch_dataset(num_rows)
        elif mode == 'restrict_branch':
            processing, str_data,  = restrict_branch_dataset(num_rows, generated_coefficients)


        data = {}
        data['instruction'] = str_data
        data['output'] = processing
        data['index'] = j
        data['category'] = 'regression'
        dataset.append(data)

    return dataset


def _preserve(dataset, path):
    with open(path, 'w', encoding='utf-8') as file:
        for record in dataset:
            json_record = json.dumps(record, ensure_ascii=False)
            file.write(json_record + '\n')
    return


def execution(train_num, test_num, num_rows, mode, dataset_prefix):
    generated_coefficients = set()
    train_dataset = _make_dataset(train_num, mode, num_rows, generated_coefficients)
    test_dataset = _make_dataset(test_num, mode, num_rows, generated_coefficients)
    dataset_name = f'{dataset_prefix}-{mode}'
    directory = f"../data/{dataset_name}"
    os.makedirs(directory, exist_ok=True)
    train_path = f'../data/{dataset_name}/train.jsonl'
    test_path = f'../data/{dataset_name}/test.jsonl'
    _preserve(train_dataset, train_path)
    _preserve(test_dataset, test_path)

    print("train_path:", train_path)
    print("test_path:", test_path)
    print("dataset_name:", dataset_name)
    return train_path, test_path, dataset_name


def upload(train_path, test_path, dataset_name):
    train_dataset = load_dataset("json", data_files = train_path)
    test_dataset = load_dataset("json", data_files = test_path)
    dataset_dict = DatasetDict({
        'train': train_dataset['train'],
        'test': test_dataset['train']
        })
    dataset_dict.push_to_hub(f"fuyu-quant/{dataset_name}")
    return
