import numpy as np
import pandas as pd
from PIL import Image, ImageFilter

# ---------------------------
# Exercise 1: 
# ---------------------------
print("=== Exercise 1: NumPy Array Manipulation ===")

arr = np.random.randint(1, 101, size=(10, 10))
print("Generated Array:\n", arr)

mean_val = np.mean(arr)
median_val = np.median(arr)
std_val = np.std(arr)

print("\nMean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", std_val)

diagonal = np.diag(arr)
print("\nMain Diagonal:", diagonal)

greater_than_80 = arr[arr > 80]
print("\nValues Greater Than 80:", greater_than_80)

arr[arr < 30] = 0
print("\nArray after replacing values < 30 with 0:\n", arr)

print("\n==============================\n")

# ---------------------------
# Exercise 2: 
# ---------------------------
print("=== Exercise 2: Pandas Data Analysis ===")

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Age': [25, 30, 45, 35, 40, 29],
    'Department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'Finance'],
    'Salary': [50000, 60000, 75000, 52000, 68000, 64000]
}

df = pd.DataFrame(data)

df['Bonus'] = df['Salary'] * 0.10

print("\nDataFrame with Bonus:\n", df)

grouped = df.groupby('Department')[['Salary', 'Bonus']].mean()
print("\nAverage Salary and Bonus by Department:\n", grouped)

highest_salary = df.loc[df.groupby('Department')['Salary'].idxmax()]
print("\nHighest Salary in Each Department:\n", highest_salary)

# Create age groups
bins = [20, 30, 40, 50]
labels = ['20-30', '31-40', '41-50']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

pivot = df.pivot_table(values='Salary', index='Department', columns='AgeGroup', aggfunc='mean')
print("\nPivot Table - Average Salary by Department and Age Group:\n", pivot)

print("\n==============================\n")

# ---------------------------
# Exercise 3: 
# ---------------------------
print("=== Exercise 3: Image Filter Application ===")

try:
    original = Image.open("input.jpg").resize((200, 200))

    blur_img = original.filter(ImageFilter.BLUR)
    contour_img = original.filter(ImageFilter.CONTOUR)
    emboss_img = original.filter(ImageFilter.EMBOSS)

    collage_width = 800
    collage_height = 200
    collage = Image.new('RGB', (collage_width, collage_height))

    collage.paste(original, (0, 0))
    collage.paste(blur_img, (200, 0))
    collage.paste(contour_img, (400, 0))
    collage.paste(emboss_img, (600, 0))

    collage.save("image_collage.jpg")
    print("✅ Collage saved as 'image_collage.jpg'")

except FileNotFoundError:
    print("❌ 'input.jpg' not found. Please place an image with that name in the same folder.")
