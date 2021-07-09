pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building.. 9th July 123'
            }
            
        }
        stage('Deploy') {
            steps {
                echo 'Deploying.......'
            }
            
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
            
        }
        stage('Release') {
            steps {
                echo 'Releasing...'
            }
            
        }
       
    }
}
