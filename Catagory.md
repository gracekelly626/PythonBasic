# Machine Learning 
- traditional ML often work with structured data/ say tabular data 
- 注意数据量 - 给direction 到用哪些model e.g. if the sample size < 10k & unlabeled data -> unsupervised learning
![image](https://user-images.githubusercontent.com/90355504/138587642-451a06e2-99ec-4bba-8e5d-eb1002c331f1.png)
https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html

## Supervised Learning - already know the ground thruth of input data （labeled）
知道input & output， 找出mapping的过程

#### classification - discrete output  一般做分类 
#### regression - continious output 一般做预测
#### classification vs regression 
e.g. object detection 
- 分类 -  classification
- 找出位置大小 - regression 

## Unsupervised Learning - do not know ground truth of unlabeled data need to find its underlying pattern but have algo to follow 
- clustering
- 其他 - 生成模型:
- 生成人脸，
-  GAN， sample 里有1，2，3，4，5 数字图像， 生成和sample不一样的新的1，2，3，4数字图像
-  医学影像生成： 数据有限， 通过已知肺癌CT生成肺癌CT图片以获取更多图片， GAN生成的图片不需要人工label， 再训练classifer， 分辨是否有肺癌

## Deep Learning - need to find intractable mapping
deep learning can work with both structured and unstructured data 
