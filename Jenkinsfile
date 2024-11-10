pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
              sh '''
                chmod 777 users-creation-and-check.py
                python users-creation-and-check.py
              '''
            }
        }
    }
}
