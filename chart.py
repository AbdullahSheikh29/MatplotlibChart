import matplotlib.pyplot as plt

# Example data
categories = ['A', 'B', 'C', 'D']
values = [27, 49, 65, 88]

# Plot the data
plt.bar(categories, values, color='black')
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()
