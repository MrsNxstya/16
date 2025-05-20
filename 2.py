3.	import nltk
4.	import string
5.	from nltk.tokenize import TreebankWordTokenizer
6.	from nltk.corpus import stopwords
7.	from nltk.stem import PorterStemmer, WordNetLemmatizer
8.	
9.	     nltk.download('stopwords')
10.	nltk.download('wordnet')
11.	
12.	text = """
13.	Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do. 
14.	Once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, 
15.	"and what is the use of a book," thought Alice "without pictures or conversation?"
16.	"""
17.	
18.	tokenizer = TreebankWordTokenizer()
19.	tokens = tokenizer.tokenize(text)
20.	
21.	lemmatizer = WordNetLemmatizer()
22.	stemmer = PorterStemmer()
23.	
24.	processed_tokens = []
25.	for token in tokens:
26.	    token = token.lower()
27.	    if token in string.punctuation:
28.	        continue
29.	    if token in stopwords.words("english"):
30.	        continue
31.	    lemma = lemmatizer.lemmatize(token)
32.	    stem = stemmer.stem(lemma)
33.	    processed_tokens.append(stem)
34.	
35.	filename = "processed_text.txt"
36.	with open(filename, "w", encoding="utf-8") as f:
37.	    f.write(" ".join(processed_tokens))
38.	
39.	print("\n📄 Оброблений текст з файлу:")
40.	with open(filename, "r", encoding="utf-8") as f:
41.	    print(f.read())
