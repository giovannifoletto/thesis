---
data: Nov. 15, 2023
author: Giovanni Foletto
Source: "DeepLog: Anomaly Detection and Diagnosis from System Logs through Deep Learning"
tags:
  - Anomaly-detection
  - RNN-LSTM
  - machine-learning-models
  - deep-learning
---
```
YELLOW: interesting for this work
GREEN: other resources/papers that may be interesting
BLUE: code and related, with algorithm explanations too
GREY: questions
```

Logs are the universal technical method to understand how a systems is performing, save systems-states and insightful events in order to allow a post-mortem forensic root causes analysis. They are used in online monitoring and anomaly detection tool, because of the particular excellent information they bring about the systems. The fact that logs records events real-time (while they are happening), they are capable of recording events **as-they occurs**.

DeepLog works with RNN-LTSM to model systems logs as a natural language sequence. The model can learn the log patterns and then is capable of alerting if an anomaly is detected.
The papers explains how to incrementally update the DeepLog model in order to maintain the anomaly detection capability during time and application changes.

Clearly, like all the ML/DL techniques, DeepLog outperform normal and traditional detection mechanism.

The authors says that the current environment working leveraging systems data for anomaly detection is mainly divided in three parts (to be clear, the paper is dated back in 2017, after that 5 publications make their way out):

1. [[PCA]] based approaches over logs message counters
2. Invariant mining based methods to capture co-occurrence patterns between different log keys
3. workow based methods to identify execution anomalies in program logic flows

The problems with these solution is that no one is effective as **universally anomaly detection methods**, capable of guarding against different attacks, in particular for a online application.

The approach presented is exploiting large model of language processing, thinking about logs like a speech with a limited vocabulary. To that, the DeepLog algorithm works in order to find patterns in the normal working systems using LSTM and modelling log sequences. That allow the algorithm to incrementally learn the correct pattern **during** the systems execution. Since this approach is learning driven, the model can adapt incrementally and automatically, in order to responds to systems/application changes.

The traditional rule-base analytics systems do not work in an environment in which there is no prior knowledge about the logs structure, the application logic and architecture and the correct and incorrect way of working things. 

For a systems like this to work, there's the need of it working real-time: what the possible application a systems that alert about an attack in 2 days?
Another necessity is that this new ML/DL AD systems can identify **also unknown** type of threats, instead of elaborating on specific known threat.

The RNN approach allow the output of a layer to be reintegrated as the input, maintaining some sort of memory on the actions made against that method. A particular type of this kind of model is LSTM, that has demonstrated to be capable of machine translations, sentiment analysis, medical self-diagnosis. That could be perfectly used for our goal, too.

The algorithm ingest log values and metrics in order to detect different type of anomaly, using a small parts of the logs as *training data*. To obtain a perfect timely-accurate pattern recognition, the algorithm divide all the logs based on the concurrent task/thread that has created the log itself. Each task or workflows in this manner gets their own model. The model allows to modify the weight of the things in real time, by incorporating live user feedback.

> MAYBE: That allow a better division of the working flow, in order to parallelize computation.

This system works only to beat a specific **threat model**, given the assumption of:
1. the integrity of the logs is not attack-able
2. the attacker cannot modify the system source code to change the logging behaviour
That said, there is a specific attack model that this systems means to identify, and they are sum-up in two categories:
1. Attacks that lead to systems execution to misbehave and hence produce anomalous patterns in logs. This group collect DoS attacks (the log receiving order or frequency is changed or the response time is intacted), BROP (Blind Return Oriented Programming) and all the attacks that change the way the program works.
2. All the attacks that could leave trace in systems logs due to the logging activities of the system monitoring services or any external monitoring tool.

## How the systems works

![[Pasted image 20231115180333.png]]

The first part the algorithm is about log parser. It is shown that by several previous works that is possible and effective using the "log key" methodology for each log entry. The difference in this application is about the use of some identifiers for understand from which nodes/part of the systems the logs came thought. 
For example are useful the `block_id` value and the `instance_id` in order to understand from which node their are come.
As the log parsing method they used the `Spell` library, that (they say) is the *state-of-the-art*.

The architecture of the systems is shown in the picture above, but mainly is divisible in three phases:
1. the log key anomaly detection model
2. the parameter value anomaly detection model
3. the workow model to diagnose detected anomalies

The identification phases is based on two results, based on the parsed log entry. These are key value and parameters value vector. If both these results are detected as anomaly, the alert is emitted.

DeepLog also provide an option of collecting users feedback, in order to eliminate false-positive, in order to allow the model to incorporate the new pattern and adapt to it.

The systems allow an external feedback, in order to flag the false-positive and so adjust the execution and how the model works. The model allow other logs to be added and allow an adjustment over them, in order to update the entire model without the necessity of retraining the entire model. In order to do that, the process receive the new data and adjust the weight in order to minimise the error-rate between model output and actual observed values from false-positive cases.

The model illustrated the methods of eliminating too much false-positives: using another feature in the machine learning model in order to make clear if something is highly possible that would be a false-positive.
Another use case of this methods allow to check the models errors analysing history of responses and tracing back model's input. With that is possible a comparison between the data, and so a "post-mortem analysis" on what about has not gone right.


# Considerations

This paper is the start of a set of papers that are heavily linked and elaborate on the same topics: automatic pattern anomaly detection using some sort of RNN and NLP (natural language processing) in order to find key-value indicators within the logs and then make them available in a time-base sequence. This allow a anomaly detection classificator that could allow a real-time AD in the wild, with the possibility of interacting and changing weights of the feature and change the anomaly detection output dinamically and automatically.
They says that the performance allow real-time, no need a specific model for use-case (like it can be applied in banking systems or animal control systems), and allow a manual insert in order to change/solve false-positive and application changes.

PROS: They elaborate all the expected anomaly of these methods, **publishing a threat model really specific**. The applications seems to be **real-time** with a model that can be update real-time in order to accomodate particular application update. 
The resource allow a really good explanatino about this systems, what the capabilities must be and the other secondary characteristic. 
It is the only paper tested for networking appliance.
CONS: no code published and dataset.

DATESET: no
ALGORITHM: explained, but not officially implemented (https://github.com/nailo2c/deeplog).

I think in the "Related Work" section there is more to dig. This is surely the most big papers to read.

Other sources:
https://github.com/Thijsvanede/DeepLog
https://github.com/wuyifan18/DeepLog
https://github.com/Wapiti08/DeepLog