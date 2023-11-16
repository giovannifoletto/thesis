---
data: Nov. 13, 2023
author: Giovanni Foletto
Source: "CSCLog: A Component Subsequence Correlation-Aware Log Anomaly Detection Method"
tags:
  - API-call-sequence-pattern
  - Anomaly-detection
  - correlation-learning
  - attention-mechanism
  - RNN-LSTM
---
The papers explain a method of classification and correlation of complex log patterns in order to capture sequence and subsequences of actions. RNN-LSTM model is used to extract dependency in log sequences.

The approach is basically use the ML/DL-model to detect patterns in logs during training, and then find the anomalies based on them. The goals is to understand the dependency in logs sequence and analyse them with it.

Usually, there are two possible approach used: 1) traditional methods, 2) neural network-based methods. The first one uses statistical feature found in log sequences to detect anomalies, while using traditional machine learning methods to capture the feature. This methods **don not allow** good performance on different datasets.
The second method usually made express use of [[Recurrent Neural Networks]], and its variants in order to capture sequential dependencies in log sequences, in order to find the pattern and make a model from it in order to be used in anomaly detection.

They make the point of the research by an example about labelling and log sequence modelling:
![[Pasted image 20231113093742.png]]
If the subsequences are not studied, the anomaly could not be detected (`T5` in this case means the systems stopped, so any other action on that should have been stopped). The precedent works, as the authors says, failed to do so, but in particular the traditional modelling techniques.
The changing point is the implicit correlation of subsequences, that do not allow the labelling in the first example, but (the authors says) CSCLog is capable of.

The working mechanism is compose in three phases:
1. subsequence modeling
2. implicit correlation modeling
3. subsequence feature fusion

\[All that summary of the algorithm is done with ChatPDF\]
In the **phase 1**, the algorithm extract semantic and temporal feature in the log sequence and subsequence.
> To extract subsequences, CSCLog first identifies the components in the log messages and groups the messages with the same component into a subsequence. If a component is not present in a log sequence, an empty subsequence is created for that component. The set of subsequences is denoted as $C = \{P_1, P_2, ..., P_{N_c}\}$, where $N_c$ is the number of components.
> Next, CSCLog applies LSTMs to model the sequential dependencies in each subsequence. Specifically, each subsequence is fed into an LSTM network, which processes the messages in the subsequence one by one and updates its hidden state at each time step. 
> The final hidden state of the LSTM is used as the embedding of the subsequence. By modeling the sequential dependencies in subsequences, CSCLog can capture the complex log patterns of components and detect anomalies that are difficult to detect by only capturing the sequential dependencies in log sequences.

The **phase 2**:

> The implicit correlation modeling module in CSCLog is designed to model the implicit correlations of subsequences and capture the interactions between them using an implicit correlation encoder and GCNs. To model the implicit correlations of subsequences, CSCLog first concatenates the embeddings of all subsequence pairs to obtain a correlation embedding matrix $X_{edge}$. 
> The correlation embedding of a subsequence pair is obtained by concatenating the embeddings of the two subsequences and passing them through a multi-layer perceptron (MLP) with a ReLU activation function. Next, CSCLog applies GCNs to model the interactions between subsequences based on the correlation embedding matrix. Specifically, CSCLog constructs a graph where each node represents a subsequence and edges represent the similarity between subsequence pairs. 
> The GCN layer aggregates information from neighboring nodes to update the hidden states of each node. 
> The updated hidden states are then used as the embeddings of the subsequences. By modeling the implicit correlations of subsequences and capturing the interactions between them, CSCLog can detect anomalies that are caused by the interactions between components, which are difficult to detect by only modeling the sequential dependencies in log sequences or subsequences.

The **phase 3**:

> The subsequence feature fusion module in CSCLog is designed to fuse the embeddings of different subsequences using attention mechanisms. To fuse the embeddings of different subsequences, CSCLog first applies a global vector $u_{att}$ to calculate the attention weights of the embeddings. Specifically, the attention weights of the embeddings of different subsequences are calculated by the attention mechanisms, which is formalized as: $\beta _i = { AttScore(X^i_m, u_{att}) \over \sum_{k=0} ^{N_c} (AttScore(X_k, u_att))}$ where $\beta _i$ is the attention weight of the $i-th$ subsequence, $X_i$ is the embedding of the $i-th$ subsequence, and $AttScore$ is the attention scoring function, which is accomplished by the dot product of vectors. 
> Next, CSCLog applies the attention weights to the embeddings of different subsequences to obtain the fused embedding. Specifically, the fused embedding is obtained by taking the weighted sum of the embeddings, which is formalized as: $E_{fused} = \sum(\beta _i * X_i)$ where $E_{fused}$ is the fused embedding. 
> By fusing the embeddings of different subsequences using attention mechanisms, CSCLog can highlight the most informative log messages for anomaly detection and reduce the impact of irrelevant or noisy log messages.

![[Pasted image 20231106112251.png]]


The algorithm is implemented in Pytorch and the log are parsed before ingesting with a tool called Drain.

CSCLogs outperforms all the previously solutions, in every given ecosystem (in each of the 4 dataset). 

# Consideration

The starting point of the research seems to be for the most part ML-based researched techniques. A lot of these are about RNN and RNN-based technologies. The other branch of the research is about log categorisation.
The whole study on logs messages it not completely pertinent in our job, since our starting point are already-parsed logs. The logs used in this research are instead plain text.

Given the data, the great things of this proposal works is that works effectively well on different kind of logs. That is really important since the other algorithm cited are not all capable of doing that.

The solution suggested that the real-time computation of this operation are possible, but given the fact that was not an initial goal, we can tell that is only a fortunate results.

DATA SET: they are working on 4 publicly available log datasets (presents [here](https://github.com/logpai/loghub)).
ALGORITHM: they used Python with PyTorch and aggregates libraries. Source code on [github](https://github.com/Hang-Z/CSCLog).

LINKS: [[DeepLog]], [[Loganomaly]], [[LogC]], [[OC4Seq]]