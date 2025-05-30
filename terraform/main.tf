terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# VPC and Networking
module "vpc" {
  source = "./modules/vpc"
  
  vpc_cidr           = var.vpc_cidr
  availability_zones = var.availability_zones
  environment        = var.environment
}

# Application Load Balancer
module "alb" {
  source = "./modules/alb"
  
  vpc_id             = module.vpc.vpc_id
  public_subnets     = module.vpc.public_subnet_ids
  environment        = var.environment
  security_groups    = [module.security.alb_security_group_id]
}

# ECS Cluster and Service
module "ecs" {
  source = "./modules/ecs"
  
  vpc_id                = module.vpc.vpc_id
  private_subnets       = module.vpc.private_subnet_ids
  environment           = var.environment
  alb_target_group_arn  = module.alb.target_group_arn
  security_groups       = [module.security.ecs_security_group_id]
  container_image       = var.container_image
  desired_count         = var.desired_count
}

# Security Groups
module "security" {
  source = "./modules/security"
  
  vpc_id      = module.vpc.vpc_id
  environment = var.environment
}

# RDS Database
module "rds" {
  source = "./modules/rds"
  
  vpc_id            = module.vpc.vpc_id
  private_subnets   = module.vpc.private_subnet_ids
  environment       = var.environment
  security_groups   = [module.security.rds_security_group_id]
  database_name     = var.database_name
  master_username   = var.database_username
  master_password   = var.database_password
} 