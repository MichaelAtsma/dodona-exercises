def SchoolMotto(woord):
    aantal_gokae = 0
    aantal_andere = 0
    
    for letter in woord:
        if letter == "G":
            aantal_gokae = aantal_gokae + 1
        elif letter == "O":
            aantal_gokae = aantal_gokae + 1
        elif letter == "K":
            aantal_gokae = aantal_gokae + 1
        elif letter == "A":
            aantal_gokae = aantal_gokae + 1
        elif letter == "E":
            aantal_gokae = aantal_gokae + 1
        else:
            aantal_andere = aantal_andere + 1
            
    print(f"{woord} bevat {aantal_gokae} GOKAE letters en {aantal_andere} andere letters.")