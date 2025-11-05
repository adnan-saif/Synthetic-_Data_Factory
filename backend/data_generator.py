import pandas as pd
import numpy as np
from faker import Faker
import random
from typing import List
import streamlit as st
from datetime import datetime


class UniversalDataGenerator:
    def __init__(self):
        self.fake = Faker()
    
    def generate_from_csv(self, csv_file: str, num_rows: int = 200, validate: bool = True):
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        status_text.text("Uploading CSV file...")
        
        try:
            original_df = pd.read_csv(csv_file)
            progress_bar.progress(25)
            
            status_text.text("Analyzing data structure...")
            
            with st.expander("Original Data Preview", expanded=True):
                st.write(f"**Dataset Info:** {len(original_df)} rows, {len(original_df.columns)} columns")
                st.dataframe(original_df.head(), use_container_width=True)
            
            synthetic = {}
            total_columns = len(original_df.columns)
            
            for i, col in enumerate(original_df.columns):
                status_text.text(f"Generating column: {col} ({i+1}/{total_columns})")
                progress_bar.progress(25 + int(25 * i / total_columns))
                
                if pd.api.types.is_numeric_dtype(original_df[col]):
                    synthetic[col] = self._generate_numeric_data(original_df[col], num_rows)
                elif pd.api.types.is_string_dtype(original_df[col]) or pd.api.types.is_object_dtype(original_df[col]):
                    synthetic[col] = self._generate_text_data(col, original_df[col], num_rows)
                else:
                    synthetic[col] = [f"Data_{i}" for i in range(num_rows)]
            
            synthetic_df = pd.DataFrame(synthetic)
            
            status_text.text("Processing relationships between columns...")
            progress_bar.progress(75)
            
            synthetic_df = self._handle_age_dob_relationship(synthetic_df)
            
            progress_bar.progress(100)
            
            status_text.text("Generation complete!")

            with st.expander("Synthetic Data Preview", expanded=True):
                st.dataframe(synthetic_df.head(10), use_container_width=True)
            
            return synthetic_df, original_df
        
        except Exception as e:
            st.error(f"Error reading CSV file: {e}")
            return None, None

    def generate_from_columns(self, columns: List[str], num_rows: int = 200):
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        status_text.text(f"Generating data for {len(columns)} columns...")
        
        synthetic = {}
        total_columns = len(columns)
        
        for i, col in enumerate(columns):
            status_text.text(f"Generating: {col} ({i+1}/{total_columns})")
            progress_bar.progress(50)
            synthetic[col] = self._generate_from_column_name(col, num_rows)
        
        synthetic_df = pd.DataFrame(synthetic)
        
        status_text.text("Processing relationships between columns...")
        progress_bar.progress(75)
        
        synthetic_df = self._handle_age_dob_relationship(synthetic_df)
        
        progress_bar.progress(100)
        
        status_text.text("Generation complete!")
        
        with st.expander("Generated Data Preview", expanded=True):
            st.dataframe(synthetic_df.head(10), use_container_width=True)
        
        return synthetic_df

    def _handle_age_dob_relationship(self, df: pd.DataFrame) -> pd.DataFrame:
        columns_lower = [col.lower() for col in df.columns]
        
        has_age = any('age' in col for col in columns_lower)
        has_dob = any('dob' in col or 'date_of_birth' in col for col in columns_lower)
        
        if has_age and has_dob:
            age_col = next(col for col in df.columns if 'age' in col.lower())
            dob_col = next(col for col in df.columns if 'dob' in col.lower() or 'date_of_birth' in col.lower())
            
            current_year = datetime.now().year
            
            dob_list = []
            for age in df[age_col]:
                try:
                    birth_year = current_year - int(age)
                    random_month = random.randint(1, 12)
                    if random_month == 2:
                        max_day = 28 if birth_year % 4 != 0 else 29
                    elif random_month in [4, 6, 9, 11]:
                        max_day = 30
                    else:
                        max_day = 31
                    
                    random_day = random.randint(1, max_day)
                    
                    dob = f"{birth_year}-{random_month:02d}-{random_day:02d}"
                    dob_list.append(dob)
                    
                except (ValueError, TypeError):
                    random_year = random.randint(current_year - 80, current_year - 18)
                    random_month = random.randint(1, 12)
                    random_day = random.randint(1, 28) 
                    dob_list.append(f"{random_year}-{random_month:02d}-{random_day:02d}")
            
            df[dob_col] = dob_list
        
        return df

    def _generate_numeric_data(self, column_data: pd.Series, num_rows: int):
        clean_data = column_data.dropna()
        
        if len(clean_data) == 0:
            if pd.api.types.is_integer_dtype(column_data):
                return np.random.randint(0, 100, num_rows)
            else:
                return np.round(np.random.uniform(0, 100, num_rows), 2)
        
        min_val = clean_data.min()
        max_val = clean_data.max()
        mean_val = clean_data.mean()
        std_val = clean_data.std()
        
        if std_val > 0:
            generated = np.random.normal(mean_val, std_val, num_rows)
        else:
            generated = np.random.uniform(min_val, max_val, num_rows)
        
        generated = np.clip(generated, min_val * 0.8, max_val * 1.2)
        
        if pd.api.types.is_integer_dtype(column_data):
            return generated.astype(int)
        else:
            return np.round(generated, 2)

    def _generate_text_data(self, column_name: str, column_data: pd.Series, num_rows: int):
        clean_data = column_data.dropna()
        
        if len(clean_data) > 0 and clean_data.nunique() <= 15:
            return np.random.choice(clean_data.unique(), num_rows)
        
        return self._generate_from_column_name(column_name, num_rows)

    def _generate_from_column_name(self, column_name: str, num_rows: int):
        col_lower = column_name.lower()
        
        faker_methods = {
            # Personal Information
            'name': self.fake.name,
            'first_name': self.fake.first_name,
            'last_name': self.fake.last_name,
            'full_name': self.fake.name,
            'username': self.fake.user_name,
            'password': self.fake.password,
            
            # Contact Information
            'email': self.fake.email,
            'phone': lambda: f"{random.randint(6000000000, 9999999999)}",
            'mobile': lambda: f"{random.randint(6000000000, 9999999999)}",
            
            # Location Information
            'address': lambda: self.fake.address().replace('\n', ', '),
            'street': self.fake.street_address,
            'city': self.fake.city,
            'state': self.fake.state,
            'country': self.fake.country,
            'zip': self.fake.zipcode,
            'postal': self.fake.postcode,
            'location': self.fake.city,
            
            # Company & Professional
            'company': self.fake.company,
            'job': self.fake.job,
            'job_title': self.fake.job,
            'industry': self.fake.bs,
            
            # Financial
            'credit_card': self.fake.credit_card_number,
            'iban': self.fake.iban,
            'currency': self.fake.currency_code,
            
            # Internet & Tech
            'url': self.fake.url,
            'website': self.fake.url,
            'domain': self.fake.domain_name,
            'ip': self.fake.ipv4,
            'user_agent': self.fake.user_agent,
            
            # Dates & Times
            'date': self.fake.date,
            'time': self.fake.time,
            'year': lambda: self.fake.year(),
            'month': lambda: self.fake.month_name(),

            # Date of Birth variations
            'dob': self.fake.date_of_birth,
            'date_of_birth': self.fake.date_of_birth,
            'birth_date': self.fake.date_of_birth,
            'birthdate': self.fake.date_of_birth,
            'birthday': self.fake.date_of_birth,

            # Products & Commerce
            'product': self.fake.word,
            'brand': self.fake.company,
            'color': self.fake.color_name,
            
            # Education
            'school': self.fake.company,
            'university': self.fake.company,
            'grade': lambda: random.choice(['A', 'B', 'C', 'D', 'F']),
            
            # Medical
            'hospital': self.fake.company,
            'doctor': self.fake.name,
            'disease': lambda: random.choice(['Flu', 'Cold', 'Headache', 'Fever', 'Allergy']),
            
            # Vehicles
            'car': lambda: f"{self.fake.company()} {self.fake.word()}",
            'license': self.fake.license_plate,
            
            # Identification
            'id': lambda: f"ID_{self.fake.random_int(1000, 9999)}",
            'ssn': self.fake.ssn,
            'passport': self.fake.passport_number,
            
            # Numeric types
            'age': lambda: random.randint(18, 70),
            'salary': lambda: random.randint(30000, 150000),
            'price': lambda: round(random.uniform(10, 1000), 2),
            'quantity': lambda: random.randint(1, 100),
            'score': lambda: random.randint(0, 100),
            'rating': lambda: random.randint(1, 5),
            'serial': lambda: f"SN{self.fake.random_number(digits=8)}",
            
            # Boolean types
            'is_': lambda: random.choice([True, False]),
            'has_': lambda: random.choice([True, False]),
            'active': lambda: random.choice([True, False]),
            'status': lambda: random.choice(['Active', 'Inactive', 'Pending']),
        }
        
        for pattern, faker_method in faker_methods.items():
            if pattern in col_lower:
                try:
                    return [faker_method() for _ in range(num_rows)]
                except:
                    continue
        
        if any(word in col_lower for word in ['first', 'given']):
            return [self.fake.first_name() for _ in range(num_rows)]
        elif any(word in col_lower for word in ['last', 'surname', 'family']):
            return [self.fake.last_name() for _ in range(num_rows)]
        elif any(word in col_lower for word in ['street', 'road', 'avenue']):
            return [self.fake.street_address() for _ in range(num_rows)]
        elif any(word in col_lower for word in ['state', 'province', 'region']):
            return [self.fake.state() for _ in range(num_rows)]
        elif any(word in col_lower for word in ['gender', 'sex']):
            return [random.choice(['Male', 'Female']) for _ in range(num_rows)]
        
        elif any(word in col_lower for word in ['number', 'count', 'total', 'amount']):
            return [random.randint(1, 1000) for _ in range(num_rows)]
        elif any(word in col_lower for word in ['percent', 'percentage', 'rate']):
            return [round(random.uniform(0, 100), 2) for _ in range(num_rows)]
        
        else:
            return [self.fake.word() for _ in range(num_rows)]