pipeline {
    agent any

    environment {
        IMAGE_NAME = "myimage"
        CONTAINER_NAME = "mycontainer"
        PORT = "8501"
    }

    stages {
        stage("Checkout Code") {
            steps {
                echo "Checking out code from GitHub..."
                git url: 'https://github.com/RaniDahihande11/project1demo.git', branch: 'main'
            }
        }

        stage("Build Docker Image") {
            steps {
                echo "Building Docker image..."
                bat "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage("Remove Existing Container") {
            steps {
                echo "Removing old container if exists..."
                bat """
                    docker ps -a -q --filter "name=${CONTAINER_NAME}" | findstr . && docker rm -f ${CONTAINER_NAME} || echo "No existing container"
                """
            }
        }

        stage("Run Docker Container") {
            steps {
                echo "Running new container..."
                bat "docker run -d -p ${PORT}:${PORT} --name ${CONTAINER_NAME} ${IMAGE_NAME}"
            }
        }
    }

}