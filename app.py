import json
import os
import tkinter as tk


class TempView(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller)

        self.controller = controller

        self.loading_title = tk.Label(
            master=controller,
            text=f"Main Application",
        )
        self.loading_title.pack(pady=20)

        quit_button = tk.Button(
            master=self, text="Quit", command=self.controller.destroy
        )
        quit_button.pack(padx=20, pady=10)


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        # Window properties
        self.title("Simple Application")
        self.geometry("600x200")
        self.eval("tk::PlaceWindow . center")
        self.focus_force()

        self.main_page = TempView(controller=self)
        self.main_page.pack(side="top", fill="both", expand=True)
        self.main_page.grid_rowconfigure(0, weight=1)
        self.main_page.grid_columnconfigure(0, weight=1)
        self.main_page.tkraise()


def _check_config():
    root_path = os.path.dirname(__file__)
    config_path = os.path.join(root_path, "config.json")
    data = {}
    if not os.path.exists(config_path):
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    else:
        try:
            with open(config_path, "r") as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            data = {}

    return


def main():
    _check_config()

    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
