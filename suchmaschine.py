import streamlit as st
import pandas as pd
import numpy as np
import pytchat as pytchat
import matplotlib.pyplot as plt
#import plotly
import plotly.graph_objects as go




#Favicon and Header
st.set_page_config(
        page_title='YouTube Livechat Analyse                 ',
        page_icon="📊"
        )



hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 






#START VALUES
authors = []
messages = []
supporters = []
timestamps = []
laugh = []
mods = []
gesuchtes_wort = []
gezeigte_worte = []



liveChat = None



col1, col2, col3, col4, col5 = st.columns([1,1,5,1,1])


with col1:
        st.write("")

with col5:
        st.write("")        


with col3:
    st.title('Youtube Livestream Analyse')

    st.write('Gebe eine URL eines bereits beendeten YouTube livestream und vergewissere dich, dass die Wiedergabe des chats aktiviert wurde. ')
    st.write('Die Analyse funktioniert nicht bei gerade laufenden livestreams! ')
    st.write('Hier ist eine Beispiel URL eines streams der 60 Minuten ging. Ich habe leider keinen kürzeren stream gefunden...')
    
    st.code('https://www.youtube.com/watch?v=e7EVbT0W9uU')
    
    st.write('Wenn du deine URL eingibst und auf "Start" drückst, wird die Analyse gestartet. Die Analyse läuft solange bis der stream einmal komplett durchgelaufen ist. Sprich, wenn der stream 2 Stunden ging, muss man 2 Stunden auf das Ergebnis warten.')
    st.markdown("***")
    
    #text box input + video url
    url = st.text_input("Enter the video url: ", placeholder="https://www.youtube.com/watch?v=QH2-TGUlwu4")

    #if url is empty display enter a url
    if url == '':
        st.write('Gebe die URL hier ein und drücke "Start"')
        video_id = 'https://www.youtube.com/watch?v=e7EVbT0W9uU'

    #if the url does not start with https://www.youtube.com/watch?v=
    if url.startswith('https://www.youtube.com/watch?v='):
        video_id = url.split('=')[1] 

    if url.startswith('https://youtu.be'):
        video_id = url.split('be/')[1] 

    
   
    




#Diese Funktion wandelt alle timestamps (25:38) zu einer einzelnen Minute um (25)
#Also aus 56:33 wird dann 56
def get_minutes(timestamps):
    minutes_list = []
    for minute in timestamps:
        #if minute is 4 characters long
        if len(minute) == 4 or len(minute) == 5:
            minutes_list.append(minute.split(':')[0])

        elif len(minute) == 7:
            #input: 1:11:01
            #output: 111
            
            minutes_list.append(minute.split(':')[0] + minute.split(':')[1])
            
    return minutes_list





chat = pytchat.create(video_id, interruptable=False)



def plot():
    st.write('Fertig! Hier ist das Ergebnis:')
    st.write('    ')
    st.write('    ')
    
    st.write('Wie viele individuelle user kommentierten?')
    st.write(len(authors))
    st.write('    ')
    st.write('Gesamtzahl aller Nachrichten')
    st.write(len(messages))
    st.write('    ')
    st.write('    ')
    st.write('    ')

    st.write('Anwesende mods')
    st.write((mods))
    st.write('    ')
    st.write('    ')
    st.write('    ')

    st.write('Verlauf der Anzahl der Nachrichten pro Minute:')
    occurences = get_minutes(timestamps)
    #plot the occurences with streamlit
    #st.write(occurences)
    st.plotly_chart(create_plotly_figure(occurences))
    #st.write(occurences)



    st.write('    ')
    st.write('    ')
    st.write('    ')

    st.write('In welcher Minute lachte der YouTube chat am meisten? (haha, lol, lel, emojis, xD, ...)')
    laugh_occurences = get_minutes(laugh)
    #plot the laugh_occurences with streamlit
    #st.write(laugh_occurences)
    st.plotly_chart(create_plotly_figure(laugh_occurences))

    





def create_plotly_figure(occurences):
    #create a figure
    fig = go.Figure()

    #add a histogram
    fig.add_trace(go.Histogram(x=occurences))

    #add some layout features
    fig.update_layout(
        #title_text='Minutes of the day',
        xaxis_title_text='In welcher Minute',
        yaxis_title_text='Anzahl der Nachrichten'
    )

    return fig    
    
    
    





#Die Hauptfunktion zum sammeln der Daten
def runChat():

  global chat
  
  st.write('Daten werden gesammelt... ')
  
  #st.image('https://media.giphy.com/media/l46Cy1rHbQ92uuLXa/giphy.gif')


  while chat.is_alive():
        

        
        #display a gif
        #data_load_state = st.text('Please wait...')
        
        

        
        for c in chat.get().sync_items():

            
            #Alle Timestamps
            #TIMESTAMPS 0:00
            #time_elapsed = format_time(time.time() - start_time)
            timestamps.append(c.elapsedTime)
            
            


            #UNIQUE AUTHORS
            if c.author.name not in authors:
                authors.append(c.author.name)
            
            if c.author.isChatModerator == True and c.author.isChatModerator not in mods:
                mods.append(c.author.name)
                


            #FILTER MESSAGES
            if c.message.startswith('!'):
                pass
            
            elif c.author.name == 'Streamlabs':
                pass
            
            #APPEND AND OUTPUT FILTERED MESSAGES 
            else:
##########################################################################################################################################                
                
                messages.append(c.message)
                #st.write(f" {c.author.name} // {c.message} // {c.elapsedTime} // {c.amountString}")
                

                
##########################################################################################################################################

            #EXTRACT LAUGHS
            if "haha" in c.message or ":rolling_on_the_floor_laughing:" in c.message or "lel" in c.message or "LeL" in c.message or "LEL" in c.message or "Haha" in c.message or ":grinning_squinting_face:" in c.message or ":face_with_tears_of_joy:" in c.message or "lol" in c.message or "LOL" in c.message or "HAHA" in c.message or "XD" in c.message or "xD" in c.message or "lol" in c.message:
                laugh.append(c.elapsedTime)


  st.write('Fertig')
  
  




with col3:
    st.write(' ')
    if st.button('Start', key="1"):
        runChat()
        plot()









footer="""<style>
a:link , a:visited{
color: red;
background-color: transparent;
text-decoration: underline;
}
a:hover,  a:active {
color: blue;
background-color: transparent;
text-decoration: underline;
}
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: transparent;
color: grey;
text-align: center;
}
</style>
<div class="footer">
<p>Entwickelt mit ❤️ von <a style='display: block; text-align: center;' href="https://www.instagram.com/max_mnemo/" target="_blank">Max Mnemo </a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
