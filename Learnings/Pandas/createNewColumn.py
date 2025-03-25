import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # Create a new column 'bonus' with values that are twice the 'salary'
    employees['bonus'] = employees['salary'] * 2
    return employees