There are pratical point in machine learning application that allow to take the most from the implementation. Other information allow to better runnability of the algorithms.

# Neurons and the Brain

The invention of neural network happened in order to find a methods of thinking for computer like our brain works, in fact the initial goals was to **mimic the brain**.
After that, in 1980's and 1990's it was wastly used for numbers recognition. After that the techniques slighlty disappear and resourge around 2005 as **deep learning**, that is the brand name of this technology until now.
Modern deep learning closes some problems on speech recognition and image recognition. After that this technology evolve in text manipulation with NLP (natural language processing).

The idea applied is that the "neuron" receive some input and respond with an output. The neuron can results something to give as input to other neurons. The representation of a neuron in machine learning or deep learning is mathematical.
Usually, when applying neural networks usually a number of neurons is applied linearly, one after the other.

The new research way for neural networks abandoned the goal of finding the automatic implementation of a human neuron. Instead, the researcher in this field try to find some other mathematical principle/model that works well for this problem.

The amount of data in the last few year drastically increase and has been digitalised. The performance on ML/DL with all this data started to become more efficient and perform better. The fact that a lot of data are available does not mean that they are usable, in fact there is a necessity of a great model to obtain something useful from a lot of data. Another discouraging point is the amount of computational costs, firstly the GPU that are the fundamental elements for elaborating this great amount of data each times.

## Demand Prediction

To predict the demand in something based on the price, the graph function is like:
$$
a = f(x) = {1 \over {1 + e^{-(wx +b)}}}
$$
in which, $x = \text{price}$, $a = \text{output}$ and the **activation**, in which in the context of the neuron is the output of the function.
The other idea of a neuron could be a computer that outputs one or more number that indicates the probability of something.

For example, it is possible to link together more neuron together:
![[Pasted image 20231205111653.png]]

In neural networks could be multiple neurons. The activation of the first layer is the output of the first layer, and the activation of the purple layer is the total probability of being a top seller. The other thing is that the yellow values is called input layers.

Usually the neural networks link toghether information in another method:
![[Pasted image 20231205112020.png]]

The hidden layers are the central ones, are not present in the training set and can have multiple neurons as input. The value of input/output is put in as $(x, y)$ and usually is not present in the output.
The big difference between neural networks and machine learning (from earlier) is that in this case, the entire network works in order to find the correct list of feature or to build a new feature in order to expect a determined output. This is why neural networks are so powerful. 
Another things that is simplified in this application is that the intermediate feature are not to be decided by the engineer, but the neural networks decide it automatically. That is the other things that make this type of technology such a powerful tool.

The question that remain is translated in the architecture of the layers, in order to make the correct number of neuron for layers and results a correct solution.


