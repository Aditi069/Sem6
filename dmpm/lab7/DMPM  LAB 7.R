# The purpose of this dataset is to predict 
# tumor log volumn based on predictor information
# the dataset contains biopsy results  for n = 97 men of various ages

library(tree)
library(dplyr)
library(caTools)
library(party)
library(magrittr)
library(Metrics)
library(rpart)
library(rpart.plot)
library(caret)


set.seed(678) # sampling function
# read the file -> "prostate.csv"  
data = read.csv(file.choose())
View(data)
dim(data)
str(data)
head(data)
tail(data)

# to check if there are any null values in the dataset
is.na(data)
which(is.na(data))

# to shuffle the data
shuffled <- sample(1:nrow(data))
#shuffled=sample(data)
shuffled
# to put records in the shuffled order
data <- data[shuffled, ]
head(shuffled)

glimpse(data)  

#to generate random list from the shuffled data
sample(1:nrow(data))

pstree <- tree(lcavol ~., data=data, mincut=1) 
#  The minimum number of observations to include in either child node  =1  
pstree

pstcut1 <- prune.tree(pstree,k=5)
plot(pstcut1)
text(pstcut1)
pstcut1

pstcut2 <- prune.tree(pstree,k=3)
plot(pstcut2)
text(pstcut2)
pstcut2

pstcut3 <- prune.tree(pstree,k=2)
plot(pstcut3)
text(pstcut3)
pstcut3

pstcut <- prune.tree(pstree)
plot(pstcut)
pstcut

# deviance vs size graph
pstcut <- prune.tree(pstree,best=3) 
pstcut
deviance(pstcut) 

set.seed(2)
cvpst <- cv.tree (pstree, K=10) # k = no. of  folds
cvpst$size
cvpst$dev
plot (cvpst, pch=21, bg=8, type="p", cex=1.5, ylim=c(65,100))

pstcut <- prune.tree (pstree, best=3) 
pstcut
plot (pstcut, col=8)
text (pstcut)

# Set up train control for cross-validation       #skip
#train <- trainControl(method = "cv", number = 10) #skip

# Build decision tree model using training data
tree_model <- rpart(lcavol ~ age + lbph + lpsa + lcp + gleason, data = data, method = "anova")
tree_model
# Identify best value for complexity parameter using cross-validation
cp_values <- seq(0, 0.05, by = 0.001)
cv_results <- train(lcavol ~ age + lbph + lpsa + lcp + gleason, data = data, method = "rpart", tuneGrid = data.frame(cp = cp_values), trControl = train)
best_cp <- cv_results$bestTune[["cp"]]
best_cp

# Prune decision tree model using best tree size
pruned_tree <- prune.rpart(tree_model, cp = best_cp)

# Plot pruned decision tree model
rpart.plot(pruned_tree)

# Build regression tree model using training data
regtree_model <- rpart(lcavol ~ age + lbph + lpsa + lcp + gleason, data = data, method = "anova", cp = best_cp)

# Predict log volume using regression tree model on testing data
predictions <- predict(regtree_model, newdata = data)
predictions
