import sys


def modifi_files(contenu: str) -> str:
    ligne = contenu.split("\n")
    ligne_modif = [ligne_u + "#" for ligne_u in ligne]
    text = "\n".join(ligne_modif)
    return text


def show(contenu: str) -> None:
    print("---")
    print()
    print(f"{contenu}")
    print()
    print("---")


def open_files(argv: list[str]) -> None:
    if len(argv) == 1:
        print("Usage: ft_ancient_text.py <file> ")
    else:
        print("=== Cyber Archives Recovery ===")
        try:
            print(f"Accessing file '{argv[1]}'")
            fichier = open(argv[1])
            contenu = fichier.read()
            show(contenu)
            fichier.close()
            print(f"File {argv[1]} closed.")
            print()
            print("Transform data:")
            text_modif = modifi_files(contenu)
            show(text_modif)
            name = input("Enter new fil name (or empty):")
            if name == "":
                print("Not saving data.")
            else:
                fichier_new = open(name, "w")
                fichier_new.write(text_modif)
                fichier_new.close()
                print(f"Saving data to {name}")
                print(f"Data saved in file {name}")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error opening file '{argv[1]}': {e}")


if __name__ == "__main__":
    open_files(sys.argv)
