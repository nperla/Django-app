#!/bin/bash

# Podman Installation Script for Ubuntu

# Update package list
sudo apt update

# Install Podman
sudo apt install -y podman

# Verify Podman installation
podman --version

# Set up Docker alias for Podman
echo "alias docker=podman" >> ~/.bashrc
source ~/.bashrc

echo "Podman installation completed successfully. Use 'docker' commands to interact with Podman."
