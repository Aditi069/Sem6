# install required packages 
install.packages("arules")
install.packages("arulesViz")
install.packages("rpart.plot")
install.packages("corrplot")

# load the required libraries 
library(dplyr)
library(ggplot2)
library(rpart.plot)
library(corrplot)
library(rpart)
library(arules)
library(arulesViz)

# import in-built data-set "Groceries" from arules package 
# Groceries is in a sparse matrix form 9835 rows  x  169 columns 
data(Groceries)
transactions <-  Groceries
transactions

#summary of data / transactions
summary(Groceries)

# from  summary identify  
  #   (a) rows , columns, density 
  #   (b) most frequent items
  #   (c) transaction length frequency distribution
  #   (d) summary  stats  of above  
##  Density of 0.026 means that there are 2.6% non zero cells 
##  in the matrix. Matrix has 9835 times 169 = 1662115 cells. 
##  Since 2.6% of that are non-zero cells, so 4.336710^{4} 
##  items were purchased.

nrow(transactions)

#  Frequency plots 
#  Support is frequency of  pattern in the rule, therefore it being set to 0.1 
#  means that the item must occur at least 10 times in 100 transactions.

itemFrequencyPlot(transactions, support=0.1, cex.names=0.8)
itemFrequencyPlot(transactions, support=0.05, cex.names=0.8)

#  Other way of selecting desired number of elements is to provide not support, 
#  but just the desired number. 
itemFrequencyPlot(transactions, topN=20)


########## CREATE RULEs ###########
# lets try eclat algorithm - to see most frequent itemsets having SUPP= 7.5%
# It is a more efficient and scalable version of the Apriori algorithm.
freq.itemsets <- eclat(transactions, parameter=list(supp=0.075, maxlen=15))
inspect(freq.itemsets)

# Lets create rules - Rules created using apriori algorithm 
# and giving minimal support and confidence of a rule.


# 8888888888888888888888888888888888888888888888
# Rule-1 
rule1 <- apriori(Groceries,parameter= list(support=0.01,confidence=0.3))
summary(rule1)
# created  125 association rules 
# rule length  2 or 3 
# summary of  support,confidence,coverage,lift,count   
# inspect top 5 rules 
inspect(head(rule1,5))
# inspect  and  interpret top 5 rules sorted by lift
inspect(head(sort(rule1,by="lift"),5))
#  interpretations ****************
#
#
#
# inspect  and  interpret top 5 rules that have high support & high confidence.
inspect(sort(sort(rule1, by ="support"),by ="confidence")[1:5])
#  interpretations ****************
#
#
#
#888888888888888888888888888888888888888888888888
# Rule-2 
rule2 <- apriori(Groceries,parameter= list(support=0.02,confidence=0.4))
summary(rule2)
# created  15 association rules 
# rule length  2 or 3 
# summary of  support,confidence,coverage,lift,count   
# inspect top 5 rules 
inspect(head(rule2,5))
# inspect  and  interpret top 5 rules sorted by lift
inspect(head(sort(rule2,by="lift"),5))
#  interpretations ****************
#
#
#
# inspect  and  interpret top 5 rules that have high support & high confidence.
inspect(sort(sort(rule2, by ="support"),by ="confidence")[1:5])
#  interpretations ****************
#
#
#
#88888888888888888888888888888888888888888888
# Rule-3 
rule3 <- apriori(Groceries,parameter= list(support=0.03,confidence=0.5))
summary(rule3)
# created 0 association rules 
# # summary of  support,confidence,coverage,lift,count   
# inspect top 5 rules 
inspect(head(rule3,5))
# inspect  and  interpret top 5 rules sorted by lift
inspect(head(sort(rule3,by="lift"),5))
#  interpretations ****************
#
#
#
# inspect  and  interpret top 5 rules that have high support & high confidence.
inspect(sort(sort(rule3, by ="support"),by ="confidence")[1:5])
#  interpretations ****************
#
#
#

#  PLOT  RULES
plot(rule1)
plot(rule2)
plot(rule3)

itemFrequencyPlot(Groceries,topN=5)
plot(rule1,method="grouped",control=list(k=5))
plot(rule2,method="grouped",control=list(k=5))
plot(rule3,method="grouped",control=list(k=5))


#Less than likely associations ? - Lift < 1
inspect(tail(sort(rule1, by = "lift")))

