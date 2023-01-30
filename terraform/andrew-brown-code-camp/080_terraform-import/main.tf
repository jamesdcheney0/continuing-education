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

data "aws_ami" "ubuntu" {

    most_recent = true

    filter {
        name   = "name"
        values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
    }

    filter {
        name = "virtualization-type"
        values = ["hvm"]
    }

    owners = ["099720109477"]
}

variable "instance_type" {
    type = string
    default = "t2.micro"
}

resource "aws_key_pair" "deployer" {
  key_name   = "deployer_key"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDZV2UlqnvO48F6rGCcrbpWlqV5mtdS9DhQv+T414r/NIj+EhvtEGzkrWEEuJzqrECI55MR84fY2Yw73Mx8uhCYNqpgNL4XEJSdZzpELl/h5GA3WgKHXeWsuCpkADEG3Gbr49wEpHzO1jp9mPoj9b7VS2SCJVwDe+/4GCjEZX0NTDGidHUuZyhcsPt38O3NDM9OwGKzLeBM6ts1l62U4vZ8oAmA5kSNGUNqSG10q92YidtToSSMKKn1LKxPvbUK/uBY/ZGh/nQRo6d7C19YKnT3NH6467fShXIAPqBDo6xHLhCOch4KXV7w0Kq/JBIskJ0++xNTeJsIWE4BvsqHLWpSxVqc+jC/pvMbdISZoYmcVWs+LJtpi5iwIh0fyvVRjwTMn9Sh57qKUpgqDw+LFTNuuCUmP7YWK9ygvPmvyxjFgjAnENo+kaibFI55Hihvq6CyjMEVsLH6Aj4T1DN5BBiyvmxSianRglv0HxMtWH/l0E4t4yUZ8mj3MIAmR8RIUDk="
}


resource "aws_instance" "my_server" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = var.instance_type
  key_name               = aws_key_pair.deployer.key_name
  # subnet_id, and not vpc_id would be how to put this into a specific place 

  tags = {
    Name = "MyServer"
  }
}

data "aws_caller_identity" "current" {}

resource "aws_s3_bucket" "bucket" {
  bucket = "${data.aws_caller_identity.current.account_id}-my-tf-test-bucket"

  depends_on = [
    aws_instance.my_server
  ]
}

# To import the resource, had to run `terraform import aws_vpc.default vpc-b44a2dce`
# terraform import <resource.id> <aws-resource-id>
# Can then copy information from state file to this resource and manage the resource 
resource "aws_vpc" "default" {
}

output "public_ip" {
  value = aws_instance.my_server.public_ip
}