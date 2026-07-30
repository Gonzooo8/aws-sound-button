variable "project_name" {
  description = "Project name used for resource naming"
  type        = string
  default     = "aws-sound-button"
}

variable "ec2_ami_id" {
  description = "AMI ID for the EC2 web server"
  type        = string
  default     = "ami-01b907a1d2977284b"
}