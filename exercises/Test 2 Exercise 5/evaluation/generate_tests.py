import os
import pyperclip
import itertools
import random
import pycountry
from random_word import RandomWords
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

def WedstrijdUitslag(scoreA, scoreB, teamA, teamB):
    if scoreA > scoreB:
        uitslag = f"{teamA} heeft gewonnen!"
    elif scoreB > scoreA:
        uitslag = f"{teamB} heeft gewonnen!"
    else:
        uitslag = "Gelijkspel!"
    return uitslag

with open(os.path.join(os.path.dirname(__file__), "city_names.txt"), "r", encoding="utf-8") as f:
        city_list = [line.strip() for line in f.readlines()]

def GetRandomCity(city_list=city_list):
    city = random.choice(city_list)
    if " (" in city:
        city = city.split(" (")[0]
    return city

def GetRandomCountry():
    return random.choice(list(pycountry.countries)).name

def GenerateRandomScoreArgs(n=50):
    for _ in range(n):
        # Generate the score
        if random.randint(0, 2):
            # one team wins
            score1 = random.randint(0, 40)
            score2 = score1
            while score2 == score1:
                score2 = random.randint(0, 40)
        else:
            # draw
            score1 = score2 = random.randint(0, 40)
        
        name_type = random.choice(["city", "country", "randomword"])
        if name_type == "city":
            team1 = GetRandomCity()
            team2 = GetRandomCity()
        elif name_type == "country":
            team1 = GetRandomCountry()
            team2 = GetRandomCountry()
        else:
            r = RandomWords()
            team1 = r.get_random_word().capitalize()
            team2 = r.get_random_word().capitalize()
        
        yield (score1, score2, team1, team2)

X = [(15, 13, "Mooncatchers", "Wall City"),
     (1, 7, "Brazilië", "Duitsland"),
     (2, 2, "Red Panthers", "Spanje")]

X = GenerateRandomScoreArgs(100)

result = ""
for args in X:
    result += f">>> WedstrijdUitslag({', '.join(map(repr, args))})\n"
    result += f"{repr(WedstrijdUitslag(*args))}\n"
copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
