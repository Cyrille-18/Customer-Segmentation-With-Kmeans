import pandas as pd 
import datetime

def create_features(df):
    """
    Build derived features from raw customer data.

    Adds Age, Total_Children, Total_Spending, Customer_since,
    accepted_campaigns, and Age_Group to the DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned raw dataset.

    Returns
    -------
    pd.DataFrame
        Original DataFrame with new feature columns appended.
    """
    
    # Work on a copy of the dataset
    df = df.copy()

    # Calculate customer age
    df["Age"] = datetime.date.today().year - df["Year_Birth"]

    # Total number of children in the household
    df["Total_Children"] = df["Kidhome"] + df["Teenhome"]

    # Product spending columns
    spending_columns = [
        "MntWines",
        "MntFruits",
        "MntMeatProducts",
        "MntFishProducts",
        "MntSweetProducts",
        "MntGoldProds"
    ]

     # Calculate total spending
    df["Total_Spending"] = df[spending_columns].sum(axis=1)

    # Calculate customer tenure in days
    df["Customer_since"] = (
        pd.Timestamp.today() - df["Dt_Customer"]
    ).dt.days

     # Campaign response columns
    campaigns = [
        "AcceptedCmp1",
        "AcceptedCmp2",
        "AcceptedCmp3",
        "AcceptedCmp4",
        "AcceptedCmp5",
        "Response"
    ]

    # Flag customers who accepted at least one campaign
    df["accepted_campaigns"] = (
        df[campaigns].sum(axis=1) > 0
    ).astype(int)

  # Create age groups
    bins = [18, 30, 40, 50, 60, 70, 90]
    labels = ["18-29", "30-39", "40-49", "50-59", "60-69", "70+"]

    df["Age_Group"] = pd.cut(
        df["Age"],
        bins=bins,
        labels=labels
    )

    return df
