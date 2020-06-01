####################################################################
requiredPackages = c('dplyr','MASS','stargazer','ggplot2','pscl','reshape2','summarytools')
package.check <- lapply(
  requiredPackages,
  FUN = function(x) {
    if (!require(x, character.only = TRUE)) {
      install.packages(x, dependencies = TRUE)
      library(x, character.only = TRUE)
    }
  }
)

# dplyr -- #basic data management & %>%
#MASS -- #for negative bin regression
#stargazer -- #for combining output
#ggplot2 -- #for graphing
#pscl -- #for zero inflated models & predprob
#reshape2 -- #convert wide to tall
#summarytools -- #freq
####################################################################


setwd('C:/Users/User/Documents/Singapore') # Setting Working Directory
filePath <- "Data/"
fileName <- "SortedRecoveryData.csv"
##################  All Recovered Data Distribution ################
COVID <- read.csv(paste(filePath,fileName,sep=""), sep=",", header = TRUE)  

COVID <- COVID %>% 
  mutate(Gender1 = ifelse(Gender %in% c("MALE"), 1, 2) 
  )
  
COVID <- COVID %>% 
  mutate(Period_Confirmed1 = case_when(
     Period_Confirmed %in% c("P_I") ~ 1,
     Period_Confirmed %in% c("P_II") ~ 2,
     Period_Confirmed %in% c("P_III") ~ 3
     ) 
  )
  
  
  
fr <- table(COVID$DaysInHospital) %>% data.frame
names(fr) <- c('articles', 'freq')
fr$articles <- as.numeric(as.character(fr$articles)) #convert factor to numeric

xlab <- fr$articles
col <- rgb(0.33, 0.77, 0.24, alpha=0.5)
gg <- ggplot(fr, aes(x = articles, y = freq))

pdf("Recover_DataDistribution_Plot.pdf", width = 10, height  = 6)

gg +
  geom_col() +  
  theme_bw() +
  lims(y = c(0, 25)) + 
  geom_line() + 
  geom_bar(stat="identity", colour="black", fill = col, alpha=0.7) +
  geom_text(aes(x = articles, y = freq, label = freq, vjust = -1)) +
  xlab("#Days from +ve-Confirmation to Clinical Recovery")+
  ylab("#Clinically Recovered Patients") +
  theme(plot.title = element_text(hjust = 0.5)) +
  theme(axis.text.x = element_text(face="bold", color="black", size=10),
      axis.text.y = element_text(face="bold", color="black", size=10),
      axis.title=element_text(size=12,face="bold")) +
  scale_x_continuous(labels = as.character(xlab), breaks = xlab)  

dev.off()
############################ GLM ########################################
linear <- glm(DaysInHospital ~ Age + Gender1 + Period_Confirmed1, data = COVID) #identity link, OLS
pois <- glm(DaysInHospital ~ Age + Gender1 + Period_Confirmed1, "poisson", data = COVID) #Poisson
negb <- glm.nb(DaysInHospital ~ Age + Gender1 + Period_Confirmed1, data = COVID) #Negative Binomial

summary(pois)
summary(negb)

po.p <- predprob(pois) %>% colMeans
po.nb <- predprob(negb) %>% colMeans
df <- data.frame(x = 0:max(COVID$DaysInHospital), Poisson = po.p, NegBin = po.nb)

obs <- table(COVID$DaysInHospital) %>% prop.table() %>% data.frame #Observed
names(obs) <- c("x", 'Observed')
comb <- merge(df, obs, by = 'x', all = T)
comb[is.na(comb)] <- 0

mm <- melt(comb, id.vars = 'x', value.name = 'prob', variable.name = 'Model')
mm <- filter(mm, Model != "OLS") #can include the linear model too if you want


pdf("Poisson_NegBin_Distribution.pdf", width = 10, height  = 6)

ggplot(mm, aes(x = x, y = prob, group = Model, col = Model)) +
  
  theme_bw() +
  geom_line(aes(lty = Model), lwd = 1) +
  scale_color_manual(values = c('blue', 'red', 'black')) +
  scale_linetype_manual(values = c('dotted', 'dotted', 'solid')) +
  xlab("#Days from +ve-Confirmation to Clinical Recovery")+
  ylab("Likelihood") +
  theme(plot.title = element_text(hjust = 0.5)) +
  theme(axis.text.x = element_text(face="bold", color="black", size=10),
        axis.text.y = element_text(face="bold", color="black", size=10),
        axis.title=element_text(size=12,face="bold"))+
  scale_x_continuous(labels = as.character(xlab), breaks = xlab) 
  
dev.off()
####################################################################