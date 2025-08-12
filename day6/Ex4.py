

def main():
    status_counts = {"200": 0, "404": 0, "500": 0}
    try:
        with open("server.log", "r") as logfile:
            for line in logfile:
                parts = line.strip().split()
                if len(parts) >= 3:
                    status = parts[1]
                    if status in status_counts:
                        status_counts[status] += 1
                else:
                    print(f" Invalid log line: {line.strip()}")

        with open("report.txt", "w") as report:
            report.write(f"Successful (200): {status_counts['200']}\n")
            report.write(f"Not Found (404): {status_counts['404']}\n")
            report.write(f"Server Error (500): {status_counts['500']}\n")

        print("✅ Log summary written to report.txt")
    except FileNotFoundError:
        print(" server.log not found.")
    except Exception as e:
        print(f" Unexpected error: {e}")

if __name__ == "__main__":
    main()
