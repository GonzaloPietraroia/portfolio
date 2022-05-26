import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
from PIL import Image
import gettext
import pandas as pd



# Configuracion de pagina(titulo,icono y layout)

st.set_page_config(
  page_title='Gonzalo Pietraroia\'s portfolio' ,
  layout="wide",page_icon='💼',
  initial_sidebar_state="auto",
  menu_items={
          'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
       'About': "# This is a header. This is an *extremely* cool app!"
     }
)


# Uso de GetText para implementar idiomas. (usar _() en strings)
# Creo los archivos base.pot "C:\Users\fezz2\AppData\Local\Programs\Python\Python310\Tools\i18n\pygettext.py -d base -o locales\base.pot app.py"
# Creo los archivos base.mo "C:\Users\fezz2\AppData\Local\Programs\Python\Python310\Tools\i18n\msgfmt.py -o locales\en\LC_MESSAGES\base.mo locales\en\LC_MESSAGES\base"

_ = gettext.gettext
language = st.sidebar.selectbox('', ['ES','EN'])
try:
   localizator = gettext.translation('base', localedir='locales', languages=[language])
   localizator.install()
   _ = localizator.gettext 
except:
    pass

# Implementacion del SideBar con contacto, cv e imagen

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


# Implementacion del cuerpo del portfolio

# with open("style.css") as f:
#     st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

st.markdown('''
<style>
header {
    visibility: hidden;
    }

.css-1lcbmhc.e1fqkh3o3{
  margin-top: 3.8rem;
    }
.css-v7iw96.edgvbvh3{
  margin-top: 5rem;
}



</style>
'''
,unsafe_allow_html=True)


# side_bar = """
#   <style>
#     /* The whole sidebar */
#     .css-1lcbmhc.e1fqkh3o0{
#       margin-top: 3.8rem;
#     }
     
#      /* The display arrow */
#     .css-sg054d.e1fqkh3o3 {
#       margin-top: 5rem;
#       }
  
#   </style> 
#   """

# st.markdown('''
# <style>
# /* Left sidebar */
# .css-1iyw2u1.edgvbvh6 {
# margin-top: 3.7rem;
# }

# /* Right drop-down */
# .css-r698ls.e8zbici2 {
# margin-top: -1.7rem;
# }
# </style>
# ''', unsafe_allow_html=True)

# st.markdown(side_bar, unsafe_allow_html=True)

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Chanin Nantasenamat</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
  <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#bioinformatics-tools">Bioinformatics Tools</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
"""
, unsafe_allow_html=True)


selected = option_menu(
    menu_title = None,
    options=["Home","Topo"],
    orientation="horizontal"
)


selected3 = option_menu(None, ["Home", "Upload",  "Tasks", 'Settings'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
        }
)
st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Experienced Educator, Researcher and Administrator with almost twenty years of experience in data-oriented environment and a passion for delivering insights based on predictive modeling. 
- Strong verbal and written communication skills as demonstrated by extensive participation as invited speaker at `10` conferences as well as publishing 149 research articles.
- Strong track record in scholarly research with H-index of `32` and total citation of 3200+.
''')

# TEST
st.title('STREAMLIT TUTORIAL')

#HEADER

st.header('this is a header')

st.subheader('this is a header')

st.text('this is a header')

st.markdown('###aaaaa')

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