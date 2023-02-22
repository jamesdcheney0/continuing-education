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

resource "aws_key_pair" "deployer" {
  key_name   = "deployer_key"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDZV2UlqnvO48F6rGCcrbpWlqV5mtdS9DhQv+T414r/NIj+EhvtEGzkrWEEuJzqrECI55MR84fY2Yw73Mx8uhCYNqpgNL4XEJSdZzpELl/h5GA3WgKHXeWsuCpkADEG3Gbr49wEpHzO1jp9mPoj9b7VS2SCJVwDe+/4GCjEZX0NTDGidHUuZyhcsPt38O3NDM9OwGKzLeBM6ts1l62U4vZ8oAmA5kSNGUNqSG10q92YidtToSSMKKn1LKxPvbUK/uBY/ZGh/nQRo6d7C19YKnT3NH6467fShXIAPqBDo6xHLhCOch4KXV7w0Kq/JBIskJ0++xNTeJsIWE4BvsqHLWpSxVqc+jC/pvMbdISZoYmcVWs+LJtpi5iwIh0fyvVRjwTMn9Sh57qKUpgqDw+LFTNuuCUmP7YWK9ygvPmvyxjFgjAnENo+kaibFI55Hihvq6CyjMEVsLH6Aj4T1DN5BBiyvmxSianRglv0HxMtWH/l0E4t4yUZ8mj3MIAmR8RIUDk="
}

data "template_file" "user_data" {
  template = file("./userdata.yml")
}

# Three kinds of provisioners - local, remote, file & some of the syntax. They should all work, 
# based on the video I watched. I have not tested them myself
resource "aws_instance" "my_server" {
  ami                    = "ami-087c17d1fe0178315"
  instance_type          = "t2.micro"
  key_name               = aws_key_pair.deployer.key_name
  vpc_security_group_ids = [aws_security_group.my_server_sg.id]
  user_data              = data.template_file.user_data.rendered
  provisioner "local-exec" {
    command = "echo ${self.public_ip} >> /home/ec2-user/public_ips.txt"
  }
  provisioner "remote-exec" {
    inline = [
      "echo ${self.public_ip} >> /home/ec2-user/public_ips.txt"
    ]
    connection {
      type        = "ssh"
      user        = "ec2-user"
      private_key = file("/Users/jamescheney/.ssh/terraform-testy-boi")
      host        = "${self.public_ip}"
    }
  }
  provisioner "file" {
    content      = "Hello World!"
    destination = "/home/ec2-user/hello-world.txt"
    connection {
      type        = "ssh"
      user        = "ec2-user"
      private_key = file("/Users/jamescheney/.ssh/terraform-testy-boi")
      host        = "${self.public_ip}"
    }
  }

  tags = {
    Name = "MyServer"
  }
}

data "aws_vpc" "main" {
  id = "vpc-b44a2dce"
}

resource "aws_security_group" "my_server_sg" {
  name        = "allow_http"
  description = "Allow HTTP inbound traffic"
  vpc_id      = data.aws_vpc.main.id

  ingress {
    description      = "HTTP from anywhere"
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = []
  }

  ingress {
    description      = "SSH from local"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["98.168.57.5/32"]
    ipv6_cidr_blocks = []
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }
}

# Wait until the instance has two successful status checks before `terraform apply` finishes
resource "null_resource" "status" {
    provisioner "local-exec" {
        command = "aws ec2 wait instance_status-ok --instance-ids ${aws_instance.my_server.id}"
    }
    depends_on = [
      aws_instance.my_server
    ]
}

output "public_ip" {
  value = aws_instance.my_server.public_ip
}