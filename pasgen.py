import os
import sys
import getpass
import argparse
from generate_entries import main as generate_entries_main


def setup_password(args=None):
    password_file = os.path.expanduser("~/.pasgen_password")
    if os.path.isfile(password_file):
        existing_password = getpass.getpass("Enter your current password: ")
        with open(password_file, "r") as f:
            stored_password = f.read().strip()
        if existing_password != stored_password:
            print("Incorrect password. Access denied.")
            return
    new_password = getpass.getpass("Enter your new password: ")
    with open(password_file, "w") as f:
        f.write(new_password)
    print("Password set up successfully.")

# Function to check if password is set up
def check_password_setup():
    password_file = os.path.expanduser("~/.pasgen_password")
    if not os.path.isfile(password_file):
        print("Password is not set up. Please run 'pasgen setup' to set up the password.")
        sys.exit(1)

# Function to authenticate the user
def authenticate():
    stored_password = get_stored_password()
    entered_password = getpass.getpass("Enter your password: ")
    if entered_password != stored_password:
        print("Incorrect password. Access denied.")
        sys.exit(1)

# Function to retrieve stored password
def get_stored_password():
    password_file = os.path.expanduser("~/.pasgen_password")
    if os.path.isfile(password_file):
        with open(password_file, "r") as f:
            return f.read().strip()
    else:
        print("Password is not set up. Please run 'pasgen setup' to set up the password.")
        sys.exit(1)

# Function to generate password
def generate_password(args):
    check_password_setup()
    authenticate()
    generate_entries_main(args)

# Main function
def main():
    parser = argparse.ArgumentParser(description="Password and Pin Generator")
    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

    # Setup subcommand
    setup_parser = subparsers.add_parser("setup", help="Set up password")
    setup_parser.set_defaults(func=setup_password)

    # Generate subcommand
    generate_parser = subparsers.add_parser("generate", help="Generate password or pin")
    generate_parser.add_argument("-l", "--length", type=int, default=12, help="Length of the password")
    generate_parser.add_argument("-p", "--pin", action="store_true", help="Generate a pin")
    generate_parser.add_argument("-pl", "--pin_length", type=int, default=6, help="Length of the pin")
    generate_parser.set_defaults(func=generate_password)

    args = parser.parse_args()
    if not hasattr(args, "func"):
        parser.print_help(sys.stderr)
        sys.exit(1)
    args.func(args)

if __name__ == "__main__":
    main()
