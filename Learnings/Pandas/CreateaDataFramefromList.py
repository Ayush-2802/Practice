import pandas as pd


# df = pd.DataFrame(data, columns=['Numbers'])
def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data,columns=['student_id','age'])
    