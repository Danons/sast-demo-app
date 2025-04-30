pipeline {
    agent any
    environment {
        GIT_REPO = 'https://github.com/Danons/sast-demo-app.git'
        GIT_BRANCH = 'master'
        GIT_CREDENTIALS_ID = 'github-token'
        BANDIT_REPORT = 'bandit_report.html'
    }
    stages {
        stage('Checkout') {
            steps {
                script {
                    // Ensure the correct repository and branch are used
                    def repoUrl = env.GIT_REPO.replace('your-username', 'Danons')
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: "*/${env.GIT_BRANCH}"]],
                        doGenerateSubmoduleConfigurations: false,
                        extensions: [],
                        userRemoteConfigs: [[
                            credentialsId: env.GIT_CREDENTIALS_ID,
                            url: repoUrl
                        ]]
                    ])
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    // Create a virtual environment
                    sh 'python3 -m venv venv'
                    
                    // Upgrade pip
                    sh './venv/bin/pip install --upgrade pip'
                    
                    // Skip requirements.txt installation if you don't need it
                    // sh './venv/bin/pip install -r requirements.txt'  // COMMENT OUT THIS LINE
                }
            }
        }
    post {
        always {
            // Clean up the virtual environment after the pipeline run
            sh 'rm -rf venv'
        }
    }
}
