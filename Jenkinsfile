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
        
            step([$class: 'Mailer', notifyEveryUnstableBuild: true, recipients: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']],body: '${BUILD_LOG}' ,sendToIndividuals: true])
              
        }
    }
    
    
}
        
            
           
    
