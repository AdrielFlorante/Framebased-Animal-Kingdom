import tkinter as tk
from PIL import Image, ImageTk
import os

# Get the absolute path of the Hunting directory
hunting_dir = os.path.dirname(__file__)


class Hunting(tk.Canvas):
    def __init__(self, master):
        super().__init__(master, width=1000, height=600)
        self.pack()
        self.frames = [ImageTk.PhotoImage(Image.open(os.path.join(hunting_dir, f"lion_frame{i}.png"))) for i in range(0, 4)]
        self.index = 0
        self.lion = self.create_image(50, 300, image=self.frames[self.index], anchor=tk.CENTER)

    def hunt(self):
        self.index = (self.index + 1) % len(self.frames)
        self.itemconfig(self.lion, image=self.frames[self.index])
        self.move(self.lion, 20, 0)  # Moves right
        self.after(100, self.hunt)

class HuntingError(Exception):
    # An error exception specifically for when the animation window is closed
    pass


root = tk.Tk()
root.title("Lion Hunting in the Savannah")
anim = Hunting(root)
anim.hunt()
root.mainloop()