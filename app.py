import streamlit as st


st.markdown(
    """
<style>
.reportview-container .markdown-text-container {
    font-family: monospace;
}
.sidebar .sidebar-content {
    background-image: linear-gradient(#2e7bcf,#2e7bcf);
    color: white;
}
.Widget>label {
    color: white;
    font-family: monospace;
}
[class^="st-b"]  {
    color: white;
    font-family: monospace;
}
.st-bb {
    background-color: transparent;
}
.st-at {
    background-color: #0c0080;
}
footer {
    font-family: monospace;
}
.reportview-container .main footer, .reportview-container .main footer a {
    color: #0c0080;
}
header .decoration {
    background-image: none;
}

</style>
""",
    unsafe_allow_html=True,
)

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

from PIL import Image
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

st.sidebar.header('about')
st.sidebar.text('this is a stream lit tut')

st.sidebar.text('this aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaut')


@st.cache
def run_f():
    return range(100)


st.write(run_f())


st.pyplot()


st.dataframe(df)

st.table(df)