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
                recordIssues tools: [genericParser( pattern: 'bandit-output.xml',regex: '<Issue severity="(?<severity>.*?)".*?lineNumber="(?<line>\\d+)".*?filename="(?<file>.*?)".*?testID="(?<category>.*?)".*?>(?<message>.*?)</Issue>',mapping: [
        file: 'file',
        line: 'line',
        severity: 'severity',
        category: 'category',
        message: 'message'
    ]
)]

            }
        }
    }
}
