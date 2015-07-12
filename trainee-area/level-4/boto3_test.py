import boto3

ec2 = boto3.client('ec2')

ec2.run_instances(
    ImageId="ami-d05e75b8", MinCount=1, MaxCount=1, KeyName="bfp_v1",
    InstanceType="t2.micro", SubnetId="subnet-d72c38ed")

