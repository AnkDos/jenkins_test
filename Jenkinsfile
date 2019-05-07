pipeline {
    agent any 
    stages{
        stage('THE FIRST STAGE') {
            steps {
                sh 'echo The first stage'
            }
        }
        stage('here comes the testing'){
            steps {
                sh 'nosetests --with-xunit'
            }
        }
        stage('I am Deploying'){
            steps{
              sh 'echo deploying'   
            }
        }
    }
    
    
    post {
        always {
        
              emailext body:  [${BUILD_LOG, maxLines=9999, escapeHtml=false}], recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], subject: 'Test'
            
        }
    }
    
    
}
        
            
           
    
