import sys


def open_files(argv: list[str]) -> None:
    if len(argv) == 1:
        print("Usage: ft_ancient_text.py <file> ")
    else:
        print("=== Cyber Archives Recovery ===")
        try:
            print(f"Accessing file '{argv[1]}'")
            fichier = open(argv[1])
            contenu = fichier.read()
            print("---")
            print()
            print(f"{contenu}")
            print()
            print("---")
            fichier.close()
            print(f"File {argv[1]} closed.")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error opening file '{argv[1]}': {e}")


if __name__ == "__main__":
    open_files(sys.argv)
