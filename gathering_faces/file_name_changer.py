import sys
import os
import sys

source = sys.argv[1]
rule = sys.argv[2]

for file_name in os.listdir(source):
    original_name = source + '/' + file_name
    new_name = source + '/' + rule + file_name
    os.rename (original_name, new_name)
