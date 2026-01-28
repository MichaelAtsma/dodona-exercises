for i in range(111):
    if i < 50:
        print(f"{i}% is een onvoldoende.")
    elif i <= 100:
        print(f"{i}% is een voldoende.")
    else:
        print(f"Je kan geen {i}% scoren.")