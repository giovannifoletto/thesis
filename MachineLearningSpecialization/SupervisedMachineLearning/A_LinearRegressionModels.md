The linear regression is the most used model in the time being.
This kind of algorithm can be useful to understand and try to find the correct house price for size. This can be reach mathematically with drawing the mean in the correct data given to the model.

As the prediction of number, the regression model is the perfect choice, the classification model allow a better understanding in categories classification.
The classification has the limit that the choice that the model can choose from is finite, so there could not be some strange solution. This is not valid in regression that can allow an output of any number possible.

The notation of describing the data is used and useful to understand and talk the machine learning models and algorithms.

The data set used to train the set is called **training model**. In this model are present the $x$ values, that is the *input* variable **feature**. The output is $y$ and is represented as the **target** variable, too. A **training example** is usually a tuple of  $(x, y)$. The symbols $m$ is usually used to represent the number of training example. 
To represent a specific tuple of the training sample, there is this notation:
$$
(x^{(i)}, y^{(i)})
$$
where $i$ represents the $i^{th}$ training example.

The training set contains the *features* and the *targets*. To start, you have to feed the algorithm with feature/target tuples, and then the learning algorithm is capable of producing some function (historically called **hypothesis**) and the job is to take the new input $x$ and output an *extimate/predictions* called $\hat y$. 
$$
x \to f \to \hat y
$$
In machine learning the convention is that the $\hat y$ is the **prediction** of $y$. The function is called the **model** and the labels inserted in the models are called **feature** (the $x$ values).
The prediction is the value that has the goal to estimate $y$, that is the **real value** in machine learning.
*That means that $\hat y$ can or cannot be similar to the real value*.

The first question to design a machine learning algorithm is how to represent $f$. The case above (extimate the house costs), the function can be written in a form like:
$$
f_{w, b} (x) = wx +b
$$
This function explains that get as input the $x$ value and return a value that will represent $\hat y$.
This function is making prediction about the value of $y$ with the help of the linear function $wx + b$. This is useful as the function that return some value can be anything and so, there could be any sort of difficulty function in the middle.
This particular function is linear, and so this function represent the **linear regression**. After that, the fact that there is only **one variable**, the model get the name of **linear regression with one variable**, that means in fact that there is only a *single feature x*. 
This model can also be called **univariate linear regression**. 

## LAB: Model Representation

```python3
import numpy as np
import matplotlib.pyplot as plt

# plt.style.use('./deeplearning.mplstyle')

# Define the input variables (x)
x_train = np.array([1.0, 2.0])
y_train = np.array([300.0, 500.0])

print(f"x_train={x_train}")
print(f"y_train={y_train}")

# Find the number of training samples (m)
print(f"x_train.shape={x_train.shape}")
m = x_traing.shape[0]
# Or can be used the 'len' python function
m = len(x_train)

# To recover the ith training example, we have to index the data from zero
i = 0
x_i = x_train[i]
y_i = y_train[i]

print(f"(x^({i}), y^({i})) = ({x_i}, {y_i})")

# To plot the data points
plt.scatter(x_train, y_train, marker='x', c='r')
# Set the title
plt.title("Housing Prices")
# Set the y-axis label
plt.ylabel('Price (in 1000s of dollars)')
# Set the x-axis label
plt.xlabel('Size (1000 sqft)')
plt.show() 

# Set the params
w = 100
b = 100

def compute_model_output(x, w, b):
    """
    Computes the prediction of a linear model
    Args:
      x (ndarray (m,)): Data, m examples 
      w,b (scalar)    : model parameters  
    Returns
      f_wb (ndarray (m,)): model prediction
    """
    m = x.shape[0]
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = w * x[i] + b
        
    return f_wb

# Print the prediction linear value:
tmp_f_wb = compute_model_output(x_train, w, b)
# Plot our model prediction
plt.plot(x_train, tmp_f_wb, c='b',label='Our Prediction')

# Plot the data points
plt.scatter(x_train, y_train, marker='x', c='r',label='Actual Values')

# Set the title
plt.title("Housing Prices")
# Set the y-axis label
plt.ylabel('Price (in 1000s of dollars)')
# Set the x-axis label
plt.xlabel('Size (1000 sqft)')
plt.legend()
plt.show()

## The right values are: w=200, b=100
w = 200
b = 100
x_i = 1.2
const_1200sqft = w * x_i + b

print(f"$ {cost_1200sqft:.of} thousand dollars")
```

## Cost Function Formula

The cost function is says **how well the model is doing**, so we can try to get it to do better.

The training set is composed by `(feature, targets)`, grouped with a linear model with params `w, b`. This two parameters are called **coefficient** or **weights**. 
Depending of the value of `w` and `b` there are different function => different lines, that represent/group data better in the data set.

If $w=0$, $\hat y = b$. That means that *b* becomes the **y-intercept** (since it cross the vertical asses). 
In every value, if we get a training example the value is represented as $(x^{(i)}, y^{(i)})$, getting the $ith$ value. After that, comes that
$$
\hat y ^ {(i)} = f_{w, b}(x^{(i)})
$$
and so:
$$
f_{w, b} (x^{(i)}) = wx^{(i)} + b
$$
To explain that: $y$ is the real data in the training example, and the $\hat y$ is the prediction given by the function $f$. The goals is to make **$\hat y ^ {(i)}$ closer to $y^{(i)}$ for all $(x^{(i)}, y^{(i)})$**.

Now comes the costs function, that take the $\hat y$ and confront with $y$. The different is called $error$. Then it's computed the quadratic value of this error, and then sum up all the value in the training set. The const function is so as that represented:
$$
\sum _{i=1}^m (\hat y ^{(i)} - y^{(i)} )^2
$$
where:
- $m$ is the number of training examples
- $(\hat y^{(i)} - y^{(i)})^2$ is the *quadratic error* for each given training example.

But this function becomes larger and larger with each given example, so we can get the mean value, dividing the whole sum by $1 \over m$. By convention, there is another division by 2 in the formula to simplify other works after that. The **Square error's Cost Function** is then denoted by **$J$**.

$$
J(w, b) = {1 \over 2m } \sum _{i=1}^m (\hat y ^{(i)} - y^{(i)} )^2
$$
There are different cost function for different model/function. This cost function works for every linear model. 

Returning to the initial problems, the formula will looks something like:

$$
{1 \over 2m} \sum _{i=1}^m (f_{w, b}(x ^{(i)}) - y^{(i)} )^2
$$
After that the ultimate goal to make the algorithm better is to find the best fitting values of `w` and `b` that makes the summary as low as possible.

### Cost Function Intuition: How to use to make the model better

The model is represented by the function: $f_{w, b} (x) = wx + b$, in which the parameters $w, b$ are the one to modify to make the algorithm better.

The cost function $J(w, b) = {1 \over 2m} \sum _{i=1}^m (f_{w, b}(x^{(i)}) -y^{(i)})^2$, represent the discrepancy between the real value and the inferred value.
The goal of the machine learning function is to *minimize* the cost function, and so, mathematically:
$$
minimize _{w, b} J(w, b)
$$
We can start simply by eliminating the $b$ value.  Doing so, the result cost function becomes:
$$
J(w) = {1 \over 2m} \sum_{i=1}^m (f_w(x^{(i)})-y^{(i)})^2
$$
And the function to find is that minimize $J(w)$.

Working in multidimensional variables (utilizing both $b$ and $w$) we obtain a function of $J(w, b)$ that works like a parabola in multidimension.  ![[Pasted image 20231106220324.png]]

That is because the variable are two and can be both discrete modified.

## Gradient Descend and its algorithm

This algorithm is used by something like all machine learning algorithms and it is used to minimise every function, not only the linear regressions function.

That is useful to find minimised value of a cost function like:
$$
min_{w1, ..., w_n, b} J(w_1, w_2, ..., w_n, b)
$$
The function can be complex and not at all a bowl like before.

This algorithm start in a point and then look around and search the best direction with the steepest descend, and so the one that go down as fast as possible.

The gradient descend has an interesting property: the algorithm can start whathever we want, but the minimum changes results in a discrete change in the minimum found. The fact that this algorithm can found different "valley" (different minimum point) allow the application in a completely random point in the graph, as the resulting value will be ever the same.

$$
w = w - \alpha {\partial \over \partial w} J (w, b)
$$
The value of $\alpha$ is the **learning rate**: that variable control how big the step is taken downhill. The other parts is the derivative to find out the steep of the steps.
The model has two parameters, 
The steps of $w$ replacing continue until the value bocome **convergent**, or in other words: the value remain as close as the precedent as possible.

The second step of the algorithm is with $b$:
$$
b = b - \alpha {\partial \over \partial b} J (w, b)
$$
This changes to update the values of $b$ and $w$ must be simultanous. That means that the correct way of implementing it is to use some temporary variables that allows to maintain the value before another calculation is done.
```pseudocode
tmp_w = w and formula over
tmp_b = secondo formula over

w = tmp_w
b = tmp_b
```

If the parameter are not simultaneous update probably will results the same, but it is not really how it has to be done.

After that the algorithm is done, the only thing is to check every round if the terms are converging or not. If the answer is yes, the result can be returned, if not, must be continue looping.

### The learning rate $\alpha$

The value that the learning rate is getting can be:
- too small => there are only tiny baby steps. The cost is decreasing but really slow, getting there with a lot of steps
- too large => there could be problems in the finding the minimum, since the correct value is skipped in the gap (this can fail to converge or even *diverge*)

When the learning rate is taken correctly, the value of $w$ could take the value of a local minimum, and so there could be that the derivative function become zero. The results is that $w$ is update with itself. This cause convergence.

We can annotate that the derivative value become smaller and smaller every round, because the parabolic shape of the function make possible that the slope of the gradient descend function decrease every round. This allow to use a **fixed-value learning rate** and so allow to simplify. That give the **linear regression algorithm**.

To implement this algorithm programmatically we can use some mathematical object:
- the first gradient descend step for $w$ becomes
$$
{1 \over m} \sum _{i=1} ^m (f_{w, b} (x^{(i)})-y^{(i)})x^{(i)}
$$
- the second gradient descend step $b$ becomes:
$$
{1 \over m} \sum _{i = 1} ^ m (f_{w, b} (x^{(i)})-y^{(i)})
$$

These formulas are derived with calculus and there is a demonstration, but not in my notes :).

A **convex function** (like the bowl function) has  a particular characteristic that allows that the local minimum is the complete general minimum (as there is only that).

### "Batch" gradient descend

The particular thing of this algorithm is that at each step of gradient descend uses all the training examples. 

There are other versions of the greater descend for linear regression and uses thing particular or other implementation of things.

