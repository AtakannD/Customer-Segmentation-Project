*Customer Segmentation with RFM Analysis*

1. Business Problem

FLO, an online shoe store, wants to segment its customers and determine marketing strategies according to these 
segments. To this end, the behaviors of the customers will be defined and groups will be formed according to the 
clustering in these behaviors.


2. Story of Dataset

The dataset consists of information obtained from the past shopping behaviors of customers who made their last 
purchases from Flo as OmniChannel (both online and offline shopper) in the years 2020-2021.


3. Variables of Dataset

master_id: Unique client number
order_channel: Which channel of the shopping platform is used (Android, iOS, Desktop, Mobile)
last_order_channel: The channel where the last purchase was made
first_order_date: The date of the first purchase made by the customer
last_order_date: The date of the customer's last purchase
last_order_date_online: The date of the last purchase made by the customer on the online platform
last_order_date_offline: The date of the last purchase made by the customer on the offline platform
order_num_total_ever_online: The total number of purchases made by the customer on the online platform
order_num_total_ever_offline: Total number of purchases made by the customer offline
customer_value_total_ever_offline: The total price paid by the customer for offline purchases
customer_value_total_ever_online: The total price paid by the customer for their online shopping
interested_in_categories_12: List of categories the customer has purchased from in the last 12 months


Task 1: Understanding and Preparing Data


	Step 1: Read the flo_data_20K.csv data. Make a copy of the dataframe.
	Step 2: in the dataset
			a. first 10 observations,
			b. variable names,
			c. descriptive statistics,
			d. null value,
			e.variable types,
		do a review.
	Step 3: Omnichannel means that customers shop from both online and offline platforms. Create new variables 
	for each customer's total purchases and spending.
	Step 4: Examine the variable types. Change the type of variables that express date to date.
	Step 5: Examine the number of customers in the shopping channels, the total number of products purchased 
	and the distribution of total expenditures.
	Step 6: List the top 10 customers that generate the most revenue for the company.
	Step 7: List the top 10 customers with the most orders.
	Step 8: Functionalize the data preparation process.


Task 2: Calculating RFM Metrics


Task 3: Calculating RF Scores


Task 4: Defining RF Scores as Segments


Task 5: 
	Step 1: Examine the recency, frequency and monetary averages of the segments.

	Step 2: With the help of RFM analysis, find the customers in the relevant profile for the 2 cases given 
		below and save the customer IDs as csv.
			a. FLO includes a new women's shoe brand. The product prices of the brand it includes 
			are above the general customer preferences. For this reason, it is desired to contact 
			the customers in the profile that will be interested in the promotion of the brand and 
			product sales. Those who shop from their loyal customers(champions, loyal_customers) and 
			women category are the customers to be contacted specifically. Save the id numbers of 
			these customers to the csv file.

			b. Nearly 40% discount is planned for Men's and Children's products. It is aimed to 
			specifically target customers who are good customers in the past, but who have not 
			shopped for a long time, who are interested in the categories related to this discount, 
			who should not be lost, who are asleep and new customers. Save the ids of the customers 
			in the appropriate profile to the csv file.





