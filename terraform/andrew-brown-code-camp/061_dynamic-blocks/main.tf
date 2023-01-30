terraform {
  required_version = "~> 1.0.0" # aka progressive versioning - defining required version like this says use TF 1.0.0 at a minimum, and use the newest version
  # required_version = ">= 1.0.0" # basically does the same thing 
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "4.48.0"
    }
  }
}

provider "aws" {
}

data "aws_vpc" "main" {
  id = "vpc-b44a2dce"
}

locals {
    ingress = [{
        port = 443
        description = "Port 443"
    },
    {
        port = 80
        description = "Port 80"
    }]
}

resource "aws_security_group" "allow_tls" {
  name        = "allow_tls"
  description = "Allow TLS inbound traffic"
  vpc_id      = data.aws_vpc.main.id

  dynamic "ingress" {
    for_each = local.ingress
    content {
        description      = ingress.value.description
        from_port        = ingress.value.port
        to_port          = ingress.value.port
        protocol         = "tcp"
        cidr_blocks      = [data.aws_vpc.main.cidr_block]
    }
  }


  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
  }
}