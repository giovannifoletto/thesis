# deepcase.pdf: 
Explain the use of automatic log correlation tools with the intent of reducing the workload of the Security Operator. That is done explaining how a SOC works and with a state-of-the-art analysis on current network analytics tool.
This approach take as starting point the alerts of the SIEM software and the logs that have caused this kind of alert and produce this system (DeepCase) that allow a correlation of event with the goal of:
- reducing the overall number of alerts
- reducing operator fatigue 
- make understandable and clear to operators complex cases and series of operation and evolving threats
This approach is useful in order of industrial application, since it could be applied literally tomorrow, but is not what we want.

https://github.com/Thijsvanede/DeepCASE


# SherLog (22808-asplos10-sherlog.pdf)

This papers explains how to use logs to forensics analyse some systems-failure or intrusion. They use only logs and source code to do that.

# Unsupervised log message anomaly detection (1-s2.0-s24....pdf)

This papers works on anomaly detection with goog and bad traffic as input and then elaborate on NLP models to understand logs and label them.
This could be useful for the part of log analysis, but no more.


# CloudSeer: Workflow Monitoring of Cloud Infrastructures via Interleaved Logs (asplos16-cloudseer.pdf)

Maybe intresting.
Log anomaly detection in order to find problems in the entire infrastructure, but in this paper they do a workflow monitoring of all the service that are working together. 
That allow to correlate services that have to work together. 
This papers allow a proper logging for systems and application failure, including the ones happening silently for non enough log or other problems.


