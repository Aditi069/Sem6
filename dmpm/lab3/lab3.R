data=read.csv(file.choose())
View(data)

library(tidyverse)
library(dplyr)	
library(ggplot2)	
library(Hmisc)

select(data, beer_servings, wine_servings) # by name
select(data, 5, 4)  # by column index

b=rename(data, beer.servings = beer_servings, wine.servings=wine_servings)
View(b)

n=mutate(data, ratio = beer_servings/wine_servings)
View(n)

m=arrange(data, beer_servings)
View(m)

a=filter(data, beer_servings > 30)
View(a)

data["beer_servings"][data["beer_servings"] == 0] <- NA
View(data)
is.na(data$beer_servings)

which(is.na(data$beer_servings))
sum(is.na(data))

mean(is.na(data)) 

c=na.omit(data)
View(c)

mean(data$beer_servings, na.rm = TRUE) #find mean leaving records with missing data

complete.cases(data) # to detect rows with complete data

d=clean=na.omit(data) # to   remove incomplete rows or data
View(d)

glimpse(data)	#summarise dataset

boxplot.stats(data$beer_servings) # for detecting outlier stats

boxplot(data$beer_servings)	# for comparing boxplots
boxplot(data$wine_servings)
boxplot(data$spirit_servings)

data <- subset(data, select = -c(country,continent))
boxplot(data)

boxplot.stats(data)$out #for setting outlier detection limit

#numeric imputation
e=data$beer_servings[is.na(data$beer_servings)] <- mean(data$beer_servings, na.rm = TRUE) # mean imputation
print(e)
f=data$beer_servings <- impute(data$beer_servings, fun = mean) # mean imputation
print(f)
g=data$beer_servings <- impute(data$beer_servings, fun = median) # median imputation
print(g)




