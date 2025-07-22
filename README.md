# Create the helm chart
`helm create python-api`

# Install the release
`helm install python-api-app`

# Upgrade after templating
`helm upgrade python-api-app python-api/ --values python-api/values.yaml`
