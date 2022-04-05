import numpy as np
RANDOM_SEED = 5


class NaiveBayes(object):
    def __init__(self):
        pass

    def likelihood_ratio(self, ratings):  # [5pts]
        '''
        Args:
            rating_stars: a python list of numpy arrays that is length <number of labels> x 1
            
            Example rating_stars for Five-label NB model:
    
            ratings_stars = [ratings_1, ratings_2, ratings_3, ratings_4, ratings_5] -- length 5
            ratings_1: N_ratings_1 x D
                where N_ratings_1 is the number of reviews that gave an Amazon
                product a 1-star rating and D is the number of features (we use the word count as the feature)
            ratings_2: N_ratings_2 x D
                where N_ratings_2 is the number of reviews that gave an Amazon
                product a 2-star rating and D is the number of features (we use the word count as the feature)
            ratings_3: N_ratings_3 x D
                where N_ratings_3 is the number of reviews that gave an Amazon
                product a 3-star rating and D is the number of features (we use the word count as the feature)
            ratings_4: N_ratings_4 x D
                where N_ratings_4 is the number of reviews that gave an Amazon
                product a 4-star rating and D is the number of features (we use the word count as the feature)
            ratings_5: N_ratings_5 x D
                where N_ratings_5 is the number of reviews that gave an Amazon
                product a 5-star rating and D is the number of features (we use the word count as the feature)
            
            If you look at the end of this python file, you will see a docstring that contains more examples!
            
        Return:
            likelihood_ratio: (<number of labels>, D) numpy array, the likelihood ratio of different words for the different classes of ratings.
        '''
        D = ratings[0].shape[1]
        #likelihood_ratio = np.ones(len(ratings), ratings[0].shape[1])
        ratios = []
        for rating in ratings:
            denominator = np.sum(rating) + D
            column_sums = np.sum(rating, axis=0) + 1
            ratios.append(column_sums / denominator)
        likelihood_ratio = np.array(ratios)
        print(likelihood_ratio.shape)
        return likelihood_ratio



    def priors_prob(self, ratings):  # [5pts]
        '''
        Args:
            rating_stars: a python list of numpy arrays that is length <number of labels> x 1
            
            Example rating_stars for Five-label NB model:
    
            ratings_stars = [ratings_1, ratings_2, ratings_3, ratings_4, ratings_5] -- length 5
            ratings_1: N_ratings_1 x D
                where N_ratings_1 is the number of reviews that gave an Amazon
                product a 1-star rating and D is the number of features (we use the word count as the feature)
            ratings_2: N_ratings_2 x D
                where N_ratings_2 is the number of reviews that gave an Amazon
                product a 2-star rating and D is the number of features (we use the word count as the feature)
            ratings_3: N_ratings_3 x D
                where N_ratings_3 is the number of reviews that gave an Amazon
                product a 3-star rating and D is the number of features (we use the word count as the feature)
            ratings_4: N_ratings_4 x D
                where N_ratings_4 is the number of reviews that gave an Amazon
                product a 4-star rating and D is the number of features (we use the word count as the feature)
            ratings_5: N_ratings_5 x D
                where N_ratings_5 is the number of reviews that gave an Amazon
                product a 5-star rating and D is the number of features (we use the word count as the feature)
            
            If you look at the end of this python file, you will see a docstring that contains more examples!
            
        Return:
            priors_prob: (1, <number of labels>) numpy array, where each entry denotes the prior probability for each class
        '''
        priors = []
        total_sum = 0
        for rating in ratings:
            total_sum += np.sum(rating)
        for rating in ratings:
            priors.append(np.sum(rating) / total_sum)
        priors_prob = np.array(priors)
        priors_prob = np.reshape(priors_prob, (1, np.size(priors_prob)))
        print(priors_prob.shape)
        return priors_prob

    # [5pts]
    def analyze(self, likelihood_ratio, priors_prob, X_test):
        '''
        Args:
            likelihood_ratio: (<number of labels>, D) numpy array, the likelihood ratio of different words for different classes of ratings
            priors_prob: (1, <number of labels>) numpy array, where each entry denotes the prior probability for each class
            X_test: (N_test, D) numpy array, a bag of words representation of the N_test number of ratings that we need to analyze
        Return:
            ratings: (N_test,) numpy array, where each entry is a class label specific for the Naïve Bayes model
        '''
        # return
        #raise NotImplementedError
        ratings = []
        num_labels, D = likelihood_ratio.shape
        N_test = X_test.shape[0]
        for test_data in X_test:
            best_label = None
            max_product = float('-inf')
            for label in range(num_labels):
                product = priors_prob[0, label]
                
                l_ratios = likelihood_ratio[label]
                for j in range(D):
                    product *= l_ratios[j] ** test_data[j]
                if product > max_product:
                    best_label = label
                    max_product = product
            ratings.append(best_label)
        return np.array(ratings)