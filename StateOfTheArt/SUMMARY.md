There are a lot of methods to identify if the systems is not working correctly and know where it is failing.

The problems are in the README.

The goal: find a systems that could detect anomalies in a systems without prior knowledge, real-time, with machine learning shenanigans.

Possible sections organisation:

- What are logs, what they are used for and what they can support/express.
	- auditing logs/plain text logs
	- Log information extracting for ML/DL models
- What are IDS/IPS systems and ML/DL based systems and anomaly detection. Different points of the whole groups of research
	- API-based ones
	- RNN analysis
- Problems with existing models for anomaly detection (domain-specific, ML-retraining, others...)
- application of the models in cloud environment, instead only kubernetes


# Presentation

- rule based systems failure
- cloud infrastructure needs:
	- too much logs
	- complicated network communications
- machine learning automatic anomaly detection:
	- API based: behavour analysis and they take it
	- code pushed need to be retrained 
	- binary classification (problem in malicious alert to take traffic and to produce traffic, more complex rerun of the model)
- Why logs
	- DeepLogs starting RNN-LSTM and PCA to perform AD
	- LogAnomaly: introduce the concept of log correlations (more accurate but slower to identify in the example)
	- LogRobust: application in a real word scenario with log instability (evolution of logs and processing log data)
		- Solution: Bi-LSTM in order to correlate the sequence similar to each other, not the same
	- LogC: introduce the component aware technolog
	- CSCLog: subsequences
	- LogGraph: correlation and real word scenario (multitreading, log data noise) and multiple anomaly concurrency

Given the current papers presentation, there are some consideration to make:
- Log Anomaly detection has positive traits
- The binary classification methods do not work. Despite that, the RNN-sequence based
methods seemingly do.
- When the complete current flow is used as training, the accuracy rating are high. Some
models take more time to train, other can update real time.
 LLM are great for log comprehension and correlation, and could be an interesting
classification tool.
- There are better cases on anomaly detection if the flow is divided by components, but this
operation increase computational costs, and so its not always possible to do it realtime
- The classification on known attacks works only in limited cases and probably leave no doubt
to zero-day vulnerability
- The usage recording mechanism is the one used in the wild, by business to run a SOC. That
means they are actually dealing with ML/DL problems and techniques now
- The problems of SOC elaborate on the fact that false-positives are not an issue, instead the literature is constantly reaching 0% false-positive.
- The communication of the logs in a real-word scenario is something to take into
consideration
- Some algorithms, more than other, are exceptionally domain-specific
- Kubernetes auditi log literature is an early state
- time needed to obtain a correlation/aler