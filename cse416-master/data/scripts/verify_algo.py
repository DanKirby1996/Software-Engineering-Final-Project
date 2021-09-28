#!/usr/bin/env python3
#
# Used to verify the files generated by the merge_neighbors_and_pop.py script.
# This looks for records which are missing k/v entries. If a record is missing
# an entry, then it's missing data, and something went wrong with the
# processing.

import sys
import json


if len(sys.argv) != 2:
    print(f"{sys.argv[0]} [algo file to verify]")
    sys.exit(0)

algo_file = sys.argv[1]
data = {}
with open(algo_file, 'r') as f:
    data = json.load(f)

exception_count = 0
for record in data:
    try:
        print(f"{record} -> neighbor list: {data[record]['neighbors']}, population: {data[record]['population']}")
    except Exception:
        print(f"{record} is missing data.")
        exception_count += 1

if exception_count == 0:
    print("Algorithm file verified.")
else:
    print(f"{exception_count} invalid records found.")