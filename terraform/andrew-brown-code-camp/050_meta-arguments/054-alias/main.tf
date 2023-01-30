terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.45.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

provider "aws" {
  alias  = "west"
  region = "us-west-1"
}

data "aws_ami" "ubuntu" {
  provider    = aws
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"]
}

data "aws_ami" "ubuntu_west" {
  provider    = aws.west
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"]
}

variable "instance_type" {
  type    = string
  default = "t2.micro"
}

resource "aws_key_pair" "deployer" {
  key_name   = "deployer_key"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDZV2UlqnvO48F6rGCcrbpWlqV5mtdS9DhQv+T414r/NIj+EhvtEGzkrWEEuJzqrECI55MR84fY2Yw73Mx8uhCYNqpgNL4XEJSdZzpELl/h5GA3WgKHXeWsuCpkADEG3Gbr49wEpHzO1jp9mPoj9b7VS2SCJVwDe+/4GCjEZX0NTDGidHUuZyhcsPt38O3NDM9OwGKzLeBM6ts1l62U4vZ8oAmA5kSNGUNqSG10q92YidtToSSMKKn1LKxPvbUK/uBY/ZGh/nQRo6d7C19YKnT3NH6467fShXIAPqBDo6xHLhCOch4KXV7w0Kq/JBIskJ0++xNTeJsIWE4BvsqHLWpSxVqc+jC/pvMbdISZoYmcVWs+LJtpi5iwIh0fyvVRjwTMn9Sh57qKUpgqDw+LFTNuuCUmP7YWK9ygvPmvyxjFgjAnENo+kaibFI55Hihvq6CyjMEVsLH6Aj4T1DN5BBiyvmxSianRglv0HxMtWH/l0E4t4yUZ8mj3MIAmR8RIUDk="
}


resource "aws_instance" "my_server" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = var.instance_type
  key_name      = aws_key_pair.deployer.key_name

  tags = {
    Name = "MyServer"
  }
}

resource "aws_instance" "my_server_west" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = var.instance_type
  key_name      = aws_key_pair.deployer.key_name
  provider      = aws.west

  tags = {
    Name = "MyServer-West"
  }
}


data "aws_vpc" "main" {
  id = "vpc-b44a2dce"
}

output "public_ip" {
  value = aws_instance.my_server.public_ip
}

output "public_ip_west" {
  value = aws_instance.my_server_west.public_ip
}