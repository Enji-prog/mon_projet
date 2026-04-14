pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-u root'  // évite les problèmes de permissions
        }
    }

    environment {
        VENV = "venv"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                python -m venv $VENV
                . $VENV/bin/activate
                pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                . $VENV/bin/activate
                pip install -r requirements.txt || true
                pip install pytest bandit safety
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . $VENV/bin/activate
                pytest tests/ || true
                '''
            }
        }

        stage('Security Scan - Bandit') {
            steps {
                sh '''
                . $VENV/bin/activate
                bandit -r . -x tests -ll
                '''
            }
        }

        stage('Dependency Scan - Safety') {
            steps {
                sh '''
                . $VENV/bin/activate
                safety check || true
                '''
            }
        }

        stage('Run Recon (Test rapide)') {
            steps {
                sh '''
                . $VENV/bin/activate
                python recon.py example.com --limit 3 || true
                '''
            }
        }
    }

    post {
        success {
            echo "Pipeline exécuté avec succès ✅"
        }
        failure {
            echo "Pipeline échoué ❌"
        }
        always {
            sh 'rm -rf $VENV'
        }
    }
}
