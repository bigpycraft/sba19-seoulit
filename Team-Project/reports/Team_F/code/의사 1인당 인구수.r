library(data.table)
library(ggplot2)
library(ggthemes)

# bb.csv input
iguana <- fread(file.choose(),header=T)
iguana <- subset(iguana, select = c(-V1))

colnames(iguana)
names(iguana) <-c("Large_Region", "Population","Doctor","Doctors_Per_People")

### 의사 1인당 인구수 ##############################################################

# ALL
plot_all <- ggplot(data=iguana, aes(x=reorder(Large_Region, -Doctors_Per_People), y=Doctors_Per_People))+geom_col(fill="blue") + labs(x = "대지역", y="의사 1인당 인구수") + theme_light()

# top 7
iguana1 <- head(iguana,7)

plot_top7 <- ggplot(data=iguana1, aes(x=reorder(Large_Region, -Doctors_Per_People), y=Doctors_Per_People))+geom_col(fill="blue") + labs(x = "대지역", y="의사 1인당 인구수") + theme_light()

# worst 7
iguana2 <- tail(iguana,7)

plot_worst7 <- ggplot(data=iguana2, aes(x=reorder(Large_Region, -Doctors_Per_People), y=Doctors_Per_People))+geom_col(fill="blue") + labs(x = "대지역", y="의사 1인당 인구수") + theme_light()


# plot
plot_all     # ALL
plot_top7    # top 7
plot_worst7  # worst 7  

######################################################################################