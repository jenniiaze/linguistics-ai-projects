import tkinter as tk
from tkinter import messagebox
import re
import csv

# Define red flag slang terms
slang_terms = ['mercancía', 'pa’ Bayamón', 'nota', 'ticket', 'verdes', 'taller', 'paquetes', 'Gordo', 'envío', 'el vuelto']

# Define function to analyze input
def analyze_text():
    transcript = text_input.get("1.0", tk.END)
    found_terms = {}

    for term in slang_terms:
        matches = re.findall(term, transcript)
        if matches:
            found_terms[term] = len(matches)

    if found_terms:
        # Save to CSV
        with open("flagged_terms.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Slang Term', 'Occurrences'])
            for term, count in found_terms.items():
                writer.writerow([term, count])
        messagebox.showinfo("Analysis Complete", f"{len(found_terms)} red flag terms found.\nResults saved to 'flagged_terms.csv'")
    else:
        messagebox.showinfo("Analysis Complete", "No red flag terms found.")

# Build GUI
root = tk.Tk()
root.title("Spanish Slang Analyzer")
root.geometry("500x400")

label = tk.Label(root, text="Paste transcript below:", font=('Helvetica', 12))
label.pack(pady=10)

text_input = tk.Text(root, height=15, width=60)
text_input.pack()

analyze_btn = tk.Button(root, text="Analyze", command=analyze_text, bg="#4CAF50", fg="white", font=('Helvetica', 10, 'bold'))
analyze_btn.pack(pady=10)

root.mainloop()
