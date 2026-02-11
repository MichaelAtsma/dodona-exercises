import pyperclip
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

def BevatEenDrie(n):
    eenheden = n % 10
    tientallen = (n // 10) % 10
    honderdtallen = n // 100  # We hebben hier getallen tot en met 500, dus we hoeven geen rekening te houden met duizendtallen
    if eenheden == 3:
        return f"{n} bevat een 3."
    elif tientallen == 3:
        return f"{n} bevat een 3."
    elif honderdtallen == 3:
        return f"{n} bevat een 3."
    else:
        return f"{n} bevat geen 3."

result = "\n".join([BevatEenDrie(i) for i in range(501)])

copy_to_clipboard(result)
print("Copied to clipboard:")
print(result)