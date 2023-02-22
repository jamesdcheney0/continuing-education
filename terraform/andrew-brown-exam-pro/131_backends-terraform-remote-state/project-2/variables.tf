variable "my_ip" {
  description = "provide local IP ending with /32"
  type        = string
}

variable "public_key" {
  type = string
}

variable "instance_type" {
  type    = string
  default = "t2.nano"
}

variable "server_name" {
  type = string
}