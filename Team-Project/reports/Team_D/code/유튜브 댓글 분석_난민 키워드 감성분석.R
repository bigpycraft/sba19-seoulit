rm(list=ls())

library(wordcloud)
library(KoNLP)
useNIADic()
fname = "C://R_Data//유튜브 난민 키워드 동영상 (70개) 댓글분석.txt"
road1 = readLines(fname)

# 02. 긍정단어 부정단어 불러오기
pos.words = scan("C://R_Data//pos_kor_words.txt", what="character", comment.char=";")
neg.words = scan("C://R_Data//neg_kor_words.txt", what="character", comment.char=";")

# 03. 불러온 텍스트 전처리
#### 의미 없는 데이터 제거, 단어 발생 빈도 등을 기반으로 감성 분석 값을 반환.
require(plyr)
require(stringr)


sentence <- road1

# 구두점 문자, ! " # $ % & ’ ( ) * + , - . / : ; < = > ? @ [  ] ^ _ ` { | } ~. 제거
sentence <- gsub('[[:punct:]]', "", sentence)  
# \n, \r 같은 제어문자 등 제거
sentence <- gsub('[[:cntrl:]]', "", sentence)
# 숫자 제거
sentence <- gsub('\\d+', "", sentence)
head(sentence)

length(sentence)


# 04. 명사추출
# ,autoSpacing = TRUE
#### 명사 추출
wordlist <- sapply(sentence, extractNoun, USE.NAMES=F)
words <- unlist(wordlist)   # 단어를 하나의 벡터로 
head(words)

length(words)

pos.matches <- match(words, pos.words)  ## 긍정단어, 부정단어 확인 /긍정단어  880 items
neg.matches <- match(words, neg.words)## 단어 존재(사전에서 위치), 없으면 NA/ 1678 items

pos.matches
neg.matches

pos.matches <- !is.na(pos.matches)# NA가 아닌것 가져오기(문장에 단어 있음)
neg.matches <- !is.na(neg.matches)
sum(pos.matches)  # 점수 합(긍정단어) [1] 0 1678 items

score <- sum(pos.matches) - sum(neg.matches)

# 단어 확인 및 빈도에 따른 정렬

pos_word <- words[pos.matches ]
neg_word <- words[neg.matches ]

pos_cnt <- table('C://R_Data//pos_word')
neg_cnt <- table('C://R_Data//neg_word')

pos_cnt_sort <- sort(pos_cnt, decreasing = T)
neg_cnt_sort <- sort(neg_cnt, decreasing = T)

#06. 긍정단어,부정단어Top 5
## TOP 5 단어 그래프 보기
barplot(pos_cnt_sort[5:0], main='긍정 단어 TOP 5', horiz=T, col=c("green", "blue", "yellow"))

barplot(neg_cnt_sort[5:0], main="부정 단어 TOP 5", horiz=T, col=c("green", "blue", "yellow"))
