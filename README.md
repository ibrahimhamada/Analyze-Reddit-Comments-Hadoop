# Analyze-Reddit-Comments-Hadoop
Mini Project 1 of the Big Data Analytics Course Offered in Fall 2022 @ Zewail City

In this project, we used Hadoop to analyze 53 million Reddit comments. 
We used [Hadoop 3.3.4](https://hadoop.apache.org/release/3.3.4.html) on Colab Environment and applied some methods to extract information from the Reddit Dataset, we first subdivided the data into two parts, User related part, and topics related part. Then on each part we merge the required data, distributing on different map reducers and each return the results. 



## Dataset:

The Dataset consists of a list of comments taken for the Reddit public API from various subreddits.

* The dataset is one file with each comment in JSON format in one line.
* Total Comments: 53,851,542.
* Compression Type: bzip2 (5,452,413,560 bytes compressed | 31,648,374,104 bytes uncompressed).
* Dataset can be found [here](https://drive.google.com/file/d/1-D_uHkn37M5ptWVQl8a5-q8NBv9jaLWr/view).
* Do NOT open the dataset file on an editor as it may cause a crash or a freeze to your application or your system 
* You can explore/generate your own samples using these commands

    Windows (Powershell): 

       $ gc <file_name> | select -first <line_number> >> sample.out

    Linux: 
    
       $ head -n <line_number> <file_name> >> sample.out



## MapReduce Jobs

    1. Top subreddits.

    2. Most discussed/used topics associated with every subreddit.

    3. Topics that yield the highest number of upvotes and lowest of downvotes

    4. The top users in top subreddits.

    5. Rate of replies compared to controversiality of comment/post.
    
    6. The usage of curse per subreddit.


## How to run a job?

We downloaded [hadoop 3.3.4](https://hadoop.apache.org/release/3.3.4.html) on colab and changed the java version to be java 8 version. After that we started working on a colab. 

Every task is assigned a dedicated folder containing a script tailored to that task. This script is responsible for executing the task and providing the required parameters to the mapper and reducer. In cases where a task necessitates the execution of two jobs to generate the final output, the script will initiate the first job and subsequently utilize its output as input for the second job.



## Using the compressed dataset

