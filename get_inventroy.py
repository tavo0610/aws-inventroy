#!/usr/bin/env
import json
import boto3
from botocore.vendored import requests

client = boto3.client('ecs')
response = client.list_clusters()
# print(response)
ecs_clusters = str(
    (sum([len(response[x]) for x in response if isinstance(response[x], list)])))
print("The number of ECS Clusters are: " + ecs_clusters)

client_cf = boto3.client('cloudfront')
response = client_cf.list_distributions()
cf_distributions = str(response['DistributionList']["Quantity"])
print("The number of CF Distributions are: " + cf_distributions)

client_s3 = boto3.client('s3')
response = client_s3.list_buckets()
buckets = str(len(response['Buckets']))
print("The number of S3 Buckets are: " + buckets)

client_agw = boto3.client('apigateway')
response = client_agw.get_rest_apis()
api_gws = str(len(response['items']))
print("The number of API GW are: " + api_gws)

client_ec2 = boto3.client('ec2')
response = client_ec2.describe_instances()
ec2 = str(len(response['Reservations']))
print("The number of EC2 are: " + ec2)
