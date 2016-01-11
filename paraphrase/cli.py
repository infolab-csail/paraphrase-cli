import argparse
import sys

from paraphrase import wrapper


def run_test_set(test_file, out_file, model):
    for l in open(test_file):
        text, hypothesis = l.strip().split('\t')
        confidence, entailment = wrapper.query(text, hypothesis, model=model)
        out_file.write('%s\t%s\t%s\t%s\n' % (text, hypothesis, entailment, confidence))


def main():
    parser = argparse.ArgumentParser(
        description='A wrapper to query textual entailment '
        'and paraphrasing systems',
    )

    parser.add_argument(
        "file",
        help="tab-separated file with two sentences in each line",
        metavar="test_file",
    )

    parser.add_argument(
        "-m",
        "--model",
        help="the entailment model",
        metavar="model",
        choices=wrapper.MODELS.keys(),
        default='maxent-all',
    )

    parser.add_argument(
        "-o",
        "--output",
        help="path to output file",
        metavar="out_file",
        default=None,
    )

    args = parser.parse_args()
    out_file = args.output
    if out_file is not None:
        out_file = open(out_file, 'w')
    else:
        out_file = sys.stdout

    run_test_set(args.file, out_file, args.model)


if __name__ == '__main__':
    main()
