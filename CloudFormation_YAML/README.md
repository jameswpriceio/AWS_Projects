# AWS CloudFormation VPC, EC2, Elastic IP & Security Group Template

---
Description: "Creates a VPC using a single EC2 instance with an Elastic IP and security group. 

## Template - Parameters and AWS Region 

---

```
Parameters (Web Server) line 17: only allowed type for Web server (EC2) is t2.nano

Region (zone and AMI type) lines 253 - 261 reads:
    # Ubuntu 20.04 free tier,64-bit x86, images
    us-east-1: 
        HVM64: ami-0885b1f6bd170450c
    us-east-2:
        HVM64: ami-0a91cd140a1fc148a
    us-west-1:
        HVM64: ami-00831fc7c1e3ddc60
    us-west-2:
        HVM64: ami-07dd19a7900a1f049
  ```
**WARNING** - verify billing prior to use




## Additional Resources

---
In the *AWS CloudFormation User Guide*, you can view more information about the following topics:

- Learn how to use templates to create AWS CloudFormation stacks using the [AWS Management Console](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) or [AWS Command Line Interface (AWS CLI)](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-cli-creating-stack.html).
- To view all the supported AWS resources and their properties, see the [Template Reference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-reference.html).