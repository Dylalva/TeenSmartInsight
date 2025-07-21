# Infrastructure Documentation

## Infrastructure Overview

TeenSmartInsight is deployed on AWS using a combination of Terraform for infrastructure provisioning and Ansible for configuration management. The application is containerized using Docker for consistent deployment across environments.

## AWS Architecture

The application is deployed on AWS with the following components:

- **EC2 Instance**: t2.micro instance running Ubuntu 22.04 LTS
- **Security Group**: Configured to allow SSH, HTTP, HTTPS, and application traffic
- **Key Pair**: Used for secure SSH access to the instance

## Infrastructure as Code (IaC)

### Terraform Configuration

The infrastructure is defined using Terraform in the `infrastructure/main.tf` file:

```hcl
provider "aws" {
  region = "us-east-2"
}

resource "aws_key_pair" "deployer" {
  key_name   = "deployer1"
  public_key = file("~/.ssh/id_rsa_flaskapp.pub")
}

resource "aws_security_group" "web_sg" {
  name        = "flask-teensmart-sg"
  description = "SSH, HTTP, HTTPS and Docker"

  # Security group rules for SSH, HTTP, HTTPS, and application port
  # ...
}

resource "aws_instance" "web" {
  ami                    = "ami-0d1b5a8c13042c939" # Ubuntu 22.04 LTS
  instance_type          = "t2.micro"
  key_name               = aws_key_pair.deployer.key_name
  vpc_security_group_ids = [aws_security_group.web_sg.id]
}
```

### Deployment Automation

The application deployment is automated using Ansible in the `infrastructure/deploy-with-docker.yml` file:

1. **Server Preparation**:
   - Update package repositories
   - Install dependencies (Docker, Nginx, Certbot)

2. **Docker Deployment**:
   - Pull the application Docker image
   - Run the container with appropriate configuration

3. **HTTPS Configuration**:
   - Set up Nginx as a reverse proxy
   - Obtain and configure SSL certificates using Certbot
   - Configure automatic certificate renewal

## CI/CD Pipeline

The project includes a GitHub Actions workflow for continuous integration and deployment:

```yaml
# .github/workflows/deploy.yml
name: Deploy to AWS
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Build and push Docker image
        # ...
      - name: Deploy to AWS
        # ...
```

## Security Considerations

The infrastructure includes several security measures:

- **HTTPS**: All traffic is encrypted using SSL/TLS
- **Secure Headers**: Nginx is configured with secure headers
- **Firewall**: Security groups restrict access to necessary ports only
- **Automatic Updates**: Security patches are applied automatically

## Monitoring and Logging

The application includes basic monitoring and logging:

- **Application Logs**: Stored in the Docker container
- **Nginx Logs**: Access and error logs for the web server
- **AWS CloudWatch**: Can be configured for additional monitoring

## Scaling Considerations

The current infrastructure is designed for a small-scale deployment. For scaling:

1. **Horizontal Scaling**: Add more EC2 instances behind a load balancer
2. **Database Scaling**: Move from CSV storage to a managed database service
3. **Container Orchestration**: Consider using ECS or Kubernetes for container management

## References

- [AWS Documentation](https://docs.aws.amazon.com/)
- [Terraform Documentation](https://www.terraform.io/docs/)
- [Ansible Documentation](https://docs.ansible.com/)
- [Nginx Documentation](https://nginx.org/en/docs/)
- [Let's Encrypt Documentation](https://letsencrypt.org/docs/)