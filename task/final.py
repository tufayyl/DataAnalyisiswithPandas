import pandas as pd
import mysql.connector
import plotly.express as px
from sqlalchemy import create_engine

def create_bar_graph(df, x_col, y_col, title):
    fig = px.bar(df, x=x_col, y=y_col, title=title)
    fig.show()
    
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="VIT@tufayl2005",
    database="test"
)
cursor = db.cursor()

file_path = r"C:\Users\tufay\OneDrive\Desktop\task\draft.xlsx"
df = pd.read_excel(file_path)


table_name = "data"
create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
for column in df.columns:
    column_name = column.replace(" ", "_")
    if pd.api.types.is_datetime64_any_dtype(df[column]):
        create_table_query += f"`{column_name}` DATE, "
    elif pd.api.types.is_integer_dtype(df[column]):
        create_table_query += f"`{column_name}` INT, "
    else:
        create_table_query += f"`{column_name}` VARCHAR(255), "
create_table_query = create_table_query[:-2] + ")"
cursor.execute(create_table_query)


for index, row in df.iterrows():
    sql = f"INSERT INTO {table_name} ({', '.join(['`'+col.replace(' ', '_')+'`' for col in df.columns])}) VALUES ({', '.join(['%s']*len(df.columns))})"
    values = tuple(row)
    cursor.execute(sql, values)

db.commit()


query = """
SELECT 
    DATE_FORMAT(reported_date, '%Y-%m') AS month,
    type,
    COUNT(*) AS count
FROM 
    data
GROUP BY 
    month,
    type
ORDER BY 
    month
"""
df = pd.read_sql_query(query, db)


fig = px.line(df, x='month', y='count', color='type', title='Month-on-Month Trend Line by Type')
fig.show()

column_head = 'area'
query = f"""
SELECT 
    `{column_head.replace(' ', '_')}`,
    COUNT(*) AS count
FROM 
    data
GROUP BY 
    `{column_head.replace(' ', '_')}`
"""
df = pd.read_sql_query(query, db)
fig = px.bar(df, x=column_head.replace(' ', '_'), y='count', title=f'Count of Records by {column_head.capitalize()}')

query = """
SELECT 
    DATE_FORMAT(reported_date, '%Y-%m') AS month,
    type,
    COUNT(*) AS count
FROM 
    data
GROUP BY 
    month,
    type
ORDER BY 
    month
"""
cursor.execute(query)
rows = cursor.fetchall()
df = pd.DataFrame(rows, columns=['month', 'type', 'count'])

fig = px.line(df, x='month', y='count', color='type', title='Month-on-Month Trend Line by Type')
fig.show()

column_head = 'type'
query = f"""
SELECT 
    `{column_head.replace(' ', '_')}`,
    COUNT(*) AS count
FROM 
    data
GROUP BY 
    `{column_head.replace(' ', '_')}`
"""
cursor.execute(query)
rows = cursor.fetchall()
df = pd.DataFrame(rows, columns=[column_head.replace(' ', '_'), 'count'])

create_bar_graph(df, x_col=column_head.replace(' ', '_'), y_col='count', title=f'Count of Records by {column_head.capitalize()}')


categories = ['area', 'status', 'rating']  
for category in categories:
    query = f"""
    SELECT 
        `{category}`,
        COUNT(*) AS count
    FROM 
        data
    GROUP BY 
        `{category}`
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=[category, 'count'])
    create_bar_graph(df, x_col=category, y_col='count', title=f'Bar Graph by {category.capitalize()}')

fig.show()
db.close()
