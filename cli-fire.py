#!/usr/bin/env python3

import fire
from mylib import logic

if __name__ == "__main__":
    fire.Fire(logic)
# This script uses the Fire library to create a command-line interface for the wiki function.
# You can run this script from the command line to get summaries of Wikipedia pages.
# Example usage: python cli-fire.py --name "Python (programming language)" --length 2
