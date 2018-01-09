## Hit page counter

### AWS and Docker setup

#### power up AWS instance
follow [this](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html#ec2-launch-instance)

#### allow ssh access from your IP
follow [this](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.html#add-rule-authorize-access)

#### install docker
either use aws docker integration or follow [these steps](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/#set-up-the-repository) for docker CE

#### clone repo with Flask app
```
git clone https://github.com/mkotov13/hit_counter
cd hit_counter

```
  
#### build docker image
```
docker build -t hit-counter .
```

#### boot up docker container
`docker run hit-counter` and specify ports if needed

### Automating with ansible

 - install ansible
follow [this](http://docs.ansible.com/ansible/latest/intro_installation.html)

 - install boto for python
`pip install boto'

 - specify group variables in `group_vars/all.yml'
 - specify hosts in `hosts`
 - add tasks for launch, docker and flask roles