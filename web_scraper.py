import pandas as pd
import urllib
import requests
from bs4 import BeautifulSoup
import wikipedia
url='https://en.wikipedia.org/wiki/South_Asian_river_dolphin'
#url='https://www.gutenberg.org/files/11/11-0.txt'
res=requests.get(url)
html_page=res.content
print(res)
check=url.split('/')
z=check[-1]
x=z.replace('_',' ')
for i in check:
       if i=='en.wikipedia.org':
              results = wikipedia.search(x)
              page = wikipedia.page(results[0])
              df = page.content
              # print(df)
              break


       else:
              def extract_text(url):
                     try:
                            response = requests.get(url)
                            soup = BeautifulSoup(response.content, 'html.parser')
                            text = soup.get_text()
                            return text
                     except Exception as e:
                            print(f"An error occurred: {e}")
                            return None


              if __name__ == "__main__":
                     df = extract_text(url)
                     if df:
                            pass
                     else:
                            print("Failed to extract text from the website.")
            

from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk
#nltk.download('punkt')
text=df
text=str(text).lower()
parser=PlaintextParser.from_string(text,Tokenizer("english"))
summarizer_lex=LexRankSummarizer()
# textrank
summary=summarizer_lex(parser.document,5)
h=str(summary)
j=h.replace('>, <Sentence:',' ' )
print(j)
with open('example.txt', 'w', encoding='utf-8') as f:
    f.write(j)
