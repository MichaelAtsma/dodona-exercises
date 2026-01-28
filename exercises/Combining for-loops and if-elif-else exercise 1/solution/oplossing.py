for i in range(501):
    eenheden = i % 10
    tientallen = (i // 10) % 10
    honderdtallen = i // 100  # We hebben hier getallen tot en met 500, dus we hoeven geen rekening te houden met duizendtallen
    if eenheden == 3:
        print(f"{i} bevat een 3.")
    elif tientallen == 3:
        print(f"{i} bevat een 3.")
    elif honderdtallen == 3:
        print(f"{i} bevat een 3.")
    else:
        print(f"{i} bevat geen 3.")