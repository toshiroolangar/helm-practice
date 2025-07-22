# Create the helm chart
`helm create python-api`

# Install the release
`helm install python-api-app`

# Upgrade after templating
`helm upgrade python-api-app python-api/ --values python-api/values.yaml`

# Access via minikube
```
servicename=$(kubectl get svc -l "app=python-api" -o jsonpath="{.items[0].metadata.name}")
minikube service $servicename
```