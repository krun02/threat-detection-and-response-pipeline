# Setup Instructions for AWS Cloud Threat Detection and Auto-Remediation
This guide walks you through setting up a real-time threat detection and response pipeline using AWS GuardDuty, Lambda, SNS, and CloudWatch Events.

# Enable Amazon GuardDuty
1. Go to [Amazon GuardDuty Console](https://console.aws.amazon.com/guardduty/home).
2. Click "Enable GuardDuty" in your region.
3. Make sure these data sources are enabled:
   - VPC Flow Logs
   - AWS CloudTrail Management Events
   - DNS Logs
  
  # Create SNS Topic for Alerts
1. Go to [Amazon SNS Console](https://console.aws.amazon.com/sns).
2. Click "Create topic" → Select "Standard".
3. Name it: `gd-alert-topic`.
4. After creating, copy the "SNS Topic ARN".
5. Click "Create subscription":
   - Protocol: "Email"
   - Endpoint: your email address
6. Confirm the subscription from your inbox.

# Create IAM Role for Lambda
1. Go to [IAM Console](https://console.aws.amazon.com/iam).
2. Create a new **role for Lambda**.
3. Attach a custom inline policy with permission

Create EventBridge Rule (CloudWatch Event)
Go to EventBridge Console.

# Create a Rule:
Name: GuardDutyHighSeverityRule
Event Source: AWS Services
Service: GuardDuty

# Test the Pipeline
Run this AWS CLI command to generate test findings:
aws guardduty create-sample-findings
  --detector-id <your-detector-id> 
  --finding-types UnauthorizedAccess:EC2/SSHBruteForce

  




