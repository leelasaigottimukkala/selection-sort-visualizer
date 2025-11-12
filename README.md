# Selection Sort Visualizer using Python Tkinter

This project is a **visual representation of the Selection Sort algorithm**, built using **Python's Tkinter GUI library**. The program displays bars of different heights that represent array elements and visually demonstrates how Selection Sort repeatedly selects the minimum element from the unsorted part and places it in the correct position.

---

## 🚀 Features

* 🔢 **Custom user input** for entering any list of numbers.
* 🎨 **Color-coded visualization**:

  * **Red** → Currently selected minimum element
  * **Yellow** → Elements being compared
  * **Blue** → Unsorted elements
  * **Green** → Sorted elements
* 🖥️ **Real-time animations** showing every comparison and swap.
* 📘 Great educational tool for understanding Selection Sort.

---

## 📌 How Selection Sort Works

Selection Sort divides the list into two parts: a **sorted section** on the left and an **unsorted section** on the right. The algorithm repeatedly finds the **smallest element** in the unsorted portion and swaps it with the first unsorted element.

### Steps:

1. Start from index 0.
2. Find the minimum element in the unsorted part of the list.
3. Swap it with the element at the current index.
4. Expand the sorted portion by one.
5. Repeat until the entire list is sorted.

---

## 📂 Project Structure

```
SelectionSortVisualizer/
│
├── selection_sort_visualizer.py   # Main program file
├── README.md                      # Project documentation
```

---

## 🛠️ Requirements

* Python 3.x
* Tkinter (comes pre-installed with Python)

---

## ▶️ How to Run

1. Clone the repository:

```
git clone https://github.com/yourusername/selection-sort-visualizer.git
```

2. Navigate to the folder:

```
cd selection-sort-visualizer
```

3. Run the program:

```
python selection_sort_visualizer.py
```

---

## 📷 Screenshots

## 📷 Screenshots


### 🎨 During Sorting
![During Sorting](screenshots/output2.png)

### ✅ Final Sorted Output
![Final Output](screenshots/output1.png)

---

## 📊 Time & Space Complexity

| Case         | Time Complexity |
| ------------ | --------------- |
| Best Case    | O(n²)           |
| Average Case | O(n²)           |
| Worst Case   | O(n²)           |

**Space Complexity:** O(1) – In-place sorting

---

## ⭐ Why This Project?

This project is perfect for:

* Students learning DSA
* Teachers demonstrating sorting algorithms
* Beginners exploring animations in Tkinter
* Anyone who wants a visual understanding of Selection Sort

---

## ❤️ Contributing

Contributions are always welcome! Submit issues or pull requests to improve the project.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🙏 Acknowledgments

Thank you for viewing this project! If you find it helpful, please ⭐ the repository.
