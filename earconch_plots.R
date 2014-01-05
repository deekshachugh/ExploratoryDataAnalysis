# Code for exercise 1
# This should produce three plots
# Histogram for earconch measurements.
# histo_earconch.png
# Side-by-side box plots of the male and female earconch measurements.
# box_plot_earconch_gender.png
# Side-by-side histograms of the male and female earconch measurements.
# histo_earconch_gender.png
earconch_plots <- function() {
  #Ploting the histogram of earconch in possum dataset  
  p1 <- ggplot(possum,aes(earconch))
  p1<-p1+geom_histogram(color="white",binwidth=0.5)
  ggsave("histo_earconch.png")
  #Ploting Side-by-side box plots of the male and female earconch measurements
  p2 <- ggplot(possum,aes(x=sex,y=earconch))
  p2 <- p2 + geom_boxplot()
  ggsave("box_plot_earconch_gender.png")
  #Side-by-side histograms of the male and female earconch measurements
  p3 <- ggplot(possum,aes(earconch))
  p3 <- p3 + geom_histogram(color="white",binwidth=0.8)
  p3 <- p3 + facet_grid(. ~ sex)
  ggsave("histo_earconch_gender.png")
  return(list(p1,p2,p3))
}

