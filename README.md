# DOCKER WORDPRESS SETUP <br >
This repository provides a Python script to Check if docker and docker-compose is installed on the system. If not present, install the missing packages and then create a WordPress site using the latest WordPress version. It utilizes the LEMP stack running inside Docker containers. <br >

## Prerequisites
* Python 3.x
* pip package manager


## USAGE
  To create a WordPress site, follow these steps: <br >
   1. Clone this repository to your local machine: <br >
    
    git clone https://github.com/vipul71098/docker_worldpress_setup.git
   2. Navigate to the cloned repository: <br>
   
    cd docker_worldpress_setup
   3. Before running the script, ensure that you have the following dependencies installed:

    Docker
    Docker Compose
If any of these dependencies are missing, the script will automatically attempt to install them. <br >
   4. Run the Python script and provide the site name as a command-line argument:
   
    python3 main.py <website_name>
  
  #### after executing above command following things will happen:
  * it will install docker dependency if not present on the system <br >
  * it will create worldpress site with the site name which we have pass as an argument <br >
  * new folder with the name **wordpress** will be created <br >
  *  new **docker-compose.yaml**  file will be created <br >
 
   4.1 To enable worldpress we have to pass argument **enable** to command line <br>
   
     python3 main.py <website_name> enable
     
  * after executing above command it will Prompt the user to open [example.com ](http://example.com)in a browser.<br>
  *  to access site on   [example.com ](http://example.com)in a browser first we have to update  **/etc/hosts** file to **127.0.0.1**  $~~~~~~~~~~~$    **example.com**
    
   4.2 To disable worldpress we have to pass argument **disable** to command line <br>
   
     python3 main.py <website_name> disable
   4.3 To delete the  wordpress site (deleting containers and local files) we have to pass argument **delete** to command line <br>
   
     python3 main.py <website_name> delete
     
  * after executing above command it will delete  the file(docker-compose.yaml), folder(wordpress) , stop  the docker conatainer and delete images respectively
