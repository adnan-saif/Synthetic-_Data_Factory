import streamlit as st
import pandas as pd
from backend import UniversalDataGenerator, DatabaseHandler, DataValidator


def main():
    st.set_page_config(
        page_title="Synthetic Data Factory",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Load custom CSS
    with open(r"C:\Users\eengi\Desktop\SB Projects\SDF\static\styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
    # Initialize session state
    if 'generator' not in st.session_state:
        st.session_state.generator = UniversalDataGenerator()
    if 'db_handler' not in st.session_state:
        st.session_state.db_handler = DatabaseHandler(st.session_state.generator)
    if 'validator' not in st.session_state:
        st.session_state.validator = DataValidator()
    if 'synthetic_data' not in st.session_state:
        st.session_state.synthetic_data = None
    
    # Header
    st.markdown('<h1 class="main-header">Synthetic Data Factory</h1>', unsafe_allow_html=True)
    st.markdown('<h6 class="main-header">Generate intelligent, realistic, and statistically balanced synthetic data — with precision and style.</h1>', unsafe_allow_html=True)
    st.markdown(" ")

    # Main Tabs Navigation
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Home", 
        "CSV Extension", 
        "Dummy Data Creation", 
        "MySQL Operations", 
        "About"
    ])
    
    with tab1:
        home_page()
    with tab2:
        csv_extension_page()
    with tab3:
        dummy_data_creation_page()
    with tab4:
        mysql_operations_page()
    with tab5:
        about_page()


def home_page():
    st.markdown("""
    <div style='margin-bottom: 2rem;'>
        <div style='
            background: linear-gradient(135deg, #20B2AA 0%, #8A2BE2 100%);
            padding: 2.5rem;
            border-radius: 15px;
            color: white;
            width: 100%;
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
            text-align: center;
        '>
            <h3 style='margin: 0 0 1rem 0; font-size: 1.5rem;'>Generate Smart Synthetic Data</h3>
            <p style='margin: 0; font-size: 1.1rem; opacity: 0.95;'>
                Create realistic, statistically validated datasets for testing, development, and machine learning applications
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Statistics Section
    st.markdown("""
    <div style='text-align: left; margin-bottom: 3rem;'>
        <h2 style='color: #2c3e50; margin-bottom: 2rem; font-size: 2rem; font-weight: 600;'>Why Choose Our Data Generator?</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style='
            background: white;
            padding: 2.5rem 1.5rem;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 8px 25px rgba(0,0,0,0.08);
            border: 1px solid #f0f0f0;
            height: 100%;
        '>
            <div style='font-size: 3rem; font-weight: 800; color: #667eea; margin-bottom: 1rem;'>100+</div>
            <div style='color: #5d6d7e; font-weight: 600; font-size: 1.1rem;'>Data Types Supported</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='
            background: white;
            padding: 2.5rem 1.5rem;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 8px 25px rgba(0,0,0,0.08);
            border: 1px solid #f0f0f0;
            height: 100%;
        '>
            <div style='font-size: 3rem; font-weight: 800; color: #f093fb; margin-bottom: 1rem;'>50x</div>
            <div style='color: #5d6d7e; font-weight: 600; font-size: 1.1rem;'>Faster Generation</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='
            background: white;
            padding: 2.5rem 1.5rem;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 8px 25px rgba(0,0,0,0.08);
            border: 1px solid #f0f0f0;
            height: 100%;
        '>
            <div style='font-size: 3rem; font-weight: 800; color: #4facfe; margin-bottom: 1rem;'>24/7</div>
            <div style='color: #5d6d7e; font-weight: 600; font-size: 1.1rem;'>Availability</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Features Section
    st.markdown("""
    <div style='text-align: left; margin-bottom: 3rem;'>
        <h2 style='color: #2c3e50; margin-bottom: 2rem; font-size: 2rem; font-weight: 600;'>Core Features</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style='
            background: white;
            padding: 2.5rem;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            border: 1px solid #e8e8e8;
            height: 100%;
            transition: transform 0.3s ease;
        '>
            <div style='font-size: 2.5rem; color: #667eea; margin-bottom: 1.5rem; font-weight: 600;'>📊</div>
            <h3 style='color: #2c3e50; margin-bottom: 1rem; font-size: 1.3rem; font-weight: 600;'>CSV Data Extension</h3>
            <p style='color: #5d6d7e; line-height: 1.6; margin: 0; font-size: 0.95rem;'>
                Upload CSV files and generate extended synthetic data that maintains original statistical properties and distributions.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='
            background: white;
            padding: 2.5rem;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            border: 1px solid #e8e8e8;
            height: 100%;
            transition: transform 0.3s ease;
        '>
            <div style='font-size: 2.5rem; color: #f093fb; margin-bottom: 1.5rem; font-weight: 600;'>✨</div>
            <h3 style='color: #2c3e50; margin-bottom: 1rem; font-size: 1.3rem; font-weight: 600;'>Custom Data Creation</h3>
            <p style='color: #5d6d7e; line-height: 1.6; margin: 0; font-size: 0.95rem;'>
                Create high-quality synthetic datasets from scratch using AI-powered column detection and intelligent data generation.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='
            background: white;
            padding: 2.5rem;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            border: 1px solid #e8e8e8;
            height: 100%;
            transition: transform 0.3s ease;
        '>
            <div style='font-size: 2.5rem; color: #4facfe; margin-bottom: 1.5rem; font-weight: 600;'>🗄️</div>
            <h3 style='color: #2c3e50; margin-bottom: 1rem; font-size: 1.3rem; font-weight: 600;'>MySQL Database Integration</h3>
            <p style='color: #5d6d7e; line-height: 1.6; margin: 0; font-size: 0.95rem;'>
                Connect to MySQL databases, generate synthetic data based on table schemas, and insert directly into databases.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # How It Works Section
    st.markdown("""
    <div style='text-align: left; margin-bottom: 3rem;'>
        <h2 style='color: #2c3e50; margin-bottom: 2rem; font-size: 2rem; font-weight: 600;'>How It Works</h2>
    </div>
    """, unsafe_allow_html=True)
    
    steps_col1, steps_col2, steps_col3, steps_col4 = st.columns(4)
    
    with steps_col1:
        st.markdown("""
        <div style='
            background: white;
            padding: 2rem 1.5rem;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 8px 25px rgba(0,0,0,0.08);
            border-top: 4px solid #667eea;
            height: 100%;
        '>
            <div style='font-size: 2.5rem; font-weight: 800; color: #667eea; margin-bottom: 1rem;'>01</div>
            <h4 style='color: #2c3e50; margin-bottom: 1rem; font-size: 1.2rem; font-weight: 600;'>Choose Source</h4>
            <p style='color: #5d6d7e; margin: 0; font-size: 0.9rem; line-height: 1.5;'>
                Select from CSV upload, manual column creation, or database connection
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with steps_col2:
        st.markdown("""
        <div style='
            background: white;
            padding: 2rem 1.5rem;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 8px 25px rgba(0,0,0,0.08);
            border-top: 4px solid #f093fb;
            height: 100%;
        '>
            <div style='font-size: 2.5rem; font-weight: 800; color: #f093fb; margin-bottom: 1rem;'>02</div>
            <h4 style='color: #2c3e50; margin-bottom: 1rem; font-size: 1.2rem; font-weight: 600;'>Configure</h4>
            <p style='color: #5d6d7e; margin: 0; font-size: 0.9rem; line-height: 1.5;'>
                Set rows, validation options, and output preferences for your available dataset
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with steps_col3:
        st.markdown("""
        <div style='
            background: white;
            padding: 2rem 1.5rem;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 8px 25px rgba(0,0,0,0.08);
            border-top: 4px solid #4facfe;
            height: 100%;
        '>
            <div style='font-size: 2.5rem; font-weight: 800; color: #4facfe; margin-bottom: 1rem;'>03</div>
            <h4 style='color: #2c3e50; margin-bottom: 1rem; font-size: 1.2rem; font-weight: 600;'>Generate</h4>
            <p style='color: #5d6d7e; margin: 0; font-size: 0.9rem; line-height: 1.5;'>
                Watch as we create and validate your synthetic data with quality metrics
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with steps_col4:
        st.markdown("""
        <div style='
            background: white;
            padding: 2rem 1.5rem;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 8px 25px rgba(0,0,0,0.08);
            border-top: 4px solid #43e97b;
            height: 100%;
        '>
            <div style='font-size: 2.5rem; font-weight: 800; color: #43e97b; margin-bottom: 1rem;'>04</div>
            <h4 style='color: #2c3e50; margin-bottom: 1rem; font-size: 1.2rem; font-weight: 600;'>Download</h4>
            <p style='color: #5d6d7e; margin: 0; font-size: 0.9rem; line-height: 1.5;'>
                Export your data or insert directly into databases for immediate use of dataset
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("""
    <div style='
        text-align: center;
        padding: 4rem 2rem;
        background: linear-gradient(135deg, #20B2AA 0%, #8A2BE2 100%);
        color: white;
        border-radius: 20px;
        margin: 2rem 0;
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.2);
    '>
        <h2 style='font-size: 2.2rem; margin-bottom: 1.5rem; font-weight: 600;'>Ready to Generate Amazing Data?</h2>
        <p style='font-size: 1.2rem; margin-bottom: 0; opacity: 0.95; line-height: 1.6;'>
            Choose your preferred method from the tabs above and start creating high-quality synthetic datasets today
        </p>
    </div>
    """, unsafe_allow_html=True)


def csv_extension_page():
    st.markdown("""
    <div style='margin-bottom: 2rem;'>
        <div style='
            background: linear-gradient(135deg, #20B2AA 0%, #8A2BE2 100%);
            padding: 2.5rem;
            border-radius: 15px;
            color: white;
            width: 100%;
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
            text-align: center;
        '>
            <h3 style='margin: 0 0 1rem 0; font-size: 1.5rem;'>Extend Your Existing Data</h3>
            <p style='margin: 0; font-size: 1.1rem; opacity: 0.95;'>
                Upload your CSV files and generate extended synthetic data that maintains original statistical properties and distributions.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("Upload CSV File", type=['csv'])
    st.markdown(" ")
    
    if uploaded_file is not None:
        with open("temp_upload.csv", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        original_df = pd.read_csv("temp_upload.csv")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Original Rows", len(original_df))
        with col2:
            st.metric("Columns", len(original_df.columns))
        
        with st.expander("Original Data Preview", expanded=True):
            st.dataframe(original_df.head(), use_container_width=True)
        
        st.markdown("### Generation Settings")
        col1, col2 = st.columns(2)
        
        with col1:
            num_rows = st.number_input("Number of Synthetic Rows", min_value=1, value=200, step=100)
        with col2:
            output_file = st.text_input("Output Filename", value="synthetic_data.csv")
        
        validate = st.checkbox("Run Validation", value=True)
        
        if st.button("Generate Synthetic Data", type="primary", use_container_width=True):
            with st.spinner("Generating synthetic data..."):
                synthetic_df, original_df_full = st.session_state.generator.generate_from_csv(
                    "temp_upload.csv", 
                    num_rows, 
                    validate=False
                )
                
                if synthetic_df is not None:
                    st.session_state.synthetic_data = synthetic_df
                    
                    if validate and original_df_full is not None:
                        st.session_state.validator.validate_synthetic_data(original_df_full, synthetic_df)
        
        if st.session_state.synthetic_data is not None:
            st.markdown("### Download Generated Data")
            csv = st.session_state.synthetic_data.to_csv(index=False)
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name=output_file,
                mime="text/csv",
                use_container_width=True
            )


def dummy_data_creation_page():
    st.markdown("""
    <div style='margin-bottom: 2rem;'>
        <div style='
            background: linear-gradient(135deg, #20B2AA 0%, #8A2BE2 100%);
            padding: 2.5rem;
            border-radius: 15px;
            color: white;
            width: 100%;
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
            text-align: center;
        '>
            <h3 style='margin: 0 0 1rem 0; font-size: 1.5rem;'>Create Custom Datasets</h3>
            <p style='margin: 0; font-size: 1.1rem; opacity: 0.95;'>
                Enter column names and let our intelligent system automatically detect the best data type for each column.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    columns_input = st.text_area(
        "Enter Column Names (one per line or comma-separated)",
        height=80,
        placeholder="name, email, age, salary, city, phone_number"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        num_rows = st.number_input("Number of Rows", min_value=1, value=200, step=100)
    
    with col2:
        output_file = st.text_input("Output Filename", value="dummy_data.csv")
    
    if st.button("Generate dummy Data", type="primary", use_container_width=True):
        if columns_input:
            columns = []
            if ',' in columns_input:
                columns = [col.strip() for col in columns_input.split(',') if col.strip()]
            else:
                columns = [col.strip() for col in columns_input.split('\n') if col.strip()]
            
            if columns:
                with st.spinner(f"Generating {num_rows} rows with {len(columns)} columns..."):
                    synthetic_df = st.session_state.generator.generate_from_columns(columns, num_rows)
                    st.session_state.synthetic_data = synthetic_df
                
                if st.session_state.synthetic_data is not None:
                    st.markdown("### Download Generated Data")
                    csv = st.session_state.synthetic_data.to_csv(index=False)
                    st.download_button(
                        label="Download CSV",
                        data=csv,
                        file_name=output_file,
                        mime="text/csv",
                        use_container_width=True
                    )
            else:
                st.error("Please enter at least one column name.")
        else:
            st.error("Please enter column names.")


def mysql_operations_page():
    st.markdown("""
    <div style='margin-bottom: 2rem;'>
        <div style='
            background: linear-gradient(135deg, #20B2AA 0%, #8A2BE2 100%);
            padding: 2.5rem;
            border-radius: 15px;
            color: white;
            width: 100%;
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
            text-align: center;
        '>
            <h3 style='margin: 0 0 1rem 0; font-size: 1.5rem;'>Database Integration</h3>
            <p style='margin: 0; font-size: 1.1rem; opacity: 0.95;'>
                Connect to your MySQL database and generate synthetic data based on existing table schemas.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Database connection
    st.subheader("Database Connection")
    col1, col2 = st.columns(2)
    
    with col1:
        host = st.text_input("Host", value="localhost")
        password = st.text_input("Password", type="password")
    with col2:
        user = st.text_input("Username", value="root")
        database = st.text_input("Database", value="test")
    
    if st.button("Connect to Database", use_container_width=True):
        with st.spinner("Connecting to database..."):
            connection = st.session_state.db_handler.connect_to_mysql(host, user, password, database)
            if connection:
                st.session_state.db_connection = connection
                st.session_state.db_tables = st.session_state.db_handler.get_mysql_tables(connection)
    
    if 'db_connection' in st.session_state and st.session_state.db_connection:
        st.success("Connected to database!")
        
        if st.session_state.db_tables:
            st.subheader("Available Tables")
            selected_table = st.selectbox("Select Table", st.session_state.db_tables)
            
            if selected_table:
                # Show table schema
                schema = st.session_state.db_handler.get_table_schema(st.session_state.db_connection, selected_table)
                
                st.subheader("Table Schema")
                schema_df = pd.DataFrame.from_dict(schema, orient='index')
                st.dataframe(schema_df, use_container_width=True)
                
                num_rows = st.number_input("Number of Rows", min_value=1, value=100, key="mysql_rows")
                validate = st.checkbox("Run Validation", value=True, key="mysql_validate")
                insert_db = st.checkbox("Insert into Database", value=False)
                
                if st.button("Generate from Table Schema", type="primary", use_container_width=True):
                    with st.spinner(f"Generating data for table '{selected_table}'..."):
                        synthetic_df, original_df = st.session_state.db_handler.generate_from_mysql_table(
                            st.session_state.db_connection,
                            selected_table,
                            num_rows
                        )
                        st.session_state.synthetic_data = synthetic_df
                        
                        if synthetic_df is not None:
                            if validate and original_df is not None and len(original_df) > 0:
                                st.info(f"Validating against {len(original_df)} original rows...")
                                st.session_state.validator.validate_synthetic_data(original_df, synthetic_df)
                            
                            if insert_db:
                                success = st.session_state.db_handler.insert_to_mysql_table(
                                    st.session_state.db_connection,
                                    selected_table,
                                    synthetic_df
                                )
        
        # Close connection button
        if st.button("Close Connection", use_container_width=True):
            if 'db_connection' in st.session_state:
                st.session_state.db_connection.close()
                del st.session_state.db_connection
                if 'db_tables' in st.session_state:
                    del st.session_state.db_tables
            st.success("Connection closed.")

        # Download button for generated data
        if st.session_state.synthetic_data is not None:
            st.markdown("### Download Generated Data")
            csv_data = st.session_state.synthetic_data.to_csv(index=False)
            st.download_button(
                label="Download CSV",
                data=csv_data,
                file_name=f"{selected_table}_synthetic_data.csv",
                mime="text/csv",
                use_container_width=True,
                key="mysql_download"
            )


def about_page():
    st.markdown("""
    <div style='margin-bottom: 2rem;'>
        <div style='
            background: linear-gradient(135deg, #20B2AA 0%, #8A2BE2 100%);
            padding: 2.5rem;
            border-radius: 15px;
            color: white;
            width: 100%;
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
            text-align: center;
        '>
            <h3 style='margin: 0 0 1rem 0; font-size: 1.5rem;'>Transform Your Data Generation Process</h3>
            <p style='margin: 0; font-size: 1.1rem; opacity: 0.95;'>
                 A powerful, intelligent tool for generating high-quality synthetic data with statistical validation and quality metrics.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Key Features with Cards
    st.markdown("### Key Features")

    features_col1, features_col2 = st.columns(2)

    with features_col1:
        st.markdown("""
        <div style='
            background: white;
            padding: 1.5rem;
            border-radius: 12px;
            border-left: 4px solid #667eea;
            margin-bottom: 1rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        '>
            <h4 style='color: #2c3e50; margin: 0 0 0.8rem 0;'>Statistical Validation</h4>
            <ul style='color: #5d6d7e; margin: 0; padding-left: 1.2rem;'>
                <li>KS tests and distribution analysis</li>
                <li>Automated quality scoring</li>
                <li>Real-time validation metrics</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='
            background: white;
            padding: 1.5rem;
            border-radius: 12px;
            border-left: 4px solid #f093fb;
            margin-bottom: 1rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        '>
            <h4 style='color: #2c3e50; margin: 0 0 0.8rem 0;'>Multiple Data Sources</h4>
            <ul style='color: #5d6d7e; margin: 0; padding-left: 1.2rem;'>
                <li>CSV file upload and extension</li>
                <li>MySQL database integration</li>
                <li>Manual column specification</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='
            background: white;
            padding: 1.5rem;
            border-radius: 12px;
            border-left: 4px solid #4facfe;
            margin-bottom: 1rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        '>
            <h4 style='color: #2c3e50; margin: 0 0 0.8rem 0;'>Advanced Analytics</h4>
            <ul style='color: #5d6d7e; margin: 0; padding-left: 1.2rem;'>
                <li>Distribution comparisons</li>
                <li>Quality metrics dashboard</li>
                <li>Interactive visualizations</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with features_col2:
        st.markdown("""
        <div style='
            background: white;
            padding: 1.5rem;
            border-radius: 12px;
            border-left: 4px solid #ffd166;
            margin-bottom: 1rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        '>
            <h4 style='color: #2c3e50; margin: 0 0 0.8rem 0;'>Smart Data Generation</h4>
            <ul style='color: #5d6d7e; margin: 0; padding-left: 1.2rem;'>
                <li>AI-powered column type detection</li>
                <li>Pattern recognition in column names</li>
                <li>Context-aware data generation</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='
            background: white;
            padding: 1.5rem;
            border-radius: 12px;
            border-left: 4px solid #06d6a0;
            margin-bottom: 1rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        '>
            <h4 style='color: #2c3e50; margin: 0 0 0.8rem 0;'>Flexible Export Options</h4>
            <ul style='color: #5d6d7e; margin: 0; padding-left: 1.2rem;'>
                <li>CSV download</li>
                <li>Direct database insertion</li>
                <li>Custom output formats</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='
            background: white;
            padding: 1.5rem;
            border-radius: 12px;
            border-left: 4px solid #ef476f;
            margin-bottom: 1rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        '>
            <h4 style='color: #2c3e50; margin: 0 0 0.8rem 0;'>Privacy & Security</h4>
            <ul style='color: #5d6d7e; margin: 0; padding-left: 1.2rem;'>
                <li>Data anonymization</li>
                <li>Privacy-preserving analytics</li>
                <li>Secure data sharing</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Technology Stack
    st.markdown("### Technology Stack")

    tech_col1, tech_col2, tech_col3 = st.columns(3)

    with tech_col1:
        st.markdown("""
        <div style='
            background: linear-gradient(135deg, #20B2AA 0%, #8A2BE2 100%);
            padding: 1.5rem;
            border-radius: 12px;
            color: white;
            text-align: center;
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
            height: 100%;
        '>
            <h4 style='margin: 0 0 1rem 0;'>Backend</h4>
            <div style='background: rgba(255,255,255,0.2); padding: 0.5rem; border-radius: 6px; margin: 0.5rem 0;'>Python 3.9+</div>
            <div style='background: rgba(255,255,255,0.2); padding: 0.5rem; border-radius: 6px; margin: 0.5rem 0;'>Pandas & NumPy</div>
            <div style='background: rgba(255,255,255,0.2); padding: 0.5rem; border-radius: 6px; margin: 0.5rem 0;'>Scipy Statistics</div>
            <div style='background: rgba(255,255,255,0.2); padding: 0.5rem; border-radius: 6px; margin: 0.5rem 0;'>Faker Library</div>
        </div>
        """, unsafe_allow_html=True)

    with tech_col2:
        st.markdown("""
        <div style='
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            padding: 1.5rem;
            border-radius: 12px;
            color: white;
            text-align: center;
            box-shadow: 0 4px 12px rgba(240, 147, 251, 0.3);
            height: 100%;
        '>
            <h4 style='margin: 0 0 1rem 0;'>Frontend</h4>
            <div style='background: rgba(255,255,255,0.2); padding: 0.5rem; border-radius: 6px; margin: 0.5rem 0;'>Streamlit</div>
            <div style='background: rgba(255,255,255,0.2); padding: 0.5rem; border-radius: 6px; margin: 0.5rem 0;'>Plotly Charts</div>
            <div style='background: rgba(255,255,255,0.2); padding: 0.5rem; border-radius: 6px; margin: 0.5rem 0;'>Custom CSS</div>
            <div style='background: rgba(255,255,255,0.2); padding: 0.5rem; border-radius: 6px; margin: 0.5rem 0;'>Responsive Design</div>
        </div>
        """, unsafe_allow_html=True)

    with tech_col3:
        st.markdown("""
        <div style='
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            padding: 1.5rem;
            border-radius: 12px;
            color: white;
            text-align: center;
            box-shadow: 0 4px 12px rgba(79, 172, 254, 0.3);
            height: 100%;
        '>
            <h4 style='margin: 0 0 1rem 0;'>Database</h4>
            <div style='background: rgba(255,255,255,0.2); padding: 0.5rem; border-radius: 6px; margin: 0.5rem 0;'>PyMySQL</div>
            <div style='background: rgba(255,255,255,0.2); padding: 0.5rem; border-radius: 6px; margin: 0.5rem 0;'>MySQL</div>
            <div style='background: rgba(255,255,255,0.2); padding: 0.5rem; border-radius: 6px; margin: 0.5rem 0;'>Secure Connections</div>
            <div style='background: rgba(255,255,255,0.2); padding: 0.5rem; border-radius: 6px; margin: 0.5rem 0;'>Schema Analysis</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Use Cases with Tabs
    st.markdown("### Use Cases")

    use_case_tab1, use_case_tab2, use_case_tab3, use_case_tab4 = st.tabs([
        "Testing & Development", 
        "Data Science", 
        "Business Intelligence", 
        "Privacy & Security"
    ])

    with use_case_tab1:
        st.markdown("""
        <div style='background: #f8f9fa; padding: 1.5rem; border-radius: 10px;'>
            <h4 style='color: #2c3e50; margin-bottom: 1rem;'>Application Development & Testing</h4>
            <div style='display: grid; gap: 0.8rem;'>
                <div style='background: white; padding: 1rem; border-radius: 8px; border-left: 4px solid #667eea;'>
                    <strong>Application Testing</strong>
                    <p style='margin: 0.5rem 0 0 0; color: #7f8c8d;'>Generate realistic test data for comprehensive application testing</p>
                </div>
                <div style='background: white; padding: 1rem; border-radius: 8px; border-left: 4px solid #667eea;'>
                    <strong>Database Population</strong>
                    <p style='margin: 0.5rem 0 0 0; color: #7f8c8d;'>Populate development databases with meaningful sample data</p>
                </div>
                <div style='background: white; padding: 1rem; border-radius: 8px; border-left: 4px solid #667eea;'>
                    <strong>Performance Testing</strong>
                    <p style='margin: 0.5rem 0 0 0; color: #7f8c8d;'>Create large datasets for load and performance testing</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with use_case_tab2:
        st.markdown("""
        <div style='background: #f8f9fa; padding: 1.5rem; border-radius: 10px;'>
            <h4 style='color: #2c3e50; margin-bottom: 1rem;'>Data Science & Machine Learning</h4>
            <div style='display: grid; gap: 0.8rem;'>
                <div style='background: white; padding: 1rem; border-radius: 8px; border-left: 4px solid #f093fb;'>
                    <strong>Model Training</strong>
                    <p style='margin: 0.5rem 0 0 0; color: #7f8c8d;'>Augment training datasets for improved machine learning models</p>
                </div>
                <div style='background: white; padding: 1rem; border-radius: 8px; border-left: 4px solid #f093fb;'>
                    <strong>Data Augmentation</strong>
                    <p style='margin: 0.5rem 0 0 0; color: #7f8c8d;'>Expand limited datasets while preserving statistical properties</p>
                </div>
                <div style='background: white; padding: 1rem; border-radius: 8px; border-left: 4px solid #f093fb;'>
                    <strong>Algorithm Testing</strong>
                    <p style='margin: 0.5rem 0 0 0; color: #7f8c8d;'>Test algorithms on diverse synthetic datasets</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with use_case_tab3:
        st.markdown("""
        <div style='background: #f8f9fa; padding: 1.5rem; border-radius: 10px;'>
            <h4 style='color: #2c3e50; margin-bottom: 1rem;'>Business Intelligence & Analytics</h4>
            <div style='display: grid; gap: 0.8rem;'>
                <div style='background: white; padding: 1rem; border-radius: 8px; border-left: 4px solid #4facfe;'>
                    <strong>Report Generation</strong>
                    <p style='margin: 0.5rem 0 0 0; color: #7f8c8d;'>Create sample reports and dashboards with realistic data</p>
                </div>
                <div style='background: white; padding: 1rem; border-radius: 8px; border-left: 4px solid #4facfe;'>
                    <strong>Dashboard Development</strong>
                    <p style='margin: 0.5rem 0 0 0; color: #7f8c8d;'>Build interactive dashboards with synthetic business data</p>
                </div>
                <div style='background: white; padding: 1rem; border-radius: 8px; border-left: 4px solid #4facfe;'>
                    <strong>Scenario Analysis</strong>
                    <p style='margin: 0.5rem 0 0 0; color: #7f8c8d;'>Generate data for what-if analysis and business scenarios</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with use_case_tab4:
        st.markdown("""
        <div style='background: #f8f9fa; padding: 1.5rem; border-radius: 10px;'>
            <h4 style='color: #2c3e50; margin-bottom: 1rem;'>Privacy & Data Security</h4>
            <div style='display: grid; gap: 0.8rem;'>
                <div style='background: white; padding: 1rem; border-radius: 8px; border-left: 4px solid #ef476f;'>
                    <strong>Data Anonymization</strong>
                    <p style='margin: 0.5rem 0 0 0; color: #7f8c8d;'>Create anonymized versions of sensitive datasets</p>
                </div>
                <div style='background: white; padding: 1rem; border-radius: 8px; border-left: 4px solid #ef476f;'>
                    <strong>Privacy-Preserving Analytics</strong>
                    <p style='margin: 0.5rem 0 0 0; color: #7f8c8d;'>Generate GDPR/CCPA compliant synthetic data</p>
                </div>
                <div style='background: white; padding: 1rem; border-radius: 8px; border-left: 4px solid #ef476f;'>
                    <strong>Secure Data Sharing</strong>
                    <p style='margin: 0.5rem 0 0 0; color: #7f8c8d;'>Share realistic data without exposing sensitive information</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()