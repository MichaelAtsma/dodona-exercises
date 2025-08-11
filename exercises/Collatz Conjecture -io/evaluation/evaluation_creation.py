import tkinter as tk


class ToolTip:
    def __init__(self, widget, text, max_width=100, max_lines=20):
        self.widget = widget
        self.text = text
        self.max_width = max_width      # max chars per line
        self.max_lines = max_lines      # max number of lines to show
        self.tipwindow = None
        widget.bind("<Enter>", self.show_tip)
        widget.bind("<Leave>", self.hide_tip)

    def _truncate_line(self, line):
        if len(line) <= self.max_width:
            return line
        return line[:self.max_width - 3] + "..."

    def _prepare_text(self):
        lines = self.text.splitlines() or self.text.split(", ")  # split on lines or commas
        truncated_lines = [self._truncate_line(line) for line in lines]

        if len(truncated_lines) > self.max_lines:
            truncated_lines = truncated_lines[:self.max_lines]
            truncated_lines[-1] = "..."  # last line is ellipsis to show more lines hidden

        return "\n".join(truncated_lines)

    def show_tip(self, event=None):
        if self.tipwindow or not self.text:
            return
        text_to_show = self._prepare_text()

        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + self.widget.winfo_height() + 5
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)  # no decorations
        tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(tw, text=text_to_show, justify='left',
                         background="#ffffe0", relief='solid', borderwidth=1,
                         font=("TkDefaultFont", 9),
                         wraplength=self.max_width * 7)  # approx width in pixels
        label.pack(ipadx=1, ipady=1)

    def hide_tip(self, event=None):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def ResultCopier(*results):
    root = tk.Tk()
    root.title("Copy Results")

    def make_copy_func(text):
        def copy():
            root.clipboard_clear()
            root.clipboard_append(text)
            root.update()  # ensures clipboard is updated
        return copy

    for i, res in enumerate(results):
        btn = tk.Button(root, text=f"Copy file {i}", command=make_copy_func(res),
                        wraplength=400, anchor="w", justify="left")
        btn.pack(fill="x", padx=100, pady=2)
        ToolTip(btn, res)  # Attach tooltip with the full text

    root.mainloop()


def Collatz(n):
    x = n
    res = f"Collatz-reeks: {n}"
    while x != 1:
        if x % 2 == 0:
            x = x//2
        else:
            x = 3*x+1
        res += f", {x}"

    return res

def MakeExercises(start, end):
    inFile = ""
    outFile = ""
    for n in range(start, end+1):
        inFile += f"{n}\n"
        outFile += f"{Collatz(n)}\n"
    return inFile.strip(), outFile.strip()

ResultCopier(*MakeExercises(1,5))
ResultCopier(*MakeExercises(6,25))
ResultCopier(*MakeExercises(26, 1000))