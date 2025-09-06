def read_and_modify_file():
    filename = input("Enter the filename to read: ").strip()
    print("Choose modification type:")
    print("1. Uppercase")
    print("2. Lowercase")
    print("3. Reverse lines")
    mod_type = input("Enter 1, 2, or 3: ").strip()

    try:
        with open(filename, 'r') as infile:
            lines = infile.readlines()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return
    except PermissionError:
        print(f"Error: Permission denied for file '{filename}'.")
        return
    except Exception as e:
        print(f"Error: Could not read file '{filename}'. Exception: {e}")
        return

    if mod_type == "1":
        modified_lines = [line.upper() for line in lines]
    elif mod_type == "2":
        modified_lines = [line.lower() for line in lines]
    elif mod_type == "3":
        modified_lines = lines[::-1]
    else:
        print("Invalid modification type selected.")
        return

    new_filename = f"modified_{filename}"

    try:
        with open(new_filename, 'w') as outfile:
            outfile.writelines(modified_lines)
        print(f"Modified file written to '{new_filename}'.")
    except PermissionError:
        print(f"Error: Permission denied for file '{new_filename}'.")
    except Exception as e:
        print(f"Error: Could not write to file '{new_filename}'. Exception: {e}")

if __name__ == "__main__":
    read_and_modify_file()
