"""
PassTool - A command-line password utility tool.

Features:
1. Generate strong passwords.
2. Evaluate password strength.
3. Check whether a password has been compromised using the 'Have I Been Pwned' API.

Author: Kalyan Koushik
"""
import random 
import string
import hashlib
import requests
import stdiomask
from colorama import Fore, init
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box

init(autoreset=True)

def main():
    """
    Run the interactive loop for the password utility tool.
    Handles user input and dispatches to the appropriate functionality.
    """
    show_banner()
    print("Welcome to your personal password utility tool! 🔧\n")

    try:
        while True:
            show_menu()
            choice = input(Fore.GREEN + "Enter your choice (1-4): " + Fore.RESET)

            if choice in  ["1", "2", "3","4"]:
                if choice == "1":
                    password_length = input("password length: ")
                    print(Fore.MAGENTA + generate_pass(password_length)) 
                elif choice == "2":
                    password_to_check = stdiomask.getpass("Enter password: ", mask="*")
                    score = check_strength(password_to_check)
                    messages = [
                        "Very Weak 💩", 
                        "Weak 🤒",
                        "Decent 😑", 
                        "Moderate 🤷", 
                        "Strong 💪", 
                        "Very Strong 🔐"
                        ]
                    # Make sure score doesn't exceed the message list length
                    score = min(score, len(messages) - 1)
                    strength_bar = "█" * score + "-" * (5 - score)
                    print(f"Strength: {messages[score]} [{strength_bar}]")


                elif choice == "3":
                    password_to_verify = stdiomask.getpass("Enter a password: ", mask="*")
                    print(Fore.RED + check_compromise(password_to_verify))
                else:
                    print(Fore.YELLOW + "\nGoodbye! 😉 Thanks for using PassTool!\n")
                    break

            else:
                print(Fore.RED + "❌ Invalid input!! Try again.")
                continue

    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nProgram terminated by user. Goodbye!")

def generate_pass(x=12):
    """
    Generate a secure random password of the given length with at least one lowercase letter, uppercase letter, digit, and symbol.
    args: 
        x (str): Desired password length (default: 12).
    returns:
        str: Generated password or error message if input is invalid.
    """
    try:
        length = int(x)
        if length < 4:
            return "❌ Length should be atleast 4 to include all character types."
        if length > 1000: # Arbitary upper limit
            return "❌ Length is too large. Choose a value under 1000."
    except ValueError:
        return "❌ Please enter a valid number for password length!"
    all_chars = string.ascii_letters + string.digits + string.punctuation

    password_chars = [
    random.choice(string.ascii_lowercase),
    random.choice(string.ascii_uppercase),
    random.choice(string.digits),
    random.choice(string.punctuation)

    ]
    
    while len(password_chars) < length:
        password_chars.append(random.choice(all_chars))
    random.shuffle(password_chars)
    password = ''.join(password_chars)
    return f"Generated password: {password}"

def check_strength(y):
    """
    Evaluate the strength of a given password.

    Args:
        y (str): Password to be evaluated.

    Returns:
        int: Score from 0 to 5 indicating strength level.
    """
    if not y:
        return 0
    score = 0
    has_lower = False
    has_upper = False
    has_digit = False
    has_punct = False
    if len(y) > 8:
        score += 1
    for char in y:
        if char in string.ascii_lowercase:
            has_lower = True
        elif char in string.ascii_uppercase:
            has_upper = True
        elif char in string.digits:
            has_digit = True
        elif char in string.punctuation:
            has_punct = True
    score += has_lower + has_upper + has_digit + has_punct
    return score

def check_compromise(z):
    """
    Check whether the password has been compromised using the Have I Been Pwned API.

    Args:
    z (str): Password to check.

    Returns:
     str: Message indicating whether the password was found in breaches.
    """
    if not z:
        return "❌ Password cannot be empty."
    hash_object = hashlib.sha1(z.encode('utf-8'))
    hashed_password = hash_object.hexdigest().upper()
    prefix = hashed_password[:5]
    sufix = hashed_password[5:]
    
    try:
        req = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}", timeout=5)
        req.raise_for_status()
    except requests.RequestException:
        return "❌ Unable to check for breach (NETWORK ERROR!!)."
    for line in req.text.splitlines():
        h,count = line.split(":")
        if h == sufix:
            return f"⚠️ Password was found {count} times in data breaches!"
    return "✅ Password is not found in known breaches."

def show_banner():
    """
    Display a rich-styled banner with color and borders.
    """
    console = Console()
    banner_text = Text("PassTool", style="bold magenta", justify="center")
    panel = Panel(
        banner_text,
        title="🔐 Password Utility",
        subtitle="by Kalyan Koushik",
        padding=(1, 4),
        style="bold cyan",
        border_style="magenta",
        box=box.DOUBLE
    )
    console.print(panel)

def show_menu():
    """
    Display the main menu with options for the user.
    """
    print(Fore.CYAN + "\nChoose an option:")
    print(Fore.YELLOW + "1." + Fore.RESET + " 🔮 Generate a strong password")
    print(Fore.YELLOW + "2." + Fore.RESET + " 📊 Check password strength")
    print(Fore.YELLOW + "3." + Fore.RESET + " 🕵️ Check if password is compromised")
    print(Fore.YELLOW + "4." + Fore.RESET + " ❌ Exit")

if __name__=="__main__":
    main()