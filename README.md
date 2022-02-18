# Harris-corner-detection
using the Harris corner detection technique to finding the data points (key points) of an image and perform the K-means clustering technique using the strongest 100 points.

HARRIS CORNER DETECTION :
Harris Corner Detector is a corner detection operator that is commonly used in computer vision algorithms to extract corners and infer features of an image.
It is being used from many decades in the world of computer vision to detect corners from an image due to good accuracy and it is easy to implement.
STEPS :
1.	Read color image.
2.	Convert it into gray scale.
3.	Apply Harris detector for corner detection.
4.	Implement dilation to enhance corner visibility.
5.	 Collect coordinates of corners.
6.	Draw blue dots on original image according to coordinates.
This project aims to use the Harris corner detection technique to find the data points (key points) of an image and perform the K-means clustering technique using the strongest 100 points.
Imported required libraries and defined getallpoints() method. Using this method perform the Harris corner detection using the built-in function goodFeaturesToTrack() method to get the image strongest points.
![image](https://user-images.githubusercontent.com/42844121/154765163-ee58b897-2f47-4887-82e6-f7b6d3221af7.png)

          Input : Original Image
![image](https://user-images.githubusercontent.com/42844121/154765211-ee11eb5e-3eb3-4bf2-bffc-5a4089aa06e3.png)

          Output: Datapoints of image
![image](https://user-images.githubusercontent.com/42844121/154765246-2ea92ab3-4580-44e5-8223-88fce03703d3.png)

K-MEANS CLUSTER :
K-Means Clustering is an Unsupervised Learning algorithm, which groups the unlabeled dataset into different clusters. 
Here K defines the number of pre-defined clusters that need to be created in the process, as if K=2, there will be two clusters, and for K=3, there will be three clusters, and so on.
It allows us to cluster the data into different groups and a convenient way to discover the categories of groups in the unlabeled dataset on its own without the need for any training.
It is a centroid-based algorithm, where each cluster is associated with a centroid. The main aim of this algorithm is to minimize the sum of distances between the data point and their corresponding clusters.
STEPS : 
1.	Select the number K to decide the number of clusters.
2.	Select random K points or centroids. (It can be other from the input dataset).
3.	Assign each data point to their closest centroid, which will form the predefined K clusters.
4.	Calculate the variance and place a new centroid of each cluster.
5.	Repeat the third steps, which means reassign each datapoint to the new closest centroid of each cluster.
6.	If any reassignment occurs, then go to step-4 else go to FINISH.
7.	The model is ready.
Created kmeanClustering() method with data points and k(cluster=5) parameters.
 And choosing the same number of random key points as initial centroids for that created the centroid_init(self,points, k) method which returns the random k points.
 
Created find_cluster(points, k, index_k_new) to assign each data point to their closest centroid, which will form the predefined K clusters.
 
Calculating the distance of each data point from the centroids. And allocating the data point to a cluster where its distance from the centroid is minimum.
Compare the outcomes of multiple runs with different values for K and choose the best one based on a predefined criterion.
      The best one is k = 3 
      
      The below figures show the clusters for various k.
      Output :
      K = 3
 ![image](https://user-images.githubusercontent.com/42844121/154765429-006d04e1-231c-4132-8dff-7820f0f9b5af.png)
 
      K = 4 
![image](https://user-images.githubusercontent.com/42844121/154765478-e90ff8b7-b53c-4a66-9e94-782aa96027c7.png)

      K = 5
![image](https://user-images.githubusercontent.com/42844121/154765502-e445b3da-7d5e-41ea-8b2f-e46392b68aed.png)

      Detected Clusters
![image](https://user-images.githubusercontent.com/42844121/154765535-d95e3c0a-a0b9-4a7a-a714-1a8e5ed295fd.png)

Draw a bounding box for each cluster of the data points of part 2. You may use the built-in function/library (cv2.rectangle()) or any other one for this part.
Created  boundingboxCluster(self, cluster_new,  k)
OpenCV-Python is a library of Python bindings designed to solve computer vision problems. cv2.rectangle() method is used to draw a rectangle on any image.
![image](https://user-images.githubusercontent.com/42844121/154765608-a235ab68-17cc-4335-b39b-c135399084d5.png)
Parameters:
It is the image on which rectangle is to be drawn.
 ![image](https://user-images.githubusercontent.com/42844121/154765699-119b4d2d-11a0-4734-8803-677de467c2b4.png)

It is the starting coordinates of rectangle. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value). 
![image](https://user-images.githubusercontent.com/42844121/154765724-7aa0db65-7421-4abf-81b3-7601cd62fbaa.png)

It is the ending coordinates of rectangle. The coordinates are represented as tuples of two values i.e. (X1 coordinate value, Y1 coordinate value).
![image](https://user-images.githubusercontent.com/42844121/154765741-96a37f00-e3fa-444b-82b4-138b07e7b5c8.png)
 
It is the color of border line of rectangle to be drawn. For BGR, we pass a tuple. e.g.: (255, 0, 0) for blue color.
![image](https://user-images.githubusercontent.com/42844121/154765766-05ee17fd-b1f7-46bb-a9ca-e020012762d1.png)
 
It is the thickness of the rectangle border line in 2px. Thickness of -1 px will fill the rectangle shape by the specified color.
![image](https://user-images.githubusercontent.com/42844121/154765797-2166ba28-8b49-42fe-930c-7feb13d8637c.png)

       Output:
        
       BoundBox1
![image](https://user-images.githubusercontent.com/42844121/154765830-ec4c80c2-8eb5-4447-aa0e-7c9b5d1d45ca.png)

       BoundBox2
![image](https://user-images.githubusercontent.com/42844121/154765872-d03a7e44-76ae-4eff-84f6-ad4fe2c3f46a.png)

       BoundBox3
![image](https://user-images.githubusercontent.com/42844121/154765913-32e85b1c-a415-449f-9d89-f811e47fd2f2.png)



 
 


