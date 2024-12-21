import sys

def print_shortest_argument():
    print(min(sys.argv[1:], key=len))

if __name__ == "__main__":
    print_shortest_argument()
