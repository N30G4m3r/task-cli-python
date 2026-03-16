import argparse

# Punto de entrada (Argparse)
def main():
    parser = argparse.ArgumentParser(description="A simple task CLI in Python")
    parser.add_argument("--name", help="Name of the user")
    args = parser.parse_args()

    if args.name:
        print(f"Hello, {args.name}!")
    else:
        print("Hello from task-cli-python!")

if __name__ == "__main__":
    main()
