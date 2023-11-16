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
The problem that this research group found in the precedent mechanism is 

This model elaborates on templating technologies in order to ingest logs in a more common/supervised method. This approach uses semantics of logs in order to model the log stream as a language sequence, and so elaborate with NLP techniques.
Another problem this paper would solve is the appearing of new log-template in every learn phase of the algorithm, and so the value of false-positive after this approach are much lower.

The things this paper introduce is the capability of getting sequential and quantitative log anomalies simultaneously. 
The fact that logs could be grouped in a **sequence** is common and already seen in the [[DeepLog]] paper, using RNN-LSTM is expected for a **sequential log anomaly detector**. The other parameter, the quantitative, it something that in the paper is described as behaviour (if there is a log of a file being opened, there must be one of the file closing at some point, but clearly you can read/write from/to it in that time).

Another innovation of this paper is the `template2vec`, a templating library that 






![[Pasted image 20231106112000.png]]


# Considerations

PROS:
CONS:

DATESET:
ALGORITHM:



