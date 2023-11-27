---
data: Nov. 12, 2023
author: Giovanni Foletto
Source: API Traffic Anomaly Detection In Microservices Architecture
tags:
  - not-interesting
  - api-microarchitecture
  - microservices
  - microservices-architecture
  - API-traffic
  - Anomaly-detection
  - denial-of-services
  - machine-learning-models
  - data-breach
  - bagging
  - randomforest
---
The goal of the paper is to produce a ML model that could works like an IDS. Most of the works is really similar to [[API Security in Large Enterprises_Leveraging Machine Learning for Anomaly Detection]] with some differences: 
- the attacks vectors most analysed are DoS and the ones in which data-breached could be involved
- the model can find which endpoint is being targeted 

In order to produce a dataset, the research group create a 5 API-endpoint application, studied like it may be a banking interface, but they say that 5 API endpoints are not capable of producing enough traffic and so the application is unable to create a dataset to train data on. The model with this data model has produced no correct results.

The model proposed has two layer of detection and a parallel DoS detection systems. The first sections (the one with two layers) is build like this:
- Layer 1: Detection with **RandomForest Classifier**. The data records is described as
> This dataset consists of data records where attackers abuse API access in an effort to take advantage of the business logic of these APIs.

The dataset used is **imbalanced** for the categories of traffic (*attack*, *outlier (abnormal)*, *normal*). This dataset has being created since the original one *failed* to identify anomalies. It is not clear if it contains malicious traffic or correct traffic, as the papers tells clearly that this layer do not identify something ever, but it is leaved like this in order to mitigate a possible **zero-day attacks**.
- Layer 2: the model uses a **Bagging Classifier**, with a dataset that changes for each kind of application. In this case, the dataset is especially true for banking applications.
The parameters are set for normal conditions in the synthetic dataset and so, the algorithms works on that.

![[Pasted image 20231106111709.png]]

The solutions proposed seems like a better alternative of the first paper, since it has a similar correct identification rate and can correctly identify the API that its being attacked, too.

The works conclude with the facts that this ML model applied in an industrial ecosystem, with the correct parameters, could allow a better solution of normal IDS. (This fact has already been significantly proven by the other paper) and for no means solve the problems of zero-day attacks, in fact, I cite the paper directly

> [...] The work can be extended to prevent the potential attacks, thus acting as an IPS. This **could** help the applications prevent zero-day attacks, one of the most dangerous forms of attacks. [...]

the authors themselves are not sure if zero-day attacks could be stopped or identify with these methods.

A special things they say is that the dataset must be created specifically for the application/use-case. It is not clear the case of an update of the business-logic could interfere on the model itself, and so start to see the new feature as an anomaly and flag it, or never elaborate something on them. The solutions provide an improved accuracy of the model for *only* a $0.01\%$.


## Consideration

In the whole paper there is something that do not sum-up: the solutions proposed, the technical explanation of the proposed model and the results processing.
The clear fact is that more of the research has been done in the [[API Security in Large Enterprises_Leveraging Machine Learning for Anomaly Detection]], and the most of the point that this research clear are already been demonstrated with a clearer code, interface and paper.
The only thing that could be added at the work of this paper could be the inclusion of the rule-based systems in the identify process of the IDS, in order to produce more accurate results. 
Like the other paper, it is not clear if new attacks could be found with this method, since there are not present in the original dataset.

The fact that so more applications and algorithm information are provided, it difficult to see an important solution in the algorithm proposed, as the data could not be validated. That sad, in addition to all explained above, the solution proposed *may be* working, but give no reason to think they *really* found a generalised way of anomaly detecting malicious traffic on any given API traffic.

PROS: they have done a great works in finding, elaborate and study on the feature section. They maybe identify some kind of problem: the origin and the utilisation of the API and the dimension of the dataset.

CONS: the feature proposed are not fully utilised in the models, so there could be some possibilities of inefficiency, but also the model cannot works with these. It is possible to mitigate a unknown attacks (like a zero day) attacks via this methods ? If not, this is only a better and more coverage, IDS rule based with more power, but that cannot identify proactive and new threats.

DATA SET: not present and it's not clear how the obtained the data and what kind of modification they have done.
ALGORITHM: They used a custom script with the two models listed above, but there are not indication of this code make public,  and only a speudo-code is provided.




# OTHER


The starting point of the research is to find some Machine learning model that will works like an IDS in order to identify an abuse in an API utilisation.
The Machine Learning application in this case was especially valid because 1)the web-application ecosystems is continuously changing, 2) the new **microservices** architecture is the most common behind big and modern application, 3) building with this new architecture is easier to build endpoint exposed or mismanaged or (worst case) forgotten.
The research use API endpoint as they preferred application since they produce a lot of traffic (and so a lot of information to train the model on). 

> I THINK
That they say they use the application API instead of the OSI model because the anomalies are more common there, instead of the OSI model. A request can be correct network-wise, but not correct for the application that is receiving it.

The decision to approach  microservice-architecture application is base on the fact that:
- microservices application produces more API traffic
- the development timeline of a such application are more restrictive, so the API is changing faster
- rules-based methods cannot keep up with all this changes, since they must be maintained and integrated every new deployment and do not take in place the possibility of sneaky attacks and malevolent behaviours
- is easier and faster identify API traffic anomalies, rather than ones in a normal OSI traffic (the traffic can be correct, but the application could be abused)






The focus is how a mismanaged or misconfigured API could be an access door for an attacker and so:

> APIs can prove to be an important source of information to track unusual behavior. Microservices generate an enormous amount of API traffic, which can be analyzed for abnormal behaviors. Therefore, it is essential to monitor API traffic continuously, detect abnormal intrusion and prevent the at- tack from escalating any further. Rule based methods cannot keep up with the changes in the application that takes place regularly in a development environment in an organization. Automation through machine learning is needed to solve these problems.

From [[Sowmya et al. - 2023 - API Traffic Anomaly Detection in Microservice Arch.pdf#page=1&selection=195,0,204,9|Sowmya et al. - 2023 - API Traffic Anomaly Detection in Microservice Arch, page 1]]
[[Sowmya et al. - 2023 - API Traffic Anomaly Detection in Microservice Arch.pdf#page=1&selection=195,0,204,7|Sowmya et al. - 2023 - API Traffic Anomaly Detection in Microservice Arch, page 1]]

The API traffic is different and the signature or rule-based systems cannot keep up on the new methods and methodologies.

Thus, the key contributions focused are summarized as follows: 
- The API anomalies in focus are data breach and DoS attacks. The data breach is detected with machine learn- ing models while the DoS attack is detected with [[Pruned Exact Linear Time (PELT) algorithm]]. 
- A sample Banking application with basic functionalities is built. API logs from this application is collected for further analysis and development. 
- A recursive compressor is implemented which extracts the necessary features from the API logs from each service, to a set of parameter values. These values are extracted every minute and used to monitor the traffic. *=> this is the parser ?*
- The API traffic is monitored at two levels. The initial layer (Layer 1) is specific to large scale attacks when the application has large resources. The next layer (Layer 2) is specific to the application itself. 
- The Layer 1 detects the abnormal API traffic with the aid of [[RandomForest]] model. This model is trained with a real-time dataset consisting of 34,400 records. 
- The Layer 2 works on a synthetic dataset which is generated by introducing new parameters. The Bagging method (the methods commonly used to reduce variance with a noisy dataset) of machine learning is trained with this dataset to detect the attack in case it bypasses Layer 1. 
- Comparison of different ML models like [[RandomForest]] Classifier, Decision tree, [[Naive Bayes]], [[Support Vector Machine (SVM)]], [[Logistic Regression Classifier]], ensemble methods is done to analyze the performance of the models. 
- The PELT search method, a change detection point algorithm is used to detect DoS attack on the application.

SECTION IV: anomaly detection learning models
SECTION VII and VIII: elaborate on the different machine learning models and performance algorithm.

## Anomaly detection in API traffic

Layer-1: Radnom Forest model trained with real time dataset that is relevant for detecting data breach attacks caused due to business vulnerabilities.
=> the attack performed on the microservices application were not detected by Layer-1 with the initial data set, and needed (at least) two other parameters (data-out-rate and the number of failed requests).

![[Pasted image 20231106121602.png]]

=> PSEUDOCODE:

```pseudocode
procedure AnomalyDetector(parameter[5], api)
	result1 = LOneMLClassifier(parameter[3], api)
	if result1 != attack then
		result2 = LTwoMLClassifier(parameter[5], api)
		if result2 = attack then
			return "{ApiEndpint} is under attack"
		endif
		
		if parameter[totalCalls] >= 1000 then
			dosDetect = DosDetection(requestRecords)
			if dosDetect = True then
				return "DoS Alert!"
			else
				pass
		endif
		else
			pass
		endif
	else
		return "{ApiEndpoint} is under attack"
	endif

procedure LowFreqRewDetector
	feature = ExtractFeature(30mins)
	ip_records = Compress_IPAddresses(features)
	for i in ip_records do
		if i.total_cals >= 15 then
			return "Possible attack from i.ip_address"

procedure DoSDetector(index):
	Sleep(20minutes)
	records = fetchLastTwentyRecords(index)
	results = PeltSeachMethod(records)
	return results
	
```

> The number of requests made by a specific IP address in last thirty minutes is kept in check. If the number of requests for one IP address is more than or equal to 15, a possible attack from that address is detected. This helps in detecting unusual request traffic in low frequencies.

From: [[Sowmya et al. - 2023 - API Traffic Anomaly Detection in Microservice Arch.pdf#page=5&selection=74,0,77,58|Sowmya et al. - 2023 - API Traffic Anomaly Detection in Microservice Arch, page 5]]

## Classification and Validation
[[Sowmya et al. - 2023 - API Traffic Anomaly Detection in Microservice Arch.pdf#page=5&selection=280,0,299,24|Sowmya et al. - 2023 - API Traffic Anomaly Detection in Microservice Arch, page 5]] sad that the classification training set (of the layer-1) contains data classification for anomalous and normal behaviour.

Accuracy:


## Think

The dDoS can be done with K-neybours and AD on that, making it real-time. The solution can be in the logs, as, for example, NGINX, could logs every information about requests and somethings like that.


# Summary

The API are important parts of the current word and are utilised everywhere to deploy and create application. More the application is complicated, more it has API endpoint and more the attack-surface increase.
The solution is an IDS (intrusion detection system) that allow a **TRAFFIC ANALYSIS** for anomalies. 
The papers explains how they used a programs called "API-Traffic Anomaly Detection (API-TAD)". That detects anomalies using machine learning and it uses 2 layer (one generalised and one application-specific is proposed) in order to provide **efficient and accurate anomaly detection**. 

## 1. Introduction

Most application are based on microservices architecture, which provide and produce a lots of logs and network traffic that can be analysed for abnormal behaviours. The vulnerability can be that, in the multitude of API endpoint, one mismanaged can be the entry-point of an attack. 

The **Signature-based and Rule-based** methods cannot keep-up with the application evolving and it is necessary a sort of **real-time protection**: a anomaly can be found at running time and solved as fast as possible.

! QUESTION: in this section ([[Sowmya et al. - 2023 - API Traffic Anomaly Detection in Microservice Arch.pdf#page=1&selection=205,0,209,5|Sowmya et al. - 2023 - API Traffic Anomaly Detection in Microservice Arch, page 1]]), the author says that is used application level logs rather than OSI model. That means they used internal application logs instead of external one only? What that means? 
- API may be something like cloud API, like AWS control API ?
- a network-based DoS can be something working with DNS doing traffic rather thatn a botnet/programs (?)

It appears that they take it from HERE: (Gaspard Baye, Fatima Hussain, Alma Oracevic, Rasheed Hussain, and SM Ahsan Kazmi. Api security in large enterprises: Leveraging machine learning for anomaly detection. In 2021 International Symposium on Networks, Computers and Communications (ISNCC), pages 1–6. IEEE, 2021.) DONE, it clearly takes most of the work from here. 
TODO: SEARCH => maybe ([[Sowmya et al. - 2023 - API Traffic Anomaly Detection in Microservice Arch.pdf#page=2&selection=167,50,172,53|Sowmya et al. - 2023 - API Traffic Anomaly Detection in Microservice Arch, page 2]])

[[Sowmya et al. - 2023 - API Traffic Anomaly Detection in Microservice Arch.pdf#page=2&selection=0,0,15,47|Sowmya et al. - 2023 - API Traffic Anomaly Detection in Microservice Arch, page 2]]=> This sections says the goals: the legacy rule-based methods cannot detect some *correct command* used to make bad things.

This methods allow to find **data-breack and dDos**. 
Has been developed an application => the model do not work on that.
The model extract data with a compressors, that do it **every minute**. Prerequisites of real time operations to be decided.
The two layers are divided like this:
- layer 1: detect dDos (don't say that directly, but it seems like this => [[Sowmya et al. - 2023 - API Traffic Anomaly Detection in Microservice Arch.pdf#page=2&selection=55,0,58,38|Sowmya et al. - 2023 - API Traffic Anomaly Detection in Microservice Arch, page 2]]). It uses **RandomForest** with a dataset of 34400sec. The dataset seems not to be included. It seems that the systems utilised PELT algo, too.
- layer 2: detect the API abuse itself. It uses a **Bagging method** (What is it?), trained on the same dataset, cleaned by the attack that didn't make trhought the layer 1.
An analysis with different models has been done, using a lots of differents model ([[Sowmya et al. - 2023 - API Traffic Anomaly Detection in Microservice Arch.pdf#page=2&selection=97,0,109,10|Sowmya et al. - 2023 - API Traffic Anomaly Detection in Microservice Arch, page 2]]).

To detect dDos is used PELT => [[Sowmya et al. - 2023 - API Traffic Anomaly Detection in Microservice Arch.pdf#page=2&selection=113,0,114,58|Sowmya et al. - 2023 - API Traffic Anomaly Detection in Microservice Arch, page 2]].

