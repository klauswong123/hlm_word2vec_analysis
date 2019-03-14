from gensim.models.word2vec import Word2Vec, LineSentence
inp='hlm.txt'
outp1 = 'hlm.text.model'
outp2 = 'hlm.zh.text.vector'
model = Word2Vec(LineSentence(inp), size=100, window=5, min_count=5, workers=4)
model.save(outp1)
model.wv.save_word2vec_format(outp2, binary=False)
