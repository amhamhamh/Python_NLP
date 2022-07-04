# ntlk(자연어 처리) 패키지 말뭉치 불러내기
import nltk
nltk.download("book", quiet=True)
from nltk.book import *

# 저작권이 만료된 gutenberg 말뭉치 샘플
nltk.corpus.gutenberg.fileids()


# austen의 문서 원문 불러내기
persuasion = nltk.corpus.gutenberg.raw('austen-persuasion.txt')
print(persuasion[:1000])

# 토큰으로 분리하여 문자열 리스트로 출력
from nltk.tokenize import sent_tokenize
print(sent_tokenize(persuasion[:1000])[0])

# 단어별 tokenize
from nltk.tokenize import word_tokenize
word_tokenize(persuasion[50:100])

# 쉼표 등의 필요없는 것들 삭제하기
from nltk.tokenize import RegexpTokenizer
# 단어인거만 추출(정규식)
retokenize = RegexpTokenizer("[\w]+")
retokenize.tokenize(persuasion[50:100])

# 쉼표 등의 필요없는 것들 삭제하기
from nltk.tokenize import RegexpTokenizer
# 단어인거만 추출(정규식)
retokenize = RegexpTokenizer("[\w]+")
retokenize.tokenize(persuasion[50:100])


# 단어의 원형 찾아내기 

import nltk
nltk.download('omw-1.4')  

from nltk.stem import WordNetLemmatizer

lm = WordNetLemmatizer()

[lm.lemmatize(w, pos="v") for w in words]


# 품사별 설명(동사)
nltk.help.upenn_tagset("VB")

# 품사별로 형태소 단위 나누기 

'''
NNP: 단수 고유명사
VB: 동사
VBP: 동사 현재형
TO: to 전치사
NN: 명사(단수형 혹은 집합형)
DT: 관형사
'''

from nltk.tag import pos_tag
sentence = "You always think about that is so different between you and me"
tagged_list = pos_tag(word_tokenize(sentence))
tagged_list


# 인칭 대명사일 경우 빼기
nonus_list = [t[0] for t in tagged_list if t[1] == "PRP"]
nonus_list


# 품사 튜플 없애기 
from nltk.tag import untag
untag(tagged_list)


# 토큰 + 품사 = 새로운 토큰 (skikit-learn에서 같은 토근 다른 품사면, 다른 토큰으로 인식 처리 방지)
def tokenizer(doc):
    return["/".join(p) for p in tagged_list]

tokenizer(sentence)

# 20개의 사용 빈도 그래프
from nltk import Text

text = Text(retokenize.tokenize(persuasion))

text.plot(20)