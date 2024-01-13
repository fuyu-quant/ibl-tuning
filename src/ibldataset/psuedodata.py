import pandas as pd
import numpy as np
from jinja2 import Environment, FileSystemLoader


def jinja_rendering(processing):
    env = Environment(
        loader=FileSystemLoader('/Users/tanakatouma/vscode/ibl-dataset/src/ibldataset')
        )
    template = env.get_template('template.txt')
    data = {'processing': processing}
    code_model = template.render(data)
    return code_model


def pseudo_data(num_rows = 100):

    df = pd.DataFrame({
        'A': np.random.randint(0, 21, size=num_rows),
        'B': np.random.randint(0, 21, size=num_rows),
        'C': np.random.randint(0, 21, size=num_rows)
    })
    return df

def data_to_string(processing):
    code_model = jinja_rendering(processing)
    df = pseudo_data()
    local_vars = {}
    exec(code_model, globals(), local_vars)
    df['y'] = local_vars['predict'](df)
    str_df = df.to_string(index=False)
    return str_df
