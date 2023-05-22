# AWS Directory Services
if the password is manually reset in the console, terragrunt wants to terminated the directory and restart. This is [expected behavior](https://github.com/hashicorp/terraform-provider-aws/issues/16745)

terragrunt import aws_directory_service_directory.MicrosoftAD
tried to import and got the following error
╷
│ Error: Resource already managed by Terraform
│ 
│ Terraform is already managing a remote object for
│ aws_directory_service_directory.MicrosoftAD. To import to this address you
│ must first remove the existing object from the state.

removed the directory from state then imported it 
didn't work, have to manually edit state file... 
https://github.com/hashicorp/terraform-provider-aws/issues/16529#issuecomment-762901542 


Doug asked if only changing the password in secrets manager prompts a replace
 