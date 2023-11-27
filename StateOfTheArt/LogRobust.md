---
data: Nov. 21, 2023
author: Giovanni Foletto
Source: Robust Log-Based Anomaly Detection on Unstable Log Data
tags: 
paper-release-date: "2019"
---
```
YELLOW: interesting for this work
GREEN: other resources/papers that may be interesting
BLUE: code and related, with algorithm explanations too
GREY: questions
```

This papers highlight the problem of un-reliable logs messages, in order to understand the anomaly everytime, every circumstances.

The principal problems for unreliable logging are:
1. the evolution of logging strategies
2. the processing noise in log data

There are studied that demonstrated that there is a line of log every 58 of code. The frequency and the moltitude of these logs do not allow a manual checking.

The other approach do not demonstrated to work in different, real word scenario because they all build detection model with *log events* and *log sequences*, and they fail to works with different unseen events. The authors studied that real-word log are **unstable** and the model failed to label different but similar log sequences.

The systems uses Bidirectional attention-based LSTM detection model (Bi-LSTM). The papers could not uses previous methods (PCA, SVM, Invariant Mining) since the instable origin of the logs.
![[Pasted image 20231121231552.png]]
![[LogRobus1.png]]
![[LogRobust2.png]]

Log robust can inject online data on run, without the necessity of a re training. With gradient descending, it can fine-tune its parameters gradually and correctly.

# Considerations

To read again.

PROS:
CONS:

DATESET:
ALGORITHM:
