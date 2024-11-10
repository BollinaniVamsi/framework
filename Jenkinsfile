pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                sh '''
                chmod 777 test.py
                python test.py | tee pdb_output.log
                echo "printing the log file output"
                cat pdb_output.log
                '''
            }
        }
    }
}
