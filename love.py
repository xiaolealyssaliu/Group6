
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from textblob import TextBlob

arrLove = [
    'love',
    'honey',
    'sweetheart',
    'baby',
    'need'
    'valentine',
    'lover',
    'romance',
    'romantic',
    'married',
    'engaged',
    'marry',
    'engage',
    'blessing',
    'blessings',
    'loving',
    'mine',
    'rose',
    'roses',
    'heart',
    'adorable',
    'amazing',
    'angel',
    'babe',
    'beautiful',
    'beloved',
    'darling',
    'dearest',
    'enchanting',
    'gorgeous',
    'handsome',
    'heavenly',
    'paramour',
    'sweetie',
    'swoon',
    'wonderful',
    'adore',
    'admire',
    'care',
    'cherish',
    'choose',
    'chosen',
    'daydream',
    'delight',
    'dream',
    'girl',
    'need',
    'prize',
    'lifetime',
    'affection',
    'passion',
    'amour',
    'sugar',
    'yearn',
    'family',
    'caring',
    'happiness',
    'forever',
    'happy',
    'trust',
    'kiss',
    'hugs',
    'warm',
    'fun',
    'kisses',
    'joy',
    'sex',
    'friendship',
    'marriage',
    'hug',
    'amore',
    'desire',
    'hope',
    'like',
    'liking',
    'loving',
    'respect',
    'wife',
    'husband',
    'faithful',
    'appreciate',
    'friends',
    'fond',
    'fondness',
    'favourite',
    'bliss',
    'chocolate',
    'darling',
    'dear',
    'intimate',
    'intimacy',
    'beloved',
    'breathtaking',
    'bright',
    'brilliant',
    'crazy',
    'dedicated',
    'devotion',
    'friendly',
    'gorgeous',
    'graceful',
    'incredible',
    'lovable',
    'lovely',
    'lucky',
    'soulmate',
    'precious',
    'attractive',
    'sweetness']
def love(data):
    pull_chars = '!;,.?'
    for pull_char in pull_chars:
        data = data.replace(pull_char, '')
    stop = stopwords.words('english')
    data = " ".join(word for word in data.split() if word not in stop)
    data = TextBlob(data).words
    bw = [1 if i.lower() in arrLove else 0 for i in data]
    k = sum(bw)/len(data)
    k = k / 0.2
    k = k // 0.1 / 10
    return k


