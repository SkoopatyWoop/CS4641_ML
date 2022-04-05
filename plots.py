from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


#TODO: MAKE SURE TO HAVE TRUTH AND PREDICTED DATA LISTS BUILT BEFORE USING THIS
#for example, look at the default values for y_true and y_pred
class plot:
    def __init__(self, y_true = [1,1,0,0,1], y_pred = [1,1,1,0,1]):
        self.FPR = 0
        self.FNR = 0
        self.y_true = y_true
        self.y_pred = y_pred

        self.cm = confusion_matrix(y_true, y_pred)

      
    def fpr_fnr(self):
        tn, fp, fn, tp = confusion_matrix(list(self.y_true), list(self.y_pred), labels=[0, 1]).ravel()

        accuracy_score(self.y_true, self.y_pred)
        acc = (tp+tn) / (tp+tn+fn+fp)
        tot = self.cm.sum()
        tot = tn+tp+fp+fn
        

        #False positive rate, False negative rate
        FPR, FNR = fp / tot, fn / tot
        ax = sns.heatmap(self.cm, annot=True, cmap='Blues')

        ax.set_title('Seaborn Confusion Matrix with labels\n\n');
        ax.set_xlabel('\nPredicted Values')
        ax.set_ylabel('Actual Values ');

        ## Ticket labels - List must be in alphabetical order
        ax.xaxis.set_ticklabels(['False','True'])
        ax.yaxis.set_ticklabels(['False','True'])

        ## Display the visualization of the Confusion Matrix.
        plt.show()

          ## Display the visualization of the Confusion Matrix.


        return (FPR, FNR)


# x = plot()
# print(x.cm)
# x.fpr_fnr()




