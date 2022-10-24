pipeline {
    agent { docker { image 'mpc31/simple_server:latest' } }
    stages {
        stage('build') {
            steps {
                sh 'echo $(hello-world)'
            }
        }
    }
}