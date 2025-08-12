

class InvalidLengthError(Exception):
    pass

class InvalidCharacterError(Exception):
    pass

def validate_username(username):
    if len(username) < 5 or len(username) > 15:
        raise InvalidLengthError("Username must be between 5 and 15 characters.")
    if not username.isalnum():
        raise InvalidCharacterError("Username must be alphanumeric.")

def main():
    try:
        username = input("👤 Enter a username: ")
        validate_username(username)
        with open("users.txt", "a") as f:
            f.write(username + "\n")
        print("✅ Username registered successfully.")
    except InvalidLengthError as e:
        print(f" {e}")
    except InvalidCharacterError as e:
        print(f" {e}")
    except Exception as e:
        print(f" Unexpected error: {e}")
    finally:
        print(" Registration attempt completed.")

if __name__ == "__main__":
    main()
