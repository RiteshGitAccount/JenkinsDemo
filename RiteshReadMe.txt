pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building.. 8th July fourth TT time'
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
