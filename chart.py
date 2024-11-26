import matplotlib.pyplot as plt

# Example data
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]

# Plot the data
plt.bar(categories, values, color='skyblue')
plt.title('Example Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()
