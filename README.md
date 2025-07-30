# Create the helm chart
`helm create python-api`

# Install the release
`helm install python-app`

# Upgrade after templating
`helm upgrade python-app python-api/ --values python-api/values.yaml`

# Create dev/prod namespaces
`kubectl create ns dev`
`kubectl create ns prod`

# Access via minikube
```
servicename=$(kubectl get svc -l "app=python-api" -o jsonpath="{.items[0].metadata.name}")
minikube service $servicename
```
# Install apps in dev or prod environment
`helm install python-app-dev python-api/ --values python-api/values.yaml -f python-api/values-dev.yaml -n dev`
`helm install python-app-prod python-api/ --values python-api/values.yaml -f python-api/values-prod.yaml -n prod`