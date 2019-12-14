"""Institutional Grammar Relations Matrices"""

import argparse
from pathlib import Path
import pandas as pd


def main(args):
    args.output.mkdir(parents=True, exist_ok=True)
    print(args.file)
    df = pd.read_csv(args.file)
    df.aim_category = pd.Categorical(df.aim_category)
    for aim_category in df.aim_category.cat.categories:
        print(aim_category)
        output_file = (args.output / aim_category).with_suffix('.csv')
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
        ).to_csv((args.output / 'all').with_suffix('.csv'), sep='\t')


def console_entry():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=Path)
    parser.add_argument('output', type=Path)
    main(parser.parse_args())


if __name__ == '__main__':
    console_entry()
