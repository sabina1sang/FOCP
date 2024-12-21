import sys

def get_argument_count():
    return len(sys.argv) - 1

def print_argument_count(count):
    print(f"Number of arguments provided: {count}")

def main():
    count = get_argument_count()
    print_argument_count(count)

if __name__ == "__main__":
    main()