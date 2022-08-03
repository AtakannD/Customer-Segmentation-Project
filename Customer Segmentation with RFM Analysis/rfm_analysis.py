import pandas as pd
import datetime as dt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
df_ = pd.read_csv(r"C:\Users\atakan.dalkiran\PycharmProjects\Customer Segmentation with RFM Analysis\flo_data_20k.csv")
df = df_.copy()

# Task 1.1 - 1.2


def check_df(dataframe, head=10):
    """
    This function gives us a first look when we import our dataset.

    Parameters
    ----------
    dataframe: pandas.dataframe
    It is the dataframe from which variable names are wanted to be taken.
    head: int
    The variable that determines how many values we want to look at beginning

    Returns
    -------
    shape: tuple
    that variable gives us to dataset's information which how many columns and rows have
    type: pandas.series
    that variable gives us to our variables' types.
    columns: pandas.Index
    gives us the names of the columns in the dataset.
    head: pandas.Dataframe
    It gives us the variables and values of our dataset, starting from the zero index to the number we entered, as a dataframe.
    tail: pandas.Dataframe
    Contrary to head, this method counts us down starting from the index at the end.
    isnull().sum(): pandas.series
    It visits the variables in the data set and checks if there are any null values and gives us the statistics of how
    many of them are in each variable.
    quantile: pandas.dataframe
    It gives the range values of the variables in our data set as a percentage according to the values we entered.

    Examples
    --------
    The shape return output is given to us as a tuple (5000, 5).
    """
    print("######################### Shape #########################")
    print(dataframe.shape)
    print("\n######################### Type #########################")
    print(dataframe.dtypes)
    print("\n######################## Columns ########################")
    print(dataframe.columns)
    print("\n######################### Head #########################")
    print(dataframe.head(head))
    print("\n######################### Tail #########################")
    print(dataframe.tail(head))
    print("\n######################### NA #########################")
    print(dataframe.isnull().sum())
    print("\n######################### Quantiles #########################")
    print(dataframe.quantile([0, 0.25, 0.5, 0.75, 0.95, 1]).T)


check_df(df)

# Task 1.3

df["total_order"] = df["order_num_total_ever_online"] + df["order_num_total_ever_offline"]
df["total_price"] = df["customer_value_total_ever_offline"] + df["customer_value_total_ever_online"]

# Task 1.4

print(df.dtypes)
datecol_list = df.columns[df.columns.str.contains("date")]
df[datecol_list] = df[datecol_list].apply(pd.to_datetime)

# Task 1.5

df.groupby("order_channel").agg({"master_id": "count",
                                 "total_order": "sum",
                                 "total_price": "sum"})

# Task 1.6

df.sort_values(by="total_price", ascending=False).head(10)

# Task 1.7

df.sort_values(by="total_order", ascending=False).head(10)

# Task 1.8


def preparation_df(dataframe, head=10):
    # checking data
    check_df(dataframe, head=head)

    # preparing data to use
    dataframe["total_order"] = dataframe["order_num_total_ever_online"] + dataframe["order_num_total_ever_offline"]
    dataframe["total_price"] = dataframe["customer_value_total_ever_offline"] + \
                               dataframe["customer_value_total_ever_online"]
    datecol_list = dataframe.columns[dataframe.columns.str.contains("date")]
    dataframe[datecol_list] = dataframe[datecol_list].apply(pd.to_datetime)
    dataframe["order_channel"].value_counts()
    dataframe["total_order"].quantile([0, 0.25, 0.5, 0.75, 0.95, 1]).T
    dataframe["total_price"].quantile([0, 0.25, 0.5, 0.75, 0.95, 1]).T
    dataframe.sort_values(by="total_price", ascending=False).head(head)
    dataframe.sort_values(by="total_order", ascending=False).head(head)

    return dataframe


preparation_df(df)

# Task 2

today_date = dt.datetime(2021, 6, 1)
rfm = pd.DataFrame()
rfm["customer_id"] = df["master_id"]
rfm["recency"] = (today_date - df["last_order_date"]).astype('timedelta64[D]')
rfm["frequency"] = df["total_order"]
rfm["monetary"] = df["total_price"]
rfm.head()

# Task 3

rfm["recency_score"] = pd.qcut(rfm["recency"], 5, labels=[5, 4, 3, 2, 1])
rfm["frequency_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])
rfm["monetary_score"] = pd.qcut(rfm["monetary"], 5, labels=[5, 4, 3, 2, 1])

rfm["RF_SCORE"] = (rfm["recency_score"].astype(str) + rfm["frequency_score"].astype(str))

# Task 4

seg_map = {
    r'[1-2][1-2]': 'hibernating',
    r'[1-2][3-4]': 'at_Risk',
    r'[1-2]5': 'cant_loose',
    r'3[1-2]': 'about_to_sleep',
    r'33': 'need_attention',
    r'[3-4][4-5]': 'loyal_customers',
    r'41': 'promising',
    r'51': 'new_customers',
    r'[4-5][2-3]': 'potential_loyalist',
    r'5[4-5]': 'champions'
}

rfm["segment"] = rfm["RF_SCORE"].replace(seg_map, regex=True)

# Task 5.1

rfm.groupby("segment").agg({"recency": "mean",
                            "frequency": "mean",
                            "monetary": "mean"})

# Task 5.2.a
target_segment_customer_ids = rfm[rfm["segment"].isin(["champions", "loyal_customers"])]["customer_id"]

target_ids = df[(df["master_id"].isin(target_segment_customer_ids)) &
                (df["interested_in_categories_12"].str.contains("KADIN"))]["master_id"]
target_ids.to_csv("new-shoes-brand-target-cust-ids.csv", index=False)

# Task 5.2.b
cust_to_be_notified = rfm[rfm["segment"].isin(['cant_loose', 'about_to_sleep', 'new_customers'])]['customer_id']

cust_to_be_notified_ids = df[(df["master_id"].isin(cust_to_be_notified)) &
                             (df["interested_in_categories_12"].str.contains("ERKEK") |
                              (df["interested_in_categories_12"].str.contains("COCUK")))]["master_id"]
cust_to_be_notified_ids.to_csv("customer-to-be-notified-discount.csv", index=False)
