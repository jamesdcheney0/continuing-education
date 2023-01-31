terraform {
  backend "s3" {
    bucket = "324754955544-us-west-1-terraform-backend"
    key    = "terraform.tfstate"
    region = "us-west-1" # has to match the region of the bucket (yes, apparently buckets have regions)
  }
}

provider "aws" {
  region = "us-east-1"
  ## to use unique roles per workspace: 
  # assume_role = "${var.workspace_iam_roles[terraform.workspace]}"
}

module "apache" {
  source        = "jamesdcheney0/apache-example/aws"
  version       = "1.0.0"
  vpc_id        = var.vpc_id
  my_ip         = var.my_ip
  instance_type = var.instance_type
  server_name   = var.server_name
  public_key    = var.public_key
}

output "public_ip" {
  value = module.apache.public_ip
}