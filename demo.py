import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
from flask import Flask, render_template



# Thiết lập tiêu đề trang
st.set_page_config('Demo by group 7')

# Đổi màu nền
background_color = '#EEF0E5'  # Mã màu hex
st.markdown(
    f"""
    <style>
        body {{
            background-color: {background_color};
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Đổi màu và phông chữ cho tiêu đề và tiêu đề phụ
header_color = '#163020'  # Mã màu hex
font_color = '#495E57'  # Mã màu hex

st.markdown(
    f"""
    <style>
        .css-19ih76x {{
            color: {header_color};
            font-size: 32px;
            text-align: left;
        }}
        .css-1l4w6pd {{
            color: {font_color};
            font-size: 24px;
            text-align: center;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Hiển thị tiêu đề và tiêu đề phụ
st.header('Telemarketing in Banking and Voicebot system development')
st.subheader('Voicebot demo')














# --- DISPLAY IMAGE & DATAFRAME
image = Image.open('Image/Voicebot.jpg')
st.image(image,
        caption='Application of using Voicebot in telemarketing',
        use_column_width=True)


### --- LOAD DATAFRAME
excel_file = 'KẾT QUẢ RUN VOICEBOT (1).xlsx'
sheet_name = 'Sheet1'
sheet_name2 = 'Sheet2'
sheet_name3 = 'Sheet3'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A:L',
                   header=1)

df1 = pd.read_excel(excel_file,
                          sheet_name=sheet_name2,
                          usecols="A:B",
                          header=1)

df2 = pd.read_excel(excel_file,
                          sheet_name=sheet_name2,
                          usecols="D:E",
                          header=1)

df3 = pd.read_excel(excel_file,
                          sheet_name=sheet_name2,
                          usecols="G:H",
                          header=1)
st.dataframe(df)


#---- columm (chia cot hai bieu do tron)
col1, col2, col3 = st.columns(3)
col1.dataframe(df1)
col2.dataframe(df2)
col3.dataframe(df3)


# --- PLOT BAR CHART
bar_chart = px.bar(df3,
                   x='MKQ',
                   y='NUMMKQ',
                   text='MKQ',
                   color_discrete_sequence = ['#4F6F52']*len(df3),
                   template= 'plotly_dark')
st.plotly_chart(bar_chart)

custom_colors = ['#739072', '#304D30']


# --- PLOT PIE CHART
pie_chart1 = px.pie(df1,
                title='TRẠNG THÁI CUỘC GỌI',
                values='NUMTTCG',
                color_discrete_sequence=custom_colors,
                names='TTCG')



pie_chart2 = px.pie(df2,
                title='TRẠNG THÁI CUỐI CÙNG',
                values='NUMTTCC',
                color_discrete_sequence=custom_colors,
                names='TTCC')



#---- columm (chia cot hai bieu do tron)
left_column, right_column = st.columns(2)
left_column.plotly_chart(pie_chart1, use_container_width=True)
right_column.plotly_chart(pie_chart2, use_container_width=True)


df4 = pd.read_excel(excel_file,
                          sheet_name=sheet_name3,
                          usecols="A:C",
                          header=0)
st.dataframe(df4)

# --- STREAMLIT SELECTION
ma_ket_qua = df['MÃ KẾT QUẢ'].unique().tolist()
timing = df4['THOILUONGGIAY'].unique().tolist()

timing_selection = st.slider('THOILUONGGIAY:',
                        min_value= min(timing),
                        max_value= max(timing),
                        value=(min(timing),max(timing)))

ma_ket_qua_selection = st.multiselect('MÃ KẾT QUẢ:',
                                    ma_ket_qua,
                                    default=ma_ket_qua)

# --- FILTER DATAFRAME BASED ON SELECTION
mask = (df4['THOILUONGGIAY'].between(*timing_selection)) & (df['MÃ KẾT QUẢ'].isin(ma_ket_qua_selection))
number_of_result = df[mask].shape[0]
st.markdown(f'*Available Results: {number_of_result}*')

# --- GROUP DATAFRAME AFTER SELECTION
df_grouped = df[mask].groupby(by=['THỜI LƯỢNG']).count()[['MÃ KẾT QUẢ']]
df_grouped = df_grouped.reset_index()
st.dataframe(df_grouped)

#--- SIDEBAR (thay vao sau khi load dataframe)
st.sidebar.header('Please filter here:')
MKQ = st.sidebar.multiselect(
    "Select the MKQ:",
    options=df["MÃ KẾT QUẢ"].unique(),
    default=df["MÃ KẾT QUẢ"].unique()

)

# --- DISPLAY IMAGE & DATAFRAME
image = Image.open('Image/Analysist.jpg')
st.image(image,
        caption='Analyst',
        use_column_width=True)























