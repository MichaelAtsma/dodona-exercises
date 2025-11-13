wachtwoord = "pass1234"

if len(wachtwoord) < 8:
    bericht = "Je wachtwoord is te kort."
elif len(wachtwoord) == 8:
    bericht = "Je wachtwoord is precies lang genoeg."
else:
    bericht = "Je wachtwoord is sterk."