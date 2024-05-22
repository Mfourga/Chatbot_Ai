pipeline {
    agent any

    environment {
        PATH = "/var/jenkins_home/workspace/Chatbot_Ai_Basket:/snap/bin:$PATH"
        KUBECONFIG = "/var/jenkins_home/.kube/config"
    }

    stages {
        stage('Create Kubernetes configuration file') {
            steps {
                script {
                    sh 'mkdir -p /var/jenkins_home/.kube/'
                    sh 'touch /var/jenkins_home/.kube/config'
                }
            }
        }

        stage('Install kubectl') {
            steps {
                script {
                    // Download kubectl
                    sh 'curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.20.5/bin/linux/amd64/kubectl'
                    // Make kubectl executable
                    sh 'chmod +x ./kubectl'
                    // Move kubectl to a location where Jenkins can execute it
                    sh 'mv kubectl /var/jenkins_home/bin/'
                }
            }
        }

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Mfourga/chatbot_Ai'
            }
        }

        stage('Deploy on Minikube') {
            steps {
                script {
                    // Apply configuration using the full path of the kubeconfig file
                    sh '/var/jenkins_home/bin/kubectl apply -f manifeste_k8s/deploiement_rasa.yaml --kubeconfig /var/jenkins_home/.kube/config --server=https://192.168.39.117:8443 --insecure-skip-tls-verify=true'
                }
            }
        }

        stage('Copy configuration files') {
            steps {
                script {
                    sh 'cp -r data/* .'
                    sh 'cp domain.yml .'
                    sh 'cp credentials.yml .'
                    sh 'cp rules.yml .'
                    sh 'cp stories.yml .'
                    sh 'cp endpoints.yml .'
                }
            }
        }

        stage('List pods') {
            steps {
                script {
                    sh '/var/jenkins_home/bin/kubectl get pods -n stage --kubeconfig /var/jenkins_home/.kube/config'
                }
            }
        }
    }
}
