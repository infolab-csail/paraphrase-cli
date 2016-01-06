import argparse


def main(args):
    parser = argparse.ArgumentParser(
        description='A wrapper to query textual entailment '
        'and paraphrasing systems',
    )

    args = parser.parse_args()

if __name__ == '__main__':
    main()
