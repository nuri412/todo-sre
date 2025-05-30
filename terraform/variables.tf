variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-west-2"
}

variable "environment" {
  description = "Environment name (e.g., prod, staging, dev)"
  type        = string
  default     = "dev"
}

variable "vpc_cidr" {
  description = "CIDR block for VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "availability_zones" {
  description = "List of availability zones"
  type        = list(string)
  default     = ["us-west-2a", "us-west-2b"]
}

variable "container_image" {
  description = "Docker image for the application"
  type        = string
}

variable "desired_count" {
  description = "Desired number of application containers"
  type        = number
  default     = 2
}

variable "database_name" {
  description = "Name of the RDS database"
  type        = string
  default     = "concertdb"
}

variable "database_username" {
  description = "Master username for RDS"
  type        = string
  sensitive   = true
}

variable "database_password" {
  description = "Master password for RDS"
  type        = string
  sensitive   = true
} 