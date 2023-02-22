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

variable "instance_type" {
  type    = string
  default = "t2.nano"
}

variable "server_name" {
  type = string
}

# variable "workspace_iam_roles" {
#   default = { # this is a map
#     staging = "if:using:multiple:accounts::staging-iam-username-here"
#     prod = "if:using:multiple:accounts::prod-iam-username-here"
#   }
# }