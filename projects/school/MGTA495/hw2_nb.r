setwd("/home/jovyan/MSBA/mysite/projects/school/MGTA495")
data <- read.csv("data/blueprinty.csv")
print(summary(data))
#hist(data$patents)

#m1 <-lm(patents ~ age, data=data)
#summary(m1)

#par(mfrow=c(2,2))
#plot(m1)

library(ggplot2)
ggplot(data, aes(x = data$iscustomer, y = data$patents)) +
  geom_point() +
  geom_smooth(method = "lm", se = FALSE)