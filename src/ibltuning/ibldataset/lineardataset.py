import random
import pandas as pd

#random.seed(123)

def linear_model(generated_coefficients):
    while True:
        coef_A = random.randint(1, 20)
        coef_B = random.randint(1, 20)
        coef_C = random.randint(1, 20)

        if (coef_A, coef_B, coef_C) not in generated_coefficients:
            generated_coefficients.add((coef_A, coef_B, coef_C))
            processing = f'y = {coef_A}*row["A"] + {coef_B}*row["B"] + {coef_C}*row["C"]'
            return processing, coef_A, coef_B, coef_C, generated_coefficients


def find_data(coef_A, coef_B, coef_C, total):
    solutions = []
    for c in range(total // coef_C + 1):
        for b in range((total - coef_C * c) // coef_B + 1):
            # a の値を計算
            a = (total - coef_B * b - coef_C * c) // coef_A

            # a, b, c が方程式を満たすかチェック
            if coef_A * a + coef_B * b + coef_C * c == total:
                solutions.append([a, b, c, total])

    return solutions


def linear_dataset(num_rows, generated_coefficients):
    #processing, coef_A, coef_B, coef_C, generated_coefficients = linear_model(generated_coefficients)
    sample_size = int(num_rows / 2)
    data_1000 = data_1500 = None
    while True:
        processing, coef_A, coef_B, coef_C, generated_coefficients = linear_model(generated_coefficients)
        for total_data in [1000, 1500]:
            data = find_data(coef_A, coef_B, coef_C, total=total_data)
            if len(data) > sample_size:
                sampled_data = random.sample(data, sample_size)

                if total_data == 1000:
                    data_1000 = sampled_data
                elif total_data == 1500:
                    data_1500 = sampled_data
                #print(f'data_{total_data}', len(sampled_data))
        # 両方のデータセットが存在するかチェック
        if data_1000 is not None and data_1500 is not None:
            break
    """
    while True:
        processing, coef_A, coef_B, coef_C, generated_coefficients = linear_model(generated_coefficients)
        data_1000 = find_data(coef_A, coef_B, coef_C, total=1000)
        if len(data_1000) > sample_size:
            data_1000 = random.sample(data_1000, sample_size)
            break

    while True:
        data_1500 = find_data(coef_A, coef_B, coef_C, total=1500)
        if len(data_1500) > sample_size:
            data_1500 = random.sample(data_1500, sample_size)
            break
    """
    #data_1000 = find_data(coef_A, coef_B, coef_C, total=5000)
    #print(coef_A, coef_B, coef_C)
    #print(len(data_1000))
    #data_1000 = random.sample(data_1000, sample_size)
    #data_1500 = find_data(coef_A, coef_B, coef_C, total=6000)
    #data_1500 = random.sample(data_1500, sample_size)
    data = data_1000 + data_1500
    random.shuffle(data)
    df = pd.DataFrame(data, columns=['A', 'B', 'C', 'y'])
    df.to_csv(f'linear_data_{num_rows}.csv', index=False)
    str_df = df.to_string(index=False)
    return processing, str_df, generated_coefficients
