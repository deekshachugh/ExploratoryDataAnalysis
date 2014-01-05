# Code for exercise 2
# write a function that given a numeric vector returns a data frame with
# columns mean, median, trimmed_mean (10% trimmed mean). 
trimmed_mean <- function(t) {
  #
  p <- subset(possum, sex == "f")
  p <- p$totlngth
  #calculating mean
  mean <- round(mean(p),2)
  #calculating median
  median <- median(p)
  #calculating trimmed mean
  trimmed_mean <- mean(p,trim=0.10)
  dataframe <- data.frame(mean,median,trimmed_mean)
  return(dataframe)
}
