terraform {
  required_version = "~> 1.15.8"

  backend "s3" {
    bucket       = "aws-sound-button-tfstate-392789867247"
    key          = "aws-sound-button/terraform.tfstate"
    region       = "ap-northeast-1"
    use_lockfile = true
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}