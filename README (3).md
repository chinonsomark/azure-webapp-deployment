# Azure App Service Web App Deployment

A Python (Flask) web application deployed to Azure App Service using GitHub-based continuous deployment.

## Live Application

**URL:** https://chinonso-flask-demo-b2hrcmh2d4e0epfp.westeurope-01.azurewebsites.net

The app is reachable over HTTPS (Azure App Service provides this by default on the `azurewebsites.net` domain). Visiting it displays a message pulled from App Service environment variables, along with a `/health` endpoint for a basic JSON health check.

## What This Project Demonstrates

- Provisioning an Azure App Service Plan and Web App (PaaS hosting)
- Deploying application code via GitHub integration with continuous deployment (GitHub Actions)
- Managing app configuration through environment variables/Application Settings, without changing code
- Verifying public accessibility over HTTPS
- Reviewing basic monitoring metrics
- Understanding deployment slots and their tier requirements

## Environment

- **Runtime Stack:** Python 3.12
- **Operating System:** Linux
- **App Service Plan / Pricing Tier:** F1 (Free)
- **Region:** West Europe
- **Deployment Method:** GitHub integration (GitHub Actions, continuous deployment)
- **Source Repository:** https://github.com/chinonsomark/azure-webapp-deployment

## Task 1 & 2: App Service Plan and Web App Provisioning

Created via the "Web App" creation wizard in the Azure Portal, which provisions both the App Service Plan (compute/pricing tier) and the Web App (runtime/hosting) in a single flow.

See: `screenshots/overview-page.png`

## Task 3 & 5: Deployment and Continuous Deployment

The app code (`app.py`, `requirements.txt`) was pushed to a GitHub repository, then connected to the Web App via the Deployment Center with GitHub Actions enabled. Azure auto-generated a workflow file in the repo that rebuilds and redeploys the app automatically on every push to `main`.

## Task 4: Environment Configuration

Two application settings were added under Environment Variables / Configuration:
- `APP_MESSAGE` — a custom message displayed on the homepage
- `APP_ENVIRONMENT` — set to `Production`

These are read by the Flask app at runtime via `os.environ.get()`, demonstrating configuration without code changes.

See: `screenshots/configuration-blade.png`

## Task 6: Verifying Accessibility

Confirmed the app loads correctly over HTTPS at the public URL above, with the configured message and environment value both displaying correctly.

See: `screenshots/app-live-configured.png`

## Task 7: Monitoring

Reviewed the Metrics blade under Monitoring, charting CPU Time over the last 24 hours to confirm telemetry is being collected for the app.

See: `screenshots/monitoring-metrics.png`

## Task 8: Deployment Slots

Reviewed the Deployment Slots blade. On the Free (F1) tier, slots are not available — Azure displays an upgrade prompt explaining that slots require Standard tier or higher, and that they allow content/configuration to be swapped between a staging slot and production with zero downtime.

See: `screenshots/deployment-slots.png`

## Troubleshooting Notes

- **First GitHub Actions deployment failed** with `Login failed... process '/usr/bin/az' failed with exit code 1`. This was caused by the OIDC-based federated credentials Azure auto-configures sometimes needing a few minutes to fully propagate. Resolved by simply re-running the failed workflow from the GitHub Actions tab.
- **App Service Plan defaulted to Basic (B1) instead of Free (F1)** during initial creation. Fixed afterward via the App Service Plan blade → Scale up → Dev/Test → F1.

## Summary

This project reinforced the core differences between PaaS and IaaS — rather than managing a VM, OS, and runtime manually, App Service abstracts away the infrastructure entirely, letting deployment focus on code and configuration. Connecting GitHub for continuous deployment also demonstrated a practical DevOps workflow: pushing code triggers an automatic build and redeploy with no manual upload step required.
