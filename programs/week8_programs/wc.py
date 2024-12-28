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

def count_lines(lines):
    return len(lines)

def count_characters(lines):
    return sum(len(line) for line in lines)

def print_counts(num_lines, num_characters):
    print(f"Lines: {num_lines}")
    print(f"Characters: {num_characters}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python wc.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    lines = read_file(filename)
    num_lines = count_lines(lines)
    num_characters = count_characters(lines)
    print_counts(num_lines, num_characters)

if __name__ == "__main__":
    main()
