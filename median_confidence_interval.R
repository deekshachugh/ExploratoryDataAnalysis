# Code for exercise 3
# Given a vector of numerical values returns the median and
# the 95% confidence interval for the median 
# Plot the density and the density of the resample medians
# in density_confidence_internal.png
median_confidence_interval <- function(x) {
  #creating dataframe of the input vector
  df1 <- data.frame(x,grp="Input")
  #Initialising values of dataframe
  dataframe <- data.frame(low_ci = 0,median = 0,high_ci = 0 )
  #calculating median
  dataframe$median <- median(x)
  sample_median=c()
  for(i in 1:1000)
    {
    #sample is the random sample
    sample <- sample(x, size=length(x),replace = TRUE)  
    #sample_median is a vector of all the sample medians
    sample_median <- append(sample_median,median(sample))
    }
  #assigning x to sample_median
  x <- sort(sample_median)
  #low_ci is the lower limit of the confidence interval
  dataframe$low_ci <- quantile(sample_median, probs = c(.025))
  #high_ci is the upper limit of the confidence interval
  dataframe$high_ci <- quantile(sample_median, probs = c(0.975))
  df2 <-data.frame(x,grp="median")
  #dfs is a dataframe of both input vector and sample median
  dfs <- rbind(df1,df2)
  #plotting of the densities of input and sample_medians 
  p1 <- ggplot(dfs,aes(x = x)) + geom_density(aes(group = grp))
  #Adding the vertical line
  p1 <- p1 + geom_vline(xintercept = c(dataframe$low_ci, dataframe$median, dataframe$high_ci))
  #saving the plot
  png("density_confidence_internal.png")
  plot(p1)
  dev.off()  
  return(dataframe)
}
