import sys

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--platform":
        print(f"Operating System Platform: {sys.platform}")
    else:
        print("Usage: python os_platform_report.py --platform")

if __name__ == "__main__":
    main()
