

def is_palindrome(word):
    return word.lower() == word.lower()[::-1]

def main():
    try:
        with open("input_words.txt", "r") as infile, open("palindromes.txt", "w") as outfile:
            for line in infile:
                word = line.strip()
                if is_palindrome(word):
                    outfile.write(word.upper() + "\n")
        print("✅ Palindromes written to palindromes.txt")
    except FileNotFoundError:
        print(" input_words.txt not found.")
    except Exception as e:
        print(f" Unexpected error: {e}")

if __name__ == "__main__":
    main()
