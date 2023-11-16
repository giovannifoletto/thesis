> The Machine Learning is the "Field of study that gives computers the ability to learn without being explicitly programmed".

In general, the more options you give the computer and the models to learn, the better it would be. 

The most used methods of machine learnings are:
- Supervised learning: most used in real-world application, most used in specialized programs.
- Unsupervised learning
- Recommender systems
- Reinforcement learning

## Supervised Learning
It is the same of supervised machine learning.
You give the learning algorithms examples that includes correct answers (the correct labels $Y$). This allow the computer to perform better and, after that, work alone.
After a sufficient number of correct label elements, the system is ready to collect a new element, and try to understand what is it based on the history of the data.

The data, then, can be represented in some kind of way, like a cartesian way. With that is appropiate to use a courve that fits this data. After that, the systems retrun the value of the function in the new input data.

> **Regression**: predict a number from infinitely many possible outputs.

The classification problems are another type of machine learning algorithm that can be applied in the reality. The classification is different from regression because there is a limited possibility in the output. The fact that there are only two possible outputs, there is the possibility to change the plotting "strategy", in a more linear way.

> **Classification**: predicts categories, and outputs a small numbers of possible one.

There is the possibility to have more than one input data. After that, the algorithm can find a boundary line (some kind of value that divide in half the possibility). Then there could be infinite boundary lines that can results in a larger set of input and outputs.

## Unsupervised Learning

In supervisor learning, each output is correlated with a specific label that tells how the particular data is respectively at the question is investigated.
The unsupervised learning are given to the algorithm a set of data without labels. The questions cannot find if the tumors is malicous or not, but the algorithm can find a structure of the data and find a/some patterns. This allow the algorithm to find out if some data in input is from a specific group or from another.
A specific techniquest of unsupervised learning is called **clustering** and perform a pattern-finding algorithm between all object, allowing to tells, if another input is inserted, if something belongs to one or to the other (from one cluster of the others). 

For examples, clustering is used in google news to link between news.
The clustering type of algorithm is used in grouping customers, too.

The unsupervised learning comes with inputs $x$ but no outputs lables $y$. 
The clustering is used to group similar data points together. Another used is the **anomaly detection** algorithm, to find unusual data points in the collections. The last used is the *dimensionality reduction* that allow a compression and representing it using fewer numbers.
