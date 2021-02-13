from troposphere import Base64, FindInMap, GetAtt
from troposphere import Parameter, Output, Ref, Template
import troposphere.ec2 as ec2

template = Template()

keyname_param = template.add_parameter(Parameter(
    "KeyName",
    Description="Name of an existing EC2 KeyPair to enable SSH access to the instance",
    Type="String",
))

# Ubuntu 20.04 free tier,64-bit x86, images 
template.add_mapping('RegionMap', {
    "us-east-1":      {"AMI": "ami-0885b1f6bd170450c"},
    "us-east-2":      {"AMI": "ami-0a91cd140a1fc148a"},
    "us-west-1":      {"AMI": "ami-00831fc7c1e3ddc60"},
    "us-west-2":      {"AMI": "ami-07dd19a7900a1f049"}
})

ec2_instance = template.add_resource(ec2.Instance(
    "Ec2Instance",
    ImageId=FindInMap("RegionMap", Ref("AWS::Region"), "AMI"),
    InstanceType="t2.micro",
    KeyName=Ref(keyname_param),
    SecurityGroups=["default"],
    UserData=Base64("80")
))

template.add_output([
    Output(
        "InstanceId",
        Description="InstanceId of the newly created EC2 instance",
        Value=Ref(ec2_instance),
    ),
    Output(
        "AZ",
        Description="Availability Zone of the newly created EC2 instance",
        Value=GetAtt(ec2_instance, "AvailabilityZone"),
    ),
    Output(
        "PublicIP",
        Description="Public IP address of the newly created EC2 instance",
        Value=GetAtt(ec2_instance, "PublicIp"),
    ),
    Output(
        "PrivateIP",
        Description="Private IP address of the newly created EC2 instance",
        Value=GetAtt(ec2_instance, "PrivateIp"),
    ),
    Output(
        "PublicDNS",
        Description="Public DNSName of the newly created EC2 instance",
        Value=GetAtt(ec2_instance, "PublicDnsName"),
    ),
    Output(
        "PrivateDNS",
        Description="Private DNSName of the newly created EC2 instance",
        Value=GetAtt(ec2_instance, "PrivateDnsName"),
    ),
])

print(template.to_json())   
