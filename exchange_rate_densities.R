# Code for exercise 4
# This should produce two plots as described in ex 4a,b
# exchange_density_a.png
# exchange_density_b.png
exchange_rate_densities <- function() {
  #diff_dy is the first order difference of dy column
  diff_dy <- diff(Garch$dy)
  mean = mean(diff_dy)
  median = median(diff_dy)
  sd = sd(diff_dy)
  mad = mad(diff_dy)
  #plotting the density of diff_dy
  p1 <- qplot(diff_dy, geom = "density")
  #plotting the normal function with mean and sd of diff_dy
  p1 <- p1 + stat_function(fun = dnorm, arg = list(mean = mean,sd =sd),linetype = 2)
  png("exchange_density_a.png")
  p1
  dev.off()
  #plotting the density of diff_dy
  p2 <- qplot(diff_dy, geom = "density")
  #plotting the normal function with median and mad of diff_dy
  p2 <- p2 + stat_function(fun = dnorm, arg = list(mean = median,sd =mad),linetype = 2)
  png("exchange_density_b.png")
  plot(p2)
  dev.off()
  
  return(list(p1,p2))
}
