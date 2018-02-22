from scipy.sparse import csr_matrix
from operator import itemgetter
import pandas as pd


def bi_gram (tweets):
    """
        Generate bi-gram tokenization
        # Input : dictionnary containing uni-gram tokenized tweets
        # Output : dictionnary containing bi-gram tokenized tweets
    """
    
    dico = {}
    for key, value in tweets.items():
        dico[key] = []
        for i in range(len(value)-1) :
            dico[key].append( (value[i],value[i+1]) )
    return dico


def tweet_term_bigram (tweets) :
    """
        Generate tweet x term matrix
        # Input : dictionnary containing bi-gram tokenized tweets
        # Output : csr sparse matrix
    """    

    indptr = [0]
    indices = []
    data = []
    vocabulary = {}
    ids = []
    for key, value in tweets.items():
        ids.append(key)
        for term in value :
            index = vocabulary.setdefault(term, len(vocabulary))
            indices.append(index)
            data.append(1)
        indptr.append(len(indices))
    
    return csr_matrix((data, indices, indptr), dtype=int)
    

def tweet_term_bigram_df (csr):
    """
        Generate tweet x term matrix
        # Input : dictionnary containing bi-gram tokenized tweets
        # Output : dataframe
    """    
    
    indptr = [0]
    indices = []
    data = []
    vocabulary = {}
    ids = []
    for key, value in tweets.items():
        ids.append(key)
        for term in value :
            index = vocabulary.setdefault(term, len(vocabulary))
            indices.append(index)
            data.append(1)
        indptr.append(len(indices))
    
    csr = csr_matrix((data, indices, indptr), dtype=int)

    csr_array = csr.toarray()
    sorted_voca = sorted(vocabulary.items(), key=itemgetter(1))
    new_voca=[]
    for i in sorted_voca:
        new_voca.append(i[0])
        
    return pd.DataFrame(csr_array, index=ids, columns=new_voca)



if __name__ == "__main__":
        
    tweets = { "doc1": ["je", "suis", "une" , "phrase"] , "doc2" : ["I" , "am" , "a" , "sentence"] , "doc3" : ["I", "suis", "a" , "phrase" , "merci" , "a" , "toi"] }
    bg = bi_gram(tweets)
    
    mat = tweet_term_bigram_df(bg)
    print(mat)
    
    
    
    
    
    
    