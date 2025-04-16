import time
import csv
import numpy as np
import matplotlib.pyplot as plt
from memory_profiler import memory_usage
from model import KMeans
from utils import get_image, error

def collect_metrics(k, num_trials=10):
    """Collect performance metrics for a specific k value."""
    metrics = {
        'runtimes': [],
        'memory_usages': [],
        'iterations': [],
        'mse_values': []
    }

    for t in range(num_trials):
        print(f"Running the trail {t}")
        # Fresh image load for each trial
        original_image = get_image('image.jpg')
        X = original_image.reshape(-1, 3)

        # Initialize model
        kmeans = KMeans(k)

        # Time measurement
        start_time = time.time()

        # Memory measurement
        mem_usage = memory_usage((kmeans.fit, (X,)), retval=True)

        # Store metrics
        metrics['runtimes'].append(time.time() - start_time)
        metrics['memory_usages'].append(max(mem_usage[0]))
        metrics['iterations'].append(kmeans.n_iter_)

        # Calculate MSE
        X_clustered = kmeans.replace_with_cluster_centers(X)
        clustered_image = X_clustered.reshape(original_image.shape)
        metrics['mse_values'].append(error(original_image, clustered_image))

    return {
        'k': k,
        'avg_runtime': np.mean(metrics['runtimes']),
        'avg_memory': np.mean(metrics['memory_usages']),
        'avg_iterations': np.mean(metrics['iterations']),
        'mse_mean': np.mean(metrics['mse_values']),
        'mse_std': np.std(metrics['mse_values'])
    }

def save_metrics_to_csv(metrics_list):
    """Save collected metrics to CSV file."""
    with open('metrics.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=metrics_list[0].keys())
        writer.writeheader()
        writer.writerows(metrics_list)

def plot_mse(metrics_list):
    """Generate and save MSE vs k plot."""
    ks = [m['k'] for m in metrics_list]
    mse_means = [m['mse_mean'] for m in metrics_list]

    plt.figure(figsize=(10, 6))
    plt.plot(ks, mse_means, 'b-o')
    plt.xlabel('Number of clusters (k)')
    plt.ylabel('Mean Squared Error')
    plt.title('MSE vs Number of Clusters')
    plt.grid(True)
    plt.savefig('mse_vs_k.png')
    plt.close()

def main():
    ks = [2, 5, 10, 20, 50]
    metrics_list = []

    for k in ks:
        print(f"Start processing k={k}.")
        metrics = collect_metrics(k)
        metrics_list.append(metrics)
        print(f"End processing k={k}.")

    save_metrics_to_csv(metrics_list)
    plot_mse(metrics_list)
    print("Metrics collection complete. Results saved to metrics.csv and mse_vs_k.png")

if __name__ == '__main__':
    main()