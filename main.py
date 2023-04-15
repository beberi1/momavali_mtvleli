import tkinter as tk
from tkcalendar import DateEntry

root = tk.Tk()
root.geometry("900x500")
root.title("მთვლელი")

# t - tarigi
# w - warwera
# k - knopka
# c - chasaweri




t1 = DateEntry(root, text="თარიღი")
t1.grid(row=0, column=0, padx=(10, 10), pady=5)
k = tk.Button(root, text="თარიღის გადმოტანა", command=lambda: c1.insert(0, t1.get_date()))
k.grid(row=1, column=0, padx=(10, 10), pady=5)
c1 = tk.Entry(root)
c1.grid(row=2, column=0, padx=(10, 10), pady=5)


w2 = tk.Label(root, text="შენიშვნა")
w2.grid(row=1, column=2, pady=5)
c2 = tk.Entry(root, justify='left')
c2.grid(row=2, column=2, padx=10, pady=5)


w3 = tk.Label(root, text="რაოდენობა - ცალი")
w3.grid(row=1, column=3, pady=5)
c3 = tk.Entry(root)
c3.grid(row=2, column=3, padx=10, pady=5)

w4 = tk.Label(root, text="წონა - კგ.")
w4.grid(row=1, column=4, pady=5)
c4 = tk.Entry(root)
c4.grid(row=2, column=4, padx=10, pady=5)

w5 = tk.Label(root, text="ღირებულება - ლარი")
w5.grid(row=1, column=5, pady=5)
c5 = tk.Entry(root)
c5.grid(row=2, column=5, padx=10, pady=5)

w6 = tk.Label(root, text="ამჟამინდელი ფასი")
w6.grid(row=0, column=6, pady=5)
c6 = tk.Entry(root, width=5)
c6.grid(row=1, column=6, padx=10, pady=5)
c6.insert(0, "8,7")   # mnishvnelobis shetana

text = tk.Text(root, height=15, width=100)
text.grid(row=3, column=0, columnspan=7, padx=10, pady=10)


tavsarti = ["    თარიღი  | შენიშვნა | რაოდენობა | წონა | ფასი | ამჟამინდელი ფასი"]
text.insert(tk.END,"".join(map(str, tavsarti)) + "\n")

def display_data():
    data = [c1.get(), c2.get(), c3.get(), c4.get(), c5.get(), c6.get()]
    text.insert(tk.END, " | ".join(map(str, data)) + "\n")



k2 = tk.Button(root, text="შეტანა", height=3, command=display_data)
k2.grid(row=2, column=6)



root.mainloop()