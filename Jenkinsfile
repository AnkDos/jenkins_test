pipeline {
    agent any 
    stages{
        stage('THE FIRST STAGE') {
            steps {
                sh 'echo The first Stage'
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
        
      emailext attachmentsPattern: 'nosetests.xml' , body: '${BUILD_LOG, maxLines=9999, escapeHtml=false}' , to: '$DEFAULT_RECIPIENTS', subject: 'Test'      
      junit 'nosetests.xml'       
            
        }
    }
    
    
}
        
            
           
    
