# README

## Install on macOS

`brew update; brew install opentofu`


## Prepare .gitignore

Ignore AWS access keys and terraform state.

```gitignore
/terraform_accessKeys.csv
.terraform.lock.hcl
*.tfstate*
.terraform
```

## Create Credentials

1. Add a new non-root user in the ui
   1. create usergroup
   2. add necessary permissions to group
   3. IAM -> Users -> Create User
   4. Add user to group
2. Create access key and download csv file
3. Store key in project folder
4. **Make sure the key file is ignored by git**
5. Set access keys environment variables
```bash
export AWS_ACCESS_KEY_ID="<from csv file"
export AWS_SECRET_ACCESS_KEY="<from csv file>"
```

## Open Tofu

1. Initialize open tofu: `tofu init`
2. Plan: `tofu plan`
3. Create Resources: `tofu apply`
4. Check in UI if resource has been created
5. When done, remove everything using `terraform destroy` to avoid costs

## Sources

- OpenTofu installation: https://opentofu.org/docs/intro/install/
- Regions: https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints
- AWS Terraform Provider: https://registry.terraform.io/providers/hashicorp/aws/latest
- AWS Terraform Provider docs: https://registry.terraform.io/providers/hashicorp/aws/latest/docs