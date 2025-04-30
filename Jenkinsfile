pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Danons/sast-demo-app.git', branch: 'master'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install bandit
                '''
            }
        }
        stage('SAST Analysis') {
            steps {
                sh '''
                    . venv/bin/activate
                    bandit -f xml -o bandit-output.xml -r . || true
                '''
		// Use the recordIssues step to publish the Bandit report
                    recordIssues(
                        tools: [bandit(pattern: 'bandit_report.xml')],
                        enablePipelineNotifications: true
                    )
                    
                    // Check for specific issues and fail the build if needed
                    def banditIssues = readFile('bandit_report.xml')
                    if (banditIssues.contains('High')) {
                        error 'High severity issues found in Bandit report.'
                    }
            }
        }
    }
}
