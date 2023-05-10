data = read.csv(file.choose())
View(data)
plot(data)
summary(data)

#visualizing the data 
library(ggplot2)
hist(data$Price, xlab = "price of the vehicle", col = 'Green' )
ggplot(data = data , aes(x = Age)) + geom_bar(color ='steelblue')+facet_wrap(~Automatic + FuelType)
ggplot(data = data , aes(x = Price, y = KM)) + geom_line(color ='steelblue')+facet_wrap(~Automatic + FuelType)
ggplot(data = data , aes(x = Price, y = Age)) + geom_line(color ='purple')+ geom_point(color = 'steelblue') +facet_wrap(~Automatic +
                                                                                                                     FuelType)
# Replacing the Fuel Type with numeric constants
data$FuelType[data$FuelType =="Diesel"] = 1
data$FuelType[data$FuelType =="Petrol"] = 2
data$FuelType[data$FuelType =="CNG"] = 3
View(data)

#data partitioning 70 : 30 training and testing partition respectively
library(caTools)
set.seed(100)
sample = sample.split(data , SplitRatio = .70)
train = subset(data, sample == TRUE)
View(train)
test = subset(data, sample == FALSE)
View(test)

#creating a multiple linear regression model from the given data and 
#visualization 
#model 1 Price vs rest of the variables
model1 = lm(Price~. , data = train)
summary(model1)
pred1 = predict(model1)
res1 = residuals(model1)
plot(train$Price ,res1, pch =20, col = "steelblue",abline(lm(Price~. , data = data)),main = "Residual plot",xlab = " PRICE OF THE VEHICLE" , ylab = "Residual")
abline(0,0)

#model 2 Price vs some variables 
model2 = lm(Price ~ Age + KM + FuelType + HP , data = train)
summary(model2)
pred2 = predict(model2)
res2 = residuals(model2)
plot(train$KM, res2 ,pch =17, col = "darkblue",main = "Residual plot 2",xlab = " KM OF THE VEHICLE" , ylab = "Residual")
abline(0,0)

#model 3 Price vs variables with greater coeffecients
model3 = lm(Price ~ HP + FuelType + KM + Age + Automatic, data = train)
summary(model3)
pred3 = predict(model3)
res3 = residuals(model3)
plot(train$Price ,res3, pch =20, col = "steelblue",abline(lm(Price~KM , data = data)),main = "Residual plot of Price excluding variables with smaller coefficients",xlab = " PRICE OF THE VEHICLE" , ylab ="Residual")
abline(0,0)

#testing and validating the data 
library(Metrics)
pred = summary(model1)
pred
mse = mean(pred$residuals^2)
mse
rmse =sqrt(mse)
rmse

AIC(model1)
BIC(model1)
AIC(model2)
BIC(model2)
AIC(model3)
BIC(model3)

#plot predicted values and actual values
plot(predict(model1), train$Price,main = "Observed VS Predicted Value 
scattelplot",xlab = "Predicted Values",ylab = "Observed Values",pch =
       18 , col = 'hotpink')
abline(a = 0, b = 1, lwd=2,col = "black")


