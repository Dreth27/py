import tkinter as tk

class AppGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        login_label = tk.Label(self, text="Login:")
        login_label.grid(row=0, column=0)

        self.login_entry = tk.Entry(self)
        self.login_entry.grid(row=0, column=1)

        password_label = tk.Label(self, text="Password:")
        password_label.grid(row=1, column=0)

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1)

        start_button = tk.Button(self, text="Start", command=self.on_start_click)
        start_button.grid(row=2, column=1)

    def on_start_click(self):
        login = self.login_entry.get()
        password = self.password_entry.get()

        if login == "admin" and password == "password":
            print("Login successful")
        else:
            print("Login failed")

app = AppGUI()
app.mainloop()