from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

def get_image(image_path):
    image = plt.imread(image_path)
    return image / 255.0


def show_image(image):
    plt.imshow(image)
    plt.show()

def save_image(image, image_path):
    plt.imsave(image_path, image)

def error(original_image: np.ndarray, clustered_image: np.ndarray) -> float:
    # Returns the Mean Squared Error between the original image and the clustered image
    return np.mean((original_image - clustered_image) ** 2).item()

def log_metrics_table():
    df = pd.read_csv('metrics.csv')
    print("\nPerformance Metrics Summary:")
    print(df.to_string(index=False))
