# Q1.Read the file "pva97nk.csv" that is supplied to you.

data=read.csv(file.choose())
View(data)

# Q2.Identify the variables in the file "pva97nk.csv" and determine whether any variable has any missing values. 

ls(data) #to view the variable names
is.na(data$DemAge) #to determine whether the variable value is missing 
which(is.na(data$DemAge)) # to find the location of the missing value
sum(is.na(data)) #to find the sum of the missing values


# Q3.Impute some of the variables that have missing values using their corresponding mean values. Verify whether your task has been correctly done.

#best method prefer this in exam
library(Hmisc)
data$DemAge=impute(data$DemAge, mean)
data$TargetD=impute(data$TargetD, mean)
impute(data$GiftAvgCard36, mean)

#second method
data["DemAge"][is.na(data["DemAge"])] <- 0 #to replace all the NA values of specific column DemAge with 0
print(data$DemAge)
mean(data$DemAge)
data["DemAge"][data["DemAge"] == 0] <- 44.45 #to replace all the 0 values of specific column DemAge with mean i.e 44.45
print(data$DemAge)

data["TargetD"][is.na(data["TargetD"])] <- 0
print(data$TargetD)
mean(data$TargetD)
data["TargetD"][data["TargetD"] == 0] <- 7.25
print(data$TargetD)

data["GiftAvgCard36"][is.na(data["GiftAvgCard36"])] <- 0
print(data$GiftAvgCard36)
mean(data$GiftAvgCard36)
data["GiftAvgCard36"][data["GiftAvgCard36"] == 0] <- 11.09
print(data$GiftAvgCard36)

# Q4.Compute the Kurtosis and Skewness of the variables and interpret the results obtained. 

library(moments) #install.packages("moments") "run this in console"
#skewness and kurtosis
print("Target D")
skewness(data$TargetD)
print("GiftCntAll")
skewness(data$GiftCntAll)
print("GiftCntCardAll")
skewness(data$GiftCntCardAll)
print("PromCntAll")
skewness(data$PromCntAll)
print("DemMedHomeValue")
skewness(data$DemMedHomeValue)
print("DemMedIncome")
skewness(data$DemMedIncome)

print("Target D")
kurtosis(data$TargetD)
print("GiftCntAll")
kurtosis(data$GiftCntAll)
print("GiftCntCardAll")
kurtosis(data$GiftCntCardAll)
print("PromCntAll")
kurtosis(data$PromCntAll)
print("DemMedHomeValue")
kurtosis(data$DemMedHomeValue)
print("DemMedIncome")
kurtosis(data$DemMedIncome)

# Q5.Determine the "summary" information for the numerical variables. 

summary(data$DemAge)
summary(data$TargetD)
summary(data$GiftCntAll)
summary(data$GiftCntCardAll)
summary(data$PromCntCardAll)
summary(data$DemMedHomeValue)
summary(data$DemMedIncome)

#for(i in range(1:28))
#{
#  temp = data[[i]]
#  print(summary(temp))
#} 

# Q6.Identify the "distributions" of the numerical variables and plot the distributions. 
#histogram frequency distribution plots
hist(data$TargetD,col = "blue")
hist(data$GiftCntAll,col = "red")
hist(data$GiftCntCardAll,col = "green")
hist(data$PromCntAll,col = "yellow")
hist(data$DemMedHomeValue,col = "purple")
hist(data$DemMedIncome,col = "cyan")

# Q7.Transform the numeric variables into their natural log values and scale [0 - 1] values. 

data$DemAge=log(data$DemAge) #to find natural log value
log(data$TargetD)
log(data$GiftCntAll)
log(data$GiftCntCardAll)
log(data$PromCntAll)
log(data$DemMedHomeValue)
log(data$DemMedIncome)


# BEST METHOD
library(scales)
rescale(data$GiftCntCardAll, to = c(0, 1), from = range(data$GiftCntCardAll, na.rm = TRUE, finite = TRUE))

data_range1 <- (data$DemAge - min(data$DemAge)) / (max(data$DemAge) - min(data$DemAge))  # Scale to 0/1
print(data_range1)

data <- subset(data, select = -c(StatusCat96NK,DemGender,DemHomeOwner)) # remove the column
scale(data)

# Q8.Check whether the numeric variables follow normality conditions. 

shapiro.test(data$DemAge) #normality test
shapiro.test(data$TargetD)
shapiro.test(data$GiftCntAll)
shapiro.test(data$GiftCntCardAll)
shapiro.test(data$PromCntAll)
shapiro.test(data$DemMedHomeValue)
shapiro.test(data$DemMedIncome)


# Q9.Find the correlation matrix for all the variables in the dataset and plot the graph of the correlation matrix. 

data <- subset(data, select = -c(StatusCat96NK,DemGender,DemHomeOwner)) # remove the column
corr=cor(data)
View(corr)

#print("Correlation matrix")
#print(corr)

#Visualization
library(corrplot)
head(data)
# correlation matrix
M=cor(data)
head(round(M,1))  

# visualizing correlogram
# as circle
corrplot(M, method="circle")

# as pie
corrplot(M, method="pie")

# as colour
corrplot(M, method="color")

# as number
corrplot(M, method="number")


# Q10.From the given dataset partition the data into 70-15-15 divisions so to construct the training, validation and test datasets. 
#partitioning the data into 70:15:15 ratio 

library(caret)
set.seed(7)
ss <- sample(1:3,size=nrow(data),replace=TRUE,prob=c(0.7,0.15,0.15))
train <- data[ss==1,]
test <- data[ss==2,]
cvr <- data[ss==3,]
View(train)
View(test)
View(cvr)

