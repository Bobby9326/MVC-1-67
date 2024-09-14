import tkinter as tk

class CowView:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x400")
        self.root.title("Cow Management System")

        # หน้า Input
        self.input_view = tk.Frame(root)
        self.input_view.pack()

        

        self.cow_id_label = tk.Label(self.input_view, text="Cow ID:")
        self.cow_id_label.pack()

        self.cow_id_entry = tk.Entry(self.input_view)
        self.cow_id_entry.pack()

        self.submit_button = tk.Button(self.input_view, text="Submit")
        self.submit_button.pack()

        self.reset_button = tk.Button(self.input_view, text="Reset")
        self.reset_button.pack() 

        # หน้า White Cow
        self.create_white_view()

        # หน้า Brown Cow
        self.create_brown_view()

        self.show_input_view()  # แสดงหน้า Input เป็นค่าเริ่มต้น

    def create_white_view(self):
        self.white_view = tk.Frame(self.root)
        self.white_view.pack_forget()  # ซ่อนหน้า white_view

        self.milk_button = tk.Button(self.white_view, text="Milk White Cow")
        self.milk_button.pack()

        self.lemon_button = tk.Button(self.white_view, text="Add Lemon")
        self.lemon_button.pack()

        self.back_button_white = tk.Button(self.white_view, text="Back")
        self.back_button_white.pack()
        

        self.white_info_label = tk.Label(self.white_view, text="", wraplength=400)
        self.white_info_label.pack()

    def create_brown_view(self):
        self.brown_view = tk.Frame(self.root)
        self.brown_view.pack_forget()  # ซ่อนหน้า brown_view

        self.milk_button_brown = tk.Button(self.brown_view, text="Milk Brown Cow")
        self.milk_button_brown.pack()

        self.back_button_brown = tk.Button(self.brown_view, text="Back")
        self.back_button_brown.pack()

        self.brown_info_label = tk.Label(self.brown_view, text="", wraplength=400)
        self.brown_info_label.pack()

    def show_input_view(self):
        self.input_view.pack()
        self.white_view.pack_forget()
        self.brown_view.pack_forget()
        self.clear_input_view()  # ล้างข้อมูลช่องข้อความ

    def show_white_cow_view(self):
        self.input_view.pack_forget()
        self.white_view.pack()
        self.brown_view.pack_forget()

    def show_brown_cow_view(self):
        self.input_view.pack_forget()
        self.white_view.pack_forget()
        self.brown_view.pack()

    def update_white_info(self, info):
        self.white_info_label.config(text=info)

    def update_brown_info(self, info):
        self.brown_info_label.config(text=info)

    def clear_input_view(self):
        self.cow_id_entry.delete(0, tk.END)  # เคลียร์ข้อมูลในช่องข้อความ

