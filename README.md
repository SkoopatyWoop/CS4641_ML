# ML - G4

## Introduction/Background
  * The topic is classifying a body of text on its ethicality. There has been substantial research done in the field of classifying the ethicality and/or morality of corpora. This will serve as an extension of existing research by leveraging contemporary text from the popular online forum Reddit. Our dataset will include the text from two highly active subreddits: LifeProTips and UnethicalLifeProTips. The dataset will be labeled as follows: if the post came from LifeProTips, it will be labeled as ethical; if the post came from UnethicalLifeProTips, it will be labeled as Unethical. The estimated samples (posts) is roughly 2 million. The features include: title, body upvotes, downvotes, and certain metadata such as user_id and data_posted.

    
## Problem Statement	
 * Misinformation on the Internet has been an ever-present problem in the age of information, leading to greater difficulty in finding trustworthy, ethical guidance online. Following advice on the internet is dangerous in and of itself, but if we can help classify advice as ethically correct or incorrect, we can help mitigate the negative effects of misinformation and help steer users towards making the decision they want to make.

## Data Collection
 * We used PushShiftAPI to access the subreddits LifeProTips and UnethicalLifeProTips and download post data from them. After downloading the posts, we upload them to our cloud database on Microsoft Azure.
 * At this point, the Azure database contains around 30000 ethical entries and only around 3000 unethical entries.
 * The reason for the large difference in entries is because the subreddit for the ethical tips is much larger, older, and more popular than the subreddit for unethical tips. As such, the number of quality posts in the ethical subreddit is much larger than the unethical subreddit.

## Data Cleaning
 * We realized that the majority of the posts we were uploading to Azure had low "score". On Reddit, score is tied to the quality of the post. If a post has low score, it could mean a variety of things, including that the post is off-topic or unfit for the subreddit it's in. Inclusion of these posts would obscure our dataset and lead to a less accurate model. So, we decided to only grab posts with positive scores, which will hopefully be more on-topic and provide our model with a more accurate view of what is and isn't ethical.
 * In order to ensure that the posts in our dataset were quality posts that were representative of their respective subreddits, we imposed a score requirement of >1. This decreased the number of entries from both subreddits: 27077 ethical and 2472 unethical.

## Methods: Dataset / Learning
 * Our group decided to use both Naive Bayes and Logistic Regression to classify ethical and unethical posts.
 * The dataset we had after data collection consisted of full text posts and labels. However, in order to feed the data to our model and have it make predictions, we need to convert the text posts to word vectors.
  
* Initally, we used the natural language processing technique, Bag of Words. Using bag of words, each text post becomes a vector with each element in the vector representing the count of each word in the original text post. 

* We later found an NLP method called [tf-idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) which converts the text contents of our Reddit posts into word vectors weighted inversely by their frequency in the posts. This works better because uncommon words are better predictors of the ethicality of the post rather than words such as "the". 

* First, we split the reddit posts using an 80% training 20% testing split. Second, we applied either bag of words or tf-idf vectorization to the text contents of our reddit posts. Third, we trained Complement Naive Bayes and Logistic Regression models on the vectorized data. Finally, we used cross validation to determine the accuracy of our model in predicting the ethicality of a Reddit post.

 * We had much more ethical entries than unethical entries. To accomodate for the imbalance in the number of entries for both of our labels, we limited the number of ethical entries our model trained on to equal the number of unethical entries.

## Results and Discussion 
 * We ran all of our models on a dataset of 4,944 total data entries with an equal number of ethical and unethical entries. 

* Using bag of words, our Naive Bayes model achieved 66.4% accuracy using cross validation with 5 folds. Our Logistic Regression model achieved 70% cross validation accuracy. Using tf-idf our Naive Bayes model achieved 79% cross validation accuracy and our Logistic Regression model achieved 80% cross validation accuracy.

* The best performing model on our dataset was Logistic Regression with tf-idf vectorization. It appears that using tf-idf vectorization boosted our accuracy by about 10% for all models. This could be because tf-idf is a more predictive representation of text than bag of words. Especially since tf-idf weights uncommon words more, training on this representation could allow our model to better associate patterns of words with ethicality.

 * For another iteration, our dataset consisted of around 27,000 ethical entries but only 2,472 unethical entries. We shuffled the dataset and trained our Naive Bayes model on the first 80% of the dataset, then tested on the remaining 20% of the dataset. The resulting model was able to predict the testing set with around 65% accuracy. This could be because of the increased amount of data we introduced, or it could be because there is vastly more ethical entries than unethical entries. Our model could have accidentally learned to predict ethical entries every time, and our testing set could just consist of 65% ethical entries. We plan to investigate this further.


## References
  * Barnes, K., Riesenmy, T., Trinh, M., Lleshi, E., Balogh, N., & Molontay, R. (2021, March 09). Dank or not? analyzing and predicting the popularity of memes on Reddit - Applied Network Science. Retrieved February 23, 2022, from [here](https://appliednetsci.springeropen.com/articles/10.1007/s41109-021-00358-7)
  * Chew, R., Kery, C., Baum, L., Bukowski, T., Kim, A., & Navarro, M. (n.d.). Predicting age groups of reddit users based on posting behavior and metadata: Classification Model Development and validation. Retrieved February 23, 2022, from [here](https://publichealth.jmir.org/2021/3/e25807/)
  * Donelson, C., Sutter, C., Pham, G., Narang, K., Wang, C., & Yun, J. (2021, February 27). Using a machine learning methodology to analyze reddit posts regarding child feeding information - journal of child and family studies. Retrieved February 23, 2022, from [here](https://link.springer.com/article/10.1007/s10826-021-01923-5)

## Potential Goals and Applications
  * Establish a model to classify new text as ethical or unethical
  * General analysis of what makes a post ethical
  * Create bot that can analyze posts on reddit that have replies tagging our reddit bot

|Date   | People Assigned  | Tasks  |
|---    |---               |---     |
| 3/4  | Aubrey, Andy, Vikas  | Data cleaning, Data visualization, Feature reduction|
| 3/11  | All members, Krish, Leul  | Implementation and coding Results and evaluation |
| 3/18  |Vikas, Leul, Krish|  Data cleaning, Data visualization, Feature reduction (As needed) |
|3/25| Aubrey, Andy, Vikas|  Implementation and coding Results and evaluation |
|4/1| All members| Cleaning up the work so far (runway) Draft Midterm report|
| 4/5  | All members  |  Midterm report date |
|4/8| All members Leul, Krish| Finalize Codes Test model |
| 4/15| All members| Draft final report  |
| 4/22  |  All members | Record video  |
|  4/26     | All members| Project due|


### [Video Proposal](https://youtu.be/TdZ1eX-1MKw)
 
### Midterm Report
 
All of our model implementation is done in the [NB_LogReg notebook](nlp/NB_LogReg.ipynb)

 * As a group, we decided to impement a Naive Bayes model instead of a Logistic Regression model. This decision was made so that we would be able to have a model running in time for the midterm report. Our reasoning behind this decision was that we were all more familiar with Naive Bayes models than with Logistic Regression models, and if we worked with something that we were more comfortable with, we would be able to implement it faster. Between the midterm report and the final report however, we may implement a Logistic Regression model and compare the accuracy of the two models.
 * For data cleaning, we went through each data entry we scraped from the two subreddits and used some common natural language processing techniques for data cleaning, like filtering out common stop words like "a", "an", or "the". We also found that most of the data entries started with the letters "LPT:" or "ULPT:", so we filtered those characters out of each entry as well. This way, we ensure that our dataset has meaningful data for our model to run with.
 * To translate the text entries to data our model can read and train on, we used Bag of Words and [tf-idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) to vectorize the text entries.
 * After implementing Bag of Words, we plan on plotting the False Positive and False Negative Rates and the Confusion Matrix
 * Since we are classifying Ethical/Unethical, we are going to have truth and predicted data as an array of 0's and 1's each, this is how the rates and confusion matrices will be made
 * We have decided to plot False Positives, False Negatives and a Confusion Matrix so that we can see how well our model is running.
 * We're currently going to limit our top features to 100 so that we don't run out of space on our systems, and so our model can run faster
 * For our Azure DB, we are using the JSON format to better pull our data into python with more ease, such as our text metadata for classification
 * We have done dimensionality reduction to make sure we don't have any unnecessary words while we train our model. We have also limited the total number of features (words) to 100 so that we don't run out of memory when training. 
 * If we have enough time and spatial resources, we will allow more features to train our model
 * We're using [Complement Naive Bayes models](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.ComplementNB.html) & [Logistic Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) to train our models because we read that both of these models work very well with NLP classification tasks like our project
* Using cross validation testing, our Logistic Regression model achieved 79% accuracy and our Logistic Regression model achieved 80% accuracy. The models were* trained on preprocessed reddit post text which was vectorized using tf-idf.
* After testing several kinds of penalty: L1, L2, elasticnet (L1 & L2), we determined that L2 norm produces the best performance with our dataset.

# Graphs & Images

![Logistic Regression Wordcloud](/images/lr-wordcloud-nosnoo.png "Logistic Regression Wordcloud (No Snoo)")

![Logistic Regression Wordcloud](/images/lr-wordcloud.png "Logistic Regression Wordcloud")

![Confusion Matrix](/images/confusionmatrix.png "Confusion Matrix")


### Final Report
 * Not implemented yet


  


