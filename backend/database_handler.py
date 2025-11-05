import pymysql
from pymysql import MySQLError
import pandas as pd
from typing import List, Dict, Any
import streamlit as st
import random


class DatabaseHandler:
    def __init__(self, data_generator):
        self.generator = data_generator
    
    def connect_to_mysql(self, host: str, user: str, password: str, database: str):
        try:
            connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            st.success("Successfully connected to MySQL database!")
            return connection
        except MySQLError as err:
            st.error(f"Failed to connect to database: {err}")
            return None

    def get_mysql_tables(self, connection) -> List[str]:
        try:
            with connection.cursor() as cursor:
                cursor.execute("SHOW TABLES")
                tables = [list(table.values())[0] for table in cursor.fetchall()]
                return tables
        except MySQLError as err:
            st.error(f"Error fetching tables: {err}")
            return []

    def get_table_schema(self, connection, table_name: str) -> Dict[str, Any]:
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"DESCRIBE {table_name}")
                schema = cursor.fetchall()
                
                schema_info = {}
                for column in schema:
                    schema_info[column['Field']] = {
                        'field': column['Field'],
                        'type': column['Type'],
                        'null': column['Null'],
                        'key': column['Key'],
                        'default': column['Default'],
                        'extra': column['Extra']
                    }
                return schema_info
        except MySQLError as err:
            st.error(f"Error fetching schema for {table_name}: {err}")
            return {}

    def generate_from_mysql_table(self, connection, table_name: str, num_rows: int = 200):
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        status_text.text(f"Generating synthetic data for table: {table_name}")
        
        schema = self.get_table_schema(connection, table_name)
        if not schema:
            return None, None
        
        status_text.text(f"Analyzing table schema: {len(schema)} columns")
        progress_bar.progress(25)

        original_data = self.get_table_data(connection, table_name, limit=1000)
        original_df = pd.DataFrame(original_data) if original_data else None
        
        synthetic_data = {}
        total_columns = len(schema)
        
        for i, (column_name, column_info) in enumerate(schema.items()):
            status_text.text(f"Generating: {column_name} ({i+1}/{total_columns})")
            progress_bar.progress(25 + int(50 * (i / total_columns)))
            synthetic_data[column_name] = self._generate_from_mysql_column(column_name, column_info, num_rows)
        
        synthetic_df = pd.DataFrame(synthetic_data)
        progress_bar.progress(100)
        
        status_text.text("Generation complete!")
        
        with st.expander("Synthetic Data Preview", expanded=True):
            st.dataframe(synthetic_df.head(10), use_container_width=True)
        
        return synthetic_df, original_df

    def insert_to_mysql_table(self, connection, table_name: str, dataframe: pd.DataFrame) -> bool:
        try:
            with connection.cursor() as cursor:
                columns = ', '.join(dataframe.columns)
                placeholders = ', '.join(['%s'] * len(dataframe.columns))
                insert_query = f"INSERT IGNORE INTO {table_name} ({columns}) VALUES ({placeholders})"
                data_tuples = [tuple(row) for row in dataframe.values]
                cursor.executemany(insert_query, data_tuples)
                connection.commit()
                
                st.success(f"Successfully inserted {cursor.rowcount} rows into {table_name}")
                return True
                
        except MySQLError as err:
            st.error(f"Error inserting data into {table_name}: {err}")
            connection.rollback()
            return False

    def get_table_data(self, connection, table_name: str, limit: int = 10):
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM {table_name} LIMIT {limit}")
                data = cursor.fetchall()
                return data
        except MySQLError as err:
            st.error(f"Error fetching data from {table_name}: {err}")
            return []

    def _generate_from_mysql_column(self, column_name: str, column_info: Dict[str, Any], num_rows: int):
        col_type = column_info['type'].lower()
        col_lower = column_name.lower()
        
        if 'auto_increment' in column_info['extra'].lower():
            return list(range(1, num_rows + 1))
        
        if column_info['key'] == 'PRI' and 'auto_increment' not in column_info['extra'].lower():
            return [f"PK_{i}" for i in range(1, num_rows + 1)]
        
        if 'int' in col_type:
            if any(word in col_lower for word in ['age', 'years']):
                return [random.randint(18, 80) for _ in range(num_rows)]
            elif any(word in col_lower for word in ['salary', 'price', 'amount', 'cost']):
                return [random.randint(1000, 100000) for _ in range(num_rows)]
            elif any(word in col_lower for word in ['id', 'code', 'number']):
                return [random.randint(1000, 9999) for _ in range(num_rows)]
            else:
                return [random.randint(1, 1000) for _ in range(num_rows)]
                
        elif 'float' in col_type or 'double' in col_type or 'decimal' in col_type:
            if any(word in col_lower for word in ['price', 'amount', 'rate', 'percentage']):
                return [round(random.uniform(1, 1000), 2) for _ in range(num_rows)]
            else:
                return [round(random.uniform(0, 100), 2) for _ in range(num_rows)]
                
        elif 'date' in col_type or 'time' in col_type:
            if 'date' in col_type:
                return [self.generator.fake.date_between(start_date='-5y', end_date='today').strftime('%Y-%m-%d') for _ in range(num_rows)]
            else:
                return [self.generator.fake.time(pattern='%H:%M:%S') for _ in range(num_rows)]
                
        elif 'bool' in col_type or 'tinyint(1)' in col_type:
            return [random.choice([True, False]) for _ in range(num_rows)]
            
        else: 
            return self.generator._generate_from_column_name(column_name, num_rows)