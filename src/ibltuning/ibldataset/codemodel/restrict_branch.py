import random
import pandas as pd
from .restrict_linear import restrict_linear_dataset
from ..psuedodata import df_to_string


def _make_processing(y_list):
    processing = ''
    branch_a = random.randint(20, 50)
    branch_b = random.randint(20, 50)
    branch_c = random.randint(20, 50)
    processing += f'if row["A"] < {branch_a}:\n'
    processing += f'    y = {y_list[0]}\n'
    processing += f'elif row["B"] < {branch_b}:\n'
    processing += f'    y = {y_list[1]}\n'
    processing += f'elif row["C"] < {branch_c}:\n'
    processing += f'    y = {y_list[2]}\n'
    processing += 'else:\n'
    processing += f'    y = {y_list[3]}'
    return processing


def restrict_branch_dataset(num_rows):
    _, _, df = restrict_linear_dataset(num_rows)
    y_list = list(set(df['y'].values))
    processing = _make_processing(y_list)
    str_df = df_to_string(processing, num_rows, df=df)
    return processing, str_df


