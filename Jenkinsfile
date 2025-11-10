pipeline {
    agent any
    stages {
        stage("checkout Code") {
            steps {
                git url:'https://github.com/RaniDahihande11/project1demo.git', branch:'main'
            }
        }
        stage("Cleanup Stage") {
steps {
                bat '''
                for /f %%i in ('docker ps -aq') do docker rm -f %%i
                '''
            }
        }
        stage("Build Docker image") {
            steps {
                bat 'docker build -t myimage .'
            }
        }
        stage("Create Container") {
            steps {
                bat 'docker run -d -p 8501:8501 myimage'
            }
        }
    }
}
