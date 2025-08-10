

import re

def is_strong(password):
    if (len(password) >= 8 and
        re.search(r'[A-Z]', password) and
        re.search(r'[a-z]', password) and
        re.search(r'\d', password) and
        re.search(r'[!@#$%^&*]', password)):
        return True
    return False

def main():
    try:
        with open("passwords.txt", "r") as infile, open("strong_passwords.txt", "w") as outfile:
            for line in infile:
                pwd = line.strip()
                if is_strong(pwd):
                    outfile.write(pwd + "\n")
                else:
                    print(f" Weak password skipped: {pwd}")
        print(" Strong passwords saved to strong_passwords.txt")
    except FileNotFoundError:
        print(" passwords.txt not found.")
    except Exception as e:
        print(f" Unexpected error: {e}")

if __name__ == "__main__":
    main()
