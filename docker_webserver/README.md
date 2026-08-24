# Docker Web Server

Containerised an nginx web server serving a custom static page, with a working
HEALTHCHECK, as practice for Docker fundamentals: image builds, the container
lifecycle, and basic health monitoring.

## What was built

- A Dockerfile based on `nginx:alpine`, serving a custom `index.html`
- A HEALTHCHECK instruction that polls the page every 30 seconds and reports
  container health status directly in `docker ps`

## Commands used

```
docker build -t devops-practice-webserver .
docker run -d -p 8080:80 --name practice-webserver devops-practice-webserver
```

## Verification

- `curl http://localhost:8080` returned the expected page content
- Browser confirmed the page loads at `http://localhost:8080` (see screenshots/01-webserver-running.png)
- `docker ps` showed the container `Up` and, after adding a HEALTHCHECK,
  `(healthy)` (see screenshots/02-container-healthy.png) — confirmed further with
  `docker inspect --format='{{json .State.Health}}' practice-webserver`,
  which logged four consecutive successful checks (exit code 0) at
  30-second intervals

## Lifecycle practice

- `docker logs` — viewed container output
- `docker exec -it practice-webserver sh` — shelled into the running
  container and confirmed the served file matched what was built
- `docker inspect` — reviewed full container configuration
- `docker stop` / `docker start` — confirmed the container stops cleanly
  (exit code 0) and restarts without needing a rebuild

## Notes

Runs entirely locally via Docker Desktop — no cloud account or spend involved.

## Teardown

```
docker stop practice-webserver
docker rm practice-webserver
docker rmi devops-practice-webserver
```
