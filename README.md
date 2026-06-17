AZURE APP SERVICE DEPLOYMENT - SUMMARY
========================================

Runtime Stack
-------------
Python 3.12, running on Linux. The application is a lightweight Flask web app
with two routes: a homepage that reads a configurable message from
environment variables, and a /health endpoint returning a JSON status check.
Python/Flask was chosen for its minimal setup overhead, making it easy to
demonstrate App Service's configuration and deployment features without
unnecessary application complexity getting in the way.

Pricing Tier (App Service Plan)
--------------------------------
F1 (Free) tier was selected. This tier provides 1 GB of memory and 60 CPU
minutes per day, which is more than sufficient for a small demonstration app
with light, intermittent traffic. It carries no cost, making it ideal for a
learning project. The trade-off is that F1 does not support some advanced
features such as deployment slots, custom domains with SSL, or autoscaling -
these require Standard tier or higher.

Deployment Method
------------------
GitHub integration with continuous deployment via GitHub Actions. The
application code was pushed to a GitHub repository, then the Azure Web App
was connected to that repository directly through the Deployment Center.
Azure automatically generated a GitHub Actions workflow file in the
repository that builds and redeploys the app on every push to the main
branch. This was chosen over manual/direct upload specifically to
demonstrate an automated, DevOps-aligned deployment pipeline rather than a
one-off manual transfer of files.

Live URL
--------
https://chinonso-flask-demo-b2hrcmh2d4e0epfp.westeurope-01.azurewebsites.net
