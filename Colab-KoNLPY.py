%%bash
apt-get update
#java 및 python, python3 개발 도구 설치
apt-get install g++ openjdk-8-jdk python-dev python3-dev
#python과 java를 연결해주는 library 설치
pip3 install JPype1
#한글 python library 설치
pip3 install konlpy

#자바 환경변수 설정
%env JAVA_HOME "/usr/lib/jvm/java-8-openjdk-amd64"

#mecab 형태소 분석기 설치
%%bash
bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)
pip3 install /tmp/mecab-python-0.996

#konlpy library 불러오기
import konlpy
from konlpy.tag import Kkma, Komoran, Hannanum, Okt
from konlpy.utils import pprint
from konlpy.tag import Mecab

mecab = Mecab()
sentence = "비 오는 날에는 역시 짬뽕이지"
temp_X = mecab.morphs(sentence)
temp_X