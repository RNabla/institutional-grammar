"""Institutional Grammar Relations Matrices"""

import argparse
from pathlib import Path
import pandas as pd


def main(input_file, output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(input_file)
    df.aim_category = pd.Categorical(df.aim_category)
    for aim_category in df.aim_category.cat.categories:
        output_file = (output_dir / aim_category).with_suffix('.csv')
        df[df.aim_category == aim_category].pivot_table(
            index='active_actor',
            columns='passive_actor',
            values='aim',
            aggfunc=set
        ).to_csv(output_file, sep='\t')
        df.pivot_table(
            index='active_actor',
            columns='passive_actor',
            values='aim',
            aggfunc=set
        ).to_csv((output_dir / 'all').with_suffix('.csv'), sep='\t')


def console_entry():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    main(args.file, args.output)


if __name__ == '__main__':
    console_entry()
