def TweetValidatie(tweet):
    lengte = len(tweet)
    if lengte <= 5:
        validatie = "Te korte tweet."
    elif lengte <= 280:
        validatie = "Geldige tweet."
    else:
        validatie = "Te lange tweet."
    return validatie