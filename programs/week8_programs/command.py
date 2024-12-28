def nl(file_path):
    try:
        with open(file_path, 'r') as file:
            for i, line in enumerate(file, start=1):
                print(f"{i}\t{line.rstrip()}")
    except FileNotFoundError:
        print(f"Error: '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python command.py <file_path>")
    else:
        nl(sys.argv[1])
