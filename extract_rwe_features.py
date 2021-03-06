import argparse
from library.utils import Utils
import numpy
import os
import time
import shutil
import sys


def main(arguments=None):
    # Argument parsing
    parser = argparse.ArgumentParser(
        description='Calculates the RWE features from a directory of files.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('MalwareDirectory',
                        help='The directory containing malware to analyze.')
    parser.add_argument('DataDirectory',
                        help='The directory that will contain the data files.')
    parser.add_argument("-w", "--window",
                        help="Window size, in bytes, for running entropy."
                             "", type=int, required=False)
    parser.add_argument("-n", "--nonormalize", action='store_true',
                        help="Disables entropy normalization."
                             "", required=False)
    parser.add_argument("-d", "--datapoints",
                        help="The number of data points to sample running window entropy."
                             "Multiple datapoints can be identified as comma "
                             "separated values without spaces."
                             "", type=str, default='512', required=False)
    parser.add_argument("-j", "--jobs", type=int, default=1,
                        help="The number of jobs to do the work, but be 1 or greater."
                             "", required=False)
    if isinstance(arguments, list):
        args = parser.parse_args(arguments)
    else:
        args = parser.parse_args()

    if args.jobs < 1:
        print("Jobs must be 1 or greater.")
        exit()

    # Normalize setup...
    if args.nonormalize:
        normalize = False
    else:
        normalize = True

    # Find window sizes
    datapoints = None
    if args.datapoints:
        datapoints = args.datapoints.split(',')
        datapoints = [x.strip() for x in datapoints]
        datapoints = [int(x) for x in datapoints]

    # Crawl the directories for malware and calculate rwe
    Utils.extract_rwe_features_from_directory(args.MalwareDirectory,
                                              args.DataDirectory,
                                              window_size=args.window,
                                              normalize=normalize,
                                              number_of_data_points=datapoints,
                                              njobs=args.jobs)


if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)
