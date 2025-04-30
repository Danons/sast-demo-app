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

                    // Publish results using a generic parser
            	    recordIssues(
                		tool: genericParser(
                    		pattern: 'bandit_report.xml',
                    		name: 'Bandit',
                    		regularExpression: '<issue severity="(.*?)".*?test_id="(.*?)".*?<test_name>(.*?)</test_name>.*?<issue_text>(.*?)</issue_text>.*?<line_number>(\\d+)</line_number>',
                    		example: '<issue severity="LOW" confidence="HIGH" test_id="B101" test_name="assert_used"><issue_text>Use of assert detected. The enclosed code will be removed when compiling to optimised byte code.</issue_text><line_number>4</line_number>',
                    		mapping: [
                        		severity: 1,
                        		category: 2,
                        		type: 3,
                        		message: 4,
                        		line: 5
                    		]
                	)
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
