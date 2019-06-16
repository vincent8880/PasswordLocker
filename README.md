# PasswordLocker
## Password locker is a simple python app that stores usernames and passwords for different user accounts

## Description
Password Locker is an application that helps users generate and store passwords on their multiple accounts.
The password locker runs on the terminal and uses short codes to navigate through it.
When starting up the application, the user is met with the following shortcodes:

    1. cc - Creates a new account
    2. ss - Sign in
    3. ex - Exit the application

The user will be met with the following commands while signing in:

    1. ad - Add your own password
    2. gn - generate random password
    3. vp - View passwords
    4. cp - Copy password to clipboard
    5. lo - Log out

## Specifications
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| Create new account | Type: cc <br>Username: musky <br>Password: pass | User musky has been created.<br>Log in to Continue |
| Sign in | Type: ss <br>Username: musky<br>Password: pass | Welcome musky! What would you like to do? |
| Add Password | Type: gn <br>Website: mywebsite.com <br>Length of password: 10 | **Generates a password with x length**<br>Your password for mywebsite.com is eyDB58eh49 |
| View list of passwords | Type: vp | Generates a lists of websites and passwords |
| Copy Password to clipboard | Type: cp <br>Enter index: 1 | Password 1 on the list has been copied and is ready for pasting |
| Log Out | Type: lo | **Logs out the user** <br>Goodbye musky! |
| Exit Application | Type: ex | **Closes the application** <br>Goodbye!! |

## Prerequiites
    - Python 3.6 required

## Set-up and Installation
    - Clone the Repo
    - Install python 3.6
    - Run `python3.6 run.py`

## Known bugs
No known errors if found drop a message on my profile

## Technologies used
    - Python 3.6

## Support and contact details
Contact me on ododovincent54@gmail.com for any comments, reviews or advice.

### License

