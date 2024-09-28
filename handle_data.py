import pandas as pd


def get_input_df():
    df = pd.read_csv('input_output_data/Input.csv')
    return df


def get_output_df():
    df = pd.read_csv('input_output_data/Output_Data_Structure.csv')
    return df


