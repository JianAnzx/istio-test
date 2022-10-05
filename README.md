# istio-test

This repo is to test how istio is working in GKE.

## Install Istio in GKE

The gcloud command `gcloud beta container clusters update CLUSTER_NAME \
    --update-addons=Istio=ENABLED --istio-config=auth=MTLS_PERMISSIVE` would not install istio egress. So the istio official method `istioctl install --set profile=demo -y` should be more easy.
    
## This repo doesn't have Github action enabled. So the conatienr image is built locally and pushed to docker hub.    

## TODO
1. Change GKE LB from TCP type to HTTPS
`istioctl install --set profile=demo -y` install ingress gateway with a TCP load balancer. Need to change the type to HTTPS. Then can use GCP HTTPS LB's TLS termiation feature to have GCP manage TLS certs

2. Enable Github action for CI/CD. Then create review envs

3. More tests about istio

