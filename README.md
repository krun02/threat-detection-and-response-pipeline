# threat-detection-and-response-pipeline
This project sets up a threat detection and response pipeline using Amazon GuardDuty, CloudWatch, and AWS Lambda to identify and react to suspicious activity in an AWS environment. It includes auto-alerting via SNS and optional automatic isolation of suspicious EC2 instances.

# Overview
This project leverages Amazon GuardDuty,CloudWatch Events,AWS Lambda, and SNS to build a real-time cloud security detection and response pipeline.

# Key Features:
- Monitor AWS activity using GuardDuty.
- Trigger alerts for high-severity threats.
- Auto-tag suspicious EC2 instances.
- Notify security team via email.

# Tech Stack
Amazon GuardDuty – Threat detection
AWS CloudTrail – Log collection
CloudWatch Events – Trigger logic
AWS Lambda (Python) – Automation script
Amazon SNS – Alert notifications
IAM – Secure permissions

# How It Works
GuardDuty monitors AWS account for threats.
High-severity findings (severity ≥ 8) trigger a CloudWatch rule.
Rule invokes Lambda function:
Extracts affected EC2 instance
Tags the instance with ThreatDetected
Publishes an alert to an SNS topic
Analyst receives an email with full threat details.
