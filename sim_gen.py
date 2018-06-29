import tools

''' Usage: python simgen.py [SV FILE] [OUTPUT SIM FILE] '''
if __name__ == '__main__':
    sv_file = argv[1]
    output_file = argv[2]
    tools.create_sim(sv_file, output_file)
