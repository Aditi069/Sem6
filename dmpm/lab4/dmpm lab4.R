install.packages("car")
library(car) # to recode variables
set.seed(1)

data=read.csv(file.choose())
View(data)
data[1:3,]

# define hours of departure # data transformation
data$sched=factor(floor(data$schedtime/100))

table(data$sched)
table(data$carrier)
table(data$weather)
table(data$dest)
table(data$origin)
table(data$dayweek)
table(data$daymonth)
table(data$delay)
class(data$delay)

data$delay=recode(data$delay,"'delayed'=1;else=0")
class(data$delay)
table(data$delay)

drn =factor(data$delay)
data$delay1=as.numeric(drn)
## delay 1=Monday 2=Tuesday 3=Wednesday 4=Thursday 5=Friday 6=Saturday
## 7=Sunday

# if dayweek= 7 (sunday) or 1 (monday) then code as 1
data$dayweek=recode(data$dayweek,"c(1,7)=1;else=0")
table(data$dayweek)

# Omit unsed variables
data=subset(data, select = -c(1,3,5,6,7,11,12))
data[1:3,]
View(data)

n=length(data$delay)
n
n1=floor(n*(0.6)) # training dataset rows
n2=n-n1 #testing dataset rows
n2

train=sample(1:n,n1) #random n1 (1320) samples between 1 & n(2201) for training dataset

# Estimation of logistic regression model
# Explanatory variables: carrier, destination, origin, weather, day of week
# (weekday/weekend), scheduled hour of departure
# create design matrix: indicators for categorical variables (factors)

Xdata=model.matrix(delay~.,data=data)[,-1]
View(Xdata)

Xdata[1:3,]
xtrain=Xdata[train,] # training dataset records 1320
View(xtrain)
ytrain=data$delay[train] #actual observed delay from training set
ytrain

xnew=Xdata[-train,] # testing dataset 881
View(xnew)
ynew=data$delay[-train] #actual observed delay from training set
ynew

ml=glm(delay~.,family=binomial,data=data.frame(delay=ytrain,xtrain))
summary(ml)

#prediction: predicted default probabilities for cases in test set
ptest=predict(ml,newdata=data.frame(xnew),type="response")
ptest # contains delay probabilities scores of 881 flights from test dataset

dnew=data.frame(ynew,ptest)
View(dnew)

#first column in list represents the case number of the test element
plot(ynew~ptest)

#coding as 1 if probability 0.5 or larger 0.5 = Threshold
gg1=floor(ptest+0.5) #floor function; for classifying into 0 or 1
gg1
ttt=table(ynew,gg1) #ynew=observed delays gg1=predicted delays
ttt
ttt[1,2]
ttt[2,1]
error=(ttt[1,2]+ttt[2,1])/n2
error # % of wrongly classified cases

# coding as 1 if probability 0.3 or larger 0.3 = threshold
gg2=floor(ptest+0.7)
ttt=table(ynew,gg2)
ttt
error=(ttt[1,2]+ttt[2,1])/n2
error


















