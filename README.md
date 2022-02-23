# ML - Our group's Project Proposal

## Introduction
  * Introduction/Background: A quick introduction of your topic and mostly literature review of what has been done in this area. You can briefly explain your dataset and its features here too.
    * The topic is classifying a body of text on its ethicality. There has been substantial research done in the field of classifying the ethicality and/or morality of corpora. This will serve as an extension of existing research by leveraging contemporary text from the popular online forum Reddit. Our dataset will include the text from two highly active subreddits: LifeProTips and UnethicalLifeProTips. The dataset will be labeled as follows: if the post came from LifeProTips, it will be labeled as ethical; if the post came from UnethicalLifeProTips, it will be labeled as ethical. The estimated samples (posts) is roughly 2 million. The features include: title, body upvotes, downvotes, and certain metadata such as user_id and data_posted.

    
## Problem Statement	
 * Misinformation on the Internet has been an ever-present problem in the age of information, leading to greater difficulty in finding trustworthy, ethical guidance online. Following advice on the internet is dangerous in and of itself, but if we can help classify advice as ethically correct or incorrect, we can help mitigate the negative effects of misinformation and help steer users towards making the decision they want to make.


## Methods: Dataset	
  * Data will be pulled from two subreddits: r/LifeProTips and r/UnethicalLifeProTips
  * Use Reddit API for collecting data, and store in Azure SQL for free ~250 GB storage
  * Data will be labeled as “ethical” or “unethical” accordingly
    * We assume all data from r/LifeProTips is ethical, all data from r/UnethicalLifeProTips is unethical
  * Projected number of samples is ~2 million
  * The features include post title, body text, upvotes, downvotes, and metadata
## Methods: Learning
  * Supervised learning
  * Logistic Regression: to classify ethical/unethical.
  * Bag of Words: to convert words to a vector, we want to represent our words by a vector, as well as the frequency of the words 
## Potential Goals and Applications
  * Establish a model to classify new text as ethical or unethical
  * General analysis of what makes a post ethical
  * Create bot that can analyze posts on reddit that have replies tagging our reddit bot






  


