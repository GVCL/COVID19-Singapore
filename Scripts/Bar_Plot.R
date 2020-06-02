###############################################
setwd("~/Singapore/Data") # Setting Working Directory
Cases <- read.csv('Datewise-Count.csv', sep=",", header = TRUE, fileEncoding="UTF-8-BOM")   
###############################################

pdf("~/Singapore/Cases-Active.pdf", width = 10, height  = 6)
   
xx <- barplot(Cases$ConFreq, 
col="#ff6666",
#col="#525252", # GrayScale
alpha=0.4,
ylim=c(0,80),
xlab = "Date (Jan 23-Apr 1, 2020)",
font.lab = 2,
axis.lty=1,
ylab = "#Patients with COVID19-Positive Confirmation")
text(cex=0.65, x=xx, y=-4, Cases$ConfirmDate, xpd=TRUE, srt=90, col = "black", font = 2)
text(x = xx, y = Cases$ConFreq, label = Cases$ConFreq, pos = 3, cex = 0.85, font = 2, col = "black")
lines(x = xx, y = Cases$ConFreq, cex = 4, col = "black", lwd = 2)
abline(v = c(14.5,64.9), col="black", lwd=2, lty=2)
box()
grid(NA, 4, lwd = 2)


dev.off()
###############################################

pdf("~/Singapore/Cases-Recovered.pdf", width = 10, height  = 6)
   
xpl <- barplot(Cases$DisFreq, 
col="#89d678",
#col = "#bdbdbd", # GrayScale
alpha=0.4,
ylim=c(0,20),
xlab = "Date (Jan 23-Apr 1, 2020)",
font.lab = 2,
axis.lty=1,
ylab = "#Clinically Recovered Patients") 
text(cex=0.65, x=xpl, y=-1, Cases$ConfirmDate, xpd=TRUE, srt=90, col = "black", font = 2)
text(x = xpl, y = Cases$DisFreq, label = Cases$DisFreq, pos = 3, cex = 0.85, font = 2, col = "black")
lines(x = xpl, y = Cases$DisFreq, cex = 4, col = "black", lwd = 2)
abline(v = c(14.5,64.9), col="black", lwd=2, lty=2)
box()
grid(NA, 4, lwd = 2)

dev.off()
rm(list=ls())
###############################################