---
data: Nov. 6, 2023
deadline: Nov. 22, 2023
author: Giovanni Foletto
Source: PPT about start find it in the mail
tags:
---
Problems of kubernetes security (the *de-facto* standard of container orchestrator):
- (most common) image vulnerability and scaling privileges
- (other) access controls, misconfiguration and overly permissive configurations

## Service Account and RBAC

The K8s API access need a Service Account bind to a cluster Role or a role in a specific namespace. 
There is the possibility of creating custom **ROLES** or used the one the default profile creates in K8s.

The main options are cluster-admin, edit and view.

The **k8s best practices documentation** suggests that the admin create more restrective profiles for each user/services that need to be create in the cluster.
This process is costly, since there are no tools available to easing the role creation process.

## IAM Audit Log on Public and Private Cloud

The public and private clouds use **Identity and Access Management (IAM)** configurations to **control** the user access to several services and products.
The main **public clouds** allow to enable **audit logs** that stores all the user's access and options sent to each service. The same also can be done on the OpenStack.

The logs produced helps in the *post-mortem analysis on invasion and misconfigurations*.

This logs are **highly verbose and do not bring any insight information**. Normally, it is *necessary* to **process the data in some external application**.

Auditing logs:
![[Pasted image 20231106110350.png]]

PROS:
- the logs follow some **patterns** and so, no need to be **parsed**. 
- they bring a lot of information on the cluster/cloud usage (we could trace every command-user/SA)
- It is demonstrated that with these logs *several invasions could be identified*
- there is **good granularity** (`Metadata`, `Requests`, `RequestResponse`) based on a *series of rules*

 
## PAPERS

|Name|Authors|Year|Place|Topic|
- [[API Traffic Anomaly Detection in Microservice Architecture]] Sowmya, M., et al.|2023|CCGridW|API Request|
- [[API Call Based Malware Detection Approach Using Recurrent Neural Network—LSTM]]|Mathew, J., et al.|2018|ISDA|API Request|
- [[Detecting Anomalous Misconfigurations in AWS IAM Policies]]|van Ede, Thijs, et al|2022|CCSW|IAM|
- [[Loganomaly|Loganomaly: Unsupervised detection of sequential and quantitative anomalies in unstructured logs]]|Meng, Weibin, et al.|2018|IJCAI|Log|
- [[MADDC|MADDC: Multi-Scale Anomaly Detection, Diagnosis and Correction for Discrete Event Logs]]|Wang, Xiaolei, et al.|2022|ACSAC|Log|
- [[CSCLOG| CSCLog: A Component Subsequence Correlation-Aware Log Anomaly Detection Method]]|Chen, Ling, et al.|2023|Arxiv|Log|
- [[LogGraph | LogGraph: Log Event Graph Learning Aided Robust Fine-Grained Anomaly Diagnosis]]|Li, Jiangming, et al.|2023|IEEE TDSC|Log|


![[Pasted image 20231106111403.png]]


## IAM AWS Dataset

Data for 3.5 years on an AWS company account use to training and practice attacks and securities configurations.
The logs has 1,939,207 events, from 2017 to 2020. 
9,402 unique IP addresses.
8,811 unique user agents.
Calls to 1,242 different APIs were attempted.
No labels.
No paper published.
Release in the end of 2020.

## ROADMAP

- review of the ppt and start digging in the papers
- reviewed the three papers of API and starting with CSCLog.
	- started a review to highlight the changes from every ML/DL log AD and then understand the pros-cons
	- 


## NOTES

The papers that are semenly more important and useful are: 
- CSCLog
- Log event sequences AD

Analysis on the API papers before hands, since they are the starting point.

The API papers utilise:
1. the normal traffic as a starting point
2. a malevolent traffic as a starting point

I think the solution most correct could be the 1st, since how many new attacks could be invented in order to bypass security systems, that the initial attacks dataset do not take in considerations.
There is no means testing about changing the application mid-running the model. How that could influence the labelling system. The solution after are better or worst?
Usually the model do not react good to attack-pattern changes, so usually the new emerging threat cannot be found if it is not present in the starting dataset.
Luis sad that to highlight this fact, they used to change the time-flow of the packets: the systems did not recognise the "new" attack. This only small insignificant change disrupt the complete flagging operation.
The problem is presented in every possibility:
- training on the safe traffic is useful only to understand anomalies, not all implementation uses to log the correct API endpoint being attacked. Whenever the application get updates (that in microservices is a fact, not a when), it must be create traffic to train a new model on.
- the train on malicious traffic is not useful since it block the possibility of other thread, breaking the concept of the machine learning => rule-base are more efficient in that case.
- pattern-base: maybe chaning the frequency of the actions could rearrange the pattern as
- changing the information that the systems contains and work with, the model change its performance (a banking systems instead of something else).

Detecting malevolent and benevolent traffic is difficult, since is difficult create all the traffic for train the malevolent traffic, and there's nothing sure about every anomaly to be detected.

All the papers diversify from DoS attacks and everything else.


LOG resources: https://github.com/logpai/loghub

Grouping the papers:
- like the two paper of API are in one
- the api systems calls analysis is with RNN and api calls.

### Section on Log Anomaly

Starting from the CSCLog paper, we found the precedent. From that we started an analysis about what is added/changed about 

Papers:
- [[DeepLog]], published during 2017
- [[Loganomaly]], published during 2019
- [[LogC]], published during 2020
- [[OC4Seq]], published during 2021 (# Improving Log-Based Anomaly Detection with Component-Aware Analysis)
- [[CSCLOG]], published during 2023
- [[OperResearchChallenges]], published on July, 2023 (Towards Detecting Anomalies in Log-Event Sequences with Deep Learning: Open Research Challenges)

How they do in industrial methods?

LogDeep => there are a lot of repository
https://github.com/donglee-afar/logdeep
https://github.com/nailo2c/deeplog