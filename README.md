# GitHub-Actions

GitHub actions is another CI/CD solution. Jenkins and GitHub actions are for same things but 
GitHub actions is only for GitHub. It allows us to automate software workflows like building, 
testing, and deploying code directly from your GitHub repository. We should use Jenkins, GitHub 
actions, and GitLab depending on our needs. If we don’t work with GitHub then we shouldn’t use 
GitHub actions. 

We don’t need to install plug-ins for GitHub actions. In the root of our repository, we create 
.github/workflows. 

We created a first-actions.yml file in our repository. Whenever there is a push action or 
whenever there is a commit created in this repository, by default, GitHub actions will execute 
that pipeline.

There is no limitation to action files that we can place in .github. All our action files have 
to be in this folder. GitHub automatically looks for workflow files in .github/workflows/ to 
trigger CI/CD actions.

For example with one action file we can verify if the user has provided all the datils in the 
pull request. Because when we have a pull request we have to provide good description, what 
issue it is solving etc.. In another pipeline we can address linting issues. We can do our CI 
and CD in different pipelines. 

We can have more than one triggering action in one action .yml file. For example we can trigger 
the action when there a push or pull. If either of them is fulfilled, then GitHub executes this 
pipeline.

We created a python script in our src folder. When we modify the code in this script and commit 
the change we can see in our first-actions.yml file is executing. 

In Github Actions documentation we can find various examples and script.

Unlike Jenkins, GitHub Actions does not require us to manually install plugins. Instead, GitHub 
Actions provides a marketplace of pre-built actions that you can use directly in your workflow 
without installation. The biggest advantage of GitHub actions is that we write less code 
compared to our CI/CD tools. We only write the name of the plugins. But the only disadvantage 
is that these plugins are limited in scope. 
In the Settings → Actions →Runners we can set our custom runners for more compute resources and 
security purposes. 

Where can we store our secrets in these scenarios? We can store our secret information in the 
settings. The basic action file can be obtained from GitHub Action’s official documentation and 
then we can modify it depending on our needs.

Another disadvantage for GitHub Actions is that it is platform specific. If we move to another 
platform from GitHub, our system will not work.

Comparing with Jenkins:

Advantages of GitHub Actions over Jenkins:
- Hosting: Jenkins is self-hosted, meaning it requires its own server to run, while GitHub
Actions is hosted by GitHub and runs directly in your GitHub repository. This is a big
advantage. If we work with GitHub actions we don’t need to maintain Jenkins.
- User interface: Jenkins has a complex and sophisticated user interface, while GitHub Actions
has a more streamlined and user-friendly interface that is better suited for simple to moderate
automation tasks.
- Cost: Jenkins can be expensive to run and maintain, especially for organizations with large
and complex automation needs. GitHub Actions, on the other hand, is free for open-source
projects and has a tiered pricing model for private repositories, making it more accessible to
smaller organizations and individual developers. But there is a limit of the free execution
time for private projects on GitHubs. But it is cheaper than Jenkins anyway.

Advantages of Jenkins over GitHub Actions:
-Integration: Jenkins can integrate with a wide range of tools and services, but GitHub Actions 
is tightly integrated with the GitHub platform, making it easier to automate tasks related to 
your GitHub workflow. 

In conclusion, Jenkins is better suited for complex and large-scale automation tasks, while 
GitHub Actions is a more cost-effective and user-friendly solution for simple to moderate 
automation needs.

GITHUB ACTIONS SELF HOSTED RUNNERS

We will take a look at self hosted runners vs GitHub hosted runners. We will learn how to use self hosted runners. We will use an EC2 instance for this.
Runner is the place where our job is executed. In Jenkins world we call this runner an agent or worker node. This is where our application runs on Jenkins. When we run our code 
on GitHub hosted runners, our code is executed in GitHub’s servers. We don’t own these compute resources, GitHub does. It allocates some resource for our code, and once the 
execution is done, we are done with these resources, GitHub doesn’t allocate it for us anymore.

We use self hosted runners primarily because of 2 things. First, when we are an enterprise our code has to remain private. Second, when the runners that are provided by GitHub 
aren’t good enough in terms of compute resources. And when we are concerned about the security of our code, we should use self hosted runners.

How do we attach self hosted runners into our GitHub actions. We will use an EC2 instance for this.
For Jenkins we used ssh protocol for the communication between the master node and the agents. For GitHub actions we need to do a set of things. 

We need to do some configuration for our EC2 instance. We will modify the inbound and outbound traffic rules. We will open both HTTP and HTTPS ports for inbound and outbound 
traffic. Because our GitHub account and EC2 instance might not be in the same network.

So we add new rules for inbound to our security group. We add a new rule with HTTP (port 80) and choose anywhere. And we add another rule with HTTPS (port 443) and choose anywhere.
This ensures that our self-hosted runner can communicate with GitHub’s servers. 
The GitHub Actions runner software (our EC2 instance)  polls GitHub to check for new jobs. This happens over HTTPS (port 443). If outbound HTTPS traffic is blocked, the runner 
won’t receive jobs from GitHub. Polling means that the runner (your EC2 instance) repeatedly contacts GitHub’s servers over HTTPS (port 443) to check if there are any new 
workflow jobs assigned to it. Unlike Jenkins, which uses an SSH connection to send jobs to agents, GitHub Actions does not "push" jobs to the runner. Instead, the runner pulls 
(or "polls") GitHub's servers at regular intervals to check if there are new tasks for it to execute.

We add HTTP and HTTPs rules for outbound for anywhere traffic as well. 
Let’s remember how GitHub actions work. We have a .yml file that tells GitHub actions that whenever there is a new commit to our repository GitHub Actions workflow automates the 
testing process. We have it in line 3: on: [push]. For this GitHub creates a runner for us that has Ubuntu as the OS. (line 7: runs-on: ubuntu-latest). The green tick on the 
commit means that the verification is successful. 

Now let’s do it with a self hosted runner. Actions → Runners we add a new runner there and do the configuration for our EC2 instance. We check if our system is x64 or arm with 
the command “uname -m”. And we install the packages there.
Note: I had a problem with installing these packages. Our free-tier EC2 instance was almost full. Deleting the files and folder didn’t work. So I terminated this one and created 
a new one with the same inbound and outbound rules.

After following the steps on the Add new self-hosted runner page on GitHub and running the “./run.sh” command we are ready. We set up Github actions on our EC2 instance. We only 
need to make 1 change in our .yml file. We change ubuntu-latest to self-hosted.
We see that our EC2 instance is listening for jobs.
When the runner is done, it sends a notification to GitHub and we see the green tick on the commit section of our repository. This is the outbound traffic. We configured the 
outbound traffic for this reason. And it gets the request from GitHub with the inbound traffic.
When we have options like Jenkins and AWS CodeBuild why would we run our code on GitHub Actions?
- If we have a public project then we should use GitHub as it offers free resources for public projects.
- If we have a private project and an ecosystem on GitHub, we can manage everything on GitHub. We can manage CI/CD with GitHub actions, Agile and Scrum methods with Projects, Confluence pages with GitHub wiki, security, and insights from GitHub. So we can use GitHub to the fullest capacity.

How do you secure sensitive information on GitHub?
We can store our secrets and sensitive information in GitHub in Settings → “Secrets and variables”. 

How do you write a GitHub CI file? 
We create a .github/workflows folder. And we have a .yml file here. With “on: [push]”, we choose when this action is triggered. 

GitHub Actions vs Jenkins → If we have a public project then we should use GitHub actions.
If it is a private project we can use Jenkins for its advantages like its own servers and its own containers. Jenkins has a good orchestration. And Jenkins has more support than GitHub Actions. There are more plugins in Jenkins. So there are more things that we can achieve with Jenkins but it all depends on the scope of our project.

We mentioned Agile and Scrum above. Let’s take a closer look at them. 
Agile and Scrum are methodologies used in software development, including DevOps, to manage projects efficiently. They help teams deliver work iteratively, collaborate effectively, and adapt to changing requirements.
Agile is a project management approach that emphasizes:
Iterative development → Work is delivered in small, usable increments rather than all at once.
Customer collaboration → Continuous feedback from stakeholders is essential.
Flexibility → Adapts to changes rather than following a strict plan.
Teamwork → Cross-functional teams work together, ensuring quick problem-solving.

Agile replaces traditional "Waterfall" methods where everything is planned upfront and delivered at the end, often leading to rigid and slow processes.

Scrum is a specific Agile framework used for project management. It structures work into time-boxed iterations called Sprints (usually 1-4 weeks). A Scrum team has:
Product Owner → Defines what should be built and prioritizes the backlog.
Scrum Master → Facilitates Scrum processes and removes obstacles.
Development Team → Builds and delivers the product increment.

Scrum Workflow:
1️⃣ Sprint Planning – The team selects tasks for the sprint.
2️⃣ Daily Standup – A 15-minute daily meeting to discuss progress.
3️⃣ Sprint Review – Show completed work to stakeholders.
4️⃣ Sprint Retrospective – Reflect on improvements for the next sprint.

How is Agile/Scrum Used in DevOps?
In DevOps, Agile/Scrum helps teams release code frequently while improving collaboration between development and operations teams. Some common practices:
Continuous Integration/Continuous Deployment (CI/CD) – Teams deploy code in smaller, frequent updates (aligned with Agile's iterative approach).
Infrastructure as Code (IaC) – Changes are tested and deployed quickly.
Kanban Boards – Used in tools like Jira, GitHub Projects, or Trello to track work.

Agile and Scrum are best learned by doing, not just by reading. 

Can you explain the CICD process in your current project ? or Can you talk about any CICD process that you have implemented ?
Example: 
In the current project we use the following tools orchestrated with Jenkins to achieve CICD.
    Maven, Sonar, AppScan, ArgoCD, and Kubernetes
Coming to the implementation, the entire process takes place in 8 steps
1. Code Commit: Developers commit code changes to a Git repository hosted on GitHub.
2. Jenkins Build: Jenkins is triggered to build the code using Maven. Maven builds the code and runs unit tests. Maven is a build automation and dependency management tool
3. primarily used for Java projects. Maven manage dependencies, compile and package Java code into .jar or .war files, run tests and ensure code quality, standardize project
4. structures using pom.xml, integrate with CI/CD tools like Jenkins, GitHub Actions, GitLab CI/CD.
5. Code Analysis: Sonar is used to perform static code analysis to identify any code quality issues, security vulnerabilities, and bugs.
6. Security Scan: AppScan is used to perform a security scan on the application to identify any security vulnerabilities.
7. Deploy to Dev Environment: If the build and scans pass, Jenkins deploys the code to a development environment managed by Kubernetes.
8. Continuous Deployment: ArgoCD is used to manage continuous deployment. ArgoCD watches the Git repository and automatically deploys new changes to the development environment
9. as soon as they are committed.
10. Promote to Production: When the code is ready for production, it is manually promoted using ArgoCD to the production environment.
11. Monitoring: The application is monitored for performance and availability using Kubernetes tools and other monitoring tools.

What are the different ways to trigger jenkins pipelines?
There should be a way for Jenkins to notice that there is a commit to a certain repository on GitHub.
- Poll SCM (Source Control Management): Jenkins can periodically check the repository for changes and automatically build if changes are detected.  This can be configured in the "Build Triggers" section of a job. Configured in Job > Configure > Build Triggers > Poll SCM. This is generally more expensive than using webhooks because Jenkins nodes waste CPU cycles checking for changes instead of running builds.        
  - Build Triggers: Jenkins can be configured to use the Git plugin, which allows you to specify a Git repository and branch to build. The plugin can be configured to automatically build when changes are pushed to the repository. The Git plugin in Jenkins allows it to check a repository for changes with GitHub webhooks.
  - Webhooks: A webhook can be created in GitHub to notify Jenkins when changes are pushed to the repository. Jenkins can then automatically build the updated code. This can be set up in the "Build Triggers" section of a job and in the GitHub repository settings.

How to backup Jenkins?
Backing up Jenkins is a very easy process, there are multiple default and configured files and folders in Jenkins that you might want to backup.
  - Configuration: We navigate to the home folder of the user where we installed Jenkins. The “~/.jenkins folder.” You can use a tool like rsync to backup the entire directory to another location. 
    - Plugins: Backup the plugins installed in Jenkins by copying the plugins directory located in JENKINS_HOME/plugins to another location.
    - Jobs: Backup the Jenkins jobs by copying the jobs directory located in JENKINS_HOME/jobs to another location.    
    - User Content: If you have added any custom content, such as build artifacts, scripts, or job configurations, to the Jenkins environment, make sure to backup those as well.   
- Database Backup: If you are using a database to store information such as build results, you will need to backup the database separately. This typically involves using a database backup tool, such as mysqldump for MySQL, to export the data to another location.
We can schedule the backups to occur regularly, such as daily or weekly, to ensure that you always have a recent copy of your Jenkins environment available. We can use tools such as cron or Windows Task Scheduler to automate the backup process.

How do you store/secure/handle secrets in Jenkins?
Handling with secrets is important for all the tools. Again, there are multiple ways to achieve this, Let me give you a brief explanation of all the posible options.
   - Credentials Plugin: Jenkins provides a credentials plugin that can be used to store secrets such as passwords, API keys, and certificates. The secrets are encrypted and stored securely within Jenkins, and can be easily retrieved in build scripts or used in other plugins.
   - Environment Variables: Secrets can be stored as environment variables in Jenkins and referenced in build scripts. However, this method is less secure because environment variables are visible in the build logs.
   - Hashicorp Vault: Jenkins can be integrated with Hashicorp Vault, which is a secure secrets management tool. Vault can be used to store and manage sensitive information, and Jenkins can retrieve the secrets as needed for builds. This is the one most used.
   - Third-party Secret Management Tools: Jenkins can also be integrated with third-party secret management tools such as AWS Secrets Manager, Google Cloud Key Management Service, and Azure Key Vault.

What is latest version of Jenkins or which version of Jenkins are you using?
We have to keep up with the latest knowledge. For now the latest one is 2.492.1.

What is shared modules in Jenkins?
Shared libraries also fall into the same category. Shared modules in Jenkins refer to a collection of reusable code and resources that can be shared across multiple Jenkins jobs. This allows for easier maintenance, reduced duplication, and improved consistency across multiple build processes. For example, shared modules can be used in cases like:
        - Libraries: Custom Java libraries, shell scripts, and other resources that can be reused across multiple jobs.
        - Jenkinsfile: A shared Jenkinsfile can be used to define the build process for multiple jobs, reducing duplication and making it easier to manage the build process for multiple projects. 
        - Plugins: Common plugins can be installed once as a shared module and reused across multiple jobs, reducing the overhead of managing plugins on individual jobs.   
- Global Variables: Shared global variables can be defined and used across multiple jobs, making it easier to manage common build parameters such as version numbers, artifact repositories, and environment variables.

Can you use Jenkins to build applications with multiple programming languages using different agents in different stages?
Yes, Jenkins can be used to build applications with multiple programming languages by using different build agents in different stages of the build process.
Jenkins supports multiple build agents, which can be used to run build jobs on different platforms and with different configurations. By using different agents in different 
stages of the build process, you can build applications with multiple programming languages and ensure that the appropriate tools and libraries are available for each language.
For example, you can use one agent for compiling Java code and another agent for building a Node.js application. The agents can be configured to use different operating systems, 
different versions of programming languages, and different libraries and tools.
Jenkins also provides a wide range of plugins that can be used to support multiple programming languages and build tools, making it easy to integrate different parts of the 
build process and manage the dependencies required for each stage.
Overall, Jenkins is a flexible and powerful tool that can be used to build applications with multiple programming languages and support different stages of the build process.
Docker can be used in this setup to provide isolated environments for different programming languages and dependencies. For example, you could run each build stage inside a 
different Docker container with the required tools pre-installed. This approach ensures consistency across builds and avoids conflicts between different environments.

How to setup auto-scaling group for Jenkins in AWS?
Here is a high-level overview of how to set up an autoscaling group for Jenkins in Amazon Web Services (AWS):
    - Launch EC2 instances: Create an Amazon Elastic Compute Cloud (EC2) instance with the desired configuration and install Jenkins on it. This instance will be used as the 
    base image for the autoscaling group.    
    - Create Launch Configuration: Create a launch configuration in AWS Auto Scaling that specifies the EC2 instance type, the base image (created in step 1), and any additional 
    configuration settings such as storage, security groups, and key pairs.
    - Create Autoscaling Group: Create an autoscaling group in AWS Auto Scaling and specify the launch configuration created in step 2. Also, specify the desired number of 
    instances, the minimum number of instances, and the maximum number of instances for the autoscaling group.  
    - Configure Scaling Policy: Configure a scaling policy for the autoscaling group to determine when new instances should be added or removed from the group. This can be based 
    on the average CPU utilization of the instances or other performance metrics.
    - Load Balancer: Create a load balancer in Amazon Elastic Load Balancer (ELB) and configure it to forward traffic to the autoscaling group.
    - Connect to Jenkins: Connect to the Jenkins instance using the load balancer endpoint or the public IP address of one of the instances in the autoscaling group.
    - Monitoring: Monitor the instances in the autoscaling group using Amazon CloudWatch to ensure that they are healthy and that the autoscaling policy is functioning as 
    expected.
By using an autoscaling group for Jenkins, you can ensure that you have the appropriate number of instances available to handle the load on your build processes, and that new instances can be added or removed automatically as needed. This helps to ensure the reliability and scalability of our Jenkins environment.

How to add a new worker node in Jenkins?
Log into the Jenkins master and navigate to Manage Jenkins > Manage Nodes > New Node. Enter a name for the new node and select Permanent Agent. Configure SSH and click on Launch.

How to add a new plugin in Jenkins?
Using the CLI, java -jar jenkins-cli.jar install-plugin <PLUGIN_NAME>
Using the UI, click on the "Manage Jenkins" link in the left-side menu. Click on the "Manage Plugins" link.

What is JNLP and why is it used in Jenkins?
JNLP is how we allow the agents or worked nodes to talk to our Jenkins master. In Jenkins, JNLP is used to allow agents (also known as "slave nodes") to be launched and managed 
remotely by the Jenkins master instance. This allows Jenkins to distribute build tasks to multiple agents, providing scalability and improving performance. When a Jenkins agent 
is launched using JNLP, it connects to the Jenkins master and receives build tasks, which it then executes. The results of the build are then sent back to the master and 
displayed in the Jenkins user interface.

What are some of the common plugins that you use in Jenkins?
Git plugin, Jira plugin, Kubernetes plugin, SonarQube plugin, Docker plugin, Maven plugin, AWS EC2 plugin, Build Pipeline plugin, Blue Ocean plugin, Mailer plugin.
