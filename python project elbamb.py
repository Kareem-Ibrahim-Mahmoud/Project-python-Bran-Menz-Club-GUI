import tkinter as tk

class Menz:
    def __init__(self):
        self.name = ""
        self.number = 0
        self.price = 0.0
        self.discount = 0.0

    def set_name(self):
        self.name = entry_name.get()

    def set_number(self):
        self.number = int(entry_number.get())

    def set_price(self):
        self.price = float(entry_price.get())

    def set_discount(self):
        self.discount = float(entry_discount.get())

    def get_total(self):
        return self.price - (self.price * self.discount / 100)

    def print_info(self):
        total = self.get_total()
        output_text.set(f"Name: {self.name}\nNumber: {self.number}\nPrice: {self.price}\nDiscount: {self.discount}%\nTotal: {total}")

    def __del__(self):
        pass

def on_button_click():
    s = Menz()
    s.set_name()
    s.set_number()
    s.set_price()
    s.set_discount()
    s.print_info()

window = tk.Tk()
window.title("Mens Club")

label_name = tk.Label(window, text="Name:")
label_name.pack()
entry_name = tk.Entry(window)
entry_name.pack()

label_number = tk.Label(window, text="Number:")
label_number.pack()
entry_number = tk.Entry(window)
entry_number.pack()

label_price = tk.Label(window, text="Price:")
label_price.pack()
entry_price = tk.Entry(window)
entry_price.pack()

label_discount = tk.Label(window, text="Discount:")
label_discount.pack()
entry_discount = tk.Entry(window)
entry_discount.pack()

button = tk.Button(window, text="Calculate Total", command=on_button_click)
button.pack()

output_text = tk.StringVar()
output_label = tk.Label(window, textvariable=output_text)
output_label.pack()

window.mainloop()