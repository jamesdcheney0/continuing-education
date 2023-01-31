data "terraform_remote_state" "vpc" {
    backend = "local"
    config = {
        path = "../project-1/terraform.tfstate"
    }
}

provider "aws" {
    region = "us-west-2"
}

module "apache" {
  source        = "jamesdcheney0/apache-example/aws"
  version       = "1.0.0"
  vpc_id        = data.terraform_remote_state.vpc.outputs.vpc_id
  my_ip         = var.my_ip
  instance_type = var.instance_type
  server_name   = var.server_name
  public_key    = var.public_key
}

output "public_ip" {
  value = module.apache.public_ip
}

# Note: this won't work unless project 1 actually has `terraform apply` performed
# current location: 8:58:22: https://youtu.be/V4waklkBC38?t=32302 