terraform {}

module "aws_instance" {
  source = "./aws_instance"
  instance_type = "t2.micro"
}

output "public_ip" {
  value = module.aws_instance.public_ip #directly be referencing the output in ./aws_instance/main.tf
}