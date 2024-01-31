import random
from ..psuedodata import df_to_string


def _make_processing():
    processing = ''
    branch_a = random.randint(10, 20)
    branch_b = random.randint(10, 20)
    branch_c = random.randint(10, 20)
    y_1 = random.randint(1, 30)
    y_2 = random.randint(1, 30)
    y_3 = random.randint(1, 30)
    y_4 = random.randint(1, 30)
    processing += f'if row["A"] < {branch_a}:\n'
    processing += f'    y = {y_1}\n'
    processing += f'elif row["B"] < {branch_b}:\n'
    processing += f'    y = {y_2}\n'
    processing += f'elif row["C"] < {branch_c}:\n'
    processing += f'    y = {y_3}\n'
    processing += 'else:\n'
    processing += f'    y = {y_4}'
    return processing


def branch_dataset(num_rows):
    processing = _make_processing()
    str_data = df_to_string(processing, num_rows)

    return processing, str_data
