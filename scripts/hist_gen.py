import tools
import sys

if __name__ == '__main__':
    input_file, output_file, reference, type = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    tools.create_hist(input_file, output_file, ref_dict, type)
    
