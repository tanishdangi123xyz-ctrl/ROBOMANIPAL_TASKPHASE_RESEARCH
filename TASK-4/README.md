# AI TASK-3

### *K-NEAREST NEIGHBOURS*
* Pick 3-5 as the number of points you want. Doesnt have to be 3-5 but has to be odd.
* Then we find the distance of all points from the point whos class we want to find.
* Pick the nearest 3-5 points and the class of the majority of the nearest points is the class of the point.
* No learning required for this classification as the points existing in the space is the learning for the model.
* It can be n-dimentional.

### *K-MEAN*
* K is the number of clusters we are looking for.
* Start by choosing random centroids but not completely randomly. They should be in between the min and max of the data.
* Find the distance of each point form each centroid and allot the point the same class as the nearest centroid.
* After this change the position of each centroid to the mean distance between the points of the same class as the centroid.
* Keep itterating this until the centroids stop changing positions.
* It can have n-dimentions.
* Then predict the point as per the cluster it belongs to.

### *SUPPORT VECTOR MACHINES*
* Find the line with the maximum distance from the support vectors.
* The line should maximise the margin between the support vectors and the line.
* For data in real life we use kernals which add a hyperplane.
* So we add a new plane instead of a line that maximises the margins.
* ##### Soft Margin:
  * They allow misclassifications upto a certain point so that a better model can be chosen.
  * The soft margin shouldnt be too high.

### DECISION TREE
* Makes branches of the dataset given.
* When the model is needed to predict it goes down those branches and then answers the question.
* Start by creating a root node.
* Keep track of the outcome for each brach.
* Keep splitting dataset till the answers become more definitive.

### RANDOM FOREST
* Decision tree might be random as the sequence of the features might be different.
* Create multiple decision tress and train them on the same data.
* Each decision tree will give the outcome and the outcome of the majority of the decision tree will be chosen.
* This helps minimise the risk of misclassification.
* Its a better system of classification with multiple decision trees and lesser chances of misclassification.

### DBSCAN
* ##### Flaws of K-MEANS:
  * Need to define the amount of clusters before the clustering.
  * K-MEANS is very sensitive to outliers.
  * As K-MEANS is a centroid based algo so when a dataset of non spherical shapes is given it doesnt cluster the data properly.
* ##### DBSCAN:
  * Density based clustering algo.
  * Finds the dense and sparse regions.
  * It classifies the dense clusters differently.
  * 3 Types of points: Core, Boundary, and Noise.

### GRADIENT BOOSTING
* Builds a strong model by combining many weak models one after another.
* Each new model is trained to fix the errors (residuals) left by the previous one.
* Starts with a simple prediction — usually just the mean of the target.
* Calculates the residual (actual − predicted) and trains the next tree on that.
* New tree's output is added to the previous prediction after being scaled by the learning rate.
* Keeps repeating this process until the specified number of trees is reached.
* The "gradient" refers to gradient descent — each tree is fitted to the negative gradient of the loss function.
* _*Random Forest*_: Trees are built independently and their results are averaged.
* _*Gradient Boosting*_: Trees are built sequentially, each one correcting the last.
* NO REGULARIZATION AND TOO MANY TRESS ARE THE REASON FOR OVERFITTING.

### XGBOOST
* ##### ADVANTAGES:
  * Uses gradient boost. Can use any loss function as gradient boost.
  * Parallel processing as it makes multiple tress at the same time. IT DOESNT MAKE MODELS PARALLELLY AS THATS NOT POSSIBLE CUS MODELING IS A SEQUENCIAL PROCESS.
  * Uses optimized data structures. Other ml algos store data rowwise. XG stores columnwise (called column block). Operate on each column block as this would allow it to make multiple decision tress in parallel.
  * Uses cache memory optimally. Uses historial based training. It makes a histogram for all numirical features. It stores the bin values in cache as the bin values will be needed constantly. It uses other methods too,
  * Uses out of core computing. Divide large dataset that arent computable into chunks and individually train the model on chunks sequintially.
  * Uses distributed computing. Train and distribute your task to different nodes. It can use multiple devices to train the same model which is very useful for a lot of datasets.
  * GPU can be used.
  * Its very flexible to most programming languages.
* ##### XGBOOST:
  * Stands for Extreme Gradient Boosting.
  * It is an optimised and enhanced version of gradient boosting.
  * Still builds trees sequentially such that each tree corrects the errors of the previous one.
  * Uses second-order gradients: Vanilla GB uses only the first derivative. XGBoost uses both the first and second derivative that gives a more precise picture of the error surface.
  * Uses L1 and L2 regularization.
  * L1: Sum of all absolute values of weights. Removes all useless features.
  * L2: Sum of all squares of the weights. Shrinks all the weights.
  * Both of these remove overfitting which is a common problem in gradient boosting.
  * Removes noise by subsampling as each tree only sees a small fraction of the data.

### NAIVE BAYES
* Based on Bayes' Theorem, which uses probability to classify data points.
* It calculates how likely a point belongs to a certain class based on the prior knowledge of its features.
* The "Naive" assumption: It assumes that every feature in the dataset is completely independent of every other feature.
* Even though this assumption is almost never true in real life (features are usually correlated), the model still performs surprisingly well.
* Very fast and computationally efficient because it just relies on counting frequencies and multiplying probabilities instead of complex iterative training.
* Works exceptionally well for text classification tasks, like spam filtering and sentiment analysis.

### ENSEMBLE SYSTEMS
* Combination of multiple models.
* The idea is about the wisdom of the crowd i.e. a group of multiple week models will outperform any one singular model.
* Each model individually has bias and variance. But together that solves the problems of it.
* ##### TYPES OF ENSEMBLE LEARNING:
  * ##### VOTING:
    * MAJORITY OF MODELS PREDICTION WILL BE CHOSEN.
  * ##### BAGGING:
    * SAME MODEL, DIFFERENT DATA.
  * ##### BOOSTING:
    * LEARNS FROM ERRORS OF PREVIOUS MODEL.
  * ##### STACKING:
    * SAME AS VOTING BUT A MODEL IS ADDED IN THE END WHICH UNDESTANDS OUTPUTS FROM EACH ALGO AND PROVIDES IMPORTANCE AND WEIGHTS TO THE OUTCOME OF EACH ALGO.