---
data: Nov. 16, 2023
author: Giovanni Foletto
Source: Improving Log-Based Anomaly Detection withComponent-Aware Analysis
tags:
  - "#Anomaly-detection"
  - log
  - deep-learning
  - RNN-LSTM
---
```
YELLOW: interesting for this work
GREEN: other resources/papers that may be interesting
BLUE: code and related, with algorithm explanations too
GREY: questions
```

The algorithm uses LSTM multi-layer to make the templating logs matching a particular algorithm. That sad, the implementation is maybe different, but the results and the implication are the same of the [[Loganomaly]] paper.

The systems uses Drain method to parse logs files and it can detect anomalies *online*.


![[Pasted image 20231119172304.png]]

![[Pasted image 20231119172317.png]]
# Considerations

PROS: They expect the components aware architecture for log parsing and AD is better, because it can understand better the flow of actions.
CONS: They provide no code and nothing else. The whole work is exceptionally un-useful.

DATESET: public on loghub
ALGORITHM: no code
