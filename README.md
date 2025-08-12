# 📊 Matplotlib Complete Guide + Netflix Data Capstone Project

Welcome to the **Matplotlib Complete Guide** repository!  
This repo contains everything you need to master **Matplotlib** — from basic charts to advanced customizations — plus a **real-world capstone project** analyzing Netflix data to create stunning and insightful visualizations.

---

## 🚀 Features
- ✅ **Covers All Matplotlib Topics** – From plotting basics to advanced concepts
- ✅ Real-world **Netflix Dataset Analysis**
- ✅ Step-by-step explanations & clean code
- ✅ Jupyter Notebooks with outputs
- ✅ Example datasets included
- ✅ Professional & aesthetic visualizations

---

## 📂 Topics Covered
### **1. Matplotlib Core Concepts**
1. Introduction to Matplotlib
2. Basic Plots – Line, Bar, Scatter, Pie
3. Customization – Titles, Labels, Legends, Colors
4. Multiple Plots – Subplots and Layouts
5. Styling and Themes
6. Annotations and Text
7. 3D Plots
8. Working with Dates and Times
9. Saving and Exporting Figures
10. Interactive Plots

### **2. Capstone Project – Netflix Data Analysis**
In the **Capstone Project**, you’ll find:
- 📥 Loading and Cleaning Netflix dataset  
- 📊 Genre popularity trends over time  
- 📅 Release patterns by month and year  
- 🌍 Country-based content distribution  
- 🎭 Visualization of top genres, ratings, and durations  
- 🎨 Custom color palettes and styling for better storytelling  

---

## 🖼 Example Output
Here’s a sample chart created in this repo:

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

plt.plot(x, y, marker='o', color='b', linestyle='--', label='Sample Line')
plt.title("Sample Matplotlib Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()
