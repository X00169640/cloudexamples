terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }
}

provider "aws" {
  region  = "eu-west-1"
}

resource "aws_vpc" "example_vpc" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "vpc-example"
  }
}
resource "aws_subnet" "example_subnet" {
  vpc_id            = aws_vpc.example_vpc.id
  cidr_block        = "10.0.0.0/24"
  availability_zone = "eu-west-1a"

  tags = {
    Name = "subnet-example"
  }
}

resource "aws_instance" "example_server" {
  ami           = "ami-06ce3edf0cff21f07"
  subnet_id = aws_subnet.example_subnet.id
  instance_type = "t2.micro"
}



