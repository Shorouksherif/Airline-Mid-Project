import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots

st.set_page_config(
    layout="wide",
    page_title="Home Page for Insights")


st.sidebar.success('select page above')
st.markdown('<h1 style= "text-align:center; color: #4169E1 ;">Airlines EDA</h1>', unsafe_allow_html= True)

# Reading CSV files into DataFrames
df = pd.read_csv('df1.csv')
first_flight_rev_year = pd.read_csv('first_flight_rev_year.csv')
age_flight = pd.read_csv('age_flight.csv')
membership_flight = pd.read_csv('membership_flight.csv')
gender_total = pd.read_csv('gender_total.csv')
top_5_cities = pd.read_csv('top_5_cities.csv')
top_5_countries = pd.read_csv('top_5_countries.csv')
top_5_countries_Rev = pd.read_csv('top_5_countries_Rev.csv')
top_5_cities_Rev = pd.read_csv('top_5_cities_Rev.csv')
top_10_last_flown_cust = pd.read_csv('top_10_last_flown_cust.csv')
top_10_loyal_cust = pd.read_csv('top_10_loyal_cust.csv')
MONTH_MEMBERHIP = pd.read_csv('MONTH_MEMBERHIP.csv')
MONTH_MEMBERHIP_COUNT = pd.read_csv('MONTH_MEMBERHIP_COUNT.csv')
SEASON_MEMBERHIP = pd.read_csv('SEASON_MEMBERHIP.csv')
DAYS_MEMBERHIP = pd.read_csv('DAYS_MEMBERHIP.csv')
DAYS_MEMBERHIP_COUNT = pd.read_csv('DAYS_MEMBERHIP_COUNT.csv')
SEASON_MEMBERHIP_COUNT = pd.read_csv('SEASON_MEMBERHIP_COUNT.csv')
MONTH_FIRST_FLIGHT = pd.read_csv('MONTH_FIRST_FLIGHT.csv')
MONTH_FIRST_FLIGHT_COUNT = pd.read_csv('MONTH_FIRST_FLIGHT_COUNT.csv')
SEASON_FIRST_FLIGHT = pd.read_csv('SEASON_FIRST_FLIGHT.csv')
DAYS_FIRST_FLIGHT = pd.read_csv('DAYS_FIRST_FLIGHT.csv')
DAYS_FIRST_FLIGHT_COUNT = pd.read_csv('DAYS_FIRST_FLIGHT_COUNT.csv')
SEASON_FIRST_FLIGHT_COUNT = pd.read_csv('SEASON_FIRST_FLIGHT_COUNT.csv')
MONTH_LAST_FLIGHT = pd.read_csv('MONTH_LAST_FLIGHT.csv')
MONTH_LAST_FLIGHT_COUNT = pd.read_csv('MONTH_LAST_FLIGHT_COUNT.csv')
SEASON_LAST_FLIGHT = pd.read_csv('SEASON_LAST_FLIGHT.csv')
DAYS_LAST_FLIGHT = pd.read_csv('DAYS_LAST_FLIGHT.csv')
DAYS_LAST_FLIGHT_COUNT = pd.read_csv('DAYS_LAST_FLIGHT_COUNT.csv')
SEASON_LAST_FLIGHT_COUNT = pd.read_csv('SEASON_LAST_FLIGHT_COUNT.csv')
total_count_flight = pd.read_csv('total_count_flight.csv')
country_flight_count = pd.read_csv('country_flight_count.csv')
distance_revenue = pd.read_csv('distance_revenue.csv')
year_membership = pd.read_csv('year_membership.csv')
top_10_max_interval_cust = pd.read_csv('top_10_max_interval_cust.csv')

df.drop('Unnamed: 0', axis=1, inplace= True)
df_sample= df.head(10)

first_flight_rev_year = df.groupby('YEAR_FIRST_FLIGHT').agg({'SUM_YR_1': 'sum'}).reset_index().sort_values(by='SUM_YR_1', ascending=False)
fig = px.bar(first_flight_rev_year, y='SUM_YR_1', x='YEAR_FIRST_FLIGHT', title='Revenue per Year', color_discrete_sequence=px.colors.sequential.Plasma, text='SUM_YR_1').update_traces(texttemplate='%{text}', textposition='outside')

gender_total = df.groupby('GENDER').agg({'FLIGHT_COUNT': 'sum'}).reset_index().sort_values(by='FLIGHT_COUNT', ascending=False)
fig1 = px.pie(gender_total, names='GENDER',values='FLIGHT_COUNT',title='Flight Counts by Gender',color='GENDER',color_discrete_sequence=px.colors.sequential.Plasma)  # Optional: color sequence


age_flight = df.groupby('AGE_CATEGORY').agg({'FLIGHT_COUNT': 'sum'}).reset_index().sort_values(by='FLIGHT_COUNT', ascending=False)
fig2 = px.bar(age_flight, y='FLIGHT_COUNT', x='AGE_CATEGORY', title='Age per Flight Counts', color_discrete_sequence=px.colors.sequential.Plasma, text='FLIGHT_COUNT').update_traces(texttemplate='%{text}', textposition='outside')

membership_flight = df.groupby('MEMBERSHIP').agg({'FLIGHT_COUNT': 'sum'}).reset_index().sort_values(by='FLIGHT_COUNT', ascending=False)
fig3 = px.bar(membership_flight, x='FLIGHT_COUNT',y='MEMBERSHIP',title='membership per flight counts',color_discrete_sequence=px.colors.sequential.Plasma,text='FLIGHT_COUNT').update_traces(texttemplate='%{text}', textposition='outside')

top_5_cities= df.groupby('WORK_CITY').agg({'FLIGHT_COUNT': 'sum'}).reset_index().sort_values(by='FLIGHT_COUNT', ascending=False).head(5)
fig4 = px.pie(top_5_cities, values='FLIGHT_COUNT', names='WORK_CITY',title='Top 5 cities by Flight count', color_discrete_sequence=px.colors.sequential.Plasma)

top_5_countries= df.groupby('WORK_COUNTRY').agg({'FLIGHT_COUNT': 'sum'}).reset_index().sort_values(by='FLIGHT_COUNT', ascending=False).head(5)
fig5 = px.bar(top_5_countries, y='FLIGHT_COUNT',x='WORK_COUNTRY',title='Top 5 countries by flight count',color='WORK_COUNTRY',color_discrete_sequence=px.colors.sequential.Plasma,text='FLIGHT_COUNT').update_traces(texttemplate='%{text}', textposition='outside')

top_5_countries_Rev= df.groupby('WORK_COUNTRY').agg({'SUM_YR_1': 'sum'}).reset_index().sort_values(by='SUM_YR_1', ascending=False).head(5)
fig6 = px.bar(top_5_countries_Rev, y='WORK_COUNTRY',x='SUM_YR_1',title='Revenue by Top 5 Countries',color='WORK_COUNTRY',color_discrete_sequence=px.colors.sequential.Plasma,text='SUM_YR_1').update_traces(texttemplate='%{text}', textposition='outside')


top_5_cities_Rev= df.groupby('WORK_CITY').agg({'SUM_YR_1': 'sum'}).reset_index().sort_values(by='SUM_YR_1', ascending=False).head(5)
fig7 = px.bar(top_5_cities_Rev, y='WORK_CITY',x='SUM_YR_1',title='Revenue by Top 5 Cities',color='WORK_CITY',color_discrete_sequence=px.colors.sequential.Plasma,text='SUM_YR_1').update_traces(texttemplate='%{text}', textposition='outside')

top_10_last_flown_cust = df.sort_values(by='DAYS_SINCE_LAST_FLIGHT', ascending=False).head(10)[['MEMBER_NO', 'DAYS_SINCE_LAST_FLIGHT']]
fig8=plt.figure(figsize=(10, 6));plt.bar(top_10_last_flown_cust['MEMBER_NO'].astype(str), top_10_last_flown_cust['DAYS_SINCE_LAST_FLIGHT'], color='rebeccapurple');plt.xlabel('Member ID');plt.ylabel('Days Since Last Flight');plt.title('Lost Customers');plt.xticks(rotation=45)

MONTH_MEMBERHIP=df.groupby('MONTH_NAME_FFP').agg({'SUM_YR_1': 'sum'}).reset_index().sort_values(by='SUM_YR_1', ascending=False)
MONTH_MEMBERHIP_COUNT= df.groupby('MONTH_NAME_FFP').agg({'FLIGHT_COUNT': 'sum'}).reset_index().sort_values(by='FLIGHT_COUNT', ascending=False)
SEASON_MEMBERHIP= df.groupby('SEASON_FFP').agg({'SUM_YR_1': 'sum'}).reset_index().sort_values(by='SUM_YR_1', ascending=False)
DAYS_MEMBERHIP= df.groupby('DAYS_FFP').agg({'SUM_YR_1': 'sum'}).reset_index().sort_values(by='SUM_YR_1', ascending=False)
DAYS_MEMBERHIP_COUNT= df.groupby('DAYS_FFP').agg({'FLIGHT_COUNT': 'sum'}).reset_index().sort_values(by='FLIGHT_COUNT', ascending=False)
SEASON_MEMBERHIP_COUNT= df.groupby('SEASON_FFP').agg({'FLIGHT_COUNT': 'sum'}).reset_index().sort_values(by='FLIGHT_COUNT', ascending=False)
fig9 = make_subplots(rows=2, cols=3, start_cell='bottom-left',subplot_titles=("Month Membership", "Season Membership","Days Membership","Days Membership count","Season Membership count","Month Membership count"))
area_fig1 = px.area(MONTH_MEMBERHIP, x='MONTH_NAME_FFP', y='SUM_YR_1',color_discrete_sequence=px.colors.sequential.Plasma, markers=True)
fig9.add_trace(area_fig1.data[0], row=1, col=1)

area_fig2 = px.area(SEASON_MEMBERHIP, x='SEASON_FFP', y='SUM_YR_1',color_discrete_sequence=px.colors.sequential.Plasma,markers=True)
fig9.add_trace(area_fig2.data[0], row=1, col=2)

area_fig3 = px.area(DAYS_MEMBERHIP, x='DAYS_FFP', y='SUM_YR_1', color_discrete_sequence=px.colors.sequential.Plasma,markers=True)
fig9.add_trace(area_fig3.data[0], row=1, col=3)

line_fig1 = px.line(DAYS_MEMBERHIP_COUNT, x='DAYS_FFP', y='FLIGHT_COUNT', markers=True)
fig9.add_trace(line_fig1.data[0], row=2, col=1)

line_fig2 = px.line(SEASON_MEMBERHIP_COUNT, x='SEASON_FFP', y='FLIGHT_COUNT', markers=True)
fig9.add_trace(line_fig2.data[0], row=2, col=2)

line_fig3 = px.line(MONTH_MEMBERHIP_COUNT, x='MONTH_NAME_FFP', y='FLIGHT_COUNT', markers=True)
fig9.add_trace(line_fig3.data[0], row=2, col=3)


fig9.update_layout(
    title="Membership Analysis Overview",
    title_x=0.5, 
    height=600,  
    width=800,   
    margin=dict(l=40, r=40, t=40, b=40)
    ,)


MONTH_FIRST_FLIGHT = df.groupby('MONTH_NAME_FIRST_FLIGHT').agg({'SUM_YR_1': 'sum'}).reset_index().sort_values(by='SUM_YR_1', ascending=False)
MONTH_FIRST_FLIGHT_COUNT = df.groupby('MONTH_NAME_FIRST_FLIGHT').agg({'FLIGHT_COUNT': 'sum'}).reset_index().sort_values(by='FLIGHT_COUNT', ascending=False)
SEASON_FIRST_FLIGHT = df.groupby('SEASON_FIRST_FLIGHT').agg({'SUM_YR_1': 'sum'}).reset_index().sort_values(by='SUM_YR_1', ascending=False)
DAYS_FIRST_FLIGHT = df.groupby('DAYS_FIRST_FLIGHT').agg({'SUM_YR_1': 'sum'}).reset_index().sort_values(by='SUM_YR_1', ascending=False)
DAYS_FIRST_FLIGHT_COUNT = df.groupby('DAYS_FIRST_FLIGHT').agg({'FLIGHT_COUNT': 'sum'}).reset_index().sort_values(by='FLIGHT_COUNT', ascending=False)
SEASON_FIRST_FLIGHT_COUNT = df.groupby('SEASON_FIRST_FLIGHT').agg({'FLIGHT_COUNT': 'sum'}).reset_index().sort_values(by='FLIGHT_COUNT', ascending=False)

fig10 = make_subplots(
    rows=2, 
    cols=3, 
    start_cell='bottom-left',
    subplot_titles=(
        "Month First Flight", 
        "Season First Flight",
        "Days First Flight",
        "Days First Flight Count",
        "Season First Flight Count",
        "Month First Flight Count"
    )
)

area_fig1 = px.area(MONTH_FIRST_FLIGHT, x='MONTH_NAME_FIRST_FLIGHT', y='SUM_YR_1', color_discrete_sequence=px.colors.sequential.Plasma, markers=True)
fig10.add_trace(area_fig1.data[0], row=1, col=1)

area_fig2 = px.area(SEASON_FIRST_FLIGHT, x='SEASON_FIRST_FLIGHT', y='SUM_YR_1', color_discrete_sequence=px.colors.sequential.Plasma, markers=True)
fig10.add_trace(area_fig2.data[0], row=1, col=2)

area_fig3 = px.area(DAYS_FIRST_FLIGHT, x='DAYS_FIRST_FLIGHT', y='SUM_YR_1', color_discrete_sequence=px.colors.sequential.Plasma, markers=True)
fig10.add_trace(area_fig3.data[0], row=1, col=3)

line_fig1 = px.line(DAYS_FIRST_FLIGHT_COUNT, x='DAYS_FIRST_FLIGHT', y='FLIGHT_COUNT', markers=True)
fig10.add_trace(line_fig1.data[0], row=2, col=1)

line_fig2 = px.line(SEASON_FIRST_FLIGHT_COUNT, x='SEASON_FIRST_FLIGHT', y='FLIGHT_COUNT', markers=True)
fig10.add_trace(line_fig2.data[0], row=2, col=2)

line_fig3 = px.line(MONTH_FIRST_FLIGHT_COUNT, x='MONTH_NAME_FIRST_FLIGHT', y='FLIGHT_COUNT', markers=True)
fig10.add_trace(line_fig3.data[0], row=2, col=3)

fig10.update_layout( 
    title="First flight Analysis Overview",
    title_x=0.5, 
    height=600,  
    width=800,   
    margin=dict(l=40, r=40, t=40, b=40)
)

MONTH_LAST_FLIGHT = df.groupby('MONTH_Name_LAST_FLIGHT').agg({'SUM_YR_1': 'sum'}).reset_index().sort_values(by='SUM_YR_1', ascending=False)
MONTH_LAST_FLIGHT_COUNT = df.groupby('MONTH_Name_LAST_FLIGHT').agg({'FLIGHT_COUNT': 'sum'}).reset_index().sort_values(by='FLIGHT_COUNT', ascending=False)
SEASON_LAST_FLIGHT = df.groupby('SEASON_LAST_FLIGHT').agg({'SUM_YR_1': 'sum'}).reset_index().sort_values(by='SUM_YR_1', ascending=False)
DAYS_LAST_FLIGHT = df.groupby('DAYS_LAST_FLIGHT').agg({'SUM_YR_1': 'sum'}).reset_index().sort_values(by='SUM_YR_1', ascending=False)
DAYS_LAST_FLIGHT_COUNT = df.groupby('DAYS_LAST_FLIGHT').agg({'FLIGHT_COUNT': 'sum'}).reset_index().sort_values(by='FLIGHT_COUNT', ascending=False)
SEASON_LAST_FLIGHT_COUNT = df.groupby('SEASON_LAST_FLIGHT').agg({'FLIGHT_COUNT': 'sum'}).reset_index().sort_values(by='FLIGHT_COUNT', ascending=False)

fig11 = make_subplots(
    rows=2, 
    cols=3, 
    start_cell='bottom-left',
    subplot_titles=(
        "Month Last Flight", 
        "Season Last Flight",
        "Days Last Flight",
        "Days Last Flight Count",
        "Season Last Flight Count",
        "Month Last Flight Count"
    )
)

area_fig1 = px.area(MONTH_LAST_FLIGHT, x='MONTH_Name_LAST_FLIGHT', y='SUM_YR_1', color_discrete_sequence=px.colors.sequential.Plasma, markers=True)
fig11.add_trace(area_fig1.data[0], row=1, col=1)

area_fig2 = px.area(SEASON_LAST_FLIGHT, x='SEASON_LAST_FLIGHT', y='SUM_YR_1', color_discrete_sequence=px.colors.sequential.Plasma, markers=True)
fig11.add_trace(area_fig2.data[0], row=1, col=2)

area_fig3 = px.area(DAYS_LAST_FLIGHT, x='DAYS_LAST_FLIGHT', y='SUM_YR_1', color_discrete_sequence=px.colors.sequential.Plasma, markers=True)
fig11.add_trace(area_fig3.data[0], row=1, col=3)

line_fig1 = px.line(DAYS_LAST_FLIGHT_COUNT, x='DAYS_LAST_FLIGHT', y='FLIGHT_COUNT', markers=True)
fig11.add_trace(line_fig1.data[0], row=2, col=1)

line_fig2 = px.line(SEASON_LAST_FLIGHT_COUNT, x='SEASON_LAST_FLIGHT', y='FLIGHT_COUNT', markers=True)
fig11.add_trace(line_fig2.data[0], row=2, col=2)

line_fig3 = px.line(MONTH_LAST_FLIGHT_COUNT, x='MONTH_Name_LAST_FLIGHT', y='FLIGHT_COUNT', markers=True)
fig11.add_trace(line_fig3.data[0], row=2, col=3)

fig11.update_layout(
    title="Last flight Analysis Overview",
    title_x=0.5, 
    height=600,  
    width=800,   
    margin=dict(l=40, r=40, t=40, b=40)
)

total_count_flight = df.groupby('YEAR_FIRST_FLIGHT').agg({'FLIGHT_COUNT': 'sum'}).reset_index().sort_values(by='FLIGHT_COUNT', ascending=False)
fig12 = px.bar(total_count_flight, y='FLIGHT_COUNT',x='YEAR_FIRST_FLIGHT',title='count of flights per year',color_discrete_sequence=px.colors.sequential.Plasma,text='FLIGHT_COUNT').update_traces(texttemplate='%{text}', textposition='outside')

country_flight_count = df.groupby(['Country'], as_index=False)['FLIGHT_COUNT'].sum()
color_palette = ['#1f77b4', '#2ca02c', '#d62728', '#ff7f0e', '#9467bd'] 
fig13 = px.choropleth(country_flight_count,locations='Country',locationmode='country names',color='FLIGHT_COUNT',title='Flight Counts by Country',color_discrete_sequence=color_palette)

distance_revenue = df.groupby(['DISTANCE_CATEGORY'], as_index=False)['SUM_YR_1'].sum()

year_membership = df.groupby('YEAR_FFP').size().reset_index(name='Member_Count')
fig15 = plt.figure(figsize=(10, 6));plt.barh(year_membership['YEAR_FFP'],year_membership['Member_Count'],color='midnightblue');plt.title('Membership Count by Year');plt.xlabel('Member Count');plt.ylabel('Year');plt.show()


fig16=plt.figure(figsize=(10, 6));plt.hist(df['MAX_INTERVAL'], bins=10, color='purple', alpha=0.7);plt.title('Distribution of Maximum Intervals Between Flights');plt.xlabel('Maximum Interval (Days)');plt.ylabel('Frequency')

st.header('Sample Data')
st.dataframe(df_sample, hide_index=True)

st.header("Revenue generated in each first year")
st.plotly_chart(fig)

st.header("Flights taken by male versus female passengers")
st.plotly_chart(fig1)


st.header("Age category with the highest number of flights")
st.plotly_chart(fig2)


st.header("Flight counts across different membership tiers")
st.plotly_chart(fig3)


st.header("Top 5 cities with the highest flight counts")
st.plotly_chart(fig4)


st.header("Top 5 countries with the highest flight counts")
st.plotly_chart(fig5)

st.header("Revenue generated from the top 5 countries")
st.plotly_chart(fig6)

st.header("Revenue generated from the top 5 cities")
st.plotly_chart(fig7)

st.header("Lost Customers ID")
st.pyplot(fig8)

st.header("Revenue and counts generated from memberships by month/days/season in memebership regestration")
st.plotly_chart(fig9)

st.header("Revenue and counts generated from memberships by month/days/season in Fisrt flight")
st.plotly_chart(fig10)

st.header("Revenue and counts generated from memberships by month/days/season in Last flight")
st.plotly_chart(fig11)

st.header("First flight counts per year")
st.plotly_chart(fig12)

st.header("Flight counts in all Countries")
st.plotly_chart(fig13)

st.header("Revenue across different distance categories of flights")
distance_categories =distance_revenue['DISTANCE_CATEGORY'].unique().tolist()
distance_categories.insert(0, 'All')
selected_category = st.selectbox('Select Distance Category', distance_categories, key=4)
if selected_category == 'All':
    filtered_revenue = distance_revenue
else:
    filtered_revenue = distance_revenue[distance_revenue['DISTANCE_CATEGORY'] == selected_category]
fig14 = plt.figure(figsize=(10, 6));plt.bar(filtered_revenue['DISTANCE_CATEGORY'],filtered_revenue['SUM_YR_1'], color='midnightblue');plt.title(f'Revenue for {selected_category} Distance Category');plt.xlabel('Distance Category');plt.ylabel('Revenue')
st.pyplot(fig14)

st.header("Highest year membership regestration")
st.pyplot(fig15)

st.header("Distribution of maximum intervals between flights")
st.pyplot(fig16)
