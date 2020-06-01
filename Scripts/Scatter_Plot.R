###############################################
requiredPackages = c('ggplot2','dplyr')
for(p in requiredPackages){
  if(!require(p,character.only = TRUE)) install.packages(p)
  library(p,character.only = TRUE)
}
###############################################
setwd('C:/Users/User/Documents/Singapore') # Setting Working Directory
filePath <- "Data/"
fileName <- "SortedRecoveryData.csv"

COVID <- read.csv(paste(filePath,fileName,sep=""), sep=",", header = TRUE)    

COVID <- COVID %>% 
  mutate(
   Gender1 = ifelse(Gender %in% c("MALE"), "A", "B") 
  )
  
pdf("ScatterPlot.pdf", width = 6, height  = 6)
   
scatterPlot <- ggplot(COVID, aes(x=Age, y=DaysInHospital, color=Gender1)) + 
geom_point(size=3) +
scale_color_manual(name="Gender", values=c("#08519c", "#df65b0"), labels=c("MALE", "FEMALE")) +
xlab("Age")+
ylab("Recovery Days In Hospital") + 
theme_bw() + 
theme(legend.box.just = "right",
      legend.title = element_text(face = "bold"),
      legend.text = element_text(size = 10, colour = "black"),
      legend.margin = margin(6, 6, 6, 6), 
      axis.text.x = element_text(face="bold", color="black", size=10),
      axis.text.y = element_text(face="bold", color="black", size=10),
      axis.title=element_text(size=12,face="bold"))
scatterPlot
dev.off()
###############################################