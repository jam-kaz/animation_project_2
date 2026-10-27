import tkinter as tk
import math
from src.models.animation_model import AnimationModel

class App:
    def __init__(self, width=600, height=600):
        self.root = tk.Tk()
        self.root.title("Превращение круга в треугольник")
        self.width = width
        self.height = height
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg="#E0E0E0")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.model = AnimationModel(radius=180)
        self.time_counter = 0.0
        self.is_running = True
        self.root.bind("<space>", self.toggle_pause)
        self.root.bind("<r>", self.reset_animation)
        self.root.bind("<R>", self.reset_animation)
        self.animate()

    def toggle_pause(self, event):
        self.is_running = not self.is_running
        if self.is_running:
            self.animate()

    def reset_animation(self, event):
        self.time_counter = 0.0
        self.update_canvas()

    def update_canvas(self):
        self.canvas.delete("all")
        morph_ratio = (math.sin(self.time_counter) + 1.0) / 2.0
        points = self.model.get_points(morph_ratio)
        center_x = self.width // 2
        center_y = self.height // 2
        pixel_points = []
        for x, y in points:
            pixel_points.append(center_x + x)
            pixel_points.append(center_y - y)
        self.canvas.create_polygon(pixel_points, fill="#D3D3D3", outline="black", width=4)

    def animate(self):
        if not self.is_running:
            return
        self.update_canvas()
        self.time_counter += 0.08
        self.root.after(16, self.animate)

    def run(self):
        self.root.mainloop()
