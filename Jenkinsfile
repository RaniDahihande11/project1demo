pipeline {
    agent any
    stages {
        stage("Checkout Code") {
            steps {
                git url:'https://github.com/RaniDahihande11/project1demo.git', branch:'main'
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
