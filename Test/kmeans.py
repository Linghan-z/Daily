import numpy as np


# 定义欧氏距离函数
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))


# 定义k-means函数
def k_means(points, k, centers, max_iter=100):
    # 初始化中心点
    centroids = np.array(centers)
    # 迭代k-means算法
    for i in range(max_iter):
        # 分配每个点到最近的簇
        clusters = [[] for _ in range(k)]
        for point in points:
            distances = [euclidean_distance(point, centroid) for centroid in centroids]
            closest_idx = np.argmin(distances)
            clusters[closest_idx].append(point)
        # 计算每个簇的中心
        new_centroids = []
        for cluster in clusters:
            if len(cluster) > 0:
                new_centroid = np.mean(cluster, axis=0)
                new_centroids.append(new_centroid)
            else:
                new_centroids.append(centroids[np.random.randint(k)])
            # 输出聚类结果
        print("Turn: ", i + 1)
        for j, cluster in enumerate(clusters):
            print("Cluster {}:".format(j + 1))
            for point in cluster:
                print(point)
            print("Centroid:", centroids[j])
            print()
        # 判断是否收敛
        if np.allclose(centroids, new_centroids):
            break
        centroids = new_centroids
    return clusters, centroids


def run():
    # 测试k-means函数
    points = np.array([[2, 10], [2, 5], [8, 4], [5, 8], [7, 5], [6, 4], [1, 2], [4, 9]])
    k = 3
    centers = [[2, 10], [5, 8], [1, 2]]
    clusters, centroids = k_means(points, k, centers)

    # 输出聚类结果
    for i, cluster in enumerate(clusters):
        print("Cluster {}:".format(i + 1))
        for point in cluster:
            print(point)
        print("Centroid:", centroids[i])
        print()
