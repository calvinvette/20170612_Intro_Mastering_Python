#/usr/bin/env python3
import os
import sys
import signal
import argparse

parser = argparse.ArgumentParser(description="Unix-like kill program")
parser.add_argument(
    '-KILL',
    dest='pid'
)
parser.add_argument(
    '-HUP',
    dest='pid'
)
parser.add_argument(
    '-USR1',
    dest='pid'
)
parser.add_argument(
    '-USR2',
    dest='pid'
)
args = parser.parse_args()
print(args.pid)
sys.exit()
os.kill(sys.argv[1], signal.SIGINT)
# end script