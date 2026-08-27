# team_devops-portfolio

Ten small, standalone DevOps practice tasks, each demonstrating a distinct
discipline: containerisation, cloud CI/CD with security scanning, build
automation, distributed build infrastructure, serverless compute, container
orchestration, database observability, continuous delivery orchestration,
cloud data warehousing, and MLOps. Tackled in order of simplicity to
complexity, with az_cicd later extended with integrated security scanning.

## Tasks

1. **docker_webserver** — containerised web server, Docker fundamentals
2. **az_cicd** — automated CI/CD pipeline on Azure (Pipelines, Container Registry, App Service, with Trivy, Dependabot, and Snyk security scanning)
3. **java_gradle** — Java build automation and dependency management with Gradle
4. **jenkins_remoting** — Jenkins controller/agent architecture, distributed and isolated build execution
5. **az_function_storage** — HTTP-triggered Azure Function (Python, Consumption plan) writing to Blob Storage
6. **az_aks_deployment** — containerised workload deployed to a genuine Azure Kubernetes Service cluster
7. **data_layer_monitoring** — Redis, MongoDB, and PostgreSQL containers with real CRUD operations, monitored via the DataDog Agent using Docker Autodiscovery
8. **octopus_deploy** — a release promoted through Development, Staging, and Production environments using Octopus Deploy, targeting a real SSH-connected Linux server
9. **data_warehousing** — Azure Synapse Analytics serverless SQL pool running real analytical queries directly against data lake files
10. **mlops_ai_pipeline** — a trained classifier registered with versioning, served behind a live endpoint, and automatically retrained and redeployed via a CI/CD pipeline

Each task folder contains its own README with what was built, real issues hit
and how they were resolved, verification evidence, and teardown confirmation
where infrastructure was involved.
