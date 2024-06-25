from tkinter import *

class Paint:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint App")

        self.canvas = Canvas(root, width=800, height=400, bg='white')
        self.canvas.pack()

        # color default
        self.color = "Green"

        # create frame for buttons
        self.button_frame = Frame(root)
        self.button_frame.pack(pady=10)

        # create select color buttons
        self.create_color_buttons()

        # create reset button
        self.reset_button = Button(self.button_frame, text="Reset", command=self.reset_canvas, font=("Arial", 12),
                                   width=10, height=2)
        self.reset_button.pack(side=LEFT, padx=5, pady=5)

        self.canvas.create_text(400, 50, text="Hello, Tkinter Canvas!", font=("Arial", 20), fill="blue")
        self.canvas.bind("<B1-Motion>", self.paint)

    def create_color_buttons(self):
        colors = ["red", "green", "blue", "yellow"]
        for color in colors:
            button = Button(self.root, text=color.capitalize(), bg=color, command=lambda c=color: self.set_color(c), width=10, height=2)
            button.pack(side=LEFT, padx=5, pady=5)

    def set_color(self, new_color):
        self.color = new_color
        print(f"Selected color: {self.color}")

    def paint(self, event):
        x1, y1, x2, y2 = (event.x - 3), (event.y - 3), (event.x + 3), (event.y + 3)
        self.canvas.create_oval(x1, y1, x2, y2, outline=self.color, width=10)

    def reset_canvas(self):
        self.canvas.delete("all")
        self.canvas.create_text(400, 100, text="Hello, Tkinter!", font=("Arial", 20), fill="blue")

