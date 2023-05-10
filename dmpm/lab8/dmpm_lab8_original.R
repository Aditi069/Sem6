# installing required packages
library(animation) 
library(factoextra) # clustering 
library(cluster) # clustering algorithms
library(dplyr) # data manipulation
library(gridExtra) # to work with grid graphics
library(tidyverse) # data manipulation
library(ggplot2) # plotting graphs
library(purrr) 

#load data
data=read.csv(choose.files())
View(data)
summary(data)
data.class(data)
head(data)
tail(data)

# remove rows with null values
data = na.omit(data)
View(data)

# replace the row no. with the country column
data = data %>% remove_rownames %>%column_to_rownames(var="Country")
View(data)

# scale all the numeric values to have a mean of 0 and sd of 1
data1 = data %>% mutate(across(where(is.numeric), scale)) #skip 
View(data1)
str(data1)

# scale each variable to have a mean of 0 and sd of 1
data = scale(data)
head(data)
View(data)

#Find the Optimal Number of Clusters
km2 <- kmeans(data, centers = 2, nstart = 25)
km2
str(km2)
fviz_cluster(km2, data = data)

#Number of Clusters vs. the Total Within Sum of Squares
#Typically when we create this type of plot we look for an "elbow" 
#where the sum of squares begins to "bend" or level off. 
#This is typically the optimal number of clusters
# fviz_nbclust() function to create a plot of the 
# number of clusters vs. the total within sum of squares
fviz_nbclust(data, kmeans, method = "wss")


#Number of Clusters vs. Gap Statistic
#Gap statistic, which compares the total intra-cluster 
#variation for different values of k with their expected 
#values for a distribution with no clustering.

#calculate gap statistic based on number of clusters
gap_stat1 <- clusGap(data,
                     FUN = kmeans,
                     nstart = 25,
                     K.max = 10,
                     B = 50)
#plot number of clusters vs. gap statistic
fviz_gap_stat(gap_stat1)

#From the plot we can see that gap statistic is 
#highest at k = 2 clusters


# kmeans with centers 3, 4 and 5

km3 <- kmeans(data, centers = 3, nstart = 25)
km3
fviz_cluster(km3, data = data)

km4 <- kmeans(data, centers = 4, nstart = 25) 
km4
fviz_cluster(km4, data = data)

km5 <- kmeans(data, centers = 5, nstart = 25)  
km5
fviz_cluster(km5, data = data)


#Comparing the Plots
plot1 <- fviz_cluster(km2, geom = "point", data = data) + ggtitle("k = 2")
plot1

plot2 <- fviz_cluster(km3, geom = "point", data = data) + ggtitle("k = 3")
plot2

plot3 <- fviz_cluster(km4, geom = "point", data = data) + ggtitle("k = 4")
plot3

plot4 <- fviz_cluster(km5, geom = "point", data = data) + ggtitle("k = 5")
plot4

grid.arrange(plot1, plot2, plot3, plot4, nrow = 2)

# let's choose K = 2 and run the K-means again
set.seed(123)
km2 <- kmeans(data, centers = 2, nstart = 20)
km2

## Calculating the silhouette coefficient
# Si > 0 means that the observation is well clustered. The closest it is to 1, the best it is clustered.
# Si < 0 means that the observation was placed in the wrong cluster.
# Si = 0 means that the observation is between two clusters.
sil <- silhouette(km2$cluster, dist(data))
fviz_silhouette(sil)

# caluculating Calinski-Harabasz index
round(calinhara(data,km2$cluster),digits=2)

# Calculates Davies-Bouldin's index
d<-dist(data)
print(index.DB(data, km2$clustering,d, centrotypes="centroids")) 


grpMeat <- kmeans(data[,c("RedMeat","WhiteMeat")],centers = 2, nstart = 25)
grpMeat
str(grpMeat)
fviz_cluster(grpMeat, data = data[,c("RedMeat","WhiteMeat")])

# Kmeans for Milk and Cereals 
breakfast <- kmeans(data[,c("Milk","Cereals","RedMeat")],centers = 3, nstart = 25)
breakfast
str(breakfast)
fviz_cluster(breakfast, data = data[,c("Milk","Cereals","RedMeat")])



