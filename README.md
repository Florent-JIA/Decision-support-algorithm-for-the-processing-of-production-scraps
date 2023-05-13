# 4.Decision-support-algorithm-for-the-processing-of-production-scraps
This is an entreprise project. My teammates and I developped a decision support algorithm for our client to help him to decide whether to throw away the production scraps, recycle it or sell it.

## Identification of needs of our client
The major need is the realization of a decision support algorithm for the processing of 2D production scraps for industrial oriented companies.

Finally, we decided that our algorithm shoul meet several criteria:
- Be generic: must be suitable for any size and any type of material.
- Must answer yes/no for internal revaluation when all data are given (shape and dimensions of scraps + criteria).
- Must be able to process a csv file as input for the shape of production scrapss (SolidWorks + integration into the algorithm) (N.B: for reasons of simplification of the work, we subsequently proceeded to excel files).
- Algorithm language: Python

## Definition of decision criteria
The criteria taken into account in the end are the following:
- Raw material cost
- Cost of storage
- Downstream waste management cost
- Taxes on waste
- Government aid
- Total cost of additional equipment
- Number of operators to be trained
- Estimated training time
- Training cost per hour
- Cost associated with additional labor for production from revaluated materials
- Cost incurred by the handling and transport of production scraps
- Carbon footprint of the contribution of a ton of raw material
- The social impact represented by a score provided by the company

## Choice of decision support model
By studying different models of decision support algorithms, we chose the one that uses a weighted sum. This model consists of setting several criteria and classifying them by assigning each of them a certain weight (a value between 0 and 1 for example).

This model is consistent with our problem, because it allows us to categorize the criteria according to 3 categories: Economic, Environmental and Social. This distinction is intended to give the choice to the company to favor an aspect according to their needs.

## Mathematical model
For each scrap i, the algorithm will decide whether it should be upgraded or not. There is a binary variable Di which is associated with each fall and which makes it possible to model this decision-making mechanism. This is worth 0 if the fall is not upgraded and 1 if it is.

For each category (Economic, Environmental and Social), there is an indicator (Respectively If, Ie and Is) between 0 and 1 which is associated, the latter represents a score, therefore the higher the value, the better it is. is for business.

The goal of the algorithm is to maximize the total score:

<br>![1](https://github.com/Weizhe-JIA/4.Decision-support-algorithm-for-the-processing-of-production-scraps/blob/main/imgs/1.png)
<br>With Af, Ae and As which are the weighting coefficients associated with the 3 categories

The program determines, for each Di, whether to associate it with 0 or 1 by exploring the space of solutions and giving the best configuration. Its output is simply the display of Di along with the values ​​of all the other variables, allowing the company to know which offcuts to reuse and what the optimal reuse rate is.

The economic indicator is at the heart of the problem, we decided to spend a majority of time on it because it seemed essential to us to have an estimate of costs and gains that was reliable and close to reality. We have therefore established a formula to determine the cost associated with the revaluation of scraps Crevalorisation

![2](https://github.com/Weizhe-JIA/4.Decision-support-algorithm-for-the-processing-of-production-scraps/blob/main/imgs/2.png)

As the If indicator must be between 0 and 1, we compared this cost with a reference cost. We have chosen to use the cost in the event that no revaluation is carried out Crien as a basis for comparison.

The If indicator being between 0 and 1 and having to increase when the revaluation cost decreases, a correct modeling is:

<br>![3](https://github.com/Weizhe-JIA/4.Decision-support-algorithm-for-the-processing-of-production-scraps/blob/main/imgs/3.png)

<br>For the environmental indicator , the calculation is done in the same way as before to ensure that Ie is between 0 and 1.

Finally, for the social indicator, as we did not manage to establish a simple formula to calculate it, we ended up taking it as a data in the form of our between 0 and 10 which is then brought back in the interval [0.1].

## Test
We created a test file in parallel (accessible in the archive) to observe the behavior of the modeling in several scenarios. The main decision variable is "𝐷𝑒𝑐𝑖
", it is therefore interesting to make a random state generator for this variable. This is what we did and, depending on the results, we adapted the definition of the economic indicator.

For example, in the table [donnees chutes](https://github.com/Weizhe-JIA/4.Decision-support-algorithm-for-the-processing-of-production-scraps/blob/main/donnees%20chutes.xlsx/) we created 9 production scraps and assigned values to their variables. The [extraction_chutes](https://github.com/Weizhe-JIA/4.Decision-support-algorithm-for-the-processing-of-production-scraps/blob/main/extraction_chutes.py/) program is used to extract information of those production scraps and create a dictionary. The table [donnes generales criteres](https://github.com/Weizhe-JIA/4.Decision-support-algorithm-for-the-processing-of-production-scraps/blob/main/donnees%20generales%20criteres.xlsx/) saves the value of each parameter in the mathematical model. The [extraction_criteres](https://github.com/Weizhe-JIA/4.Decision-support-algorithm-for-the-processing-of-production-scraps/blob/main/extraction_criteres.py/) is used to extract these values and create a dictionary.

In the [test](https://github.com/Weizhe-JIA/4.Decision-support-algorithm-for-the-processing-of-production-scraps/blob/main/test.py/) program, we used a loop to look at all possible combinations of treatment options for these 9 production scraps and calculate the value of the economic indicator for each case. Finally, we can get the case with the highest value of the economic indicator.

Specifically, production scraps 2, 6 have No for theier compability attribute. So, the must be discarded. For the reminders, the economic indicator value is the largest when reusing ID 3, 4, 5, 7 production scraps.
