data "amazon-ami" "ubuntu" {
    filters = {
        virtualization-type = "hvm"
        name = "ubuntu/images/*ubuntu-xenial-16.04-amd64-server-*"
        root-device-type = "ebs"
    }
    owners = ["099720109477"] #is this the us-east-1 ubuntu account? CLI initially errored with the AMI return, saying image ID doesn't exist, when region was us-west-2 on line 21
    most_recent = true
}
# needed to be signed in with AWS vault before this would pull anything useful 

locals {
    app_name = "httpd"
    source_ami_id = data.amazon-ami.ubuntu.id
    source_ami_name = data.amazon-ami.ubuntu.name
}

source "amazon-ebs" "httpd" {
    ami_name            = "my-server-${local.app_name}-${local.source_ami_name}"
    instance_type       = "t2.micro"
    region              = "us-east-1"
    source_ami          = "${local.source_ami_id}"
    ssh_username        = "ec2-user" # packer wasn't able to SSH into the instance 
    tags = {
        Name = "My-server-${local.app_name}"
    }
}

build { 
    sources = ["source.amazon-ebs.httpd"]

    provisioner "shell" {
        inline = [
            "sudo yum install -y httpd",
            "sudo systemctl start httpd",
            "sudo systemctl enable httpd"
        ]
    }
}

# spins up an ec2 instance to build the image, then kills it immediately after 