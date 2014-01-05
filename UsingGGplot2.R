library(foreign)
p <- read.csv(file.choose())
library(ggplot2)

emp <- make_factor( levels = p$emp, data = p$emp )
p1<-ggplot(group = p$q6a)+geom_histogram(aes(x=p$usr),data= p,binwidth = 0.5,color="white",fill="blue")+facet_grid(~q6a)
p1
p2<- ggplot(aes(x=p$age), data=p)+geom_histogram(binwidth = 5,color="white",fill="blue")+facet_grid(~sex)
p2
p3<- ggplot(aes(x=as.factor(p$inc)), data =p)+geom_histogram(binwidth = 5,color="white",fill="blue")
p3
p4<- qplot(age,q6a,data=p)
p4
p6<- ggplot(aes(x=p$p), data=p)+geom_histogram(binwidth = 5,color="white",fill="blue")+facet_grid(~sex)
p6
p7<-ggplot(data=p, aes(x=factor(p$q6b), y=age, fill=as.factor(emp))) + geom_bar(stat="identity", position=position_dodge())
p7
p8<-ggplot(data=p, aes(x=p$age, y= as.factor(p$educ), fill=as.factor(p$q6a))) + geom_bar(stat="identity", position=position_dodge())
p8