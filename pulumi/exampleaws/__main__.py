import pulumi
import pulumi_aws as aws

example_vpc = aws.ec2.Vpc("exampleVpc",
    cidr_block="10.0.0.0/16",
    tags={
        "Name": "vpc-example",
    }
)

example_subnet = aws.ec2.Subnet("exampleSubnet",
    vpc_id=example_vpc.id,
    cidr_block="10.0.0.0/24",
    availability_zone="eu-west-1a",
    tags={
        "Name": "subnet-example",
    }
)

example_server = aws.ec2.Instance("exampleServer",
    ami="ami-06ce3edf0cff21f07",
    subnet_id=example_subnet.id,
    instance_type="t2.micro")