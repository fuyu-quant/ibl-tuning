import random
from ..psuedodata import df_to_string

def _make_processing():
    processing = ''

    coef_A = random.randint(1, 30)
    coef_B = random.randint(1, 30)
    coef_C = random.randint(1, 30)
    processing += f'y = {coef_A}*row["A"] + {coef_B}*row["B"] + {coef_C}*row["C"]'

    return processing


def linear_dataset(num_rows):
    processing = _make_processing()
    str_data = df_to_string(processing, num_rows)

    return processing, str_data
