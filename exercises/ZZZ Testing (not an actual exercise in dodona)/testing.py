import io
import sys

def capture_output(func, *args, **kwargs):
    """Capture the output of a function call."""
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        func(*args, **kwargs)
        return sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout

def PrintDeelbaarheden3(getallen):
    for getal in getallen:
        if getal % 3 == 0:
            print(f"{getal} is deelbaar door 3.")
        else:
            print(f"{getal} is niet deelbaar door 3.")

theoutput = capture_output(PrintDeelbaarheden3, [1, 2, 3, 4, 5, 6])
print(f"-----LOOK HERE--------{theoutput}------I CAUGHT IT-------")