import matplotlib.pyplot as plt
import numpy as np

def visualize_data(data):
  """Visualizes the data using a line graph."""
  plt.plot(data)
  plt.xlabel("X")
  plt.ylabel("Y")
  plt.show()

if __name__ == "__main__":
  data = np.random.randint(0, 100, 100)
  visualize_data(data)
