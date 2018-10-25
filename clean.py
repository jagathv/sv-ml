import sys
import os

keyword = sys.argv[1]
output = sys.argv[2]
os.system('cat ' + keyword + '*tsv > ' output)
os.system('rm ' + keyword + '*')

