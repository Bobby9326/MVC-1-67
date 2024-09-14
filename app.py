import tkinter as tk
from controller import CowController
from model import CowModel, MilkModel
from view import CowView




if __name__ == "__main__":
    root = tk.Tk()
    milk_model = MilkModel()
    cow_model = CowModel(milk_model)
    view = CowView(root)  # สร้าง View
    controller = CowController(cow_model, view)  # สร้าง Controller และเชื่อมโยงกับ View
    root.mainloop()


