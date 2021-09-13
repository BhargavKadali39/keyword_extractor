# pip install rake-nltk
from rake_nltk import Rake
rale_nltk_var = Rake()
text = str(input('Enter your data'))

# extracting keywords from the given text using Rake module
rale_nltk_var.extract_keywords_from_text(text)

# importing only ranked and weighty phrases from previous
keyword_extracted = rale_nltk_var.get_ranked_phrases()
print(keyword_extracted)
