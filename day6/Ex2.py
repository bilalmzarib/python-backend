
def convert_c_to_f(celsius):
    return (celsius * 9/5) + 32

def main():
    try:
        with open("celsius.txt", "r") as infile, open("fahrenheit.txt", "w") as outfile:
            for line in infile:
                try:
                    c = float(line.strip())
                    f = convert_c_to_f(c)
                    outfile.write(f"{c:.2f}C = {f:.2f}F\n")
                except ValueError:
                    print(f"⚠️ Invalid temperature: {line.strip()}")
        print("✅ Converted temperatures written to fahrenheit.txt")
    except FileNotFoundError:
        print(" celsius.txt not found.")
    except Exception as e:
        print(f" Unexpected error: {e}")

if __name__ == "__main__":
    main()
