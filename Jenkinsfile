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
                sh 'python3 -m unittest tes.TEST_SUITE'
            }
        }
        stage('I am Deploying'){
            steps{
              sh 'echo deploying'   
            }
        }
    }
}
        
            
           
    
