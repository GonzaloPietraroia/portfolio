import streamlit as st
import streamlit.components.v1 as components
import numpy as np
from PIL import Image, ImageDraw
from IPython.display import display

st.set_page_config(page_title='Gonzalo Pietraroia\'s portfolio' ,layout="wide",page_icon='💼')

#embed_component= {'linkedin':"""<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
 #   <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="gonzalo-pietraroia-7398241b9" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://www.linkedin.com/in/gonzalo-pietraroia-7398241b9/"></a></div>"""}

#with st.sidebar:
 #       components.html(embed_component['linkedin'],height=300)

img = Image.open('images/Perfil-modified.png')
st.sidebar.image(img)


st.sidebar.caption('Wish to connect?')
st.sidebar.write('📧: gonzalo.pietraroia@gmail.com')
pdfFileObj = open('pdf/CV - Pietraroia Gonzalo.pdf', 'rb')
st.sidebar.download_button('Download resume',pdfFileObj,file_name='CV - Pietraroia Gonzalo.pdf',mime='pdf')





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


