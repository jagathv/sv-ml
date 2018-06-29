import tools
import sys

''' Usage: python simgen.py [SV FILE] [OUTPUT SIM FILE] '''
if __name__ == '__main__':
    sv_file = sys.argv[1]
    output_file = sys.argv[2]
    tools.create_sim(sv_file, output_file)
