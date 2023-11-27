---
data: Nov. 16, 2023
author: Giovanni Foletto
Source: "LogAnomaly: Unsupervised Detection ofSequential and Quantitative Anomalies in Unstructured Logs"
tags:
  - "#Anomaly-detection"
  - "#machine-learning-models"
---
```
YELLOW: interesting for this work
GREEN: other resources/papers that may be interesting
BLUE: code and related, with algorithm explanations too
GREY: questions
```

This paper presents a log anomaly detection mechanism heavily based on the precedent paper ([[DeepLog]]). 
The problem that this research group found in the precedent mechanism is only partially correct, since they approach the problems only from index-based methods, instead the new methods would make some improvements the analysis of log based on quantitative methods and qualitative, instead only with qualitative (like DeepLog has done). That allow, in additional to the normal detection capabilities, a better correlation in logs, and so increase the possibility of identify anomaly.

The fact that logs could be grouped in a **sequence** is common and already seen in the [[DeepLog]] paper, using RNN-LSTM is expected for a **sequential log anomaly detector**. The other parameter, the quantitative, it something that in the paper is described as behaviour (if there is a log of a file being opened, there must be one of the file closing at some point, but clearly you can read/write from/to it in that time).
This methods allow to reduce false-positive since different index could have information that are useful for themselves, and this model allow them to "exchange information".

The approach of this methods is parsing logs with **templates** instead of relying only on index. This is useful for the qualitative research they are doing, but it comes handy even during retraining. In fact, applying templates allow different template to be "merged", instead of throwing an alert. That, following the thought of the writers, is a better approach instead of the users-input driven approach explained by [[DeepLog]].

The algorithms works with an hybrid approach, using supervised and unsupervised learning. The unsupervised learning components can detect anomalies in the data without the need of labelled components, while the supervise model allow to mark templates as they arrive.

The authors present a simulation between DeepLog and their implementation:![[Pasted image 20231116135103.png]]

As you can see, the DeepLog implementation is more in time, but (they say) that the LogAnomaly implementation produced $3.5$ less false-positive than DeepLog.



![[LogAnomaly.png]]


# Considerations

The model propose is something like DeepLog, with some improvements. I don't think that the section of supervised learning is a great add, and it's not clear if the goal of less false-positive is correct. Clearly, to obtain what its needed, will be necessary a better correlation, in order to allow different pattern recognition to interact with each other and with the other cloud infrastructure, in order to understand if the operation is an anomaly.

PROS: 
CONS: 

DATESET: 
ALGORITHM: https://github.com/ljm0022/LogGraph.



