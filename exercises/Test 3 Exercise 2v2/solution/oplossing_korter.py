def SchoolMotto(woord):
    gokae_letters = "GOKAE"
    aantal_gokae = 0
    aantal_andere = 0
    
    for letter in woord:
        if letter in gokae_letters:
            aantal_gokae += 1
        else:
            aantal_andere += 1
            
    print(f"{woord} bevat {aantal_gokae} GOKAE letters en {aantal_andere} andere letters.")