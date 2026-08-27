# team_devops-portfolio

![Azure](https://img.shields.io/badge/Azure-0078D4?style=flat&logo=microsoftazure&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

Ten small, standalone DevOps practice tasks, each demonstrating a distinct discipline — containerisation, cloud CI/CD with security scanning, build automation, distributed build infrastructure, serverless compute, container orchestration, database observability, continuous delivery orchestration, cloud data warehousing, and MLOps.

Tackled in order of simplicity to complexity, with `az_cicd` later extended with integrated security scanning.

---

## Tasks

| # | Task | What it demonstrates |
|---|------|----------------------|
| 1 | [`docker_webserver`](./docker_webserver) | Containerised web server — Docker fundamentals |
| 2 | [`az_cicd`](./az_cicd) | Automated CI/CD on Azure (Pipelines, Container Registry, App Service) with Trivy, Dependabot, and Snyk security scanning |
| 3 | [`java_gradle`](./java_gradle) | Java build automation and dependency management with Gradle |
| 4 | [`jenkins_remoting`](./jenkins_remoting) | Jenkins controller/agent architecture — distributed, isolated build execution |
| 5 | [`az_function_storage`](./az_function_storage) | HTTP-triggered Azure Function (Python, Consumption plan) writing to Blob Storage |
| 6 | [`az_aks_deployment`](./az_aks_deployment) | Containerised workload deployed to a genuine Azure Kubernetes Service cluster |
| 7 | [`data_layer_monitoring`](./data_layer_monitoring) | Redis, MongoDB, and PostgreSQL with real CRUD operations, monitored via DataDog and Docker Autodiscovery |
| 8 | [`octopus_deploy`](./octopus_deploy) | Release promoted through Development, Staging, and Production via Octopus Deploy, to a real SSH-connected target |
| 9 | [`data_warehousing`](./data_warehousing) | Azure Synapse serverless SQL pool running real analytical queries against data lake files |
| 10 | [`mlops_ai_pipeline`](./mlops_ai_pipeline) | Trained classifier, versioned, served live, automatically retrained and redeployed via CI/CD |

---

## Structure

Every task folder follows the same layout:

- **What was built** — a plain account of the components and architecture
- **Commands used** — complete, real commands
- **Verification Evidence** — screenshots proving it worked
- **Troubleshooting notes** — genuine issues hit and how they were resolved
- **Teardown** — confirmation that infrastructure was cleanly removed

---

*Every cloud resource in this repository was created, verified, documented, and deleted.*
