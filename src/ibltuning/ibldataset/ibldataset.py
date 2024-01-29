from .codemodel.branchlinear import branchlinear_model
from .branchdataset import branch_model
from .codemodel.branch_easy import branch_easy_model
from .codemodel.linear import linear_model
from .psuedodata import df_to_string
import json
from datasets import load_dataset, DatasetDict
import os
import random
from tqdm import tqdm
from .lineardataset import linear_dataset
from .branchdataset import branch_dataset

def make_dataset(num_data, mode, num_rows, generated_coefficients):
    dataset = []

    for j in tqdm(range(num_data)):
        if mode == 'mix':
            processing = branchlinear_model()
            str_data = df_to_string(processing, num_rows)
        elif mode == 'linear':
            processing, str_data, generated_coefficients = linear_dataset(num_rows, generated_coefficients)
        elif mode == 'branch':
            #processing = branch_model()
            #str_data = df_to_string(processing, num_rows)
            processing, str_data = branch_dataset(num_rows)
        elif mode == 'branch_easy':
            processing = branch_easy_model()
            str_data = df_to_string(processing, num_rows)
        elif mode == 'all':
            functions = [branchlinear_model, linear_model, branch_model, branch_easy_model]
            selected_function = random.choice(functions)
            processing = selected_function()
            str_data = df_to_string(processing, num_rows)

        data = {}
        data['instruction'] = str_data
        data['output'] = processing
        data['index'] = j
        data['category'] = 'regression'
        dataset.append(data)

    return dataset


def preserve(dataset, path):
    with open(path, 'w', encoding='utf-8') as file:
        for record in dataset:
            json_record = json.dumps(record, ensure_ascii=False)
            file.write(json_record + '\n')
    return


def upload(train_path, test_path, dataset_name):
    train_dataset = load_dataset("json", data_files = train_path)
    test_dataset = load_dataset("json", data_files = test_path)
    dataset_dict = DatasetDict({
        'train': train_dataset['train'],
        'test': test_dataset['train']
        })
    dataset_dict.push_to_hub(f"fuyu-quant/{dataset_name}")
    return


def execution(train_num, test_num, num_rows, mode, dataset_name):
    generated_coefficients = set()
    train_dataset = make_dataset(train_num, mode, num_rows, generated_coefficients)
    test_dataset = make_dataset(test_num, mode, num_rows, generated_coefficients)
    directory = f"../data/{dataset_name}-{mode}"
    os.makedirs(directory, exist_ok=True)
    train_path = f'../data/{dataset_name}-{mode}/train.jsonl'
    test_path = f'../data/{dataset_name}-{mode}/test.jsonl'
    preserve(train_dataset, train_path)
    preserve(test_dataset, test_path)
    #upload(train_path, test_path, f'{dataset_name}-{mode}')
    return
