from dune_client.client import DuneClient
import pandas as pd


dune = DuneClient("OFmmvt1cFUQGznqYGG1JvgQHHILUK9IB")

def json_to_dataframe(json_data):
    # Extracting the rows from the JSON data
    rows = json_data.result.rows
    
    # Creating a DataFrame from the extracted rows
    df = pd.DataFrame(rows)
    df.fillna(0, inplace=True)
    
    return df


def fetch_stake_data():
    stake_shares_by_entity_query = dune.get_latest_result(2394100)
    stake_shares_by_entity_df = json_to_dataframe(stake_shares_by_entity_query)

    stake_by_category = stake_shares_by_entity_df.groupby('entity_category')['amount_staked'].sum().reset_index()
    return stake_by_category