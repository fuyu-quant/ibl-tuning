import pandas as pd
import numpy as np
from ..utils.utils import jinja_rendering

def _pseudo_data(num_rows):

    df = pd.DataFrame({
        'A': np.random.randint(0, 31, size=num_rows),
        'B': np.random.randint(0, 31, size=num_rows),
        'C': np.random.randint(0, 31, size=num_rows)
    })
    return df



def df_to_string(processing, num_rows, df=None):
    if df is None:
        df = _pseudo_data(num_rows)
    code_model = jinja_rendering(processing)
    local_vars = {}
    exec(code_model, globals(), local_vars)
    df['y'] = local_vars['predict'](df)
    str_df = df.to_string(index=False)
    return str_df
