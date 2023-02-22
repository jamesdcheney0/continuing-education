terraform {
  # backend "remote" {
  #   hostname = "app.terraform.io"
  #   organization = "terraform-exploration"

  #   workspaces {
  #     name = "vcs-tf-test"
  #   }
  # }
  ## Tf cloud wasn't working for me & didn't like the credentials I gave it. I didn't  try to seriously fix it though
}

provider "aws" {
  region = "us-east-1"
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