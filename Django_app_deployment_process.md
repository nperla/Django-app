## Activating virtual environment:
sudo apt install python3-virtualenv
virtualenv venv
source venv/bin/activate

To set up Podman as a replacement for Docker using an alias, you can add the alias command to either your current shell session or, for a more permanent setup, to your shell configuration file (such as .bashrc, .zshrc, or .profile). 
This way, whenever you type docker, it will invoke Podman instead.
1: nano ~/.bashrc
-> Add the following line at the end of the file:
2: alias docker=podman
-> After updating the configuration file, you’ll need to reload it to apply the changes. Run:
3: source ~/.bashrc
-> Test the alias by typing:
4: docker --version

## Azcli Install with one command:
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

## Django application project:
https://www.civo.com/learn/build-deploy-restfulapi-fastapi-kubernetes

## ACR Access:
az acr login --name akstestxksregistry --expose-token
podman login testxksregistry.azurecr.io -u 00000000-0000-0000-0000-000000000000 -p <access_token>

## Docker image tagging:
podman tag localhost/sample-django-app:0.0.1 testxksregistry.azurecr.io/sample-django-app:0.0.1
podman push testxksregistry.azurecr.io/sample-django-app:0.0.1


## aks access:
az aks list -o table
az get-credentails --resource-group <rg-group> --name <cluster-name> 

## Grafana Installation:
sudo apt-get install -y apt-transport-https software-properties-common wget
sudo mkdir -p /etc/apt/keyrings/
wget -q -O - https://apt.grafana.com/gpg.key | gpg --dearmor | sudo tee /etc/apt/keyrings/grafana.gpg > /dev/null
echo "deb [signed-by=/etc/apt/keyrings/grafana.gpg] https://apt.grafana.com stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
sudo apt-get update
sudo apt-get install grafana
