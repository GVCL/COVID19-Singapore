###############################################
requiredPackages = c('ggplot2','dplyr')
package.check <- lapply(
  requiredPackages,
  FUN = function(x) {
    if (!require(x, character.only = TRUE)) {
      install.packages(x, dependencies = TRUE)
      library(x, character.only = TRUE)
    }
  }
)
###############################################

setwd("~/COVID19-Singapore-master/Data") # Setting Working Directory
COVID <- read.csv('SortedRecoveryData.csv', sep=",", header = TRUE, fileEncoding="UTF-8-BOM")      

######  Box Plot with all Age groups and Genders of Clinically Recovered Cases ####
pdf("~/COVID19-Singapore-master/AgeRange_Gender_BoxPlot.pdf", width = 8, height  = 5)

newCOVID <- COVID %>% 
  mutate(
    newGender = ifelse(Gender %in% c("MALE"), "A", "B") 
  )
  
g <- ggplot(newCOVID, aes(x = AgeRange, y=DaysInHospital, fill=newGender)) 

g +          
geom_boxplot(position="dodge", alpha=0.5, outlier.colour="transparent") + 
scale_fill_manual(name="Gender", values=c("#08519c", "#df65b0"), labels=c("MALE", "FEMALE")) +
xlab("Age Group (in years)")+
ylab("#Days from +ve-Confirmation to Clinical Recovery") + 
#ggtitle ("Clinical Recovery") +
theme(plot.title = element_text(hjust = 0.5)) +
theme_bw() + 
theme(axis.text.x = element_text(face="bold", color="black", size=10),
      axis.text.y = element_text(face="bold", color="black", size=10),
      axis.title=element_text(size=12,face="bold")
    ) 
    
dev.off()   

g <- ggplot(newCOVID, aes(x = AgeRange, y=DaysInHospital, fill=newGender))  + geom_boxplot()
pdata <- ggplot_build(g)$data   
pdata

####################################################################################

#######  Box Plot with all Age groups of Clinically Recovered Cases ################

pdf("~/COVID19-Singapore-master/AgeGroup_BoxPlot.pdf", width = 8, height  = 6)

p <- ggplot(COVID, aes(x = AgeRange, y=DaysInHospital, fill=AgeRange)) 
dims <- COVID %>% group_by(AgeRange) %>% mutate(med=median(DaysInHospital))
#dims1 <- COVID %>% group_by(AgeRange) %>% mutate(mean=mean(DaysInHospital))
min <- COVID %>% group_by(AgeRange) %>% mutate(minima=min(DaysInHospital))
max <- COVID %>% group_by(AgeRange) %>% mutate(maxima= max(DaysInHospital))
fqr <- COVID %>% group_by(AgeRange) %>% mutate(fQR=quantile(DaysInHospital, 0.25))
tqr <- COVID %>% group_by(AgeRange) %>% mutate(tQR=quantile(DaysInHospital, 0.75))
                    

p +          
geom_boxplot(position="dodge", alpha=0.8, outlier.colour="transparent") + 
labs(fill = "Age Group") +
scale_fill_manual(values=c('#5977e3', '#7b9ff9', '#9ebeff', '#c0d4f5', '#dddcdc', '#f2cbb7', '#f7ac8e', '#ee8468', '#d65244')) + #coolwarm palette
# scale_fill_manual(values=c("#006837", "#1a9850", "#66bd63", "#a6d96a", "#d9ef8b", "#fdae61", "#f46d43", "#d73027", "#a50026"))+ # green to red scale
xlab("Age Group (in years)")+
ylab("#Days from +ve-Confirmation to Clinical Recovery") + 
#ggtitle ("Clinical Recovery") +
theme(plot.title = element_text(hjust = 0.5)) +
theme_bw() + 
geom_text(aes(y = dims$med,x=as.numeric(AgeRange) + 0.2, label = round(dims$med,2)),position=position_dodge(width = 0.8),size = 3, vjust = -0.5,colour="black")+
#geom_text(aes(y = dims1$mean,x=AgeRange, label = round(dims1$mean,2)),position=position_dodge(width = 0.8),size = 3, vjust = -0.5,colour="black")+
geom_text(aes(y = min$minima,x=as.numeric(AgeRange) + 0.2, label = round(min$minima,2)),position=position_dodge(width = 0.8),size = 3, vjust = -0.5,colour="black")+
geom_text(aes(y = max$maxima,x=AgeRange, label = round(max$maxima,2)),position=position_dodge(width = 0.8),size = 3, vjust = -0.5,colour="black")+
geom_text(aes(y = fqr$fQR,x=as.numeric(AgeRange) + 0.2, label = round(fqr$fQR,2)),position=position_dodge(width = 0.8),size = 3, vjust = -0.5,colour="black")+
geom_text(aes(y = tqr$tQR,x=as.numeric(AgeRange) + 0.2, label = round(tqr$tQR,2)),position=position_dodge(width = 0.8),size = 3, vjust = -0.5,colour="black")+
theme(axis.text.x = element_text(face="bold", color="black", size=10),
      axis.text.y = element_text(face="bold", color="black", size=10),
      axis.title=element_text(size=12,face="bold")) 
dev.off()  

g <- ggplot(COVID, aes(x = AgeRange, y=DaysInHospital, fill=AgeRange))  + geom_boxplot()
pdata <- ggplot_build(g)$data 
pdata
rm(list=ls())
####################################################################################