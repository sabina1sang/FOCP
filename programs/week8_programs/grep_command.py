import sys

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def search_pattern(pattern, lines):
    for line in lines:
        if pattern in line:
            yield line

def print_lines(lines):
    for line in lines:
        print(line, end='')

def main():
    if len(sys.argv) != 3:
        print("Usage: python grep.py <pattern> <filename>")
        sys.exit(1)
    
    pattern = sys.argv[1]
    filename = sys.argv[2]
    
    lines = read_file(filename)
    matching_lines = search_pattern(pattern, lines)
    print_lines(matching_lines)

if __name__ == "__main__":
    main()
