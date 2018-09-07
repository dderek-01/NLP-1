import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer as pst

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = pst(train_text)

# tokenize into sentences
tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
	try:
		for i in tokenized:
			words = nltk.word_tokenize(i)
			tagged = nltk.pos_tag(words)

			# chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""

			chunkGram = r"""Chunk: {<.*>+}
									}<VB.?|IN|DT|TO>+{"""
			chunkParser = nltk.RegexpParser(chunkGram)
			chunked = chunkParser.parse(tagged)

			print chunked.draw()

	except Exception as e:
		print(str(e))

process_content()
