pipeline {
	agent any
	stages {
		stage('Build + Tests + Sécurité') {
			steps {
				sh '''
				python3 -m venv venv
				venv/bin/pip install --upgrade pip
				venv/bin/pip install -r requirements.txt
				venv/bin/pytest tests/
				venv/bin/pip install bandit safety
				venv/bin/bandit -r src/ -ll
				venv/bin/safety check
				'''
			}
		}
		stage('Nettoyage') {
			steps {
			  sh 'rm -rf venv'
			}
		}
	}
	post {
		success {
			echo "Pipeline exécuté avec succès."
		}
		failure {
			echo "Pipeline échoué"
		}
	}
}
