import cv2
import numpy as np
import random
import copy

color = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (0, 0, 0), (255, 0, 255), (0, 255, 255), (255, 255, 0), (255, 255, 255)]
image_path = "C:\\Users\\saika\\Downloads\\image1.jpg"
k_val = 3
class ClusterInfo:
    def show_save(self,title, image):
        cv2.imshow(title, image)
        cv2.imwrite('fig/' + title + '_' + str(k_val) + '.jpg', image)

    def centroid_init(self,points, k):
        index_k = []
        index = np.random.choice(points.shape[0], k, replace=False)
        for j in range(0, k):
            index_k.append([points[index[j]][0, 0], points[index[j]][0, 1]])
        print("k---->> ",index_k)
        return index_k

    def find_cluster(self,points, k, index_k):
        cluster = []
        for i in points:
            x = i[0, 0]
            y = i[0, 1]
            dist = []
            for j in range(0, k):
                xk = index_k[j][0]
                yk = index_k[j][1]
                dist.append([((((x - xk) ** 2) + ((y - yk) ** 2)) ** 0.5), j])
            dist.sort()
            cluster.append([x, y, dist[0][1], (x ** 2) + (y ** 2)])
        return cluster

    def showcluster(self,cluster_new, k):
        img1 = cv2.imread(image_path)
        obj1=ClusterInfo()
        for j in range(0, k):
            tmp = [t[0:2] for t in cluster_new if t[2] == j]
            for i in range(0, len(tmp)):
                cv2.circle(img1, (tmp[i][0], tmp[i][1]), 3, color[j], -1)
        obj1.show_save('detected clusters', img1)

    def Average(self,lst):
        if len(lst) > 0:
            return sum(lst) / len(lst)
        else:
            print("cluster zero len")
            return 0

    def centroid_find(self,cluster, k):
        index_k_new = []
        obj1 = ClusterInfo()
        for j in range(0, k):
            ave = obj1.Average([t[3] for t in cluster if t[2] == j])
            for i in range(0, len(cluster)):
                if cluster[i][2] == j:
                    cluster[i][3] = abs(cluster[i][3] - ave)
            tmp = sorted([t for t in cluster if t[2] == j], key=lambda x: x[3])
            index_k_new.append([tmp[0][0], tmp[0][1]])
        return index_k_new


class HarrisCornerDetectandKmeans():
    def getallpoints(self):
        obj1=ClusterInfo()
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        keypoints = cv2.goodFeaturesToTrack(gray, 100, 0.05, 15)
        keypoints = np.int0(keypoints)
        for i in keypoints:
            x, y = i.ravel()
            cv2.circle(img, (x, y), 3, (255, 0, 0), -1)

        obj1.show_save('data points of image', img)
        return keypoints

    def kmeanClustering(self,points, k):
        obj1 = ClusterInfo()
        cluster_old = []
        cluster_new = []
        index_k_new = []
        indexofkmeanold = []
        indexofkmean = []
        index_k_new = obj1.centroid_init(points, k)
        cluster_new = obj1.find_cluster(points, k, index_k_new)
        indexofkmean.append(copy.deepcopy(index_k_new))

        cnt = 0
        while indexofkmeanold != index_k_new:
            index_k_old = copy.deepcopy(index_k_new)
            cluster_old = copy.deepcopy(cluster_new)
            index_k_new = obj1.centroid_find(cluster_new, k)
            cluster_new = obj1.find_cluster(points, k, index_k_new)

            diff1 = []
            for elem in [x[0:3] for x in cluster_new]:
                if elem not in [x[0:3] for x in cluster_old]:
                    diff1.append(elem)

            cnt = cnt + 1
            if ((len(diff1) / len(cluster_new)) <= 0.1) & cnt > 50:
                break
            elif cnt > 100:
                break

            if index_k_new in indexofkmean:
                break
            indexofkmean.append(copy.deepcopy(index_k_new))

        obj1.showcluster(cluster_new, k)
        #print(cnt)
        return cluster_new
        #obj1.cluster_boun_box(cluster_new, k)

    def boundingboxCluster(self,cluster_new, k):
        obj1 = ClusterInfo()
        img1 = cv2.imread(image_path)
        img2 = cv2.imread(image_path)
        img3 = cv2.imread(image_path)
        for i in range(0, len(cluster_new)):
            cluster_new[i][3] = (cluster_new[i][0] ** 2) + (cluster_new[i][1] ** 2)
        for j in range(0, k):
            tmp = sorted([t for t in cluster_new if t[2] == j], key=lambda x: x[3])
            x = tmp[0][0]
            y = tmp[0][1]
            x1 = tmp[len(tmp) - 1][0]
            y1 = tmp[len(tmp) - 1][1]
            image = cv2.rectangle(img1, (x1, y1), (x, y), color[j], 2)
            cv2.putText(image, 'Object' + str(j), (x + 20, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 3)
            obj1.show_save("bound box1", image)

            tmp = sorted([t for t in cluster_new if t[2] == j], key=lambda x: x[0])
            x = tmp[0][0]
            x1 = tmp[len(tmp) - 1][0]
            tmp = sorted([t for t in cluster_new if t[2] == j], key=lambda x: x[1])
            y = tmp[0][1]
            y1 = tmp[len(tmp) - 1][1]
            image1 = cv2.rectangle(img2, (x1, y1), (x, y), color[j], 2)
            cv2.putText(image1, 'Object' + str(j), (x + 20, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 3)
            obj1.show_save("bound box2", image1)
            
            tmp = sorted([t for t in cluster_new if t[2] == j], key=lambda x: x[0])
            x = tmp[0][0]
            x1 = tmp[len(tmp) - 1][0]
            tmp = sorted([t for t in cluster_new if t[2] == j], key=lambda x: x[1])
            y = tmp[0][1]
            y1 = tmp[len(tmp) - 1][1]
            image2 = cv2.rectangle(img2, (x1, y1), (x, y), color[j], 2)
            cv2.putText(image1, 'Object' + str(j), (x + 20, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 3)
            obj1.show_save("bound box3", image2)


obj=HarrisCornerDetectandKmeans()
points=obj.getallpoints()
print(points)
cluster=obj.kmeanClustering(points, k_val)
obj.boundingboxCluster(cluster, k_val)
cv2.waitKey(0)
cv2.destroyAllWindows()