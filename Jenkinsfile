pipeline {
    agent any

    // Removed empty environment block

    stages {
        stage('Checkout') {
            steps {
                // Get the code from the version control system.
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    // Setup Python environment
                    sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    '''
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install necessary dependencies
                    sh '''
                    . venv/bin/activate
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run pytest
                    sh '''
                    . venv/bin/activate
                    pytest
                    '''
                }
            }
        }
    }
    
    post {
        always {
            // For demonstration, added a simple echo statement
            echo 'This will always run'
        }
        success {
            // Actions to take if stage completes successfully
            echo 'The pipeline was successful!'
        }
        failure {
            // Actions to take if the pipeline fails
            echo 'The pipeline failed :('
        }
    }
}
