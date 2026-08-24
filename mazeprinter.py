RED = "\033[41m"
GREEN = "\033[42m"
YELLOW = "\033[43m"
BLUE = "\033[44m"
RESET = "\033[0m"  # Resets the terminal color back to default

# Print a red square and a blue square
RED = "\033[41m"
def print_one(n :int) -> None:
    if n == 1:
        print(f"{RED}   {RED}   {RED}   {RESET}", end="")
    elif n == 2:
        print(f"{BLUE}   {BLUE}   {BLUE}   {RESET}", end="")
print_one(1)
