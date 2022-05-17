pipeline {
    agent {
        label 'jenkins-node-intern'
    }
    stages {
        stage('Build docker image') {
            steps {
                sh 'cd ..'
                sh 'git clone https://gitlab.tkhtechnology.com/CCT_114_DEVOPS_INTERNAL_PROJECT/backend'
                sh 'cd backend'
                sh 'docker build . -t backend'
            }
        }
        stage('Build docker image') {
            steps {
                sh 'docker build -t internal_project_frontend:${BUILD_NUMBER} -t internal_project_frontend:latest .'
            }
        }
        stage('Push docker image to nexus') {
            steps {
                withDockerRegistry(credentialsId: 'nexus_admin', url: 'https://nexus.tkhtechnology.com/'){
                    sh "docker tag internal_project_frontend nexus.tkhtechnology.com/interal_project/frontend:${BUILD_NUMBER}"
                    sh "docker tag internal_project_frontend nexus.tkhtechnology.com/interal_project/frontend:latest"
                    sh "docker push nexus.tkhtechnology.com/interal_project/frontend:${BUILD_NUMBER}"
                    sh "docker push nexus.tkhtechnology.com/interal_project/frontend:latest"
                }
            }
        }
    }
}
