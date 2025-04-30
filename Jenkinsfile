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
        stage('Bandit Security Scan') {
            steps {
                script {
                    // Run Bandit security scan and generate HTML report
                    sh './venv/bin/bandit -r . -f html -o ${env.BANDIT_REPORT}'
                }
            }
        }
        stage('Publish Bandit Report') {
            steps {
                script {
                    // Publish the Bandit HTML report as an artifact
                    archiveArtifacts artifacts: env.BANDIT_REPORT, allowEmptyArchive: true
                }
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
