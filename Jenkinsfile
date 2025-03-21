pipeline {
    agent { label "vinod" }

    stages {
        stage('Clone Repo') {
            steps {
                git(url: 'https://github.com/knightabir/flask-system-monitor.git', branch: 'main')
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my-flask-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                // Stop and remove existing container if it exists
                sh '''
                docker ps -a | grep flask-container && docker stop flask-container && docker rm flask-container || true
                docker run -d -p 5000:5000 --name flask-container my-flask-app
                '''
            }
        }
    }
}
