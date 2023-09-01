    pipeline {
        agent {
            docker {
                image 'python:3.8-bullseye'
                args '-p 3000:3000'
            }
        }
        stages {
            stage('Build') {
                steps {
                    sh 'python3 --version'
 		    sh 'pip --version'
   		   
		                    
                }
            }
            stage('Test') {
                steps {
                    sh 'pip install streamlit --user'
                }
            }
            stage('Deploy') { 
                steps {
                    input message: 'Sudah selesai menggunakan Streamlit? (Klik "Proceed" untuk mengakhiri)' 
                }
            }
        }
    }
