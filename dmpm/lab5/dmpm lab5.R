#linear regression
data=read.csv(file.choose())
View(data)

#Explore data
class(data)
data[1:3,]
head(data)
str(data)
summary(data)
hist(data$Price,col="Yellow")

#Create Numeric Variables for the Categorical variable
#Fueltype with its three nominal outcomes:CNG, Diesel and Petrol

drn= factor(data$FuelType)# factor allocates the encoder by itself
class(drn)
data$FuelType1=as.numeric(drn)
View(data)
data[1:3,]
str(data)

#Remove unwanted Predictor
auto=data[-4]
View(auto)
auto[1:3,]

library(caTools)
sample=sample.split(data, SplitRatio=0.80)
train=subset(data, sample=T)
test=subset(data, sample=F)

#data Visualization
plot(Price~.,data = auto,pch=20,col="pink")
correlations = cor(subset(auto, select = -MetColor))
correlations["Price", ]

#Regression model constructed on all predictors
m1=lm(Price~.,data=train)
summary(m1)
# residual summary shows the minimum and maximum values of the 
#difference between the actual and predicted values of the dependent variable.
#The coefficients section provides the estimated coefficients of the independent variables
#in the model, along with their standard errors, t-values, and corresponding p-values.
#The model's adjusted R-squared value is 0.8649, 
#indicating that the model explains 86.49% of the variance in the dependent variable.
#The F-statistic tests whether all the coefficients in the model are zero 
#simultaneously. The p-value for the F-statistic is less than 2.2e-16, 
#indicating that at least one coefficient is non-zero, and the model is statistically significant.
#The model includes one variable, "FuelType1," with missing values,
#which is denoted by NA in the coefficients section.
pred= predict(m1)
pred
res=residuals(m1)
res

predd=summary(m1)
predd
mse= mean(predd$residuals^2) 
mse

rmse=sqrt(mse)
rmse

library(Metrics)
AIC(m1)
BIC(m1)
#AIC as a way to compare regression model. the model with the lowest AIC offers best fit.
#The smaller the BIC value, the better the time series model.
#The Akaike information criterion (AIC). can use AIC for more complex model.
# The Bayesian Information Criterion is an index used in Bayesian statistics to choose between two or more models



