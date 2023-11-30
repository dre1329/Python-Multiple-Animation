import tkinter as tk
import random
from PIL import Image, ImageTk

root = tk.Tk()
root.title("dre multiple animation")


background_image = Image.open("background.jpg")
background_image = ImageTk.PhotoImage(background_image)


canvas_width = 1920
canvas_height = 1080

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()


canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

num_fish = 20
fish_radius = 50
fish_speed = 7
fish_images = []


def create_bubble():
    x = random.randint(0, canvas_width)
    y = canvas_height
    radius = random.randint(5, 20)
    speed = random.uniform(1, 5)
    bubble = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="lightblue")
    return bubble, speed

bubble_images = [create_bubble() for _ in range(20)]

for _ in range(num_fish):
    x = random.randint(fish_radius, canvas_width - fish_radius)
    y = random.randint(fish_radius, canvas_height - fish_radius)
    dx = random.uniform(-fish_speed, fish_speed)
    dy = random.uniform(-fish_speed, fish_speed)

    fish_image = Image.open("fish.png")
    fish_image = fish_image.resize((2 * fish_radius, 2 * fish_radius))
    fish_image = ImageTk.PhotoImage(fish_image)

    fish = canvas.create_image(x, y, image=fish_image)
    fish_images.append((fish, dx, dy, fish_image))

def update():
    for i in range(num_fish):
        fish, dx, dy, fish_image = fish_images[i]
        x, y = canvas.coords(fish)

        if x - fish_radius < 0 or x + fish_radius > canvas_width:
            dx = -dx
        if y - fish_radius < 0 or y + fish_radius > canvas_height:
            dy = -dy

        canvas.move(fish, dx, dy)
        fish_images[i] = (fish, dx, dy, fish_image)

    for bubble, speed in bubble_images:
        canvas.move(bubble, 0, -speed)
        x1, y1, x2, y2 = canvas.coords(bubble)
        if y2 < 0:
            canvas.delete(bubble)
            bubble_images.remove((bubble, speed))
            create_bubble()

    root.after(50, update)

update()
root.mainloop()