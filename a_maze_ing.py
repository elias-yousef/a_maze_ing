import sys

if len(sys.argv) < 2:
    print("missing config file")
else:
    argument = {}
    text_file = sys.argv[1]
    with open(text_file, 'r') as text_file:
        for line in text_file:
            if line.startswith("#"):
                pass
            else:
                data = line.split("=")
                argument[data[0].strip()] = data[1].strip()
        


            