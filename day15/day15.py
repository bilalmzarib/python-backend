import numpy as np
import pandas as pd
from PIL import Image

print("=== NumPy Example ===")
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Original Array:")
print(arr)
print("\nTransposed Array:")
print(arr.T)
print("\nArray + 10:")
print(arr + 10)
print("\nArray * 2:")
print(arr * 2)
print("\n====================\n")

print("=== Pandas DataFrame Example ===")
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)
print("\nFull DataFrame:")
print(df)
print("\nSummary Statistics:")
print(df.describe())
print("\nEmployees older than 30:")
print(df[df['Age'] > 30])
print("\n====================\n")

print("=== Image Processing with Pillow ===")
image_path = "day15/348753.png"

try:
    img = Image.open(image_path)
    print("\nOriginal Image Info:")
    print("Format:", img.format)
    print("Size:", img.size)
    print("Mode:", img.mode)

    resized_img = img.resize((200, 200))
    gray_img = resized_img.convert("L")
    gray_img.save("output_grayscale.jpg")

    print("\n✅ Image processed and saved as 'output_grayscale.jpg'")

except FileNotFoundError:
    print(f"\n❌ Image file '{image_path}' not found. Please add it to the same folder.")
