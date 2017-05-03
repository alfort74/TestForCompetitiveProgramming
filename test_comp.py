# -*- coding:utf-8 -*-
import sys
import os
import time
import tempfile

def measure_elapse_time(script_file, input_file):
    with open(file_name, 'r') as script_code, open(input_file, 'r') as f:
        sys.stdin = f
        start_time = time.time()
        exec(script_code)
        elapsed_time = time.time() - start_time
        print elapsed_time


def make_virtual_file(fd):
    while True:
        input = raw_input()
        if input == "":
            break
        os.write(fd, input+"\n")


if __name__ == '__main__':

    if len(sys.argv) <= 1:
        print "usage: {script_name} foo_program.py [sample_input.txt]".format(script_name=sys.argv[0])
        sys.exit(0)
    file_name = sys.argv[1]

    if len(sys.argv) <= 2:
        fd, filename = tempfile.mkstemp()
        try:
            make_virtual_file(fd)
            measure_elapse_time(file_name, filename)
            os.close(fd)
        finally:
            os.remove(filename)
    else:
        input_file = sys.argv[2]
        measure_elapse_time(file_name, input_file)

