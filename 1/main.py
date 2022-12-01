import sys

import pandas as pd


def get_answers(file):
    df = pd.read_table(file, header=None, skip_blank_lines=False, names=['calories'])
    df.calories = df.calories.astype('Int64')
    df['elve'] = df.calories.isna().cumsum() + 1
    df.dropna(inplace=True)
    return {'max_cal': df.groupby('elve').sum().max().item(),
            'top_three': df.groupby('elve').sum().sort_values('calories', ascending=False).head(3).sum().item()}


if __name__ == '__main__':
    fn = sys.argv[1]
    answers = get_answers(fn)
    print(answers)
