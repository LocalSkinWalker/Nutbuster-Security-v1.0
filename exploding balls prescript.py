while True:
    sifra = input("enter your password: ")
    if len(sifra) < 8:
        print("Password must contain with at least 12characters, at least one number and one upper latter")
    elif not any(c.isupper() for c in sifra):
        print("Password must contain with at least 12characters, at least one number and one upper latter")
    elif not any(c.isdigit() for c in sifra):
        print("Password must contain with at least 12characters, at least one number and one upper latter")
    else:
        print("your password is saved!")
        break

print("your password:", sifra)



