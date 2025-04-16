from model import KMeans
from utils import get_image, save_image, error
import matplotlib.pyplot as plt

def main():
    ks = [2, 5, 10, 20, 50]
    mse_list = []

    for k in ks:
        original_image = get_image('image.jpg')
        img_shape = original_image.shape
        X = original_image.reshape(-1, 3)

        kmeans = KMeans(k)
        kmeans.fit(X)

        X_clustered = kmeans.replace_with_cluster_centers(X)
        clustered_image = X_clustered.reshape(img_shape)

        mse = error(original_image, clustered_image)
        mse_list.append(mse)
        save_image(clustered_image, f'image_clustered_{k}.jpg')

    plt.plot(ks, mse_list, 'b-o')
    plt.xlabel('Number of clusters (k)')
    plt.ylabel('Mean Squared Error')
    plt.title('MSE vs Number of Clusters')
    plt.savefig('mse_vs_k.png')
    plt.show()

if __name__ == '__main__':
    main()