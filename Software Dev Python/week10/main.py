import argparse
import os
from program.autompg import AutoMPGData
from program.custom_logger import my_logger


def my_parser():
    """
    Creates and returns an argument parser for the command-line interface.

    This parser will handle the 'log', 'save', '--year', and '--mpg' arguments.

    Returns:
        argparse.ArgumentParser: The configured argument parser.
    """
    # The parser
    parser = argparse.ArgumentParser(description='AutoMPG Data Processor')

    # Arguments
    # Positional arguments
    parser.add_argument('log', type=str, help='Name of log file my_log.log')
    parser.add_argument('save', type=str, help='Store output in data folder')
    # Optional arguments
    parser.add_argument('-y', '--year', action='store_true',
                        help='Sort data by year')
    parser.add_argument('-m', '--mpg', action='store_true',
                        help='Sort data by mpg')

    return parser


def main():
    """
    Main function to handle the command-line interface and data processing.

    This function parses command-line arguments, sets up logging, creates an instance of AutoMPGData with the specified sorting options, and then saves the sorted data.
    """
    # Parse command-line arguments
    parser = my_parser()
    args = parser.parse_args()

    # Setup logger
    log_path = (os.path.join('program', args.log))
    logger = my_logger(log_path)

    # Create an instance of AutoMPGData
    auto_mpg_data = AutoMPGData(logger, sort_year=args.year,
                                sort_mpg=args.mpg, sort_year_mpg=(args.year and args.mpg))

    # Sort the data
    auto_mpg_data.sort_data()

    # Save the sorted data
    auto_mpg_data.save_data(args.save)

    return


if __name__ == "__main__":
    main()
