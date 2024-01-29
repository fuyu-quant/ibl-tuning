import random
import pandas as pd
from ..utils.utils import jinja_rendering

def make_if_statement(processing):
    feature_list = ['A', 'B', 'C']
    select_feature1 = random.choice(feature_list)
    if_figure = random.randint(50, )
    processing += f'if row["{select_feature1}"] < {if_figure}:\n'
    processing += '    y = 1000\n'
    return processing


def make_else_statement(processing):
    processing += 'else:\n'
    processing += '    y = 1500\n'
    return processing


def branch_model():
    processing = ''
    processing = make_if_statement(processing)
    processing = make_else_statement(processing)
    return processing


def branch_dataset(num_rows):
    processing = branch_model()
    code_model = jinja_rendering(processing)
    df = pd.read_csv(f'./data/linear_data_{num_rows}.csv')
    df = df.drop('y', axis=1)
    local_vars = {}
    exec(code_model, globals(), local_vars)
    df['y'] = local_vars['predict'](df)
    str_df = df.to_string(index=False)
    return processing, str_df
