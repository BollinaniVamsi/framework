pipeline {
    agent any
       parameters {
        string(name: 'USER_INPUT', defaultValue: 'default_value', description: 'Enter a value')
    }

    stages {
        stage('Hello') {
            steps {
              script {
                def input_value = params.USER_INPUT
                echo "Received input value: ${input_value}"
                sh '''
                chmod 777 test.py
                python test.py
                '''
              }
            }
        }
    }
}
