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

Some recurrent methods of evasion?

### Section on Log Anomaly

Starting from the CSCLog paper, we found the precedent. From that we started an analysis about what is added/changed about 

Papers:
- [[DeepLog]], published during 2017
- [[Loganomaly]], published during 2019
- [[LogRobust]], release 2019
- [[LogC]], published during 2020
- [[OC4Seq]], published during 2021
- [[CSCLOG]], published during 2023
- [[OperResearchChallenges]], published on July, 2023 (Towards Detecting Anomalies in Log-Event Sequences with Deep Learning: Open Research Challenges)
- [[LogGraph]], release 2023, not yet published

How they do in industrial methods?

LogDeep => there are a lot of repository
https://github.com/donglee-afar/logdeep
https://github.com/nailo2c/deeplog

RESEARCH ONN KUBE MONITORING, LOGGING AND METRICS.

FATIGUE ALERT: https://link.springer.com/chapter/10.1007/978-3-030-36708-4_62

NTMALTRACE: https://github.com/cwkeam/NtMalDetect
NNI (Neural Netowork Intelligence): https://nni.readthedocs.io/en/stable/

# Search in files


```bash
find /path -name '*.pdf' -exec sh -c 'pdftotext "{}" - | grep --with-filename --label="{}" --color "your pattern"' \;
```


## TODO TODAY:

considerations
SOC read the paper.

# After Meeting

1. Intorduction to Kubernetes, Kubernetes' Audit Logs, Kubernetes Security
	1. https://kubernetes.io/training/
	2. https://aws.amazon.com/it/cloudtrail/
	3. https://blog.aquasec.com/kubernetes-exposed-one-yaml-away-from-disaster
	4. https://github.com/easttimor/aws-incident-response
	5. https://www.sumologic.com/blog/kubernetes-logs/
2. Introduction to Kubernetes/cluster related possible attacks, how they works and how is possible to reproduce
	1. https://www.linkedin.com/pulse/top-15-common-attacks-kubernetes-vicky-budhiraja/
	2. The state-of-the-art in container technologies: Application, orchestration and security (PDF: state_art_container_security.pdf)
	3. KubAnomaly: Anomaly detection for the Dockerorchestration platform with neural network approaches (pdf: kubAnomaly qualcosa .pdf)
	4. Batch and online anomaly detection for scientific applications in a Kubernetes environment (batch_kube.pdf)
	5. Outlier Detection in Dynamic Systems with Multiple Operating Points and Application to Imporove Industrial Flares Monitoring (outlier_detection.pdf)
3. DL/ML and application of RNN-LSTM
	1. Toward_Explainable_Deep_Neural_Network_Based_Anomaly_Detection.pdf
	2. Recurrent_Neural_Network_Attention_Mechanisms.pdf
	3. A Comparative Study of Two Network-based Anomaly Detection Methods
	4. Learning stochastic differential equations using RNN with log signature features (https://arxiv.org/abs/1908.08286)
	5. LogBERT: Log Anomaly Detection via BERT
	6. ADA: Adaptive Deep Log Anomaly Detector
	7. Network_Log_Anomaly_Detection_Based_on_GRU_and_SVDD.pdf
	8. Log File Anomaly Detection
	9. Long Short-Term Memory based Operation Log Anomaly Detection
	10. LLAD_LifeLog_Anomaly_Detection_Based_on_Recurrent_Neural.pdf
	11. Leveraging Clustering and Natural Language Processing to Overcome Variety Issues in Log Management
	12. Deep_Learning_Approaches_for_Intrusion_Detection_System.pdf
	13. A Real-Time Audit Mechanism Based on the Compression Technique
	14. Cloud_Security_Auditing_Based_on_Behavioral_Modeling.pdf 
	15. Based_on_the_user_behavior_characteristic ff_mining_database anomaly_detection_model_design.pdf
	16. Microservices Monitoring with Event Logs and Black Box Execution Tracing
	17. Analysing and alerting on application logs within Kubernetes infrastructure
	18. Log Clustering based Problem Identification for Online Service Systems
	19. NIPS-2010-robust-pca-via-outlier-pursuit-Paper.pdf
4. pytorch/tensorflow

https://github.com/autumn0409/Log-based-Anomaly-Detection-System

Papers not found, maybe interesting: 
1. The Implementation of a Network Log System Using RNN on Cyberattack Detection with Data Visualization (https://link.springer.com/chapter/10.1007/978-981-15-3250-4_38).
2. Exploiting Event Log Event Attributes in RNN Based Prediction (https://link.springer.com/chapter/10.1007/978-3-030-46633-6_4)
3. https://www.inderscienceonline.com/doi/epdf/10.1504/IJBPIM.2014.063518
4. https://link.springer.com/chapter/10.1007/978-3-031-28790-9_2
5. https://link.springer.com/chapter/10.1007/978-1-4842-5458-5_8

Da leggere 29 papers and a github repo + kubernetes foundation + ML/DL foundation 
+ AdvProg
+ networking 2
