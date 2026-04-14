pipeline {
    agent any
    stages {

        stage('Build + Tests + Sécurité') {
            steps {
                sh '''
                python -m venv venv
                . venv/bin/activate

                pip install --upgrade pip
                pip install -r requirements.txt || true

                pip install pytest bandit safety

                pytest tests/ || true
                bandit -r . -x tests -ll
                safety check || true
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
