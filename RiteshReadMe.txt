pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building.. 9th July Trigger'
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
