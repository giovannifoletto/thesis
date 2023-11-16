---
data: Nov. 12, 2023
author: Giovanni Foletto
Source: "API security in Large Enterprises: Leveraging Machine Learning for Anomaly Detection"
tags:
  - api-microarchitecture
  - interesting
  - API-application-programming-interface
  - machine-learning-models
  - support-vector-machines
  - microservices
  - Anomaly-detection
---
```
YELLOW: interesting for this work
GREEN: other resources/papers that may be interesting
BLUE: code and related, with algorithm explanations too
```

The paper illustrates a Machine Learning model that works like and IDS in the area of API security. The further approach, specifically in the this area is made after the authors elaborates, based on different resource, on how the ML model applied on normal network traffic fails in detecting API-endpoint specific attacks. 

> Several other works such as [8]–[13] have studied network traffic anomaly detection and have reported failures when applied to API traffic due to the unique nature and behaviour of API traffic.

Furthermore, the paper elaborate on the possibility of this approach, since they quote a Capital One works in which they managed to get good results in finding anomalies in API traffic analysis. They especially say that this is not a definitive proof of the methods found, since in only based on Capital One systems, but evaluate the possibility of this work. That alone leave space to a possible general application model that can plug-and-play in every API and microservices application ecosystem.

After that, the papers make another great point really clear: the application of Machine Learning (ML) in this fields could have great results. That is demonstrated by the great amount of data that an API traffic analysis needs and produce, and the fact that can identify anomalies without being especially programmed for.

The ultimate goals the researcher expect are summarised in a questions that can broke in other two:

> Can ML-based techniques be used to efficiently analyse and detect anomalies in API traffic?
> 1) Can we trust the accuracy and analysis made by the employed ML algorithm? 
> 2) How fast is the analysis process? Can this be done in real time?

# Considerations

PROS: The questions the authors asked themselves at the start are conceptually similar to ours. The "why use ML in this case"-section of the paper (here over) is especially precise and complete, taking a lot of real cases scenario as examples. They successfully created a model that could works in real time, that successfully beat rule-based IDS systems with an accuracy of $83.5\%$ and an error rate of $7,3\%$ false positives.

CONS: The concept that these methods could works in this situations are especially useful applied to their case, but not really to ours. The dataset labelling could not be done for certain in every industrial context, in which the feature to take count could be more, different and no easily labelled as normal/abnormal with the techniques of standard deviation. In general, the approach take in place a supervised methods may be not the best solution of our particular research case.

DATA SET: not present for privacy reason, but they elaborated on how they get it, optimise and work on that.
ALGORITHM: they used the SVM from SciKitLearn for the whole work.

## More in depth
## Algorithm

The application model they found exploits the Gaussian distribution: the data are catalogued by the statistical distance from the mean and so defined as outliers (*anomalies*) or normal.
The data are analysed by a SVM algorithm in order to detect abnormal patterns. The SVM algorithms has been chosen because:
- it is know that find the *local-optimal* values with fewer iterations rather other DL (deep learning) model
- is simple but powerful
- works well on dataset having limited number of parameters
The model is used taking it from the SciKitLearn python library, and, as the specification sad, it has been seeded with 100k samples.

### Data Generation

Because there are not dataset publicly available and updated, the research group start in the creation of synthetic one. 
The data are taken from a synthetic API communication traffic inspired by real-word examples, over which is applied the standard deviation range ($\sigma$). The values that have fallen out that are labelled as anomalies (abnormal traffic).

### Feature Engineering and KPIs

The paper analyse 6 feature:
1. Bandwidth consumption
2. Client IP addresses
3. Number of consecutive requests
4. Connections durations
5. HTTP requests

### Used classifier

It  is used SVM, with an exhaustive explanation on why they decide to use that (I think).

### Testing and Validations 

![[Pasted image 20231112182222.png]]