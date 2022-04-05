# ML - G4 Midterm Report

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
 * Our group decided to change from using Logistic Regression model to Naive Bayes model in order to get the model up and running for the midterm report. We were more familiar with Naive Bayes than with Logistic Regression, so to save on implementation time, we went forward with a Naive Bayes implementation.
 * The dataset we had after data collection consisted of full text posts and labels. However, in order to feed the data to our model and have it make predictions, we need to convert the text posts to word vectors. To do this, we used the natural language processing technique, Bag of Words. Using bag of words, each text post becomes a vector with each element in the vector representing the count of each word in the original text post. We'll be able to feed this data to our Naive Bayes net.
 * We had much more ethical entries than unethical entries. To accomodate for the imbalance in the number of entries for both of our labels, we limited the number of ethical entries our model trained on to equal the number of unethical entries.

## Results and Discussion
 * TODO: get results and discussion


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
 
### Final Report
 * Not implemented yet


  


