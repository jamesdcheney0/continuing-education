terraform {

}

variable "str" {
    type = string
    default = "hello, world" 
}

## outputs in TF console
# split(",",var.str)
# tolist([
#   "hello",
#   " world",
# ])

# replace(var.str,"world","barsoon")
# "hello, barsoon"

# bcrypt(var.str)
# "$2a$10$kstjIr4Q6p6uY8M43VSzVejXgMcLOaqjbdUc9BRu.3E28.Wtcj4n."

variable "items" {
    type = list
    default = [null,null,"","last"]
}

variable "stuff" {
    type = map
    default = {
        "hello" = "world"
        "goodbye" = "moon"
    }
}