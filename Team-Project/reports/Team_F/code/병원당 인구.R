options(digits = 2)

library(data.table)
library(ggplot2)
library(dplyr)
library(plyr)
library(ggthemes)
library(gridExtra)

# aa.csv input
aa <- fread(file.choose(),header=T)
head(aa)

aa <- subset(aa, select = c("지역","대지역","소지역","총인구","65세이상","계","상급종합","종합병원","요양병원","권역"))

# 헤더변경 및 변수 선택
names(aa) <- c("region", "large_legion", "small_region","population","older","hospital","hospital1","hospital2","hospital3","area")

# 대지역 기준 합치기
aa_region1 <- aa %>% group_by(large_legion) %>% summarise(population = sum(population))       # population : 총인구
aa_region2 <- aa %>% group_by(large_legion ) %>% summarise(older  = sum(older))               # older : 65 세 이상
aa_region3 <- aa %>% group_by(large_legion  ) %>% summarise(hospital   = sum(hospital ))      # hospital : 계 (총병원수)
aa_region4 <- aa %>% group_by(large_legion  ) %>% summarise(hospital1   = sum(hospital1 ))    # hospital1 : 상급종합
aa_region5 <- aa %>% group_by(large_legion  ) %>% summarise(hospital2  = sum(hospital2 ))     # hospital2 : 종합병원
aa_region6 <- aa %>% group_by(large_legion ) %>% summarise(hospital3   = sum(hospital3 ))     # hospital3 : 요양병원 

# 대지역 기준 데이터 합치기
l_region <- left_join(aa_region1, aa_region2, by="large_legion") %>% 
  left_join(.,aa_region3,by="large_legion") %>% 
  left_join(.,aa_region4,by="large_legion") %>% 
  left_join(.,aa_region5,by="large_legion") %>% 
  left_join(.,aa_region6,by="large_legion")

head(l_region)

# 파생변수 

l_region$pop_hos <- l_region$population/l_region$hospital
l_region$pop_hos1 <- l_region$population/l_region$hospital1
l_region$pop_hos2 <- l_region$population/l_region$hospital2
l_region$pop_hos3 <- l_region$population/l_region$hospital3

head(l_region)
names(l_region)
summary(l_region)

# ALL
pop_hos <- ggplot(data=l_region, aes(x=reorder(large_legion, -pop_hos), y=pop_hos))+geom_col(fill="blue") + labs(title ="전체병원 1개당 지역별 인구수",x = "대지역", y="병원 1개당 인구수") + theme_light()
pop_hos1 <- ggplot(data=l_region, aes(x=reorder(large_legion, -pop_hos1), y=pop_hos1))+geom_col(fill="blue") + labs(title ="상급종합병원 1개당 지역별 인구수",x = "대지역", y="상급종합병원 1개당 인구수") + theme_light()
pop_hos2 <- ggplot(data=l_region, aes(x=reorder(large_legion, -pop_hos2), y=pop_hos2))+geom_col(fill="blue") + labs(title ="종합병원 1개당 지역별 인구수", x = "대지역", y="종합병원 1개당 인구수") + theme_light()
pop_hos3 <- ggplot(data=l_region, aes(x=reorder(large_legion, -pop_hos3), y=pop_hos3))+geom_col(fill="blue") + labs(title ="병원 1개당 지역별 인구수", x = "대지역", y="병원 1개당 인구수") + theme_light()
pop_hos4 <- ggplot(data=l_region, aes(x=reorder(large_legion, -pop_hos4), y=pop_hos4))+geom_col(fill="blue") + labs(x = "대지역", y="요양병병원 1개당 인구수") + theme_light()

grid.arrange(pop_hos, pop_hos1, pop_hos2, pop_hos3, ncol=2)