In a single-feature scenario, there is only a linear function to represent the problem. 
The example of which we are working with is the same, but there are added some feature:
- number of bedrooms
- number of floors
- age of home in years

To use more than one variables, there will be used $x_1, x_2, x_3, ...$. Some Notation:

$$
x_j = j^{th} \space feature
$$
$$
n = \text{number of feature}
$$
$$
\vec x^{(i)} = \text{feature of } i ^{th} \text{training example}
$$

Usually $\vec x$ is called **row vector**, instead of colum-vector. The arrow is necessary since this is a vector, not a single variable.
The new model becomes:
$$
f_{x, b} (x) = w_1 x_1 + w_2x_2 + w_3x_3 + w_4x_4 + b
$$
This expression can be rewritten with:
$$
\vec w = [w_1 \space w_2 \space w_3 \space ... \space w_n]
$$
That allow to rewrite the entire formula as:
$$
f_{\vec w, b} ( \vec x) = \vec w * \vec x + b = w_1 x_1 + w_2x_2 + ... + w_n x_n + b
$$
(where, $*$ is the dot-product).

## Vectorization

This techniques make the code shorter and also much more efficient. With this concept is possible to use some modern numerical algebra libraries.
The parameters and feature are represented as:
$$
\vec w = [w_1 \space w_2 \space w_3], \text{ with } n = 3
$$
$$
b \text{ is a number}
$$
$$
\vec x = [x_1 \space x_2 \space x_3]
$$
To represent it in `NumPy`, the most used linear geometry library in Python3:
```python3
w = np.array([1.0, 2.5, -3.3])
b = 4
x = np.array([10, 20, 30])
```

With factorization, the mathematical formula becomes:
$$
f _{\vec w, b} (\vec x) = \sum _{j=1} ^{n} w_j x_j + b
$$
That, in python, is:
```python3
f = 0
for J in range(n):
	f = f + w[j] * w[j]

 f = f +b
```
This implementation is better that the linear one (because it uses `for-loop`), but it is not using vectorization. The most optimal implementation is:
```python3
f = np.dot(w, x) + b
```
This code run much more faster, because it use vectorization and the fact that is more optimized within the NumPy library.
This implementation is much better when $n$ is larger, since it is not necessary to type the full mathematical operation for each $n$.
Lastly, the code is easier to read.

The code is present to read in the file with C1... in this folder.

The code, then, can be used to represent a gradient-linear descend. This implementation can be done using the gradient of the entire vector of feature.

![[Pasted image 20231127125036.png]]There is an alternative to gradient descend: **normal equation**:
Advantages:
- only for linear regression
- solve for $w$, $b$, without iteration

Disadvantages:
- doesn't generalize to other learning algorithms
- slow when number of feature is large ($>10,000$)

Is useful to know, since this is the method may be used in machine learning libraries that implement linear regression. Most use case, use the greater descend with better results rather normal equation.

## Feature Scaling

The transformation of the data can be useful in order to have data in determined in a specified range of value, resulting in more comparable function/values and then simpler to execute function.
![[Pasted image 20231127155123.png]]
With this approach, the grater descend is faster since the path is more direct to calculate.

In order to **scale** the feature we could divide by the maximum value. The resulting value will be calculated as this:
$$
\text{Before: } 300 \le x_1 \le 2000
$$
$$
\text{After: } {300 \over 2000} \le x_! \le {2000 \over 2000}
$$
That is using the maximum value ($2000$).

Another method can be the **mean normalization**: the value are rescaled in order to have some value around zero ($-1 \le x, y \le 1$):
$$
x_1 = { {x_1 - \mu_1} \over {2000-300} } 
$$
And the new value, will be ranged between: $-0.18 \le x_1 \le 0.82$.
The **Z-score normalization** is using the standard normalization. We start calculating the *standard deviation $\sigma$*. This methods works with this formula:
$$
x_1 = { {x_1 - \mu _1} \over \sigma_1}
$$
The values in this case would be: $-0.67 \le x_1 \le 3.1$.

The scaling section/operation is usually done to obtain data in a specified range. That predefined range is useful when the starting data are too wide or too stretch (is ok to apply when $-191 \le x \le 26$ and its ok in $-0.00001 \le x \le 0.000001$, its not ok for example on $0\le x \le 3$).

## Checking if Gradient Descend is Converging

There is the possibility of knowing if the greater descend is converging, and so changing $\alpha$ accordingly.
In order to the function to work, the parameters to change are $b$ and $w$, in the function $min _{w, b} J(\vec w, b)$.

The learning curve is the number of iteration needed to obtain the minimum of the function (to solve the function). After some iteration the learning value is getting something and get to decrease every iteration. The value should always decrease, if not there are problems. The function will be similar to that:
![[Pasted image 20231127171834.png]]

If the curve is not getting down, there could be a value of $\alpha$ taken porely, or could be a bug in the code. This function is really useful because when the curve is not decreasing (the curve flatter out), we can say that the function $J(\vec w, b)$ has converged. Different application could take more or less time to converge. 
The curve can say also when to stop training the model. Usually, we can solve this problem with the **automatic convergence test**:
- we take $\epsilon = 10 ^{-3}$
- if $J(\vec w, b) \le \epsilon$ in one iteration, we could definitively say the function is **converging** (as the $\vec w, b$ get close to the global minimum).

That sad, this can be applied in the search of correct learning rate, and so set all the different variables in a correct way. If the learning curve is not lineraly descending, there could be bugs in the code or the $\alpha$ can be too large (this cause to overshoot the minimum). If the cost increase usually the parameters are taken incorrectly or there is some bugs.
If the $\alpha$ is taken too small, we can estimate that visualising the learning rate. We can start from a small value, like $0.001$ and then make it bigger until the learning rate curve present problems.


The **choice of feature** can have a huge impact on the learning algorithm. Some feature could be calculated in newly created one, in order to obtain a value more usable or more important information. For example, instead using the "length" and the "depth", we can use the newly calculated "area" value.

The **polynomial regression** is a function to when the same feature is inserted in the function as the first value ($x$), as the second ($x^2$) and as the third ($x^3$). This choice of feature could be useful to increase the learning curve and the information present in the model, in order to get other information in the model (like quadratic dependency).