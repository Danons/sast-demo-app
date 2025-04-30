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
                script {
                    // Run Bandit and output the results in XML format
                    sh 'bandit -r . -f xml -o bandit_report.xml || true'

                    // Publish the Bandit report using recordIssues (without the invalid parameter)
                    recordIssues(
                        tools: [bandit(pattern: 'bandit_report.xml')]
                    )
                    
                    // Check the Bandit report for specific issues
                    def banditIssues = readFile('bandit_report.xml')
                    
                    // Custom logic: Fail the build if there are high severity issues
                    if (banditIssues.contains('High')) {
                        error 'High severity issues found in Bandit report.'
                    }
                }
            }
        }
    }
}
