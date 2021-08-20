provider "aws" {
  region = var.aws_region
}


# Centralizar o arquivo de controle de estado do terraform
terraform {
  backend "s3" {
    bucket = "datalake-smedina-4323-igti-edc"
    key    = "infrastructure/state/mod1/terraform.tfstate"
    region = "us-east-2"
  }
}