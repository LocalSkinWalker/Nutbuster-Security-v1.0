import time
import winsound

while True:
    password = input("enter your password: ")
    if len(password) < 8:
        print("Password must contain with at least 8characters, at least one number and one upper latter")
    elif not any(c.isupper() for c in password):
        print("Password must contain with at least 8characters, at least one number and one upper latter")
    elif not any(c.isdigit() for c in password):
        print("Password must contain with at least 8characters, at least one number and one upper latter")
    else:
        print("your password is saved!")
        winsound.Beep(1750, 150)
        break

print("please enter your password to login, WARRNING incorect password will prevail in your balls exploding!")
num_of_tries = 4

for attempt in range(num_of_tries):
    login_password = input("Enter password: ")
    if login_password == password:
        print("Don't worry, your balls won't explode.")
        winsound.Beep(1261, 150)
        time.sleep(0.05)
        winsound.Beep(1329, 150)
        time.sleep(0.05)
        winsound.Beep(1392, 150)
        time.sleep(0.1)
        winsound.Beep(1523, 300)
        break
    else:
        remaining = num_of_tries - attempt - 1
        if remaining > 0:
            print(f"Oops, your password is incorrect. You have {remaining} more {'tries' if remaining > 1 else 'try'}!")
            winsound.Beep(1750, 150)
            winsound.Beep(1750, 150)
        else:
            print("Your balls will explode in:")
            for i in range(10, 0, -1):
                print(f"...{i} second{'s' if i > 1 else ''}")
                winsound.Beep(1200, 200)
                time.sleep(1)
            print("BOOM!")
            for _ in range(5):
                winsound.Beep(1200, 100)
                time.sleep(0.05)
                