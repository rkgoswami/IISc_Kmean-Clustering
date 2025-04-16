import numpy as np
import time
from memory_profiler import memory_usage

class KMeans:
    def __init__(self, k: int, epsilon: float = 1e-6) -> None:
        self.num_clusters = k
        self.cluster_centers = None
        self.epsilon = epsilon
        self.n_iter_ = 0  # Track number of iterations
    
    def fit(self, X: np.ndarray, max_iter: int = 100) -> None:
        # Initialize cluster centers (need to be careful with the initialization,
        # otherwise you might see that none of the pixels are assigned to some
        # of the clusters, which will result in a division by zero error)

        self.n_iter_ = 0
        n_samples = X.shape[0]
        indices = np.random.choice(n_samples, self.num_clusters, replace=False)
        self.cluster_centers = X[indices]

        for _ in range(max_iter):
            self.n_iter_ += 1
            # Compute squared distances
            diff = X[:, np.newaxis] - self.cluster_centers
            squared_distances = np.sum(diff ** 2, axis=2)
            labels = np.argmin(squared_distances, axis=1)

            new_centers = np.zeros_like(self.cluster_centers)
            for i in range(self.num_clusters):
                mask = (labels == i)
                if np.sum(mask) == 0:
                    # Assign a random data point if cluster is empty
                    new_center = X[np.random.choice(n_samples)]
                else:
                    new_center = X[mask].mean(axis=0)
                new_centers[i] = new_center

            # Check for convergence
            delta = np.max(np.linalg.norm(self.cluster_centers - new_centers, axis=1))
            if delta < self.epsilon:
                break
            self.cluster_centers = new_centers
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        # Predicts the index of the closest cluster center for each data point
        diff = X[:, np.newaxis] - self.cluster_centers
        squared_distances = np.sum(diff ** 2, axis=2)
        return np.argmin(squared_distances, axis=1)
    
    def fit_predict(self, X: np.ndarray, max_iter: int = 100) -> np.ndarray:
        self.fit(X, max_iter)
        return self.predict(X)
    
    def replace_with_cluster_centers(self, X: np.ndarray) -> np.ndarray:
        # Returns an ndarray of the same shape as X
        # Each row of the output is the cluster center closest to the corresponding row in X
        labels = self.predict(X)
        return self.cluster_centers[labels]
