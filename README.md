# Assignment1

## Original Intention:

Suppose that I am interested in the area of Android development. I like to browse and answer Stack Overflow questions that are related to Android. However, it is tedious to search for the relevant questions on Stack Overflow. 

I would like to see the titles of the 10 newest Android-related questions and the 10 most voted Android-related questions posted in the past week, on one page. In this way, I can easily keep track of the relevant questions. In addition, I would like to be able to read the full information of these questions in a convenient way. 

## Requirements:
1. Extracting from stackoverflow.com the 10 newest Android-related questions, as well as the 10 most voted Android-related questions are created in the past week. <br/>
2. Providing a convenient way of displaying the full question thread after I click on the titles. <br/>
3. Adding a cool feature. 


## Implementation:
Browse stackoverflow.com. In the search bar, enter "Android". Applied 'Newest' filter to find the newest posts questions that related to Android. Copy the link. Using 'BeautifulSoup' and 'requests' to scrape content from the copied link. And, using 'flask' to make a simple website. 

## How to run:
Download the stackoverflow.zip file and unzip it to a folder. Using terminal to the path folder. Type "pyhton3 statckoverflow.app". Waiting for 15sec to let the program scrape. After http://127.0.0.1:5000/ shows up in the terminal, click it or copy it to any browser to browse the web. On the webpage, click any left sied or right side questions, then click "View details", you will be directed to the corresponding StackOverflow website to browse the content. 

## Added feature: 
I added a feature of statistics. In the opened webpage, click the questions under the "10 newest Android-related questions", you will see their existing timestamps in every listed questions. Under the "10 most voted Android-related questions", click any questions, you will see there have a votes number indicated how many votes of this question got. At the bottom of the webpage, you will see the total questions that posted for the last week. 

## Regarding the most voted questions: 
When you see the votes numbers under the "10 most voted Android-related questions", you probably will realize that the votes numbers of each question is really small (like 3, 5, 8). This happens depends on how you define the words "Newest" because the stackoverflow.com defined the time which is different as our understanding. I implemented this strictly by the requirements which I scraped the questions posted (Asked) last week not Active. If you do the following steps: <br />1. go to stackoverflow.com <br />2. In the search bar enter "Android lastactive:7d.." ("lastactive:" means look back to the same date in the previous period of this question, "7d.." means seven days. Detail: https://stackoverflow.com/help/searching) <br />3. Click 'Votes' and select 'Votes' which made all the questions sorted by most votes. <br/>
You will see the most voted Android-related questions is 2343. Click this question, then, you will see under this question there are "Asked, Active, and Viewed". This website's time rule is based on 'Active' not 'Asked'. This is a paradox from our requirments. So, I implemented this part as 'Asked' (which the question post) not 'Active' (discussed). This is acturally can be a defect for people who just wants to see the trends of Android problems based on these questions. Because, those 'Active' questions will disturb them to see the real trends of this field. See pictures below. 

![github](https://github.com/66stevengai/Assignment1/blob/master/Images/Search%20results.png=500x250)

## Improvements:
1. It takes me a while to try to use the API of this website, but I failed. So, I just used the dumbest way to "manually" scrape content from this website. Later, I'll try to figure out how to use the API of this website. <br />
2. The website is not good looking enough. Due to the time limitations, I did not make the website really good looking by using CSS. This part also needs to be improved. 

