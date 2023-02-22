Terraform module to provision an EC2 instance running Apache

Not intended for public use. Showcase of creating public module for terraform registry

```hcl
terraform {

}

provider "aws" {
  region = "us-east-1"
}

module "aws-apache" {
  source = "./terraform-aws-apache-example"
  server_name = "apache-example-instance"
  instance_type = "t2.micro"
  public_key = "<cat .pub ssh key>"
  my_ip = "<my.public.ip>/32"
  vpc_id = "vpc-xxxxxx"
}

output "public_ip" {
    value = module.aws-apache.public_ip
}
```

# Notes
- To initialize this as a module, cd INTO the `terraform-aws-apache-example` directory THEN init the git repo

- Terraform registry requires tags for modules. Provide tags by being in the git directory, and `git tag <major-version>.<minor-version>.<patch>` then `git puss --tags`. To initialize this directory, I ran `git tag 1.0.0 && git push --tags`