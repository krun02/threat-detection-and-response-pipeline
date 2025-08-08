import boto3
import json
import logging
import os

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


SNS_TOPIC_ARN = os.environ.get("SNS_TOPIC_ARN")

ec2_client = boto3.client('ec2')
sns_client = boto3.client('sns')

def lambda_handler(event, context):
    logger.info("Received event: %s", json.dumps(event))

    detail = event.get('detail', {})
    findings = detail.get('findings', [])
    instance_ids = []

    for finding in findings:
        resources = finding.get('resources', [])
        for resource in resources:
            if resource.get('type') == 'AwsEc2Instance':
                instance_arn = resource.get('id')
                instance_id = instance_arn.split('/')[-1]
                instance_ids.append(instance_id)

    logger.info("Affected EC2 instances: %s", instance_ids)

    for instance_id in instance_ids:
        try:
            ec2_client.create_tags(
                Resources=[instance_id],
                Tags=[{'Key': 'ThreatDetected', 'Value': 'GuardDuty_HighSeverity'}]
            )
            logger.info(f"Tagged EC2 instance {instance_id} successfully.")
        except Exception as e:
            logger.error(f"Failed to tag EC2 instance {instance_id}: {str(e)}")
    try:
        sns_client.publish(
           TopicArn=SNS_TOPIC_ARN,
            Subject="🚨 GuardDuty High-Severity Threat Detected",
            Message=json.dumps(event, indent=2)
        )
        logger.info("SNS alert sent.")
    except Exception as e:
        logger.error(f"Failed to send SNS alert: {str(e)}")

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda executed successfully.')
    }
