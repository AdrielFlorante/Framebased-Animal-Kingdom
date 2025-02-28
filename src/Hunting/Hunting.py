import tkinter as tk
from PIL import Image, ImageTk


class Hunting(tk.Canvas):
    def __init__(self, master):
        super().__init__(master, width=400, height=200)
        self.pack()
        self.frames = [ImageTk.PhotoImage(Image.open(f"anim_frame{i}.png")) for i in range(0, 3)]
        self.index = 0
        self.lion = self.create_image(50, 100, image=self.frames[self.index], anchor=tk.CENTER)

    def hunt(self):
        self.index = (self.index + 1) % len(self.frames)
        self.itemconfig(self.lion, image=self.frames[self.index])
        self.move(self.lion, 5, 0)  # Moves right
        self.after(100, self.hunt)


root = tk.Tk()
anim = Hunting(root)
anim.hunt()
root.mainloop()