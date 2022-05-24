import streamlit as st
import streamlit.components.v1 as components
import numpy as np
from PIL import Image
import gettext
import pandas as pd


import plotly.graph_objects as go


st.set_page_config(page_title='Gonzalo Pietraroia\'s portfolio' ,layout="wide",page_icon='💼')


_ = gettext.gettext
language = st.sidebar.selectbox('', ['ES','EN'])
try:
   localizator = gettext.translation('base', localedir='locales', languages=[language])
   localizator.install()
   _ = localizator.gettext 
except:
    pass


img = Image.open('images/Perfil-modified.png')
st.sidebar.image(img,width=180)
st.sidebar.subheader('Gonzalo Pietraroia')
st.sidebar.caption('Data Scientist')


st.sidebar.caption(_('Queres conectar?'))

link_linkedin = '[LinkedIn](https://www.linkedin.com/in/gonzalo-pietraroia-7398241b9/)'
with st.sidebar:
    st.markdown(link_linkedin, unsafe_allow_html=True)

link_github = '[GitHub](https://github.com/GonzaloPietraroia)'
with st.sidebar:
    st.markdown(link_github, unsafe_allow_html=True)

st.sidebar.markdown('📧: gonzalo.pietraroia@gmail.com')
pdfFileObj = open('pdf/CV - Pietraroia Gonzalo.pdf', 'rb')
st.sidebar.download_button(_('Descargar Curriculum Vitae'),pdfFileObj,file_name='CV - Pietraroia Gonzalo.pdf',mime='pdf')

edu = [['B.Tech','CSE','2020','IIIT Jabalpur','8.1 CGPA'],['12th','Science','2016','Bhavan\'s KDKVM', '94.2%'],['10th','-','2012','Bhavan\'s KDKVM','10 CGPA']]

info = {'name':'Mehul Gupta', 'Brief':'Data Scientist with 2+ years of professional experience looking out to solve complex business problems using AI; Experienced in developing data-driven solutions for automating digitalization of health documents reducing manual efforts by 100% for lab reports & 50% for prescriptions; Love to learn new things. Right now : Streamlit !! ','photo':{'path':'abc.jpg','width':150}, 'Mobile':'8103795345','Email':'mehulgupta2016154@gmail.com','Medium':'https://medium.com/@mehulgupta_7991/about','City':'Nagda, Madhya Pradesh','Stackoverflow_flair':'''<a href="https://stackoverflow.com/users/8422170/mehul-gupta"><img src="https://stackoverflow.com/users/flair/8422170.png?theme=clean" width="250" height="70"  alt="profile for Mehul Gupta at Stack Overflow, Q&amp;A for professional and enthusiast programmers" title="profile for Mehul Gupta at Stack Overflow, Q&amp;A for professional and enthusiast programmers"></a>''','edu':pd.DataFrame(edu,columns=['Qualification','Stream','Year','Institute','Score']),'skills':['Data Science','RDBMS','Cassandra','AWS Athena','Snowflake','Comet-ML','Python','Java','C++','Airflow','AWS S3','Tableau','Metabase','Thoughtspot','Streamlit'],'achievements':['Top AI writer @ Medium','1.4k+ reputation points on Stackoverflow','TCS humAIn Finalist,2019','25 Kaggle medals','Shikshan Bharati Kulapati K.M. Munshi Award in Mathematics,2014','Bharatiya Vidya Bhavan Shri C. Subramaniam Award for excellence in character, 2009 & 2012','Certificate of Merit(Proficiency in Co-curricular activities) for Declamation and Extempore'],'publication_url':'https://medium.com/data-science-in-your-pocket/tagged/beginner'}

st.subheader('Education 📖')

fig = go.Figure(data=[go.Table(
    header=dict(values=list(info['edu'].columns),
                fill_color='paleturquoise',
                align='left',height=65,font_size=20),
    cells=dict(values=info['edu'].transpose().values.tolist(),
               fill_color='lavender',
               align='left',height=40,font_size=15))])

fig.update_layout(width=750, height=400)
st.plotly_chart(fig)




# TEST
st.title('STREAMLIT TUTORIAL')

#HEADER

st.header('this is a header')

st.subheader('this is a header')

st.text('this is a header')

st.markdown('### aaaaa')

st.success('success')

st.info('information')

st.warning('this is a warning')

st.error('error')

st.exception('NameError("name three not defined")')

st.help(range)

st.write('Text with write')

st.write(range(10))


img = Image.open('shaco.png')
st.image(img,width=300,caption='shaco')

vid_file = open('biza.mp4','rb').read()
#vid_bytes = vid_file.read()
st.video(vid_file)

audio_file = open('cancion.mp3','rb').read()
st.audio(audio_file,format='audio/mp3')

if st.checkbox('Show/Hide'):
    st.text('Showing or hiding widget')

status = st.radio('what is your status',('active','negative'))

if status == 'active':
    st.success('you are active')
else:
    st.warning('inactive, activate')

occupation = st.selectbox('your ocupaation',['programer','datascience','doctor'])
st.write('your selected this option',occupation)

location = st.multiselect('where do you work',('london','new york','topo'))
st.write('you selected',len(location),'locations')

level = st.slider('what is your level',1,5)


st.button('simple button')

if st.button('about'):
    st.text('soy piola')

firstname = st.text_input('enteryour name','TYPE here..')

if st.button('submit'):
    result = firstname.title()
    st.success(result)
    

message = st.text_area('enteryour name','TYPE here..')

if st.button('submit2'):
    result = message.title()
    st.success(result)
    

import datetime
today = st.date_input('today is',datetime.datetime.now())

the_time = st.time_input('the time is',datetime.time())

st.text("display json")
st.json({'name':'topo','gender':'male'})

st.text('display raw code')
st.code('import numpy as np')

with st.echo():
    import pandas as pd
    df = pd.DataFrame()

import time
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p + 1)

with st.spinner('waiting ..'):
    time.sleep(1)
st.success('finished!')

#st.balloons()



@st.cache
def run_f():
    return range(100)


st.write(run_f())


st.pyplot()


st.dataframe(df)

st.table(df)





# linkedin robado
# embed_component= {'linkedin':"""<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
#     <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="gonzalo-pietraroia-7398241b9" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://www.linkedin.com/in/gonzalo-pietraroia-7398241b9/"></a></div>"""}

# with st.sidebar:
#         components.html(embed_component['linkedin'],height=300)

# linkedin no funciona en server
# with st.sidebar:
#     if st.button('LinkedIn'):
#         webbrowser.open_new_tab('https://www.linkedin.com/in/gonzalo-pietraroia-7398241b9/')