terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "6.20.0"
    }
  }
}

provider "aws" {
  region = "eu-central-2" # zurich
}

resource "aws_s3_bucket" "example" {
  # set a unique bucket name
  bucket = "this-needs-to-be-unique"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}