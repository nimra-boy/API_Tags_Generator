# Import Python libraries
from bs4 import BeautifulSoup
import re
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
# import nltk
# nltk.download('wordnet')
# nltk.download('stopwords')

# Preprocessing for the question
def preprocess_text(text):
    # remove code tag
    soup = BeautifulSoup(text,"lxml")
    code_to_remove = soup.findAll("code")
    for code in code_to_remove:
        code.replace_with(" ")
    # remove html tag
    txt_without_html_tag = soup.get_text()
    # only letters
    letters_only = re.sub("[^a-zA-Z]", " ", txt_without_html_tag)
    #lowercase
    lowercase = letters_only.lower()
    # Create an instance of RegexpTokenizer for alphanumeric tokens
    tokeniser = RegexpTokenizer(r'\w+')
    # Tokenise string
    tokens = tokeniser.tokenize(lowercase)
    # Create an instance of WordNetLemmatizer
    lemmatiser = WordNetLemmatizer()
    # lemmatise tokens
    lemmas = [lemmatiser.lemmatize(token, pos='v') for token in tokens]
    # Remove stops words
    keywords = [lemma for lemma in lemmas if lemma not in stopwords.words('english')]
    return keywords
