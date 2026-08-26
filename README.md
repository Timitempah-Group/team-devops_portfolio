# team_devops-portfolio

Six small, standalone DevOps practice tasks, each demonstrating a distinct discipline:
containerisation, cloud CI/CD with security scanning, build automation, distributed
build infrastructure, serverless compute, and container orchestration. Tackled in
order of simplicity to complexity, with az_cicd later extended with integrated
security scanning.

## Tasks

1. **docker_webserver** — containerised web server, Docker fundamentals
2. **az_cicd** — automated CI/CD pipeline on Azure (Pipelines, Container Registry, App Service, with Trivy, Dependabot, and Snyk security scanning)
3. **java_gradle** — Java build automation and dependency management with Gradle
4. **jenkins_remoting** — Jenkins controller/agent architecture, distributed and isolated build execution
5. **az_function_storage** — HTTP-triggered Azure Function (Python, Consumption plan) writing to Blob Storage
6. **az_aks_deployment** — containerised workload deployed to a genuine Azure Kubernetes Service cluster

Each task folder contains its own README with what was built, real issues hit and how they
were resolved, verification evidence, and teardown confirmation where infrastructure was involved.
