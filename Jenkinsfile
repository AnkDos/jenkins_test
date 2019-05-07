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
        
            emailext(body: '${DEFAULT_CONTENT}', mimeType: 'text/html',replyTo: '$DEFAULT_REPLYTO', subject: '${DEFAULT_SUBJECT}',to: emailextrecipients([[$class: 'CulpritsRecipientProvider'],[$class: 'RequesterRecipientProvider']]))              
        }
    }
    
    
}
        
            
           
    
