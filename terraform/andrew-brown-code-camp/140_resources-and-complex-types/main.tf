terraform{

}

variable "planets" {
    type = list
    default = ["mars","earth","moon"]
}

variable "plans" {
    type = map
    default = {
        "PlanA" = "10 USD",
        "PlanB" = "50 USD",
        "PlanC" = "100 USD"
    }
}

variable "plans_object" {
    type = object({
        PlanName = string
        PlanAmount = number
    })
    default = {
        "PlanName" = "Basic",
        "PlanAmount" = 10
    }
}

variable "random" {
    type = tuple([string,number,bool])
    default = ["hello",22,false]
}