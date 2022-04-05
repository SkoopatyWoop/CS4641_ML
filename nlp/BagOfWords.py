import nltk
import numpy as np
from typing import List

from pyparsing import col

nltk.download('stopwords')

#TODO: once done, plot false negative rate and folse postive rate using matplotlib
class BOW:

    def __init__(self, data) -> None:
        self.vocab = set()
        self.X = []
        self.y = []
        bags = []
        for post in data:
            self.y.append(post["ethical_tag"])
            bags.append(self.getBagOfWords(post["text"]))
            
        for i, post in enumerate(data):
            bag = bags[i]
            row = self.populate_row(bag)
            self.X.append(row)
        self.X = np.asarray(self.X)
        self.y = np.asarray(self.y)
        column_sums = -np.sum(self.X, axis=0)
        indices = column_sums.argsort()
        top_100 = indices[:100]

        self.X = self.X[:, top_100]

        
    # Bag of words will vectorize each post. It takes a text and creates a vector containing
    # counts for each word. It will also automatically filter out common words that do not
    # provide meaning using nltk.corpus.stopwords.words().
    def getBagOfWords(self, text: str) -> List[str]:
        # clean data, remove some unnecessary words
        # im gonna just steal all this - aubrey
        array = text.split()
        array = [word for word in array if word not in nltk.corpus.stopwords.words('english')]
        
        counts = {}
        for word in array:
            if word not in counts:
                counts[word] = 0
            self.vocab.add(word) # add word to global vocabulary
            counts[word] += 1
        return counts
        
    


    # ensure all datapoints have the same dimensions. for each datapoint,
    # check it agains the global vocab. any word in the global vocab that isn't
    # in the datapoint gets added to that datapoint.
    def populate_row(self, counts):
        row = []
        for word in self.vocab:
            if word not in counts:
                row.append(0)
            else:
                row.append(counts[word])
        return row
    
    

def main():
    data = [{
        "id": "rtbuap",
        "num_awards": 4,
        "num_reports": 0,
        "score": 3069,
        "ups": 3069,
        "upvote_ratio": 0.86,
        "text": "LPT: Don’t fall for the “started my company in a basement/garage” trope. ",
        "ethical_tag": True,
        "_rid": "pnokAKaWZtICAAAAAAAAAA==",
        "_self": "dbs/pnokAA==/colls/pnokAKaWZtI=/docs/pnokAKaWZtICAAAAAAAAAA==/",
        "_etag": "\"1f0075c9-0000-0100-0000-623144cd0000\"",
        "_attachments": "attachments/",
        "_ts": 1647396045
    },
    {
    "id": "rtbtn4",
    "num_awards": 0,
    "num_reports": 0,
    "score": 8,
    "ups": 8,
    "upvote_ratio": 0.63,
    "text": "LPT: Do you enjoy procrastination but don’t like it? How about procrastinating procrastination? ",
    "ethical_tag": True,
    "_rid": "pnokAKaWZtIDAAAAAAAAAA==",
    "_self": "dbs/pnokAA==/colls/pnokAKaWZtI=/docs/pnokAKaWZtIDAAAAAAAAAA==/",
    "_etag": "\"1f0076c9-0000-0100-0000-623144cd0000\"",
    "_attachments": "attachments/",
    "_ts": 1647396045
},
{
    "id": "rtav32",
    "num_awards": 0,
    "num_reports": 0,
    "score": 37,
    "ups": 37,
    "upvote_ratio": 0.75,
    "text": "LPT: Use paragraphs when typing a long story [deleted]",
    "ethical_tag": True,
    "_rid": "pnokAKaWZtIGAAAAAAAAAA==",
    "_self": "dbs/pnokAA==/colls/pnokAKaWZtI=/docs/pnokAKaWZtIGAAAAAAAAAA==/",
    "_etag": "\"1f007ac9-0000-0100-0000-623144cd0000\"",
    "_attachments": "attachments/",
    "_ts": 1647396045
}]
    bow = BOW(data)
    print(bow.X)
    print(bow.y)

if __name__ == "__main__":
    main()