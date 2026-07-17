import sys
from MazeGenerator import MazeGenerator


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("missing config file")
    else:
        # passing the argument
        mandatory = ["WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"]
        argument = {}
        text_file = sys.argv[1]
        with open(text_file, 'r') as text_file:
            for line in text_file:
                if line.startswith("#") or line.startswith("\n"):
                    pass
                else:
                    data = line.split("=")
                    argument[data[0].strip()] = data[1].strip()
            print(argument)
            for items in mandatory:
                if items not in argument:
                    print(f"CRITICAL ERROR:  missing required_item={items}")
                    sys.exit(1)
            print(f"all required items are in {sys.argv[1]}")
            # check for the argument
            #=================================================#
            if_error = False
            try:
                width = int(argument["WIDTH"])
                height = int(argument["HEIGHT"])
            except ValueError as e:
                if_error = True
                print("width and height must be int values")

            try:
                if argument["PERFECT"] not in ("True", "False"):
                    raise ValueError
                else:
                    if argument["PERFECT"] == "True":
                        is_perfect = True
                    elif argument["PERFECT"] == "False":
                        is_perfect = False
            except ValueError as e:
                if_error = True
                print("PERFECT must be 'True' or 'False'")

            try:
                entry = argument["ENTRY"].split(",")
                exit = argument["EXIT"].split(",")
                entry_x, entry_y = int(entry[0]), int(entry[1])
                exit_x, exit_y = int(exit[0]), int(exit[1])
            except ValueError as e:
                if_error = True
                print("ENTRY and EXIT point must be x,y int values")
            if if_error:
                sys.exit(1)
        #===============================================#
            arr = [["F" for i in range(width)] for j in range(height)]
            arr_string = ""
            for item in arr:
                for hx in item:
                    arr_string += hx
                arr_string += "\n"
        #==============================================#
            with open(f"{argument["OUTPUT_FILE"]}", "w") as output:
                output.write(arr_string + "\n")
                output.write(argument["ENTRY"] + "\n")
                output.write(argument["EXIT"] + "\n")

        
        
        


            