#  Crawling using request package
## Crawling TOI Archive News
To crawl any site using request a deep analysis of the site is required.

### Analysis
Start URL: https://timesofindia.indiatimes.com/archive.cms

The inital crawling url contains a links for each month and in each month there are date for each day.
![](images/TOI/001_Initial_page.png)
![](images/TOI/002_TOI_Date.png)

If we analise the url and the Javascript the we can calculate the url for each day

![](images/TOI/003_JS.png) and ![](images/TOI/004_PAGE_URL.png)

by using
``` python 
pre_date = datetime(1899,12,30)
d =  floor((date - pre_date).total_seconds()/86400)
```


### Flow Diagram

```mermaid
graph TB
    start([start]) --> P1[Range over date]
    P1 --> C1{If range over date finished}
    C1 -- no --> P2[Decrease the date day by 1]
    P2 --> P3[Compute the date archive url]
    P3 --> P4[Make a request and fetch the response]
    P4 --> P5[Parse the response and get the links of the article]
    P5 --> P6[Iterate over the links]
    P6 --> C2{If all links completed}
    C2 -- yes --> P1
    C2 -- No --> P7[Make a request and fetch the response]
    P7 --> P8[Parse the response and get the details of the article]
    P8 --> P6
    C1 -- yes --> exit([exit])
```