pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                sh '''
                chmod 777 test.py
                python test.py 
                '''
            }
        }
    }
}
