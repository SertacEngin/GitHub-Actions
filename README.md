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

Advantages of Jenkins over GitHub Actions
-Integration: Jenkins can integrate with a wide range of tools and services, but GitHub Actions 
is tightly integrated with the GitHub platform, making it easier to automate tasks related to 
your GitHub workflow. 

In conclusion, Jenkins is better suited for complex and large-scale automation tasks, while 
GitHub Actions is a more cost-effective and user-friendly solution for simple to moderate 
automation needs.
