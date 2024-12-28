import sys

def open_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
        sys.exit(1)

def find_pattern_in_lines(pattern, lines):
    return [line for line in lines if pattern in line]

def print_matching_lines(matching_lines):
    for line in matching_lines:
        print(line, end='')

def main():
    if len(sys.argv) != 3:
        print("Usage: python grep.py <pattern> <file>")
        sys.exit(1)

    pattern, file_name = sys.argv[1], sys.argv[2]
    
    lines = open_file(file_name)
    matching_lines = find_pattern_in_lines(pattern, lines)
    print_matching_lines(matching_lines)

if __name__ == "__main__":
    main()
