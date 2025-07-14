#!/bin/bash

# 🚀 Local Deployment Script for Calculator App
# This script deploys the latest CircleCI-built image to your local minikube

set -e

echo "🧮 Calculator App - Local Deployment"
echo "=================================="

# Check if minikube is running
if ! minikube status > /dev/null 2>&1; then
    echo "❌ Minikube is not running. Please start it first:"
    echo "   minikube start"
    exit 1
fi

# Get the latest commit SHA (or use provided argument)
if [ "$1" != "" ]; then
    COMMIT_SHA="$1"
    echo "📝 Using provided commit SHA: $COMMIT_SHA"
else
    COMMIT_SHA=$(git rev-parse HEAD)
    echo "📝 Using latest commit SHA: $COMMIT_SHA"
fi

IMAGE_NAME="minjun6251/calculator-app:$COMMIT_SHA"
echo "🐳 Docker image: $IMAGE_NAME"

# Check if the image exists on Docker Hub
echo "🔍 Checking if image exists on Docker Hub..."
if ! docker manifest inspect "$IMAGE_NAME" > /dev/null 2>&1; then
    echo "❌ Image $IMAGE_NAME not found on Docker Hub"
    echo "💡 Make sure CircleCI has built and pushed this commit"
    echo "💡 Or specify a different commit SHA: ./deploy-local.sh <commit-sha>"
    exit 1
fi

echo "✅ Image found on Docker Hub"

# Update deployment with new image
echo "📝 Updating Kubernetes deployment..."
sed "s|image: minjun6251/calculator-app:.*|image: $IMAGE_NAME|g" k8s/deployment.yaml > /tmp/deployment-updated.yaml

# Deploy to minikube
echo "🚀 Deploying to local minikube..."
kubectl apply -f k8s/service.yaml
kubectl apply -f /tmp/deployment-updated.yaml

# Wait for deployment
echo "⏳ Waiting for deployment to be ready..."
kubectl rollout status deployment/calculator-app --timeout=300s

# Show deployment status
echo ""
echo "📊 Deployment Status:"
kubectl get deployments,pods,services -l app=calculator-app

# Get service URL
echo ""
echo "🔗 Getting service URL..."
SERVICE_URL=$(minikube service calculator-app-service --url)
echo "✅ Your app is accessible at: $SERVICE_URL"

# Show useful commands
echo ""
echo "🛠️  Useful Commands:"
echo "   View logs:    kubectl logs -f deployment/calculator-app"
echo "   Get pods:     kubectl get pods -l app=calculator-app"
echo "   Port forward: kubectl port-forward service/calculator-app-service 8080:80"
echo "   Open app:     minikube service calculator-app-service"
echo "   Delete app:   kubectl delete -f k8s/"

# Clean up temp file
rm -f /tmp/deployment-updated.yaml

echo ""
echo "🎉 Deployment complete! Your Calculator app is running in minikube." 