library(caTools)
library(caret)
#Read a dataset of your choice suitable for logistic regression.
datas=read.csv(file.choose())
View(datas)

#Identify the response variable (dichotomous) and predictors (2 or 3).
res=datas$Purchased
pred=c(datas$Gender,datas$Age)

#Display dataset summary statistics.
summary(datas)

#Use relevant R packages for model building and model evaluation.
# Create training & testing datasets by splitting the available dataset in ratio 80:20.
div=createDataPartition(datas$Purchased,p=0.8,list=FALSE)
train=datas[div,]
test=datas[-div,]
View(train)
View(test)

#Build suitable logistic model using training dataset for predicting the response.
model=glm(datas$Purchased~datas$Gender+datas$Age,data=train,family="binomial")

#Display model summary and derive equation of estimated probability of response variable.
summary(model)

#Predict values of response variable using the model built with the testing dataset.
pred=predict(model,newdata=test,type="response")
pred

#Transform the predicted response obtained in step 8 based on the threshold level=0.7 (means if p >0.7, 1, 0 )
tpred=ifelse(pred > 0.7, 1, 0)
tpred

#Plot the graph à Any one predictor Vs predicted probability of response variable.
plot(datas$Age,tpred)
plot(datas$Age,pred)

install.packages('epitools')
library(epitools)
#Display the odds ratio for each of the predictors and write its interpretation.
od1=oddsratio(datas$Age)
od1

#Build confusion matrix of actual Vs predicted responses and evaluate model accuracy.
cm=table(datas$Purchased,tpred)
cm
specificity(cm)
sensitivity(cm)

#Draw the ROC-AUC Curve for your model and comment on effectiveness of the model.
library(pROC)
test_prob = predict(model, test, type = "response")

test_roc = roc(datas$Purchased ~ test_prob, plot = TRUE, print.auc = TRUE)

as.numeric(test_roc$auc)

auc(roc(datas$Purchased, tpred))
