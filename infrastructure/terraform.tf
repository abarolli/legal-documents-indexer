terraform {
    backend "remote" {
        organization = "personal-github-5885"

        workspaces {
            name = "legal-document-indexer"
        }
    }

    required_providers {
      aws = {
        source = "hashicorp/aws"
        version = "~> 4.0"
      }
    }
}

provider "aws" {
    region = "us-east-1"
}