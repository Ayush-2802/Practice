import pandas as pd 
# Create a DataFrame with student information
data = {
    'student_id': [101, 102, 103, 104],
    'name': ['John', 'Emma', 'Michael', 'Sophia'],
    'age': [20, 21, 19, 22],
    'grade': ['A', 'B', 'A-', 'B+']
}
df = pd.DataFrame(data)

# Select the name and age of the student with student_id = 101
result = df.loc[df['student_id'] == 101, ['name', 'age']]
print(result)

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    column = ["name","age"]
    return students.loc[students['student_id']==101, column]