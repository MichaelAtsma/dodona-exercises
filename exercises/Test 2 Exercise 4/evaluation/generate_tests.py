import pyperclip
import itertools
import random
import io
import sys

def copy_to_clipboard(text):
    pyperclip.copy(text)

def capture_output(func, *args, **kwargs):
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        return_value = func(*args, **kwargs)
        return return_value, sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout

def TweetValidatie(tweet):
    lengte = len(tweet)
    if lengte <= 5:
        validatie = "Te korte tweet."
    elif lengte <= 280:
        validatie = "Geldige tweet."
    else:
        validatie = "Te lange tweet."
    return validatie

# Please note, the lorem ipsum below has 445 characters. If you want more, add it yourself.
lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

X = [("hoi",), 
     ("Hallo",),
     ("POV: je leerkracht is cringe met taalgebruik",), 
     ("Dit is een tweet die precies 280 tekens bevat. Zou je niet denken hè? Heb jij het aantal tekens geteld? Let op dat de spaties ook mee doen! We zijn nu ongeveer op de helft. Voeg jij wel eens wat woorden toe aan je verslagen zodat je het minimum aantal woorden behaalt? We zijn er!",), 
     ("Dit is een tweet die meer dan 280 tekens bevat. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",)
    ]

X = [(lorem_ipsum[:i],) for i in range(10)] + [(lorem_ipsum[:i],) for i in range(20, 401, 4)]

result = ""
for args in X:
    result += f">>> TweetValidatie({', '.join(map(repr, args))})\n"
    result += f"{repr(TweetValidatie(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)