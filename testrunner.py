import argparse
import unittest
import sys


def main(test_path):
    suite = unittest.loader.TestLoader().discover(test_path)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if not result.wasSuccessful():
        sys.exit(result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run unit tests for how-was-your-day python codes.')
    parser.add_argument('--testpath', help='Path to package containing test modules', required=False, default='./tests')
    args = parser.parse_args()
    print('Testing package in {}...'.format(args.testpath))
    main(args.testpath)
