from gensim.models.word2vec import Word2Vec, LineSentence
import pandas as pd

model = model = Word2Vec.load('hlm.text.model')

def most_similar(w2v_model, words, topn=10):
    similar_df = pd.DataFrame()
    for word in words:
        try:
            similar_words = pd.DataFrame(w2v_model.wv.most_similar(word, topn=topn), columns=[word, 'cos'])
            similar_df = pd.concat([similar_df, similar_words], axis=1)
        except:
            print(word, "not found in Word2Vec model!")
    return similar_df

print(most_similar(model, ['宝玉','黛玉']))