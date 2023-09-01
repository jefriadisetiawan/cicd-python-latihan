    pipeline {
        agent {
            docker {
                image 'python:3.8-bullseye'
                args '-p 8501:8501'
            }
        }
        stages {
            stage('Build') {
                steps {
                    sh 'python3 --version'
 		    sh 'pip --version'
  		    sh 'pip install streamlit' 		   
		                    
                }
            }
            stage('Test') {
                steps {
                    sh 'streamlit run app.py'
                }
            }
            stage('Deploy') { 
                steps {
                    input message: 'Sudah selesai menggunakan Streamlit? (Klik "Proceed" untuk mengakhiri)' 
                }
            }
        }
    }
