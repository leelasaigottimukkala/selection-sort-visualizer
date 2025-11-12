from tkinter import *
import time

root = Tk()
root.title("Selection Sort Visualizer")
root.geometry("600x420")

canvas = Canvas(root, height=300, width=560, bg="white")
canvas.pack(pady=20)

def drawbars(data, color_array):
    c_height = 300
    c_width = 560
    margin = 20
    bar_width = (c_width - 2 * margin) / len(data)
    max_value = max(data)
    canvas.delete("all")

    for i, val in enumerate(data):
        x0 = margin + i * bar_width
        y0 = c_height - (val / max_value) * (c_height - 40)
        x1 = margin + (i + 1) * bar_width
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(val), fill="black")
    root.update()

def selectionsort(data):
    n = len(data)
    for i in range(n):
        minn = i
        for j in range(i + 1, n):
            # color current comparison
            color_array = []
            for x in range(n):
                if x == minn:
                    color_array.append("red")        # current minimum
                elif x == j:
                    color_array.append("yellow")     # current comparison
                elif x < i:
                    color_array.append("lightgreen") # sorted portion
                else:
                    color_array.append("skyblue")
            drawbars(data, color_array)
            time.sleep(0.15)

            if data[j] < data[minn]:
                minn = j

        # Swap after finding the minimum
        data[i], data[minn] = data[minn], data[i]

        # visualize the swap
        color_array = ["lightgreen" if x <= i else "skyblue" for x in range(n)]
        drawbars(data, color_array)
        time.sleep(0.3)

    # Finally, mark all as sorted
    drawbars(data, ["lightgreen" for _ in range(n)])

def start_sort():
    raw = entry.get()
    if not raw.strip():
        return
    try:
        data = list(map(int, raw.split()))
    except ValueError:
        return
    drawbars(data, ["skyblue" for _ in range(len(data))])
    selectionsort(data)

Label(root, text="Enter numbers (space-separated):", font=("Arial", 12)).pack(pady=(5,0))
entry = Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=10)

Button(root, text="Start Selection Sort", command=start_sort,
       bg="orange", fg="black", font=("Arial", 12, "bold")).pack(pady=15)

Button(root, text="Example", command=lambda: entry.delete(0, END) or entry.insert(0, "5 2 9 1 6 3"),
       bg="lightgray", font=("Arial", 11)).pack()

root.mainloop()
