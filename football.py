import numpy as np
import matplotlib.pyplot as plt

# Enter win probabilties after each possibility:
prob_FG_miss = 51.6
prob_FG_make = 60.3
prob_TD_miss = 55.5
prob_TD_make = 90.1

# Define the function for the inequality
def inequality(x, y):
    return prob_FG_make*x + prob_FG_miss*(1 - x) - (prob_TD_make*y + prob_TD_miss*(1 - y))

# Create plot
x = np.linspace(0, 1, 400)
y = np.linspace(0, 1, 400)
X, Y = np.meshgrid(x, y)
Z = inequality(X, Y)
plt.figure(figsize=(8, 6))
plt.contourf(X, Y, Z, levels=[-1e10, 0, 1e10], colors=['green', 'red'], alpha=0.5)
plt.contour(X, Y, Z, levels=[0], colors='black', linewidths=2)

# Add labels and title
plt.xlabel('Probability of Made FG')
plt.ylabel('Probability of Converted TD')
plt.title('Going For It or Kicking on 4th & Goal')

plt.show()

