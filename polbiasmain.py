import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from polbiasbackend import analyze_text

#main analysis func
def analyze_text_and_display():
    text = text_entry.get("1.0", "end-1c")
    results = analyze_text(text)
    
    #msg box
    messagebox.showinfo("Analysis Results", results)

#main window
window = tk.Tk()
window.title("Political Bias Analyzer")
#text, text styles
text_label = ttk.Label(window, text="Enter text:")
text_label.pack()
text_entry = tk.Text(window, width=50, height=10)
text_entry.pack()
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))

#go button
go_button = ttk.Button(window, text="Go", command=analyze_text_and_display)
go_button.pack()

window.mainloop()