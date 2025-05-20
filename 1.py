3.	import matplotlib.pyplot as plt
4.	from collections import Counter
5.	import string
6.	import requests
7.	import os
8.	
9.	filename = "carroll-alice.txt"
10.	if not os.path.exists(filename):
11.	    print("Файл не знайдено. Завантаження з інтернету...")
12.	    url = "https://www.gutenberg.org/files/11/11-0.txt"
13.	    response = requests.get(url)
14.	    with open(filename, "w", encoding="utf-8") as f:
15.	        f.write(response.text)
16.	    print("Файл збережено як", filename)
17.	
18.	with open(filename, "r", encoding="utf-8") as file:
19.	    text = file.read()
20.	
21.	words = text.split()
22.	print("Кількість слів у тексті:", len(words))
23.	
24.	word_counts = Counter(words)
25.	top_words = word_counts.most_common(10)
26.	
27.	words_, counts = zip(*top_words)
28.	plt.figure(figsize=(10, 5))
29.	plt.bar(words_, counts, color='skyblue')
30.	plt.title("10 найбільш вживаних слів (без фільтрації)")
31.	plt.xticks(rotation=45)
32.	plt.tight_layout()
33.	plt.savefig("top10_raw.png")
34.	plt.show()
35.	
36.	stop_words = {
37.	    "the", "and", "to", "of", "a", "i", "it", "in", "was", "that", "you", "is",
38.	    "he", "she", "for", "on", "with", "as", "his", "at", "had", "be", "but",
39.	    "not", "her", "they", "this", "my", "me", "or", "so", "what", "all"
40.	}
41.	punctuation = set(string.punctuation)
42.	
43.	filtered_words = [
44.	    word.lower().strip(string.punctuation)
45.	    for word in words
46.	    if word.lower() not in stop_words and word not in punctuation and word.isalpha()
47.	]
48.	
49.	filtered_counts = Counter(filtered_words)
50.	top_filtered = filtered_counts.most_common(10)
51.	
52.	words_, counts = zip(*top_filtered)
53.	plt.figure(figsize=(10, 5))
54.	plt.bar(words_, counts, color='orange')
55.	plt.title("10 найбільш вживаних слів (після фільтрації)")
56.	plt.xticks(rotation=45)
57.	plt.tight_layout()
58.	plt.savefig("top10_filtered.png")
59.	plt.show()
60.	
