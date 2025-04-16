# 📘 E0-270 (O): Assignment 2 – K-Means Clustering for Image Compression

## 👤 Author
**Rishav Goswami**  
Master of Technology - AI  
Indian Institute of Science (IISc)  
Reg. No: 13-19-01-19-52-24-1-24708  
📧 `rishavg@iisc.ac.in`

---

## 📝 Project Overview

This project implements the **K-Means clustering algorithm from scratch** in Python to compress RGB images by reducing the number of unique colors. The goal is to analyze how different numbers of clusters \(k\) affect the reconstructed image quality and Mean Squared Error (MSE).

---

## 📂 Files Included

| File                          | Description                                      |
|-------------------------------|--------------------------------------------------|
| `main.py`                     | Main script for running K-Means image compression |
| `model.py`                    | Contains the K-Means algorithm implementation     |
| `utils.py`                    | Helper functions for image processing and plotting |
| `image_clustered_{k}.jpg`     | Compressed images for various values of \(k\)     |
| `mse_vs_k.png`                | Plot of MSE versus number of clusters             |
| `report.tex`                  | LaTeX source code for the final report            |
| `README.md`                   | You're reading it!                               |

---

## 🔍 Methodology Summary

- **Input**: A 512×512 RGB image
- **Algorithm**: K-Means clustering with random initialization
- **Steps**:
    1. Initialize cluster centers by selecting \(k\) random pixels
    2. Assign each pixel to its nearest cluster using Euclidean distance
    3. Update cluster centers based on the mean of assigned pixels
    4. Repeat until convergence or max iterations (100)
- **Evaluation**: Mean Squared Error (MSE) between original and compressed images

---

## 🛠️ How to Run

1. Clone or download the repository
    ```bash
    git clone
    ```
2. Install required Python packages:
   ```bash
   pip install numpy matplotlib pillow
   ```
3. Run the code
    ```bash
    python main.py
   ```
4. Output
   - Compressed image files will be saved as image_clustered_{k}.jpg 
   - MSE plot saved as mse_vs_k.png

---

## 📊 Results

- Cluster counts tested: `k = 2, 5, 10, 20, 50`
- **Observation**: As \(k\) increases, image quality improves and MSE decreases
- **Trade-off**: More clusters = better quality, but also higher computation

    <img src="mse_vs_k.png" alt="mse_vs_k" style="width: 350px;"/>

---

## 🖼️ Output Images

Each image below shows the result of compressing the original image using different numbers of clusters:


| Cluster Count                          | Compressed Image                                                     |
|-------------------------------|----------------------------------------------------------------------|
| k = 2                     | <img src="image_clustered_2.jpg" alt="k=2" style="width: 250px;"/>   |
| k = 5                    | <img src="image_clustered_5.jpg" alt="k=5" style="width: 250px;"/>   |
| k = 10                    | <img src="image_clustered_10.jpg" alt="k=10" style="width: 250px;"/> |
| k = 20     | <img src="image_clustered_20.jpg" alt="k=20" style="width: 250px;"/> |
| k = 50                | <img src="image_clustered_50.jpg" alt="k=50" style="width: 250px;"/> |

---