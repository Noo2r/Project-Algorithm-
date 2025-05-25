import tkinter as tk
from tkinter import messagebox, font

def min_cut_palindrome_partition(s):
    n = len(s)
    is_palindrome = [[False]*n for _ in range(n)]

    for i in range(n):
        is_palindrome[i][i] = True

    for i in range(n-1):
        if s[i] == s[i+1]:
            is_palindrome[i][i+1] = True

    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if s[i] == s[j] and is_palindrome[i+1][j-1]:
                is_palindrome[i][j] = True

    dp = [float('inf')] * n
    for i in range(n):
        if is_palindrome[0][i]:
            dp[i] = 0
        else:
            for j in range(i):
                if is_palindrome[j+1][i] and dp[j]+1 < dp[i]:
                    dp[i] = dp[j]+1

    return dp[-1], is_palindrome, dp

def get_palindromic_partitions(s, is_palindrome, dp):
    n = len(s)
    result = []
    i = n - 1
    cuts = []

    while i >= 0:
        for j in range(i + 1):
            if is_palindrome[j][i] and (j == 0 or dp[j - 1] + 1 == dp[i]):
                cuts.append((j, i))
                i = j - 1
                break

    cuts.reverse()
    for start, end in cuts:
        result.append(s[start:end + 1])
    return result

def calculate():
    s = input_entry.get().strip()
    if not s:
        messagebox.showwarning("Warning", "Please enter a string!")
        return

    cuts, pal_table, dp_array = min_cut_palindrome_partition(s)
    partitions = get_palindromic_partitions(s, pal_table, dp_array)

    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"Minimum cuts needed: {cuts}\nPartition: ", "center")

    colors = ["#FFCDD2", "#F8BBD0", "#E1BEE7", "#D1C4E9", "#C5CAE9",
              "#B2EBF2", "#C8E6C9", "#FFF9C4", "#FFE0B2", "#FFCCBC"]

    for i, part in enumerate(partitions):
        tag_name = f"color{i}"
        result_text.tag_configure(tag_name, background=colors[i % len(colors)], foreground="black", justify="center")
        result_text.insert(tk.END, part, (tag_name, "center"))
        if i < len(partitions) - 1:
            result_text.insert(tk.END, " | ", "center")

    result_text.tag_add("center", "1.0", "end")
    result_text.config(state=tk.DISABLED)

    for widget in pal_table_frame.winfo_children():
        widget.destroy()
    
    if len(s) <= 15:
        for j in range(len(s)):
            lbl = tk.Label(pal_table_frame, text=s[j], width=3, borderwidth=1, relief="solid",
                          bg="#ddd", font=("Arial", 10, "bold"))
            lbl.grid(row=0, column=j+1, sticky="nsew")
        
        for i in range(len(s)):
            lbl = tk.Label(pal_table_frame, text=s[i], width=3, borderwidth=1, relief="solid",
                          bg="#ddd", font=("Arial", 10, "bold"))
            lbl.grid(row=i+1, column=0, sticky="nsew")
        
        for i in range(len(s)):
            for j in range(len(s)):
                value = "✓" if pal_table[i][j] else "×"
                bg_color = "#c6ebc9" if pal_table[i][j] else "#eee"
                lbl = tk.Label(pal_table_frame, text=value, width=3, borderwidth=1, relief="solid",
                              bg=bg_color, font=("Arial", 10))
                lbl.grid(row=i+1, column=j+1, sticky="nsew")
        
        tk.Label(pal_table_frame, text="Palindrome Table:", font=("Arial", 12, "bold")).grid(row=len(s)+1, column=0, columnspan=len(s)+1, pady=(10, 0))
    else:
        tk.Label(pal_table_frame, text="Input too large to display palindrome table", font=("Arial", 12)).pack(pady=10)

    for widget in dp_values_frame.winfo_children():
        widget.destroy()

    tk.Label(dp_values_frame, text="DP Table (Minimum Cuts at each index):", font=("Arial", 12, "bold")).pack(pady=(10, 5))
    
    dp_container = tk.Frame(dp_values_frame)
    dp_container.pack()
    
    for i in range(len(s)):
        lbl = tk.Label(dp_container, text=str(i), width=4, borderwidth=1, relief="solid", 
                      bg="#ddd", font=("Arial", 10, "bold"))
        lbl.grid(row=0, column=i, padx=1, pady=1)
    
    for i, val in enumerate(dp_array):
        disp_val = str(val) if val != float('inf') else "∞"
        lbl = tk.Label(dp_container, text=disp_val, width=4, borderwidth=1, relief="solid", 
                      bg="lightyellow", font=("Arial", 10))
        lbl.grid(row=1, column=i, padx=1, pady=1)

def reset():
    input_entry.delete(0, tk.END)
    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, "Results will appear here")
    result_text.tag_add("center", "1.0", "end")
    result_text.config(state=tk.DISABLED)

    for widget in pal_table_frame.winfo_children():
        widget.destroy()

    for widget in dp_values_frame.winfo_children():
        widget.destroy()

root = tk.Tk()
root.title("Palindrome Partitioning Tool")
root.geometry("800x700")
root.configure(bg="#f5f5f5")

app_font = font.Font(family="Arial", size=15)
title_font = font.Font(family="Arial", size=16, weight="bold")

container = tk.Frame(root, bg="#f5f5f5", padx=20, pady=20)
container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

title_label = tk.Label(container, text="Palindrome Partitioning Tool", font=title_font, bg="#f5f5f5", fg="#333")
title_label.pack(pady=(0, 20))

input_frame = tk.Frame(container, bg="#f5f5f5")
input_frame.pack(fill=tk.X, pady=10)

tk.Label(input_frame, text="Enter a string:", font=app_font, bg="#f5f5f5").pack()
input_entry = tk.Entry(input_frame, width=50, font=app_font, relief=tk.GROOVE, bd=2)
input_entry.pack(pady=5, ipady=5)

button_frame = tk.Frame(container, bg="#f5f5f5")
button_frame.pack(pady=15)

calculate_btn = tk.Button(button_frame, text="Calculate Cuts", command=calculate, 
                          width=15, font=app_font, bg="#4CAF50", fg="white",
                          relief=tk.RAISED, bd=2, cursor="hand2")
calculate_btn.pack(side=tk.LEFT, padx=10)

reset_btn = tk.Button(button_frame, text="Reset", command=reset, 
                      width=15, font=app_font, bg="#f44336", fg="white",
                      relief=tk.RAISED, bd=2, cursor="hand2")
reset_btn.pack(side=tk.LEFT, padx=10)

result_frame = tk.Frame(container, bg="#f5f5f5")
result_frame.pack(fill=tk.X, pady=15)

result_container = tk.Frame(result_frame, bg="#000000", bd=2, relief=tk.GROOVE)
result_container.pack(fill=tk.X)

result_text = tk.Text(result_container, height=4, width=70, font=app_font, wrap=tk.WORD,
                    bg="#000000", fg="#ffffff", bd=0)
result_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
result_text.tag_configure("center", justify='center')
result_text.insert(tk.END, "Results will appear here")
result_text.tag_add("center", "1.0", "end")
result_text.config(state=tk.DISABLED)

canvas_frame = tk.Frame(container, bg="#f5f5f5")
canvas_frame.pack(fill=tk.BOTH, expand=True, pady=10)

canvas = tk.Canvas(canvas_frame, bg="#f5f5f5", highlightthickness=0)
scrollbar = tk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#f5f5f5")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

pal_table_frame = tk.Frame(scrollable_frame, bg="#f5f5f5")
pal_table_frame.pack(fill=tk.X, pady=10)

dp_values_frame = tk.Frame(scrollable_frame, bg="#f5f5f5")
dp_values_frame.pack(fill=tk.X, pady=10)

footer_frame = tk.Frame(container, bg="#f5f5f5")
footer_frame.pack(fill=tk.X, pady=(20, 0))

footer_text = tk.Label(footer_frame, text="Minimum cuts needed to partition a string into palindromes",
                       font=("Arial", 9), bg="#f5f5f5", fg="#666")
footer_text.pack()

root.bind('<Return>', lambda event: calculate())

root.mainloop()
