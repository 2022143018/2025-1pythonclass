# text에 들어있는 단어 갯수 세기
# 딕셔너리 응용 프로그램
from collections import defaultdict

text = "My heart leaps up when I behold A rainbow in the sky:" \
    "So was it when my life began;" \
    "So is it now I am a man;" \
    "So be it when I shall grow old," \
   "Or let me die!"\
"The Child is father of the Man;"\
"And I could wish my days to be"\
"Bound each to each by natural piety."


print(text)
textlist = text.split() # 스트링을 리스트로 변환
print(textlist)
# 간단버전
wordcount = dict()

for word in textlist:
    if word in wordcount:
        wordcount[word] = wordcount[word] + 1
    else:
        wordcount[word] = 1

# wordcount = {"So":3, "And":1}
print(wordcount)

for key, value in wordcount.items():
    print(f'{key},{value}')

# 두번째 버전: defaultdict
from collections import  defaultdict
wordcount = defaultdict()
for word in textlist:
    wordcount[word] += 1

print(wordcount)