#R 

?web pages
stackoverflow

#Objects and Function

5+4
a <- 5
b <- 5

names <- c("John", "James")

friends <- data.frame(names, ages)
View(friends)
str(friends)

friends$ages
   
// assigning new values 

//str() structure
sum(friends$ages)

friends[1,1]
friends[1, ]
friends[ ,1]

# built in data sets to practice with
data()
View(starwars)

# Installing Packages and uusing packages
install.packages("tidyverse")
library(tidyverse)

// starwars dataset is in tidyverse

starwars %>%
    filter(height > 150 & mass < 200) %>%
    mutate(height_in_meters = height/100) %>%
    select(height_in_meters, mass) %>%
    arrange(mass) %>%
    View()
    
    #plot()

#Explore

# Data structure and types of variables
View(msleep)
glimpse(msleep)

head(msleep)

class(msleep$name)


length(msleep)

names(msleep)
 
unique(msleep$vore)

missing <- !complete.cases(msleep)

msleep[missing, ]

starwars %>%
    select(name, height, mass)

starwars %>%
    select (1:3)

starwars %>%
    select(ends_with("color")) %>%
    View()

starwars %>%
    select(name, mass, height, everything())

starwars %>%
    rename("characters" = "name") %>%
    head()

class(starwars$hair_color)

starwars$hair_color <- as.factor(starwars$hair_color)

starwars %>%
    mutate(hair_color = as.character(hair_color)) %>%
    glimpse()


install.packages("dplyr")
library(dplyr)

install.packages("readxl")
library(readxl)

mydata=read.csv(file.choose(), header=TRUE)
mydata=read.table(file.choose(), header=TRUE, sep="\t", na.strings="-9")

mydata=read_excel(file.choose())

summary(mydata)

edit(mydata)

str(mydata)

names(mydata)

head(mydata)
head(mydata, n=10)
head(mydata, n=-10)

tail(mydata)
tail(mydata, n=10)
tail(mydata, n=-10)

mydata[1:10]



head(starwars)
View(starwars)
starwars[]
starwars[1: ]



emp.data <-data.frame(emp_id=(1:5),
    emp_name=c("Sujal", "Arvind", "Taksh", "Baqar", "Rayhan"),
    salary = c(10000, 5000, 2000, 1000, 3000),
    start_month = c("August", "November", "August", "September", "September"),
    stringsAsFactors = FALSE
)

print(emp.data)
str(emp.data)

emp.data$male <- c(T,F,F,T,T)

emp.data
print(result <- data.frame(emp.data))



Plottingwith Base R


x <- seq(-pi, pi, 0.01)
plot(x,sin(x))

Plotting done via plot function