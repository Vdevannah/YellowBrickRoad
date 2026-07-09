import tkinter as tk
from tkinter import Canvas
from Shape import Shape


class Oval(Shape):
    def __init__(self, canvas: Canvas, x: int = 20, y: int = 60, height: int = 10, width: int = 40, color: str = "blue", fill: str = None, line: int = 2, tag: str = None):
        super().__init__(canvas=canvas, x=x, y=y, color=color, fill=fill, line=line)
        self.height = height
        self.width = width

    def draw(self):
        if self.is_visible:
            print(f"Drawing oval at ({self.x_position},{self.y_position}) height {self.height} width {self.width} color {self.color} fill {self.fill} line {self.line}")
            self.shape_id = self.canvas.create_oval(
                self.x_position, self.y_position,
                self.x_position + self.height, self.y_position + self.width,
                outline=self.color, fill=self.fill, width=self.line
            )

    def erase(self):
        if self.is_visible:
            print("Erasing Oval")
            super().erase()
