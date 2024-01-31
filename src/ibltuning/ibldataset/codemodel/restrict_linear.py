import random
import pandas as pd


def _make_processing():
    coef_A = random.randint(1, 20)
    coef_B = random.randint(1, 20)
    coef_C = random.randint(1, 20)
    processing = f'y = {coef_A}*row["A"] + {coef_B}*row["B"] + {coef_C}*row["C"]'
    return processing, coef_A, coef_B, coef_C

def _find_data(coef_A, coef_B, coef_C, total):
    solutions = []
    for c in range(total // coef_C + 1):
        for b in range((total - coef_C * c) // coef_B + 1):
            # a の値を計算
            a = (total - coef_B * b - coef_C * c) // coef_A

            # a, b, c が方程式を満たすかチェック
            if coef_A * a + coef_B * b + coef_C * c == total:
                solutions.append([a, b, c, total])

    return solutions


def restrict_linear_dataset(num_rows):
    while True:
        processing, coef_A, coef_B, coef_C = _make_processing()
        random_numbers = [random.randint(1000, 2000) for _ in range(4)]
        all_data = []
        data_found = False
        for total_data in random_numbers:
            data = _find_data(coef_A, coef_B, coef_C, total=total_data)
            if 1000 < len(data) < 10000:
                #print(f'data_{total_data}', len(data))
                sampled_data = random.sample(data, num_rows)
                all_data = all_data + sampled_data
                data_found = True
                break
        if data_found:
            break
    random.shuffle(all_data)
    df = pd.DataFrame(data, columns=['A', 'B', 'C', 'y'])
    str_df = df.to_string(index=False)
    return processing, str_df, df
