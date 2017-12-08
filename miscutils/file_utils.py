import os

# Used to open a data driven file with the following example syntax:
# # Input file with input data and expected data
# input1,expected1
# input2,expected2


def get_datafile_data(target_file):
        with open(target_file, 'r') as inputFile:
            my_list_of_tuples = [tuple(line.rstrip().split(',')) for line in inputFile.readlines()
                                 if not line.startswith("#")]
        return my_list_of_tuples


def get_auto_loc_root():
    current_path = os.getcwd()
    auto_loc = current_path.find("dc_integ_auto")
    return current_path[0:auto_loc]
