def check_sender(email: str) -> bool:
    if "@" not in email:
        return False

    name_part, domain_part = email.split("@")

    if "." not in name_part:
        return False

    name_split = name_part.split(".")
    if len(name_split) != 2:
        return False

    fname, lname = name_split
    if len(fname) < 2 or len(lname) < 2:
        return False

    domain_split = domain_part.split(".")
    if len(domain_split) != 3:
        return False

    for word in domain_split:
        if len(word) < 2:
            return False

    return True


# בדיקה
print(check_sender("stephen.marquard@uct.ac.za"))  # True
print(check_sender("s.m@uct.ac.za"))  # False (קצר מדי)
