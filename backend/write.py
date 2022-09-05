import pandas as pd

# write 2 value to a csv file
def write_csv(Name: str, Password: str, inputParams):
    extraData = inputParams
    df = pd.DataFrame({'Device Name': [Name], 'Password': [Password], 'Input Params' : [extraData]})
    df.to_csv('backend\decorator.csv', mode='a', index=False, header=False)