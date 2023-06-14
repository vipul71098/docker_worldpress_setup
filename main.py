import os
import sys
import webbrowser
import subprocess
import shutil 


def check_installed(command):
    try:
        subprocess.check_output([command, '--version'])
        return True
    except OSError:
        return False

# Check if Docker is installed
if not check_installed('docker'):
    print("Docker is not installed. Installing Docker...")
    subprocess.run(['curl', '-fsSL', 'https://get.docker.com', '-o', 'get-docker.sh'])
    subprocess.run(['sh', 'get-docker.sh'])

# Check if Docker Compose is installed
if not check_installed('docker-compose'):
    print("Docker Compose is not installed. Installing Docker Compose...")
    subprocess.run(['curl', '-L', 'https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)', '-o', '/usr/local/bin/docker-compose'])
    subprocess.run(['chmod', '+x', '/usr/local/bin/docker-compose'])

print("Docker and Docker Compose are installed.")



def generate_docker_compose(site_name):
    # Docker Compose configuration
    docker_compose = f'''
    version: '3'

    services:
      db:
        image: mariadb
        restart: always
        environment:
          MYSQL_ROOT_PASSWORD: example_root_password
          MYSQL_DATABASE: {site_name}
          MYSQL_USER: {site_name}
          MYSQL_PASSWORD: example_db_password

      wordpress:
        depends_on:
          - db
        image: wordpress
        restart: always
        ports:
          - "80:80"
        environment:
          WORDPRESS_DB_HOST: db:3306
          WORDPRESS_DB_NAME: {site_name}
          WORDPRESS_DB_USER: {site_name}
          WORDPRESS_DB_PASSWORD: example_db_password
        volumes:
          - ./wordpress:/var/www/html
    '''

    # Write docker-compose.yml file
    with open('docker-compose.yml', 'w') as f:
        f.write(docker_compose)

def create_wordpress_site(site_name):
    # Generate docker-compose.yml
    generate_docker_compose(site_name)

    # Create WordPress directory
    os.makedirs('wordpress', exist_ok=True)
    print(f"WordPress site '{site_name}' has been created successfully.")


def enable_site(url):
  
    if os.path.exists('docker-compose.yml'):
        os.system('docker-compose up -d')
        user_input = input(f"Do you want to open {url} in a browser? (y/n): ")
        if user_input.lower() == "y":
            webbrowser.open(url)
            print("Enabling site...")
    else:
        print("Please first create a site by executing command 'python3 main.py <website_name>'")

def disable_site():

    os.system('docker compose down')
    print("Disabling site...")

def delete_site():
    
    if os.path.exists('docker-compose.yml'):
        os.system('docker-compose down')
        os.remove('docker-compose.yml')
    
    if os.path.exists('wordpress') and os.path.isdir('wordpress'):
        shutil.rmtree('wordpress')
    
    # os.system('docker rmi wordpress')
    # os.system('docker rmi mariadb')
    print("Deleting site...")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide the site name as a command-line argument.")
        sys.exit(1)



    if len(sys.argv) == 2:
        site_name = sys.argv[1]
        create_wordpress_site(site_name)

    url = "http://example.com"
    
    if len(sys.argv) >= 3:
        if sys.argv[2] == 'enable':
            enable_site(url)
        elif sys.argv[2] == 'disable':
            disable_site()
        elif sys.argv[2] == 'delete':
            delete_site()
        else:
            print("Please choose enable,disable or delete")