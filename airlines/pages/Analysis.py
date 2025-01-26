import streamlit as st
import pandas as pd
import plotly.express as px

# Set up the Streamlit page configuration
st.set_page_config(
    layout='wide',
    page_title='Analysis Dashboard',
    page_icon='📊'
)

st.sidebar.success('Select page above')
st.markdown('<h1 style="text-align:center; color: #4169E1;">Analysis</h1>', unsafe_allow_html=True)

# Create tabs for different analyses
tap1, tap2 = st.tabs(['📈 Stats', '📊 Analysis'])

# Load and preprocess the data
df = pd.read_csv('df1.csv')
df.drop('Unnamed: 0', axis=1, inplace=True)

# Adding filters to the sidebar
st.sidebar.header("Filters")

# Filter by Membership
membership_filter = st.sidebar.multiselect(
    'Select Membership Tier',
    options=df['MEMBERSHIP'].unique(),
    default=df['MEMBERSHIP'].unique()  
)
# Filter by Gender
gender_filter = st.sidebar.multiselect(
    'Select Gender',
    options=df['GENDER'].unique(),
    default=df['GENDER'].unique()  
)

# Filter by Distance Category
distance_filter = st.sidebar.multiselect(
    'Select Distance Category',
    options=df['DISTANCE_CATEGORY'].unique(),
    default=df['DISTANCE_CATEGORY'].unique()  
)

# Filter by Year
year_filter = st.sidebar.multiselect(
    'Select Year',
    options=df['YEAR_FFP'].unique(),
    default=df['YEAR_FFP'].unique()  
)

# Apply filters to the DataFrame
filtered_df = df[
    (df['MEMBERSHIP'].isin(membership_filter)) &
    (df['GENDER'].isin(gender_filter)) &
    (df['DISTANCE_CATEGORY'].isin(distance_filter)) &
    (df['YEAR_FFP'].isin(year_filter))
]

# Descriptive statistics
num = filtered_df.describe()
cat = filtered_df.describe(include='O')

# Numerical and categorical descriptive statistics
with tap1:
    col1, col2, col3 = st.columns([6, 0.5, 6])
    with col1:
        st.subheader('Numerical Descriptive Statistics')
        st.dataframe(num.T, 500, 400)
        
    with col3:
        st.subheader('Categorical Descriptive Statistics')
        st.dataframe(cat.T, 500, 400)

# Analysis
with tap2:
    col1 = st.columns([8])
    sort = filtered_df.sort_values(by='MAX_INTERVAL', ascending=False)
    top_10 = sort.head(10)
    top_10_max_interval_cust = top_10[['MEMBER_NO', 'MAX_INTERVAL']]
    st.header("Top 10 Customers by Maximum Interval")
    st.dataframe(top_10_max_interval_cust)
    
    top_10_loyal_cust = filtered_df.sort_values(by='DAYS_SINCE_LAST_FLIGHT', ascending=True).head(10)[['MEMBER_NO', 'DAYS_SINCE_LAST_FLIGHT']]
    st.header("Top 10 Loyal Customers")
    st.dataframe(top_10_loyal_cust)
    
    st.subheader('Loyalty Points per Flight by Distance Category and Gender')
    fig17 = px.histogram(filtered_df, 
                         x='DISTANCE_CATEGORY', 
                         y='LOYALTY_POINTS_PER_FLIGHT', 
                         color='GENDER', 
                         title='Loyalty Points per Flight by Distance Category and Gender',
                         labels={'DISTANCE_CATEGORY': 'Distance Category', 
                                 'LOYALTY_POINTS_PER_FLIGHT': 'Loyalty Points per Flight'},
                         category_orders={'DISTANCE_CATEGORY': ['Short', 'Medium', 'Long']},
                         color_discrete_map={'Male': '#191970', 'Female': '#8B0000'})
    st.plotly_chart(fig17, use_container_width=True)
    
    st.subheader('Average Age by Year and Gender')
    average_age_df = filtered_df.groupby(['YEAR_FFP', 'GENDER'], as_index=False)['AGE'].median()
    fig18 = px.bar(average_age_df, 
                   x='YEAR_FFP', 
                   y='AGE', 
                   color='GENDER', 
                   title='Average Age by Year and Gender',
                   labels={'AGE': 'Average Age'},
                   category_orders={'YEAR_FFP': sorted(filtered_df['YEAR_FFP'].unique())},
                   color_discrete_map={'Male': '#191970', 'Female': '#8B0000'})
    st.plotly_chart(fig18, use_container_width=True)
    
    st.subheader('Flight Count by Age and Distance')
    total_flight_count = filtered_df.groupby(['DISTANCE_CATEGORY', 'AGE_CATEGORY'], as_index=False)['FLIGHT_COUNT'].sum()
    fig19 = px.bar(total_flight_count, 
                   x='AGE_CATEGORY', 
                   y='FLIGHT_COUNT', 
                   color='DISTANCE_CATEGORY', 
                   title='Flight Count by Age and Distance',
                   labels={'AGE_CATEGORY': 'Age Category'},
                   color_discrete_map={
                       'Long-haul': '#483D8B',  
                       'Medium-haul': '#191970',  
                       'Short-haul': '#8B0000'})
    st.plotly_chart(fig19, use_container_width=True)
    
    st.subheader('Average Revenue by Distance and Interval Category')
    average_rev_distance = filtered_df.groupby(['DISTANCE_CATEGORY', 'INTERVAL_CATEGORY'], as_index=False)['SUM_YR_1'].mean()
    fig20 = px.bar(average_rev_distance, 
                   x='SUM_YR_1',  
                   y='DISTANCE_CATEGORY',  
                   color='INTERVAL_CATEGORY',  
                   title='Average Revenue by Distance and Interval Category',
                   labels={'SUM_YR_1': 'Total Revenue', 'DISTANCE_CATEGORY': 'Distance Category'},
                   color_discrete_map={
                       'Frequent': '#8B0000',  
                       'Infrequent': '#191970',  
                       'Occasional': '#483D8B'})
    st.plotly_chart(fig20, use_container_width=True)
    
    st.subheader('Average Revenue by Membership Tier and Interval Category')
    interval_by_tier = filtered_df.groupby(['MEMBERSHIP', 'INTERVAL_CATEGORY'], as_index=False)['SUM_YR_1'].mean()
    fig21 = px.bar(interval_by_tier, 
                   x='SUM_YR_1', 
                   y='INTERVAL_CATEGORY', 
                   color='MEMBERSHIP', 
                   title='Average Revenue by Membership Tier and Interval Category',
                   labels={'SUM_YR_1': 'Total Revenue', 'INTERVAL_CATEGORY': 'Interval Category'},
                   color_discrete_map={
                       'Gold': '#FFD700',      
                       'Silver': '#C0C0C0',    
                       'Platinum': '#CD7F32'})
    st.plotly_chart(fig21, use_container_width=True)
    
    st.subheader('Max Interval by Unique Member Count')
    filtered_df['MEMBER_NO'] = filtered_df['MEMBER_NO'].astype(str) 
    count_by_membership = filtered_df.groupby(['MEMBERSHIP', 'MAX_INTERVAL'], as_index=False).agg(
        Unique_Member_Count=('MEMBER_NO', 'nunique'))
    fig22 = px.line(count_by_membership, 
                    x='MAX_INTERVAL', 
                    y='Unique_Member_Count', 
                    color='MEMBERSHIP', 
                    title='Max Interval by Unique Member Count',
                    labels={'MAX_INTERVAL': 'Maximum Interval', 'Unique_Member_Count': 'Unique Member Count'},
                    color_discrete_map={
                        'Gold': '#FFD700',      
                        'Silver': '#00008B',    
                        'Platinum': '#FF0000'})
    st.plotly_chart(fig22, use_container_width=True)
    
    st.subheader('Discounted Flights vs. Flight Count')
    fig23 = px.scatter(filtered_df, 
                       x='FLIGHT_COUNT', 
                       y='DISCOUNTED_FLIGHTS', 
                       title='Discounted Flights vs. Flight Count',
                       labels={'FLIGHT_COUNT': 'Number of Flights', 'DISCOUNTED_FLIGHTS': 'Discounted Flights'})
    st.plotly_chart(fig23, use_container_width=True)
