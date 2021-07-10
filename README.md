--- a/README.md
+++ b/README.md
@@ -8,33 +8,32 @@ How to run tests:
 
 
### DEskription:
The project contains UI and API tests for [CosmosID](https://www.cosmosid.com/)


### Instruments used:
* Selenium Webdriver
* Pytest
* Allure

### Requirements
* Python 3.6+
* Packages from requirements.txt

### How to run tests
 Where:
    `<descriptive_feature_name>` - human-readable name of new feature or descriptive change name
* Clone the project
Before, make sure there is an [SSH key](https://gitlab.com/profile/keys) in your profile in Gitlab.
  * Run tests in terminal
 
### Tasks:
 
1. Create framework structure for https://app.cosmosid.com Api documentation: https://docs.cosmosid.com/docs/api-documentation
 
1.1. It shall contain folders for:
 
1.1.1. configuration
 
1.1.2. application specific libraries/helpers
 
1.1.3. app api clients
 
1.1.4. page objects
 
1.1.5. tests
 
2. Create Config class
 
2.1. It shall be possible to set config variables via Environment variables
 
2.2. It shall be possible to set config variables via YAML file
 
2.3. It shall be possible to set config variables inside Config class
 
3. Create class for sending HTTP requests
 
3.1. It shall be able to send requests:
-- GET
-- PUT
-- POST
-- DELETE
4. Create API web client 
4.1. Use CID specs from last tab in document
4.2. Create 2-4 API tests for each endpoint   
-- Using fixtures/before/aftertests is mandatory 
   Tests shall not contain hardcode
5. Selenium
5.1. Create base class 
5.2. Create some pages
5.3. Create some tests 
6. Docker
6.1. Dockerize
6.1.1 Install Docker(https://docs.docker.com/engine/install/)
   On Linux: [Create a Unix group called 'docker' and add user to it.]
   (https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user)
6.1.2 Clone the project: 'git clone git@github.com'
6.1.3 Run tests on Linux: 'bash run_docker.sh'
6.1.4 Run tests on Windows: 'run_docker.cmd'
    Command should be run from the project root folder
6.1.5 Test Report
    Open the report.html file to see the report

   