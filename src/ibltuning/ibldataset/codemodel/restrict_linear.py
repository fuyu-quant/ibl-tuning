import random
import pandas as pd


def _make_processing():
    coef_A = random.randint(1, 30)
    coef_B = random.randint(1, 30)
    coef_C = random.randint(1, 30)
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


def _split_number_into_four(number):
    if number < 40:
        raise ValueError("Number should be at least 40 to ensure each segment is at least 10")

    remaining = number - 40
    points = sorted([random.randint(0, remaining) for _ in range(3)])
    segments = [points[0] + 10, points[1] - points[0] + 10, points[2] - points[1] + 10, remaining - points[2] + 10]
    return segments



def restrict_linear_dataset(num_rows):
    while True:
        processing, coef_A, coef_B, coef_C = _make_processing()
        y_list = random.sample(range(100, 801), 4)
        num_sample =  _split_number_into_four(num_rows)
        all_data = []
        all_data_valid = True
        i = 0
        for total_data in y_list:
            data = _find_data(coef_A, coef_B, coef_C, total=total_data)
            if 1000 < len(data) < 5000:
                sample_data = random.sample(data, num_sample[i])
                all_data = all_data + sample_data
                i += 1
            else:
                all_data_valid = False  # 条件を満たさないデータが見つかった場合
                break

        if all_data_valid:
            random.shuffle(all_data)
            df = pd.DataFrame(all_data, columns=['A', 'B', 'C', 'y'])
            str_df = df.to_string(index=False)
            if len(str_df) <= 3800:
                break
    return processing, str_df, df
