data "aws_vpc" "main" {
  id = var.vpc_id
}


resource "aws_security_group" "sg_my_server" {
  name        = "sg_my_server"
  description = "MyServer Security Group"
  vpc_id      = data.aws_vpc.main.id

  ingress = [
    {
      description      = "HTTP"
      from_port        = 80
      to_port          = 80
      protocol         = "tcp"
      cidr_blocks      = ["0.0.0.0/0"]
      ipv6_cidr_blocks = []
      prefix_list_ids  = []
      security_groups  = []
      self             = false
    },
    {
      description      = "SSH"
      from_port        = 22
      to_port          = 22
      protocol         = "tcp"
      cidr_blocks      = ["${var.my_ip}"]
      ipv6_cidr_blocks = []
      prefix_list_ids  = []
      security_groups  = []
      self             = false
    }
  ]

  egress = [
    {
      description      = "outgoing traffic"
      from_port        = 0
      to_port          = 0
      protocol         = "-1"
      cidr_blocks      = ["0.0.0.0/0"]
      ipv6_cidr_blocks = ["::/0"]
      prefix_list_ids  = []
      security_groups  = []
      self             = false
    }
  ]
}

resource "aws_key_pair" "deployer" {
  key_name   = "deployer-key"
  public_key = var.public_key
}

data "template_file" "user_data" {
  template = file("${path.module}/userdata.yml")
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

# data "aws_subnets" "subnet_ids" {
#   filter {
#     name = "vpc-id"
#     values = [var.vpc_id]
#   }
# }

# data "aws_subnet" "subnet_ids" {
#   for_each = toset(data.aws_subnets.subnet_ids.ids)
#   id = each.value.id
# }

# with subnet_id              = data.aws_subnet.subnet_ids.id[0] was not working. mix of 
# │ Error: Missing resource instance key
# │ 
# │   on ../../100_modules/terraform-aws-apache-example/main.tf line 95, in resource "aws_instance" "my_server":
# │   95:   subnet_id              = data.aws_subnet.subnet_ids.id
# │ 
# │ Because data.aws_subnet.subnet_ids has "for_each" set, its attributes must be accessed on specific instances.
# │ 
# │ For example, to correlate with indices of a referring resource, use:
# │     data.aws_subnet.subnet_ids[each.key]

# and 

# │ Error: Error in function call
# │ 
# │   on ../../100_modules/terraform-aws-apache-example/main.tf line 95, in resource "aws_instance" "my_server":
# │   95:   subnet_id              = flatten(data.aws_subnet.subnet_ids)[0]
# │     ├────────────────
# │     │ data.aws_subnet.subnet_ids is object with 6 attributes
# │ 
# │ Call to function "flatten" failed: can only flatten lists, sets and tuples.


# data "aws_subnet_ids" "subnet_ids" {
#   vpc_id = data.aws_vpc.main.id
# }

# `subnet_id              = tolist(data.aws_subnet_ids.subnet_ids.ids)[0]` works with that data module 

data "aws_subnets" "private" {
  filter {
    name   = "vpc-id"
    values = [var.vpc_id]
  }
}

resource "aws_instance" "my_server" { 
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = var.instance_type
  key_name               = aws_key_pair.deployer.key_name
  vpc_security_group_ids = [aws_security_group.sg_my_server.id]
  subnet_id              = tolist(data.aws_subnets.private.ids)[0]
  user_data              = data.template_file.user_data.rendered

  tags = {
    Name = var.server_name
  }
}

# this code `subnet_id = data.aws_subnet_ids.subnet_ids.ids[0]` resulted in this error
# ╷
# │ Error: Invalid index
# │ 
# │   on ../../100_modules/terraform-aws-apache-example/main.tf line 121, in resource "aws_instance" "my_server":
# │  121:   subnet_id              = data.aws_subnet_ids.subnet_ids.ids[0]
# │ 
# │ Elements of a set are identified only by their value and don't have any separate index or key to select with, so it's only
# │ possible to perform operations across all elements of the set.

# finally, changing to using `tolist()[0]` worked! 