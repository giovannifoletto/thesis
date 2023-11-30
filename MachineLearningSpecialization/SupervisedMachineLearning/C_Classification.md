The linear regression can predict some numbers, but classification problems can output something casual, even not a number.

Classification problems could be useful to different problems:
- is an email spam?
- is the transaction fraudolent?
- ...

There are different types of classification algorithms, like **binary classification** that can output only two values ("no"/"yes", "0"/"1", "true"/"false").

To reach the goal of such a classification algorithm, we can start to plot the training set on a graph. 

![[Pasted image 20231128103256.png]]

If there are used wrong function, is possible to have an incorrect classification, and so results incorrect data.

## Logistic regressions

Linear regression is usually not a great fit for classification problems, usually something more like a S is used. This function is called **sigmoid**, and is used in the logistic algorithm classification problems.

![[Pasted image 20231128104002.png]]

The output of this algorithm could be only $0$ or $1$, and:
$$
g(z) = {1 \over {1 + e^{-z}}}, \space 0 < g(z) < 1
$$
Then, combinated with the linear regression, we obtain the linear regression model:
$$
f _{\vec w, b} (\vec x) = g(\vec w * \vec x + b) = {1 \over {1 + e ^ {-(\vec w * \vec x + b)}}}
$$

This kind of output is the idea of "probability" that the value is either $0$ or $1$. If the output for example is $0.7$, the idea behind is that the patient has $70\%$ chance of being $1$.

The concept of probability implies that $P(y=0) + P(y=1) = 1$, that sad that the probability has to be completed entirely.
Some research papers on logistical problems, use this other function:
$$
f _{\vec w, b} (\vec x) = P(y=1| \vec x; \vec w, b)
$$
Since the concept is this function explain the probability of $f$ given the value of $x$, and with the parameters $\vec w$ and $b$.

## Decision boundaries

The decision boundaries allow to set a trash-hold in which the prediction change. The solution is made up by the solution being up or down the solution.

To calculate the decision boundaries, (in the original case) could be operate an operation to solve the function in zero:
$$
z = \vec w * \vec x + b = 0
$$
Solved as:
$$
z = x_1 + x_2 -3 = 0
$$
$$
x_1 + x_2 = 3
$$

The more complex example in which the decision boundary is different (more complicated), like the operation on circles (inside: true, outside: false).

Te polynomial decision boundaries can becomes really difficult, really fast, in order to classify the problems in the correct way. The goal of the operation is to have a geometric element that can represent the test cases correctly, and so, give a better representation. 
The solution must also take in place the possibility of false-positive, and the fact that the program must flag more in order to get everything, or flag less in order to get sometimes.

The **squared error cost function** for the logistic regression is:
$$
J(\vec w, b) = {1 \over m} \sum _{i=1}^m {1\over 2} (f_{\vec w, b} (\vec x ^{(i)}) - y^{(i)})^2
$$
The function will appear like:
![[Pasted image 20231129120053.png]]
and for this reason, the logistic regression is called **non-convex** function. That means also that this cost function is not the perfect solution.
To solve this problems. we have to change the definition of cost function, using the **loss function**. The different forms of this function allow to solve the basic case even when there is the costs function.

The **loss function** is like:
$$
L(f_{\vec w, b} (\vec x ^{(i)}), y^{(i)}) = \begin{cases} -log(f_{\vec w, b} (\vec x ^{(i)}) ), \space if \space y^{(i)} = 1 \\
-log(1 - f_{\vec w, b} (\vec x ^{(i)})), \space if \space y^{(i)} = 0 \end{cases}
$$
With this formula we can completely describe the whole loss-function formula. The graph will be like this:
![[Pasted image 20231129122228.png]]
but, really, what is usually for us is the first part:
![[Pasted image 20231129122321.png]]
And this function indicates the probability of something happening.

![[Pasted image 20231129123626.png]]

This allow the prediction to be automatically penalised in case of great loss, or not in other cases.
With this cost function the resulting function will be convex.and so it is possible for it to reach a global minimum. The cost function can be a function of the entire training set. The resulting loss function becomes now:
$$
J(\vec w, b) = {1 \over m} \sum_{i=1} ^{m} L ( f_{\vec w, b} (\vec x ^{(i)}), y^{(i)})
$$

There is also a simpler way to get the cost function in logistic regression. Since we are working on a binary classification problem, the $y$ could be only $0$ or $1$. The unified equation in the system could be simplified in a one-line function:
$$
L( f_{\vec w, b} (\vec x ^{(i)}, y^{(i)})) = - y ^{(i)} log(f_{\vec w, b} (\vec x^{(i)})) - (1-y^{(i)})log(1- f_{\vec w, b} (\vec x^{(i)}))
$$
and remember that $y$ could be either $0$ or $1$, and so, the two function are "active" one each cases, they could not "operate" at the same time. This formula is simpler, since it uses the function unified, and there's no need of checking before execution.

The cost function sum all the possible loss function. This cost function is called **maximum likelihood** in probability courses, and it is used in order to find the minimum of the function, since this function is convex.

To implementation of the logistic regression is the same as the greater descend, using a repetitive task of derivative operations on the costs function (the upper function), and then stop when reached the baseline parameters.
The costs function to implement is the following:
$$
J(\vec w, b) = - {1 \over m} \sum _{i=1} ^{m} [y^{(i)} log ( f_{\vec w, b} (\vec x ^{(i)}) ) + (1- y^{(i)}) log(1 - f_{\vec w, b}(\vec x^{i}))]

$$
As the greater descend operation, the correct implementation is to calculate each term at the same time and then use them the same time. The resulting algorithm mathematically is the same, but there is another problem, in which the function $f_{\vec w, b}(\vec x)$ is different.

Other concepts apply to this function, too:
1. monitor gradient descend using the learning curve
2. vectorized implementation
3. feature scaling

## Overfitting problems

Logistic regression and linear regression could be applied with exceptional results, but there are some cases in which the algorithm could run into **overfitting**, and so perform poorly. The related, but opposite problem, is **underfitting**.

The solution of these problems is called **regularisation**.

The underfit problem is when the model does not fit the trainig set well, in this case **bias** are introduced. Bias in the world of machine learning can represent a large set of problem in which the code produce a solution more easily than the others. 
The algorithm could approximate the training set better by doing an operation of **generalization**, in which some other components are taken in the function (like a quadratic one). The resulting formula is making up of all the components:
$$
w_1x + w_2 x^2 + b
$$
The new model could fit the model better.
Usually, the polynomial function is use to generalise the model, approximating the whole training set correctly. This process could end up in **overfitting** the model, in fact there is the possibility of getting the model take count of every piece of the training set, and so exposing it to make up results incorrect (bias by the outlier). This model is no more generalised, but fall under a **high bias** model. Sometimes, this case is called **high variance**.

The right case is when there is no overfitting (high variance) and no underfitting (high bias).

![[Pasted image 20231129162754.png]]


There are methods to understand when the model is underfitting or overfitting, but is not the concept of this lesson. The thing we can do now, is, *when we now that something is not right*, how can we address the problem.
The number 1 tools to avoid overfitting is adding **more data**. That is not always an option, but, when there is the possibility, this solution works really well.

The second solution is removing some feature, in order to make the model less correct in a specialised case, but more general, as a specific feature could introduce a really high variance. This can be a solution that remove information, so there could be problems implementing this solution. There are more advanced algorithms that allow an automatic feature selection, in order to solve (partially) this problem.

The third technique is called **regularisation** and imply the use of zero-value variables. This is a more kind application of feature elimination, as the feature is not really eliminated, but the impact on the resulting model is more controlled. This model is encouraging the algorithm to use smaller parameters values in order to fit better the test examples and without removing the feature completely.
There are two theory there: not touching $b$ or regularise even $b$. In practice is clear that either solutions do not make any difference.

The regularisation process can be integrated in the cost function directly, in order to make the model fit better than the original one. This implementation take the initial goal to better/more probably select the feature with smaller values.

The idea of regularization is using smaller parameters value, in order to take count of every feature. The difficult task in this context is choosing what feature must be penalized. Usually, the choice is solved penalizing every feature and it possibly to demonstrate that this approach solve the overfitting problem.

To implement the concept just explained, we can insert a new element to the cost function called **regularization term**, in which the $\lambda$ represent the value (with $\lambda > 0$) of penalty:

$$
J(\vec w, b) = {1 \over 2m} \sum _{i=1}^m ( f_{\vec w, b} (\vec x ^{(i)}) -y^{(i)})^2 + {\lambda \over 2n} \sum _{j=1}^n w_j^2 + {\lambda \over 2n} b^2 
$$
The solution for the ML model is the $min _{\vec w, b} J(\vec w, b)$. The two function ideologically works at the opposite side:
- the first works in order to fit the data
- the second part works to keep $w_j$ small
- in the middle $\lambda$ balances both goals

The component $b$ can be inserted or removed in this context. If $\lambda$ is really big, the values of $w_j$ would be nearly zero, and the resulting graph will be represented only by $b$ (and will be a line). The model will **underfit** in this case. The other solution is that $\lambda$ will be small, and so the model will overfit. The correct solution, event this time, will be the mid case.


### Regularized linear Regression

The algorithm seen before update the value of $w_j$, insteda the new solution will works the same but the cost of $J$ will be indicated differently.
The solution calculates the value of $w_j$ in order to find the partial derivative of $J$ and then adding the value of ${\lambda \over m} w_j$.

The algorithm, mathematically will be:
![[Pasted image 20231129180605.png]]

Continuing, the function can be deconstructed, revealing the initial function of costs of this course, with all the components explained:
![[Pasted image 20231129181123.png]]

The effect is that you are motlipling the value of $w_j$ for a slightly value under $1$. For that reason the function works.
![[Pasted image 20231129181337.png]]

To regularized logistic regression, the algorithm seems like:
![[Pasted image 20231129181824.png]]
