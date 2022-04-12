## timemarks-for-youtube-channels

Search a YouTube channel for a specific word/phrase. 

Demo --> https://share.streamlit.io/maximilianfreitag/timemarks-for-youtube-channels/main/suchmaschine.py

<br>

![Bildschirmfoto 2022-02-14 um 17 30 31](https://user-images.githubusercontent.com/46624616/153905222-e51d9d3d-17d2-49b4-b06f-58172cb718b9.png)




<br>


__________________________________________________

<br>

### Current bugs: 🐞

- [ ] If you type in E.g. "red" into the search bar words like discoveRED will be displayed. Also non-english words will show up e.g. the german word "REDen" if you type in red as the search again.


<br>
__________________________________________________

<br>
<br>

### To-Do list: (Things that I want to add as a functionality)

- [ ] Implement multi threading for faster results (Iterating over 500 videos takes way too long)

--> Note: Here is my google colab file where I was able to increase the data fetching part by 500% using multi threading and code run in parallel
https://colab.research.google.com/drive/1i5dHBNwIw8iV2kTg_LnKOrT_fIT3DtMI?usp=sharing

- [ ] Implement a cache where results are stored, so that the user don't need to fetch every video again if he/she wants to search a different word
- [ ] Being able to search the entire YouTube channel. For demonstration purposes I only indexed 30 videos because my iterative algorithm is too slow for now
- [ ] Add 50 YouTube channels


<br>
<br>

__________________________________________________

<br>
Note to myself: This is the code for fetching all the IDs of a YouTube channel

--> https://colab.research.google.com/drive/1rlverbo9tYslhXyvKMQh591u6MylJWLu?usp=sharing

<br>

__________________________________________________
<br />
<br />
#YouTube #SearchEngine #GoogleForYoutube #Mnemo #Informatik #python 
<br />
<br />



## License
This project falls under the MIT license.

