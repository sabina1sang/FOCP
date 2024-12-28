import sys

def comparison_of_files(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            contents1 = f1.readlines()
            contents2 = f2.readlines()

            if contents1 == contents2:
                print("The files are the same.")
            else:
                print("The files are different.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python diff.py <file1> <file2>")
        sys.exit(1)
    
    file1, file2 = sys.argv[1], sys.argv[2]
    comparison_of_files(file1, file2)
