import argparse, re, shutil

# re mappings for replacement
mappings = [
    ('.', '[.]'),
    (':', '[:]'),
    ('http', 'hxxp'),
    ('ftp', 'fxp'),
    ('@', '[AT]')
]

def defang(arg):
    infile = arg
    with open(infile, 'r+') as f:
        # get all file contents
        file = f.read()
        # loop over contents and begin replacing
        for k,v in mappings:
            file = re.sub(re.escape(k), v, file, flags=re.IGNORECASE)
        # set pos to top of file for writing    
        f.seek(0)
        # write replaced
        f.write(file)
        # truncate filesize to prevent bloat
        f.truncate()

    print(f'{infile} has been defanged. The links are safe to share')

def refang(arg):
    infile = arg
    with open(infile, 'r+') as f:
        # get all file contents
        file = f.read()
        # loop over contents and begin replacing
        for k,v in mappings:
            file = re.sub(re.escape(v), k, file, flags=re.IGNORECASE)
        # set pos to top of file for writing    
        f.seek(0)
        # write replaced
        f.write(file)
        # truncate filesize to prevent bloat
        f.truncate()

    print(f'{infile} has been refanged. Exercise caution when handling the links')


# usage: redefang -i [1] -m [2]
# 1 expects an existing file
# 2 expects either defang or refang
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--inputfile', type=argparse.FileType('r'), required=True,
                    help='Input file')
parser.add_argument('-m', '--method', required=True,
                    help='Method: either defang or refang')
args = parser.parse_args()

# make a copy of the file just in case of shenanigans
infile = args.inputfile.name
shutil.copy(infile, f'{infile}-bak.txt')

if args.method == 'defang':
    defang(infile)

elif args.method == 'refang':
    refang(infile)


