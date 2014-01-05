# Code for exercise 5
# This code is optional
qq_plots <- function() {
diff_bp <- diff(Garch$bp)
qqnorm(Garch$bp, datax=TRUE)
qqline(Garch$bp, col=2, datax=TRUE)
qqnorm(diff_bp, datax=TRUE)
qqline(diff_bp, col=2, datax=TRUE)
normal <- rnorm(nrow(Garch)-1,0,1)
qqnorm(normal, datax=TRUE)
qqline(normal, col=2, datax=TRUE)
}
