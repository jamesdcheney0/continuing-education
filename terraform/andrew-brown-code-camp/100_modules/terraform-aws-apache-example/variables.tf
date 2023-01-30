variable "vpc_id" {
  type = string
}

variable "my_ip" {
  description = "provide local IP ending with /32"
  type        = string
}

variable "public_key" {
  type = string
}

variable "server_name" {
  type = string
  default = "apache-example-instance"
}

variable "instance_type" {
  type    = string
  default = "t2.micro"
}
