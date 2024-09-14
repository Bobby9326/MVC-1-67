from tkinter import messagebox

class CowController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # เชื่อมโยงปุ่ม Submit จากหน้า Input View
        self.view.submit_button.config(command=self.on_submit)
        # เชื่อมโยงปุ่ม Reset จากหน้า Input View
        self.view.reset_button.config(command=self.reset_cows)

        # เชื่อมโยงปุ่ม Back ของหน้า White Cow
        self.view.back_button_white.config(command=self.go_back_to_input)

        # เชื่อมโยงปุ่ม Back ของหน้า Brown Cow
        self.view.back_button_brown.config(command=self.go_back_to_input)

    def on_submit(self):
        cow_id = self.view.cow_id_entry.get()
        if not cow_id.isdigit() or len(cow_id) != 8 or cow_id[0] == '0':
            messagebox.showerror("Error", "Invalid Cow ID")
        else:
            cow = self.model.get_cow_by_id(cow_id)
            if cow:
                if cow.breed.lower() == "white":
                    self.view.show_white_cow_view()
                    self.setup_white_cow_buttons()
                elif cow.breed.lower() == "brown":
                    self.view.show_brown_cow_view()
                    self.setup_brown_cow_buttons()
            else:
                messagebox.showerror("Error", "Cow not found")

    def setup_white_cow_buttons(self):
        # เชื่อมโยงปุ่มของหน้าวัวสีขาว
        self.view.milk_button.config(command=self.milk_white_cow)
        self.view.lemon_button.config(command=self.add_lemon)

    def setup_brown_cow_buttons(self):
        # เชื่อมโยงปุ่มของหน้าวัวสีน้ำตาล
        self.view.milk_button_brown.config(command=self.milk_brown_cow)

    def milk_white_cow(self):
        cow_id = self.view.cow_id_entry.get()
        cow = self.model.get_cow_by_id(cow_id)
        if cow:
            milk_type, bottles = cow.milk()
            amount_all,amount_cow = self.model.get_milk_info(cow_id)
            self.view.update_white_info(f"Milk Type: {milk_type}, Bottles: {bottles}\n จำนวนนมทั้งหมดที่วัวตัวที่ผลิต คือ {amount_cow} \n จำนวนนมทั้งหมดที่ใช้ได้ คือ {amount_all}")

    def milk_brown_cow(self):
        cow_id = self.view.cow_id_entry.get()
        cow = self.model.get_cow_by_id(cow_id)
        if cow:
            milk_type, bottles = cow.milk()
            amount_all,amount_cow = self.model.get_milk_info(cow_id)
            self.view.update_brown_info(f"Milk Type: {milk_type}, Bottles: {bottles}\n จำนวนนมทั้งหมดที่วัวตัวที่ผลิต คือ {amount_cow} \n จำนวนนมทั้งหมดที่ใช้ได้ คือ {amount_all}")

    def add_lemon(self):
        cow_id = self.view.cow_id_entry.get()
        cow = self.model.get_cow_by_id(cow_id)
        if cow:
            cow.eat_lemon = True

    def go_back_to_input(self):
        self.view.show_input_view()
    def reset_cows(self):
        self.model.reset_all_bsod()
        messagebox.showinfo("Info", "All cows' BSOD status has been reset.")