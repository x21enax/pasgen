import argparse
import random
import string

def generate_password(length=12):
    # Define character sets
    amharic_chars = 'ሀሄህሆለሉሊሡሢሣሤሓሔሁሂሃሕላሌልሎሏሐሑሒመሙሞሟሠሖሗሚማሜምሥሦሧረሩሪራሬርሮሯ'
    english_chars = string.ascii_letters
    symbols = '!@#$%^&*()-=_+[]{}|;:,.<>?'

    # Combine character sets
    all_chars = amharic_chars + english_chars + symbols

    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def generate_pin(length=6):
    # Generate pin
    pin = ''.join(random.choice(string.digits) for _ in range(length))
    return pin

def save_entry(name, value, entry_type):
    with open('pasgen-entries.txt', 'a') as f:
        f.write(f'{name.ljust(50)} {value.ljust(50)} {entry_type}\n')

def main(args):
    name = input("Enter your name or email: ")

    if args.pin:
        pin = generate_pin(args.pin_length)
        save_entry(name, pin, 'Pin')
        print(f"Pin generated and saved in pasgen-entries.txt with length {args.pin_length}")
    else:
        password = generate_password(args.length)
        save_entry(name, password, 'Password')
        print("Password generated and saved in pasgen-entries.txt")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Password and Pin Generator')
    parser.add_argument('-l', '--length', type=int, default=12, help='Length of the password')
    parser.add_argument('-p', '--pin', action='store_true', help='Generate a pin')
    parser.add_argument('-pl', '--pin_length', type=int, default=6, help='Length of the pin')
    args = parser.parse_args()
    main(args)
