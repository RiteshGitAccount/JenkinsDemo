pipeline {
    agent anyone

    stages {
        stage('Build') {    
            steps {    
                echo 'Building.. 8th March 2023 Sucessfully          '
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
