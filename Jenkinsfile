pipeline {
    agent any 
    environment {
    DOCKERHUB_CREDENTIALS = credentials('docker-hub-mpc31')
    }
    stages {
        stage('Build docker image') {
            steps {  
                sh 'sudo docker build . -t mpc31/simple_server:latest .'
            }
        }
        stage('Run docker image') {
            steps {  
                sh 'sudo docker run -p 8000:8000 mpc31/simple_server:latest .'
            }
        }
        stage('login to dockerhub') {
            steps{
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('push image') {
            steps{
                sh 'sudo docker push mpc31/simple_server:latest'
            }
        }
}
post {
        always {
            sh 'sudo docker logout'
        }
    }
}
