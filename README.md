# mask-inventory

Mask-inventory is a website provide useful mask selling source to the public. 
The website mainly uses selenium as the crawling engine, and crawl from the biggest online shopping website ing Hong Kong, like HKTVMall, and Watsons.
AWS EC2 is used to build the webserver, and run the automated crawling script. The data crawlied from the internet is stored into a AWS S3 service for analysis purposes.
