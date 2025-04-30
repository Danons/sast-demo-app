	pipeline {
		agent any
		stages {
			stage('Checkout') {
				steps {
					git url: 'https://github.com/Danons/sast-demo-app.git', branch:'master'
				}
			}
			stage('Install Dependencies') {
				steps {
					sh 'pip install bandit'
				}
			}
			stage('SAST Analysis') {
				steps {
					sh 'bandit -f xml -o bandit-output.xml -r . || true'
					recordIssues tools: [bandit(pattern: 'bandit-output.xml')]
				}
			}
		}
