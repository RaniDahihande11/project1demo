pipeline{
    agent any
    
    stages{
        stage('Checkout Code'){
            steps{
                git url:'https://github.com/RaniDahihande11/project1demo.git', branch:'main'

            }
        }
        stage('Build Image'){
            steps{
                bat 'docker build -t myimage .'
            }
        }
        stage('Create Container'){
            steps{
                bat 'docker run -d -p 8501:8502 myimage'
            }
        }

    }
}