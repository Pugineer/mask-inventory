# mask-inventory

### Introduction
Mask-inventory is a website provide useful mask selling source to the public.
All resources are automatically web-scraped and collected by a script, built by Selenium.
Python is used as the main language of this project.

### Tools of development
+ AWS EC2
  + It is used to deploy the auto-web-scraping program and run the code automatically.
+ AWS S3
  + S3 storage is used to store the json file which scraped.
+ Selenium
  + The core of the script, it creates a Chrome instance to simulate a user browsing the website, and scraps the data.
 
### Screenshot
![](https://i.imgur.com/YuIMDih.png)
> Without filtering

![](https://i.imgur.com/Y7nMfg2.png)
> With filtering
