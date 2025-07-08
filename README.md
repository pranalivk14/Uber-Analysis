# Uber-Analysis
Using the provided dataset, which includes supply and Demand insights for Uber's 2-week data, I have answered the following questions.

1.	Which date had the most completed trips during the two week period?
_The date with the most completed trips is 22-Sep-12 with 248 trips._

2.	What was the highest number of completed trips within a 24 hour period?
_The highest number of completed trips within a 24 hour period is 248 on 22-Sep-12_

3.	Which hour of the day had the most requests during the two week period?
_23th hour had the most requests during the two week period_

4.	What percentages of all zeroes during the two week period occurred on weekend (Friday at 5 pm to Sunday at 3 am)? Tip: The local time value is the start of the hour (e.g. 15 is the hour from 3:00pm - 4:00pm)
_Percentage of all zeroes during the two week period that occurred on weekend: 5.68%_

5.	In drafting a driver schedule in terms of 8 hours shifts, when are the busiest 8 consecutive hours over the two week period in terms of unique requests? A new shift starts in every 8 hours. Assume that a driver will work same shift each day.
_The busiest 8 consecutive hours are from 16:00 to 23:59 with 1032 unique requests over the two week period._

6.	True or False: Driver supply always increases when demand increases during the two week period. Tip: Visualize the data to confirm your answer if needed.
_FALSE_
7.	In which 72 hour period is the ratio of Zeroes to Eyeballs the highest?
_The 72-hour period with the highest ratio of Zeroes to Eyeballs is from 2012-09-10 07:00:00 to 2012-09-13 06:00:00, with a ratio of 0.0293._

8.	If you could add 5 drivers to any single hour of every day during the two week period, which hour should you add them to? Hint: Consider both rider eyeballs and driver supply when choosing
_5 drivers can be added to hour 4:00 each day, which has the highest average Zeroes to Eyeballs ratio (0.4483) over the two week period._


9.	True or False: There is exactly two weeks of data in this analysis
_TRUE_

10.	Looking at the data from all two weeks, which time might make the most sense to consider a true "end day" instead of midnight? (i.e when are supply and demand at both their natural minimums) Tip: Visualize the data to confirm your answer if needed.
_4:00 AM often makes the most sense as a true end day for operational or reporting purposes, rather than midnight._


Metadata:

Date: 2012-09-10

Time (Local): 16

Eyeballs: 11

Zeroes: 2

Completed Trips: 3

Requests: 4

Unique Drivers: 6

This means that during the hour beginning at 4pm (hour 16), on September 10th, 2012, 11 people opened the Uber app (Eyeballs). 2 of them did not see any car (Zeroes) and 4 of them requested a car (Requests). Of the 4 requests, only 3 complete trips actually resulted (Completed Trips). During this time, there were a total of 6 drivers who logged in (Unique Drivers)
