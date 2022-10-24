#!groovy
pipeline { 
    agent any 
  stages { 
    stage('Docker Pull') { 
        agent { 
        docker { 
            image 'mpc31/simple_server:latest'
        }
      }
    }
    stage('Docker Build') { 
	agent any 
      steps { 
	sh 'docker build -t mpc31/simple_server:latest'
      }
    }
    stage('Docker Run'){ 
	agent any 
      steps{ 
	sh 'docker run -d -p 8000:8000 mpc31/simple_server:latest'
      }
    }
  }
}
