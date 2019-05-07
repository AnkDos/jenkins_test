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
        
            step([$class: 'Mailer', notifyEveryUnstableBuild: true, recipient: 'santosh.kumar@innopark.in' ,body: '${BUILD_LOG}' ,sendToIndividuals: true])
              
        }
    }
    
    
}
        
            
           
    
