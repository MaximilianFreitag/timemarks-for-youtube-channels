import streamlit as st
from PIL import Image
import youtube_transcript_api
import simplejson
from youtube_transcript_api import YouTubeTranscriptApi
import urllib.request
import json
import urllib
import os 




#Favicon and Header
st.set_page_config(
        page_title='Search YouTube content                 ',
        page_icon="🔎"
        )


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 








col1, col2, col3, col4, col5 = st.columns([1,1,5,1,1])
img = Image.open("google.jpg")








with col3:
        list_of_video_ids = []
        all_transcripts = []
        
        #YouTube Video IDs 
        #Example: (https://www.youtube.com/watch?v=...VIDEO_ID_HERE) 
        
        cubby_Emu = ['EWfZ907Cpy8', 'sx93aUj4A_o', 'GE_00MgKMEI', 'gF69voHU_ys', 'tAtaIZD0Ebs', '3E75UvmY9GA', 'fOPP9Qe10Rg']
        veritasium = ['IgF3OX8nT0w', 'ao2Jfm35XeE', '9cNmUNHSBac', 'bHIhgxav9LY', 'cUzklzVXJwo', 'q-_7y0WUnW4', 'H1_OpWiyijU']
        kurzgesagt = ['xAUJYP8tnRE', 'XFqn3uy238E', 'F1Hq8eVOMHs', 'LmpuerlbJu0', 'Nv4Nk4AAgk8', 'xaQJbozY_Is', '0FRVx_c9T0c']
        blue_brown = ['ltLUadnCyi0', 'F3Qixy-r_rQ', 'LqbZpur38nw', '-RdOwhmqP5s', 'ojjzXyQCzso', 'e50Bj7jn9IQ', 'O85OWBJ2ayo', 'lG4VkPoG3ko', 'b3NxrZOu_CE', 'X8jsijhllIA', 'mH0oCDa74tE', 'wTJI_WuZSwE', 'QvuQH4_05LI', 'pq9LcwC7CoY', 'D__UaR5MQao', 'elQVZLLiod4', '4PDoT7jtxmw', 'cEvgcoyZvB4', 'IAEASE5GjdI', 'ZxYOEwM6Wbk']
        leeroy = ['Ii1oL0oiTD4', 'pd2rmvu5cPE', 'dzConRV8BiA', '9coLQehAAdE', '6plNOU6bIcQ', 'XJLLLMmRfek', 'xxC2JYPbc6g', 'cc0FhX6GrHI', '_W_Kw8tS5sI', 'JlMBK6Oq8gI', 'DnhpLDKX-s4', 'XfGz-I8BRL8', 'O8fVfA8udFM', 'HTe0fGFDyRY', '_tVJQhVO6j8', 'vYGEkC_0LX0', '_gPSeKkoC2c', 'BDHidPgyxkM', 'jKC9LNw5nQw', 'Ro2tYAjTZvg', 'aNZhJ5wtUZ0', '2V7Ls6gRpeY', 'qYoT-ArMvmQ', 'JHmkQJydins', 'HglW5Xpxyho', 'oJ2er4EnQiU', 'GjwysOCv3TI', 'MVQb_5rQZBI', '3MQjDCIevMQ', 'RRsvOCzEZzM', 'dnuW9o3nNec', '0RG6JY3PGec', 'm9hZzWA0R3k', 'VG2pFPyK_lg', 'Wm6JPGy9-cE', 'zv0w05lXCgo', '5CNYjeHt8V0', 'n_9XT_cIr1M', 'ICK6w0wRkCw', 'DsI-9DWNeMM', 'A2Mslb7dhV4', 'i5wPWkDaQJo', 'NDQ6TB4BLbc', 'cUwawuKZw9Y', 'CE7cbhWJTfw', 'pdYMuJnV-iI', '_jy_gbSebAo', 'RFQVZhs-IgE', 'iZ0RNzTzSno', 'WoqPCpMfW3g', 'Yc3BDOHhaeA', 'gdNDBLJjol8', 'A70i3AEcc40', 'gyv-SSvgzSw', '5fa-s7s2GQY', 'MUU1smdnXdU', '8lgtqe2b1Fk', 'L6afYqup8_A', 'Ex6h9emJMkg', 'br8dwCYo7JE', 'eaQTRUIddNs', 'OlErDHStAZo', 'z2J3IcAzWi4', 'duJJgmj5QvA', 'eGZjLDlLiU4', 'tezsFICNqcQ', '_ftEYiTbExY', 'gqDlGthwfxU', 'k9NiBFmvF3k', 'k_IAq4jvb60', 'OK5jZYHHsJE', 'FiBoIp1Z0cE', 'gLjPPy7RKWs', '9Ay4nh23ljA', 'aphBoPknQUM', 'oghsit8sMS4', 'u_18E5NhJSg', 'XmZEHCCmeYs', 'LSqz-WIUe7k', 'Md4ggn87EzA', 'PbUQ0PhzW-A', 'bIS2xHyrRf0', 'gUSYrlf3miA', 'Pp-GDNQ2awQ', 'nL-CMGhlKzI', '7Ryg1LwCPiA', 'dvVTBKbWdSQ', '5nR0DGIWGLU', 'DTVIgoDKL1g', 'mDmtIs8hh7Y', 'gTVhj1bXew8', 'wRQyrlHPGCA', 'VgRz3cur--4', 'HKudBgDEOoo', '3-A654195lo', 'hJ6MLPqD2pI', 'poOyaxmdGd4', 'onvwng5lgqg', 'x7p7Pfu_ubg', 'kiBuWb1x1Cc', 'aKaES7IZtbc', 'mj1Xp00TucA', '5osyByeS6Gg', 'UKT-cKoVRpA', 'xk4XHcaFDSU', '4HFVtxApzpA', 'PK_FTp4iHaQ', 'Hj4z0EUKBes', 'NfA4MAQ8qc0', 'yRrPZXI-_jA', 'QzO-N0mM-eQ', 'm5e49ak61Tc', 'gZwXQx7d0rg', 'OJr4CYj7-q0', 'ksOOZZslwPg', 'jmaWzgmjopw', 'zNRgcTKPH-Y', 'ieHwy3SNU9s', '0q35I2fX2ks', 'wqiBZiX_LKE', '8C2hirxrDYk', 'dsdTPOgsS7o', 'vES5zEQZDzU', 'F73iM-ej9M4', 'zHjLOpYXxpI', 'A8aDVI4jO70', '__Olbh-8scw', 'PwWbBYPS2nA', 'J5dfFN73AEM', 'HzNuzx-igz4', 'ejt4Q7Eeojk', 'mf0Q95pB8ME', 'L4v9oY7XQs8', 'LTBqrlS0JGQ', 'Y6ZL-xiQn68', '-Qb5GHqzZ_s', '2so8q-3L5Lo', 'JMdFVKj995o', 'IWBJnCTOs48', 'lZm8VjQs46k', 'xf-rbUFacFA', 'aDZiyP8vDRA', 'OinZnZdiXGY', 'VwQ10v_2NBY', 'sDdbo3C1Odo', '-fjAYYGoK1o', 'jpo29R289d0', 'LaXUYmWAQNo', 'IwH_9c1El_k', 'IQAR2oC3gj0', 'b1DEtEJ_-IQ', 'o9cAq_YcaKI', '-nEORAuyi9s', 'jG8Z39IIYiw', 'WOcvfR207U4', 'A_LVdNv3j_M', 'kDoqUnHQlnw', 'CToR0kTNWvE', 'FDgExmX0vyA', 'WEIX7hOH_zM', 'SeHWLYOiXrs', '23PtwdZaMg4', 'G01bQYIbl8s', 'iicL0R4kWUM', 'W3KwqN9L0Dk', 'yElkYuNGfdM', 'Ebym_TJccPs', 'TUUj7FSJ7Xo', 'IYwolMFNQbk', '7fJqNFfKerI', 'nMfLkJDnY60', 'zANucVCPyek', 'ZjFHIXMTamI', '9nVe5GKDAvk', 'd1ykSESpiok', 'C6xAYIWxcCg', 'kLqWEsHeNgg', 'YKUjc8xoZ9I', 'n4Oxn2MCrZo', 'Cf_MO8zraBg', 'J6e8IO7cryI', '4ANtqaoP7Js', 'gZLSfmWzUhc', 'Fg89N5ZuAa4', 'gKd92bHPzJ8', '8imD9KwWMjY', 'WZhmXPNo72c', 'M80KrvOR9uw', 'UKf_skvq7z4', '5VVCyBhARpo', 'DzRlK3HGp7E', 'B3m6CRRHm1E', 'VX3rGH7GpIs', 'JvdojQsc7wk', 'KWKsvSZar2w', '1VMo1dgJRgY', 'czQJjHzGnPs', 'BXO-_T8ptgs', 'YFf2tF0UEqg', 'BG6kFZKXxk4', 'mc9eLKZpVYo', 'jP11zwAwxis', 'Ks-vAlOnOBI', 'H2iXuDFK_h0', 'Rbx2w3BYHNc', 'XThK5Ac_Ckc', 'P3TCyOPCS7w', 'nA3FOFhy5No', 'GFgHLKZuMF8', 'O1v10doZ5qc', 'W6iKwYCS2Ck', 'JghUxkAHBDk']
        mrWissen = ['BeBH7Q0DvZ0', 'Hx5ozHSi3ek', '4JbaK-h-T04', '8wG7JnV-EAk', 'IRnxpdF2gLo', 'RMc-BREDmIk', 'Q9bkKI2i9jc', 'QBj7MBCzodQ', 'kyqXJx2R248', '3ZEhLpSjHZk', 'Tm1L0zXxREU', 'Z9oB3z63-yU', 'S5AJvJKUy6E', 'q9oPnnAuo4w', 'mNwRnTF-Jdk', 'wyjenzWbg5E', 'DoH_MWRZhIE', '2U5rDhkYQAE', 'qowsHwEBjoA', 'oWHGtvMchOQ', '89jYKquWSOs', 'gxKY_hseLNA', 'cxhPfQyn_Rw', 'j51lrdzxBg0', 'eZ10URGGzng', 'YjKKy361zZ0', 'pdDMf1Ra8G4', 'rkHcqYBUjcc', 'ZVBxklE6o-I', 'IhrLae646tQ', '8kESpELLv_U', 'US3fwfUaTPM', 't7hi_QWZ2GE', 'jCAuKo3XK-I', 'VFiLOorwV1M', 'wriZyLXD6G8', 'Abjh2bOlXoc', 'LUaY5LPJTFg', 'jf3mKjF1_w8', 'qUaJ8HvS1j4', 'RWddBq4WnPs', 'TiXzhQr5AUc', 'wSfuyIAUsu8', 'nlqIkRQyYD0', 'KFn_KTcll6w', 'Ao1Rof8kkAs', 'iRsMmKnBthM', 'jET5873K-KA', 'bGTHexacG7w', 'whLho7HfN4Q', '2weZNQ1xmdE', '7XRlZErHwpM', 'It8E6CwqTio', 'SssutSHO9C0', 'igLeP6H3OBE', 'yeaNw2HiSwk', '1h_jPCsBGNk', 'blktjPp2E6A', 'pLzQc6OZHik', '5_Qi6u23hPc', 'gspCJFPUWDw', 'x6C2oyDLjw4', '3ZXGvYQI5Y8', '_oLLW13DzDA', 'yefSs2VY4IQ', 'zSHv1m4dTOM', 'QOnel4W34So', 'zPN1RgoyFSE', 'j1roahcF3zI', 'hzB3fbTPIKU', 'bGOthUru6hA', 'zyoyxDNhkAo', 'DcVePbOWETU', 'pyXS4ytSIGY', 'NBhQjirlsS0', 'IUqGpj7dLfg', 'osEC93tPcw4', 'BPs58x2h0Hw', 'rjyhtZxsP20', 'ozk5wUhLAxI', 'wm0qawlD5ko', 'IHlilIRt-qY', 'IMWcEEKBwvg', 'Fh5U7l7CXho', 'V6lo6yQ9_34', 'POU5TGGiNVQ', '1EI4Vwhq9Ew', 'tKxMwnxhsXw', '2pGCo8b-Vjg', 'p6dY4pfKbZg', 'yS4CQMMYTA0', 'dAc_UzsY1_E', 'eskstAZEAN0', 'rseY3MX1KqI', 'mViegARpy4I', 'Ec_Nn0OiTRc', 'Awrr2GLN-1I', 'I5EIs-LtEKM', '850IcWQkV8o', 'bqhoQcWqGNA', 'vdJuUqd0iK4', 'EtL5-VJBjx0', '0ZUvVUfyP9I', 'GkLCj_6p0fE', 'OGOtAOtfHiE', 'x89EvbjWftE', '-3Y9oqT-rVU', 'tRVj0i3VOvY', 'Hhq0TbyRrwI', 'Fb6I1fZ3N_U', 'H7Qy7MhbedE', '0YVmA-XdXsI', '67c01f95oto', 'XPlU6K2jltQ', 'B1QEdWOnGSg', '8D2x1MzqVpM', 'D_w-SycRJPU', 'lePXiqkK7tI', 'w7cf0kaYvKE', 'EorxpSjcTuI', 'zOUQZvm7c7E', '-NLUWZqGpyc', 'iFXOGunGx88', 'Y3t5EH3MQqo', 'z8sEN9K3LEg', '6LTz9YZwapU', 'eQoEd6TPClQ', 'K4vwnFuGNuY', 'DSMsNtHBFJA', 'JFGUBQj0RP4', 'iB2E8jlEt_Q', 'xNcaMTqWRYw', 'pBfQ5bp6SAc', 'Hkbw1Pn6FEE', 'FvzrAyXkHr0', '11ofQQOKrPY', 'coJSLiUhaKc', 'XXrMv4xrc3s', 'spNoe-kzOto', 'CI0Rb-Yha1Y', '_cHaliJoAiQ', 'xP5zaQTo7X0', 'zMJLx5VdGlE', 'mjak9u_sdRY', 'BQpbIjXESwE', 'YWAzVYPivWE', 'DAe5BuOQCSM', 'EmZ9meLKQWA', 'opssCasA7MA', 'AKlDC-If7CI', 'AeOtbACux5w', 'i6qq-MIogEE', 'tTYkretSGgE', 'LS1X965Sfpo', 'DeRkwrWh_Os', 'rK-sIAjvwpU', 'oIjlYW3eXdQ', '7BTELBjyiVM', 'GNoCKvPEbW8', 'RMP0BqUKJmk', '5CIQqad8nEg', 'upRKqcKKSfQ', 'dGg8nhserMg', '7x6_m_mswaM', 'q13SVk54PL4', '3lcSWnm757E', 'prEO9S-ThXI', '5TknElWTvYc', 'Wf3ifPUf5OM', 'IWZwx3lNdys', 'xr4janMiEPE', 'SVAN-vASnl8', 'sN3V1ppdTk4', 'j2Gqj84sm60', '1mUY2nWsg4I', 'xgR4H2i9eBI', 'CzsTk_JRj80', 'NW9W6z-pkg8', '0J2kpdAlKF0', 'HQKJ4mNMxyY', 'v25hjmf34wQ', 'qSA6YiHAIFw', 'xkm4BEU_-R8', '2Ow9PXtJ6VI', 'QlT43c1PZyk', 'VB_aXW0CSlQ', 'kW-r5zggueQ', 'jKTIrfOY4qk', 'FaMfrufKp6U', '1e8sRPB7kAo', 'RfL6WmyUrdU', '-Bqo40ipk3I', '2T6j5QqBta8', 'wUWrhLNCnqw', '11V0YvPrRGc', 'fdG7s4XvKoM', 'stq0ZB5HHyA', 'RJlVzkfpvN0', 'Ogg9xvsJrXA', 'vrDDyhTpepk', 'tDcgefrLslE', '5rXM2MfywS4', '5ruqOdW3il8', 'ZSMvWosDDmw', '3M2-mvXsxVk', 'NjPl4RivIYE', 'oEDmdefpiQg', 'PJK81Gqo4js', 'TRl7p0GamlU', 'inlN3HiHL80', 'LhSaqWniSac', 'FHvP4RKLUp4', 'y9vGwYCR4wY', 'uxxMMuHFlVM', 'ClYYtBRCETc', 'jer1xIKCOMg', 'AGdFG7_jDbQ', 'znUg17W526o', 'BLu3qJ_p0ZU', 'uFcpGmN_bEY', 'kjiUEuCPEeQ', 'tQHlOjMGS-M', 'nE7wCyvCXS8', '2HjRnr3AfFo', 'weB79v4Zstk', 'XapB1C7P09A', 'sWkC_529gUY', 'd0L0VOsgUoE', 'AZOiUtVj5tU', 'YPpmeLjUTSM', 'Q9tnTi4oCEk', 'N833JSKYZcs', 'e58AXKUCGhM', 'yQufBfxzjwY', 'Jt4RJJ3-PqQ', 'HjOu7oOXHSQ', 'aXYRnGtPJi0', 'MyuC5kYqRTk', '194eD9wCW4k', 'JQ5k3Amavqg', 'SJz-EDV2C4Y', 'iCrFm56hguo', 'Pj3ku92lb6Y', '6GiiP5ZXe4s', 'XvKp77qPA-w', '-FyFCXCuGoc', 'XkCgeI9r5as', 'bGKoHhntqYU', '_m5enJeq6j4', 'xiGBkOQaZys', '7SV4cj-dcTg', 'NCS-d9dxEPc', '2broOTfT57c', 'x-S6x1OCdD8', 'zusFLoaV2ls', 'KcQ47ZBbuBo', 'GiDB8giv_Xk', 'GQJ54nI0wGk', 'jziBPIVh4XI', 'mLOCv3ZcwuQ', 'amzqgKpI88E', 'WsRNDJgUbLI', 'GYwkMErXK48', 'QCVkDM59PvA', 'hcxnlMDXj1U', 'uFJuSilOA_o', 'wlFMwAuYxsk', 'S-WU2zCMC7E', 'WXwING44xBw', 'BqigJmEHYuw', 'B8Opg4p_LPg', 'pYRwTWzSEqg', 'z6TPjly_6tA', 'FpCWTyYnSDo', '6_G8FIhrtIk', 'F5tuXkd7a-8', 'sJy6XUyUV9o', '3SNCow6cGSg', 'TIvk_r7TEYc', 'v0_qKrSlMZ8', 'TTfBfqfi-kM', 'YBZHEYZnjkA', 'sE5OJ3H30fs', '5dL-OF5JY8E', '0PZmEbwUGV8', 'KNC-tDt0YRs', 'u7YEFl63xXc', 'gVH6LDoTCzY', 'KZp15FYS_ds', '8WLyAe15UBE', '9X2J5dqaELw', 'iWL3Fp0Uh80', 'bqTY5H2DLjc', 'NAq2KB--ayE', 'E-7XPit-R7g', 'KfkfUJjRdJU', 'uQkPNIZMhos', 'tja28N-4Tj8', 'RAojDzz8nTY', 'l08mAGfNbiA', '5Dz79zu26FI', 'XSAxi8SzUYo', '9oa4dLbNHK4', 'k1wuYnZhxSM', 'jESUFb9mpO4', 'qEwxPW24kJw', 'hCIyB-jO0cY', 'YIPYoUa7ytA', 'HtEriwPA7s0', 'GVSIyyC0dx0', 'TmAjpStEtyQ', 'm7QA9GH_rXM', 'jlWIdVXQABo', 'vMquMgDI39k', 'iWvi21FuzhI', '9Q35Zp_NN3g', 'WlGTJAz4k9w', 'Q31vEAz9y5A', 'bJ0B0RUmeEs', 'sCB8_AuA_Mo', 'DathnYDq_Tg', 'N4DyS7rGfWo', 'Y5Z9tDB4if4', 'hB8vJuO4CUI', 'G4DVxsq6JSE', 'q9FyeDvCy98', 'DIsgtXtob1k', 'yMBzMQYZZys', 'pDdKN_tpdT4', 'vlbAj3jd1qo', 'ma1M81GuT5I', 'oyZ1g6J5Zb4', 'BPQ1Zp980D0', 'iQ6NxvQRfq4', 'O5dxXNVV9co', '0905ODYCxxg', '8YqMZLVd2h8', 'hCA4iOPjZ2w', 'iAfsGvvnbXo', 'XxEmM5raDec', 'eRbAQilJWKs', 'VfjQ-qCWTLc', 'iaVNDMgUtRo', 'yXCNSrQxUu0', 'X9QdRgEilGE', 'pQNR0cgd5bg', 'upo_P3e0Rzg', 'GD4w3G6_Zx8', 'u_qpOs6nifQ', 'aTwGpS5eGLY', 'gg7LWb2sL1Q', 'vUFJmoEuPEc', '3yS3lLM0zAo', 'fhm7oxpeFP0', 'HSW0lYWzze8', '10r_xwYTKbI', 'H2cpxUryixA', 'Q_9QsETSXaM', 'rUfdQeUYmug', 'TFFfXI8iyko', 'i8tYV6hQyuU', 'ZWdA4p9sFro', 't7SoWmiFk7k', 'Jg6R9AxdXSQ', 'OYNaXMq7znE', '0tNbgVXtQIU', 'Bp_hdF4i68w', 'Y8lQnAYWrhw', '_uSkqIPwWsY', 'JOy3nAA8A_c', 'ZbX__5vK01I', 'DzOectt3mNg', 'bbgtc0f7G8M', '7rqD_cZ-KGU', 'lQjoOa2LezY', '7rU15qRVg9w', '2jvIDv9ZXh4', 'v4y5dmpK4IM', 'HAaaQWbnO8Y', 'ZFLkEKQZ-pA', 'MZuCC2nNeYE', 'dtkeU9EgqvM', '3ykd8jv3nWY', '_raOIUoLvcI', 'NSpy80caNBs', 'o9SVU-G1mLw', 'L2B4kY-wdCY', 'TlX3fWKKMpQ', 'h5Tu-L_doCk', 'QwpBJVppmaU', '-tZ2tK4_G5M', 'sw_ZRJK4PnY', 'TG1X7uasgLE', 'Kzhl7pNVLNU', 'yKoO_oZMS70', 'hDonVDFwpwg', 'MHRrjnxHEHY', 'ESLa3YT1nps', 'TN_ROjzbtUo', 'xwMqd3GV7is', 'xqXlQY7mOhg', 'xHBAgKlEXy0', '2OJZzdXpObs', 'dHmYeutMm98', '2O7A7GtkAmU', 'QqqF82KTWeI', 'R4-VQkFYh-s', 'ExYkWSLbBOI', 'nqkNiPPoGxQ', 'XgQiOXCRb3Y', 'LWiTgV5-xO8', 'MW9EUpESqQQ', 'gYm86N5vPv8', 'pvoQOPAHZJw', '_ttpZXcb7OQ', 'T7GyA4UseZ0', 'T4M67GzzGLU', 'spD9G5s8G0w', 'gmurpUWByfY', '2ga-ZDxwl7Y', '0AqO5NFuIIA', 'FRFUP8U7U8w', 'Zp1oSn9m9j8', 'hpI6Y1Hq3Fc', 'NIDRiKHC3_A', 'ixfqAgvuzFc', '7Jf0H9no8vM', '-SqjAHnVK8M', 'aOzTmW2I_us', 'j3JOmrR9rNc', 'c88tm-WnjWc', '1zi41PatKto', '9MJivK9UHKI', 'wRLZJOI--sw', 'PB92t2Q_sx0', 'LsEC8F9PiQs', 'Fh-exEElOU0', 'ORTZf9XX47k', '9W57bnSzToY', 'q4uUMmnIwds', 'yHfEubzV2mc', 'ignGZnYKXQg', 'QY6KE3io42E', 'SLTMd34ZrMg', 'WDxKQaqi1JE', 'NGv2lkDVkIA', 'WnVR5zBrh_w', 'so_l-CaJvH8', 'YjhS-SSCVbc', '10E7345eViM', '8LkIx1bESbw', '1ZjpmsXGlbU', 'eFVv1vPHedI', 'xxI0lHNc-uI', 'pVCMOFqInGo', 'slVmDcmFECA', '5RHRXE6v54U', 'XdBixhJM7Uk', 'i0gqIYuzpJs', 'paaKNerl0rg', 'Xc9BDgKIQdk', 'bauzzIOwGbs', '0UNkBqI3F7w', 'qjmaPytroMo', 'ssOy_wBbWEg', 'okSQd1ogUgo', 'reADZNVgeH4', 'GFvmGMJ2CZo', 'GnCjP7bfLzo', 'a9s-bko1YDY', 'EinSd4xPoK8', 'FlEJ6uo6Ob4', '3l1KLZMitI0', 'lxySZZCcO9A', 'tee3u8qIJEY', 'ZHM_n_C1KqI', 'J-Q3_VpZWso', 'JKwIGzcqOXg', 'ibKbclaE0AQ', 'orS3UqRPOTo', 'kZ-j4dH7f70', 'WxZrCluDWcE', 'WbY7AY-rRGE', 'Ele_qyMOLKE', 'Fey84ju3FoY', 'deQHO4h-_Lc', 'hZECsgs_1W4', '8sCzsr6SAjk', 'udKCtCg_zEg', '6-LcibwR7kM', 'BiMqniWA9Ek', 'XvOYzTV_XU0', '-sKxT1-JVp8', 'v2ImIhhiL8U', 'AIm_VIaNG04', 'VVoY-HEJnDA', 'Z3b0mHLiwPQ', 'BZ_mjUd3Vu0', 'hdfVpkCPIXI', '-MznmW1O_IE', 'XYZgPEmbKqg', 'YzCSJmbU5Nc', 'c8WiD7zd0M4', 'jzIAkmAB1ac', 'YVa5Xq6ODBY', '1gBtstAYL1o', 'E_MBWW-z3N8', 'HCaWjjkQfTY', 'k-3PhTTcsqE', 'XFUCOz_suyc', '3o8Mcr5j0P4', 'vrljhSNK2Ro', '08yvW-n5X64', 'nfj5yz_5DYs', 'y5Oxjs6Hn2I', 'FoJ5I3p0Ovo', 'MVE9MZjzTvA', 'KKjfONXewtA', 'v1Eu8t94Qio', 'RvCUtgyG0lI', 'qZvsXFbEmRA', 'MyyPdn6O4Xo', 'dBdvODaRcbE', 'Ymo7jlG6CAU', 'MBApqMZGbt0', 'G-89Fgvc6xo', 'GNE0NOhN0pU', 'JDQMLjGAyNc', 'sFXuBWg9mXo', 'slW5wJBzad4', 'O17BfR5L3Ps', 'Ww4q-Fc7__4', 'qGAREJOexOI', 'stmWpqbGLWU', 'RKoAUknCkxY', '8W7NkGtnK58', 'nQsRhE0LQ2Q', 'LWVsupY8oco', 'wDY1bDLBubc', 'lp32-d2FCDQ', 'ZKkCNBVYQDk', 'OrXRvrBU1kE', 'jdbShawcsKI', 'V3XagMeG36A', 'BGsNGnDiv5A', 'vH6ySq-_oaM', 'MsoOL2KLwgE', 'bYQ887x2dhA', 'GZISQPQIKro', 'Bz4j6CswZPQ', '0431mWYeuKQ', 'O_yGogwGKSs', '9U5PIal6Gyg', 'jR8czENYgc0', 'zgrBmCVSP9Q', 'ev14cqwu2vk', 'QvKCRUOKj0c', 'gCeK5vapPrY', 'jvJS8IyZvUc', '-G7U4JV3brM', 'PMOIw645EKc', 'sXZYvjSjliA', 'BW3M2mJmu_8', 'W2fsSkMdiBU', 'S2nTKGuIoNE', 'B96dyDKR4bI', 'G0CWaYp3s5Y', 'TwDhMihOjLk', 'oYjZvQfA-4A', 'BsacPL1BZ-8', 'l9Nc7A3cnNw', 'FWYqniCwg_Q', 'yMQtl0eVxyk', 'DX4LauAy-2Y', 'xXHlGMWu_48', 'djgPAUQBMTk', 'V_579LG9NJE', 'J9KuZhTMDP4', 'j-xbdiqd564', 'P45e88VRVb4', '8SiYM8WA-9Q', 'BQNjokQDkFc', 'SWGMC5oO3YI', 'mOmRO6Ez42U']
        sahrawagenknecht = ['5Ms0f7XnsTc', 't4noGdNNXXw', 'avtmxgsVux8', '58qxTjXnPPE', 'HEzT9HKj6D8', 'Cbnrgm8V4uo', 'hFMMeqC8fuY', 'SYLsSPSjTX8', 'cjday8GQ1oE', 'C9-oJhuYIOI', 'SLlsrkGwPCA', 'nB_ueqshBRo', 'WCwx94TOGPQ', 'LbnRTQTJ7bQ', 'JaE6UMk1u6I', 'dOCB87649D0', 'l3DwwQ6ePIg', '3zbciNWbCO8', 'Cg4JNKVJ7ik', 'I8MYqaGFTc8', 'ZdtBVODJqBU', 'CAC9F3_pjjE', 'hvQKE0bGq5U', 'kyUaDbVjMr0', 'lirz_z7JSuE', 'kpyHz_7Q5wE', 'zvcdzf5jjd4', '4JwTr2xZjXI', 'Q7bEhtzMqZQ', 'wDXe-3FYhmA', 'xw3qY4kS4HQ', 'juQMBphcboo', '0b-VGNDnN9I', 'rPpYwaNRAFI', 'z9JF07KLECA', 'QsE3xEwsTtI', 'KYrGVcvpz3A', 'bJBEI9Hg6_Y', 'eJSnp0z16MY', 'DQNg15cw-x4', 'm-2ya_y1JJg', 'iwt0EsCe5CM', 'rIlUci-PJVA', 'wqrXAYUtmbc', '0xq5B7Gn2Mk', 'q9XeZOvFUTQ', 'I5Qd6xiU55k', 'yVsj7e0FcgI', 'ZDtCMKdZ_gU', 'PMg-s5dsrrs', 'epVDA5oJm-4', 'UDGl7rCLrVI', '_JW1NmPCOWI', 'Vqv_DLeF3Uw', 'T2bivIDGCMI', 'SX2C60SiB20', 'KUg0UGFjKFU', 'ZFlyZV1jK2Q', 'MiymfIpeupY', '2hWf8bG2yj0', 'wEIvCcPKj20', 'OskHcSVvIY4', 'RDnbyvvRRDA', 'y1oJ1TaLfww', 'RhKSSpCXvnQ', 'SLNoXja7jX4', '0mU5_aIBc-8', 'biY2vY7wPto', '027G5JGJovo', 'zZnCpotRxkQ', '1zgEuAkJm6c', 'tbzWfrUP5JI', 'IkDGL1kFYwU', 'xyLibyPE0ww', 'S-rtuWjSTAk', 'L60hLi8KZbk', '8KZiHF2Ifjs', '0TSy5OMN5M8', 'R3T9YKho2Yk', 'lU_-eCvbkTk', 't7_sLtCKULE', 'bPXSAUkPsgI', 'aLJe9NWt7EE', 'jRE0qb4bG1o', 'uwsV7vKyF3E', 'GiU85X3T6Po', '_T9wZFLt6pI', 'plSg9TxvUwo', 'afNmsL0d0c8', 'yKvCzwhTu-w', 'XQm5DVHSaU0', 'HlGUrEOE9po', 'q3W0zBY_lqU', '_Ocq6Ka_1Lc', 'dUoskQc0Pto', 'iyLVwAmvRx8', 'G6_9tJfaklw', '8CaMZYSPwwA', '2CB_jzEGWOM', 'spJCcYnEiJc', 'MrsMs5fM1Rg', '0tI1iR8bWXM', 'P_tW9MVl50g', 'iXQpNxjU1lw', 'HdXIrXQwgw0', '9wque3La5ZQ', 'y0_oQ-Mg-VI', 'SogcnVxRj4M', 'K5J3e_L3ZZQ', 'ZxAmrKudGRU', 'PN742VYeofg', 'c9NGTX8JxXc', '8WnDcK8Y_2o', 'DsB2_jG6cl0', 'QEBxD-XsWiM', 'SeUMY6t3NUo', 'gDLyedyRGu4', 'b52Irouu_xE', 'a0nCOCPNlxk', '2M8xqY1LITg', 'RGhgywjoY7Q', 'GVUVHfp9apo', '7kpqXdn3puQ', 'sD288bB83RI', '0m_ZjGLB5lk']
        yKollektiv = ['0HFrMjlujig', '2NSDmXWm8kg', 'LyGS30WYej4', 'B2o5zWBRKbY', 'vPdEyRjyBWY', 'OBR0i8QUZVk', 'tnDH8kIFl78', 'IhGmzuH3JDw', 'q4zM3fGG8H4', 'ktqibMVgBMY', 'HgrgLXpbVwA', '2bgSlJRYmOw', 'hUoW0eQqDlw', 'bZZeS_LfNWA', 'qhS6RaIXHpw', '8eA0Fs97yXg', '0P6PXAxhJFY', 'av7JuMKam5Q', 'ePwC698DChM', 'HOJ0nYGLtXY', 'pOW391aA5Gg', '9ZlC4YTtqN0', '7PfeK_w7QKs', '-olxfn88Pbo', 'XcIsw2Jo7As', 'iZU7FWOxpAI', 'Xjblo2rixFk', '2ymXV994HGc', 'TxnuB_zgKZg', 'ZVyaqoiycbs', '6oze4Xd9ndI', 'tkbMtwqC-Hg', 'axH_cSOjEp8', 'c7RPaZkWKQc', 'pdj1Dwsw17M', 'zYGm2CoG67c', '3LnYVQTzTEQ', 'r5iWCHkyxm8', 'O_TYEBZZ38g', 'IuuvgbJUyK8', 'PNy10TfknWk', 'gQp40lfFJwY', 'EqZOcapHzMY', 'ENtBwmS01EM', 'aSnETtKrFbU', 'ru8iZU4qVwE', 'FnyGoN7rNgM', '5NRVJKDa4Eo', 'F0WxOE3bUh8', 'Cj2f296Juuw', 'nPEYyX6KMuA', 'Stsl-mvSbYw', 'kf1ixJICwTQ', 'xD_8sWRmw-k', 'N0CeGmVN99A', 'lxXBQ6s15ZQ', '-Qe7kTAUn2E', 'EtWWCZZwao8', 'j9UA5G3tb30', '3nCt1Ee1v5A', 'rkw4D90dM_I', '_81BpxeA2DM', 'ILD3kNrSetU', 'UAD6Od2D1wE', 'PZPfO7vozVs', '5demogZO60c', 'oc_ZPt-LVBQ', 'FY7XboW7Qgo', 'DW5gu8lqhzs', '-qvkVMRN0gs', 'umDppT51wPU', '5u85INLRgU4', 'DuMKzrfVPqM', 'N3UBM1Jef0Q', 'E8g7n4Gpurc', 'WRqEHqYvxio', 't9DPe8MfgsE', 'o1TJBGjRPh0', 'rufgzq9vTLo', 'GORdLG6snt4', 'TVCOPF9CLN0', 'hOKFvVXTlhI', 'S7Z8B_k9FhE', 'sFwU_NsEVNk', 'xg0ejl1f07c', '0uMiN-GL9NY', 'J7Wd9MFJwbA', '1sxdxJBnmLc', 'SdTsKgohqYQ', 'CrR6ColIikk', 'pbIhmqRhvFo', 'pAqVgCfkLds', 'ArKsF6nbMHA', 'W9aQIrPIYYs', 'umafqnmvRsY', 'PirBEYWiEKk', 'gaU2AIRzG-M', 'oMUwSaPmX-8', 'NBOQ3nXgQBM', 'HeIVI8t2uSk', 'ToMHPRleTGo', 'vGyUR8Q6IIE', '4GtZd4wCX8k', 'C_xuCjikFrg', 'Y4jn-F3lK0g', 'fiCtEg7atxs', 'MR4HWuj2jik', 'PShAl1dY1m4', 'Su0lcdU0gSE', 'yItGm5rPhog', 'JkGdA-aDloQ', 'S5jyZBAKllQ', 'Rq78IITgvJA', 'xxJSLPAfO-s', 'gcN07RfeSsM', 'QGLLH2xvMZg', 'joTyG2npUlI', 'OLY4rxhcOhU', 'I1fnTY_FduE', 'eVGjlZTEEJw', 'ej9-kB7-jRo', 'pUsDtExoBRk', 'mPe4uS9xZYI', 'Ku8NHTHqRUI', 'PzNMTNce4HY', 'nNcFOpVjNc0', '3x8mIaaba0s', '8yYV93qZRXQ', 'cCUwWeD47qo', 'xw0CEcT9Mvo', 'FvJ3U4NH0X8', 'gT9ubFcROkg', 'DOXDewtsEMU', 'oQWwM7tYPYQ', 'yLNfkbKu4KY', 'bnGxqmqJKBM', 'xyxSWCVKDZM', 'bDrNgxIOQ7Y', 'hUM43Up4MEk', 'sJQJ5QxPDdc', '8iTsj6NdUSE', '0GpgZrgh2Do', 'VkG8dDnOZSs', 'riZX1GP-B0w', '0CATD58E83o', '4KJK-cVruQs', '7e9uK6c49iQ', 'AzQBrfNFfUQ', 'ruJB8Sm0yY8', 's1FVPAdtKWw', 'ypxkGrrB99I', 'x53pwDg4350', 'L_RGmz54390', 'GRw5qtFFZNo', 'rmVEepJf8Zk', 'D5HdZMvFjHo', 'b5k0SXg_xl4', 'MAsvflRwKKQ', 'qiqYuSQwkHo', 'uGDKTrKa72k', 'b60bvxQsskQ', 'buPV4LBFkMA', 'eqLIHxGHHtg', '-ksA2NPuuNw', 's53nwHYA3O0', 'bxN-umOKSRU', 'vKBUdVZzudU', 'qlRec7rDHpc', 'wYQQzt0XMzU', '6nKWIYMA6fw', 'sB4cUlPWZhg', '14B5j8MEKUU', 'iOb1FjDMRGY', 'FsLMDeFKu-U', 'wZgSymcGS3Q', 'Y-sh5CyhcxI', 'mEztI2p_9Qc', 'P--RJFrLTnw', 'ZTZEBcIMOpg', '80e40XfIcKY', 'lfmqOOtmTE4', 'e_7hxSX0KTU', 'W1ZuOJ3Tj7g', 'mqqgacDIU9E', 'fR1PRLpEGm0', 'beckbXBfxe8', 'bNfAjzhvJa8', 'XnkshDVaU2o', 'fi2yADrWnuY', 'zKNglpj8iIk', 'KVH9B2K4UqA', 'yoQhwbDwtd4', '4FwVQV8FpFk', '5j760b0JrD0', 'qYkfqQ3xqlc', 'zAQK6PAsbDg', 'vrpY3Buy7JY', 'jhUrQ8Ae02U', 'Q1GEhZ2hOBs', 'Ijfw9K1XreE', 'gR4F7V419yo', '1iifBtfIMZU', 'rYy4hdeiDCM', 'na69XxRZoCI', 'oRKhhGqqDtY', '2bR5d2FkIbA', '6IBejDWPaSc', 'O4dkJVE2-_k', 'Twd_pecEcTU', 'vogs4NzqI3Q', 'KHrTfZ7pDU0', 'zu9KtSvFGMI', 'cjMk5gsJ6Co', '0FyWV3tYrAM', 'Ta8GhGssNmE', '6L7J1O0hmp8', 'uBIj5aIaqMU', 'Rd_2eUAMMDM', '9iCst4KB2U4', 'gInMUjbLSo8', 'TSOWkizLbw8', 'xN-ealYmiiA', 'zLyfkbqTcvo', 'RCb3GPt5bkY', '1nya4uk-e3I', '-BwqXMrn-w8', 'gEmPfVCOO9M', 'dVz27uxmkWw', '9eo5fCcBqHM', 'MeM74loJxc4', 'gKewWjgkL7o', 'ogja5YT7Wfc', 'L9713Le4tTc', '0G0HgxItL6k', 'DhfOgZoL2N4', 'ZhCjr3tBvkM', 'f27jzVW-Oow', 'I1ePOHgz64c', 'oLy3KEzN9Ao', 'Dh9lyE2BTqo', 't73OgjdA4oI', 'rq0tItM8gYE', 'SLYHDDRG6ZM', 'Z9nU6KFDltA', '0cM6bAxZPJk', '-NM5P2jaR2k', 'RdwD5s4dgps', 'irXFHm1ooWI', 'hgIemQMm_sQ', 'iIJ4PWdwDxE', 'D7NQSlEWBmE', '620AOt8gYYk', 'G_oSUzT5iw8', 'PSpManip4qs', 'uk9xWSgWmiI', '2oGpgA0OfqA', 'N-3B-7cAkFI', 'NOaz1J2ziP0', 'xZVrj14fTkg', 'FHVYQ3-xdjw', 'yTFTalhhcw8', '6-ZJB8it_Fo', '8gbQ2qHJwWQ', 'H1Rtcn145dY', 'VZpSwo0UoCg', 'zWrN_IpgiDA', 'f72NUXe4wTE', 'kQHfpBQOFHo', '2IKGxmFy3Cs', '4KWjSns0kQQ', 'Ojy5zAqzt_o', 'ORa1KjjUVt8', 'm3yi8Y7bHB0', 'tq6caVL15fY', '9vzhzOX2ADk', 'WQWYpWjI3v0', 'zTAf0nyId0U', 'EfSSxwHAHe0', 'dm3TiZqp3nw', 'lnd8kxCtpbY', 'MzsFzaE7mYc', '-le2P03f-pA', 'GegsXxdH2zI', 'F38jmgP_d3k', 'dw-KvRHM3Iw', 'loBJOGSmBKU', 'ggI9PCxs_w8', 'tuSdoJ2iJhQ', 'CRtPs4wI9cg', '0oR4zCwc-1M', 'JeIjvCSuO0U', 'i-KO7nsjuBQ', 'XeX5B-1AkpI', '31GQDcOTOgs', 'zJMuiXjkKjg', 'hvOddQ2x4U4', '6kw5DV3XQd0', '71Svya00ukU', '7GOMPfSiE_g', '9DvrlkPzQms', '1iZC-4VggwM', 'PO3KRB9HdkE', 'i4q0XaBS3PY', 'ltZnsPpHZnk', 'fZTRdckXlIc', 'm8IWLdMRuI0', 'qpOVfrIyU2k', 'YVRx4AJJrvQ']
        simpli = ['jVOwJOnvIRw', 'Owdcdub2sf0', 'vS80QWz7IPs', 'iPxMfgh2QgY', 'UOKkZF_qK9M', 'Oco1ftuKqbU', 'pQ0s5FLifAU', 'c_uVfPJS4oE', 'Emqj_pOJWa8', 'Wxkc6NkWhLw', 'rp-XhyyW56w', '1ibo01JGLRI', 'aynpxkN6O9E', 'WBnLnp4eGA4', 'C5UC7YvjL8w', 'QUWMuuEzSk4', 'svDGHu-bW8Q', 'pBiNayftkpE', '2Go4Npf1hYU', 'Hqmvw07FY0k', 'NlNK75eOmks', 'UhUzyTVpaVA', 'x5-PbyQ8w-M', 'qnmJYjOrNWE', 'VDyiW70GRe4', 'UyE8qeenK1U', '5tz0Cq6wxYA', '7MQnkq1zIZ0', 'awf0sgtPO1c', 'QTBg9la6RPE', '11nuT6wNDgg', 'xk0Cbdvq-oc', '9dGnVbR3e3U', '8yEAOhKnLOM', 'JCB_s4tZBB4', 'y0LEZ1S1cSU', '_NH4jtHQ4qQ', 'L81pYPZ0EcQ', '840vo4eMvUs', 'uletKRPMnuo', '_A8Yq9t-u0k', 'uy-nvLH5zH8', 'Nz55AoaMVlw', 'oeH-V3SFMwc', '5gmqFXnAslc', 'yewkv8pTAu0', 'MCJvVUlNZ5c', 'YOfv30fSXk0', 'OdXHSOPhnKg', 'pgyu4sY-61I', 'ERFnSII5Pbs', 'RYsdZ7oXZfs', 'iz5ADI4glnY', 'I29vWJOxrtA', 'm_X51Wal3ek', 'FbJBZz0jdtw', 'y20Hr_x4sRs', 'oo5u5ZQEJH0', 'HoyIlBERbtY', 'Rv_7-o7ZABs', 'brH-JY2779s', 'emz1dpWUPoM', 'ydLX0XWsunE', 'uPFnCfVqRHI', 'GLZLpbkj8JU', 'ZwOwv3-cKmY', 'WYqIlqp2_9c', '6hGIXpJK4Zg', 'ieOgOESfU0U', 'pF60KQe2qNs', 'nD5YLLPpWMg', 'hJgAB88QIik', 'mbtZv3dI6xc', 'VtPYISJmV0s', 'Rv_pe39MSuo', 'R1KxwgOpiv4', 'Kw5w5dk4BSQ', 'XS3z_PEkMMw', '6UQMPS_8bw0', 'SvNFE_X5QeU', 'wXZ_gn5txU8', 'xVdFubWkQrc', 'Yz1S9K3idHQ', 'Ou_DYlhNBuU', 'Bms0FR0l_V4', 'EQRZSBe4nBM', 'jN8PTgrc4FQ', 'LuJXqKHbnp8', 'g2MU79pTAi4', '5kk0ggmH664', 'ATEVN6ysIFw', '0ponCPbsLoM', 'JcCPnsfPaus', 'KODpP29AHD4', 'f-dMdh3QNE8', 'yPSzGyGnLlg', 'nEEQ0X9jFKQ', 'NdGWztL6KOU', '1oBxKX21orU', 'rBxXlSTYeSw', '7RtPgwOXuQg', 'xn0Trd8IZXk', 'XEZfLjzjmJQ', 'ZYsTveUkhrw', 'bkLaxy05xgk', 'MxLYctB3Rwg', 'T9VbIj1o2sc', 'WDkkwYAwMCk', 'UZODvGK8bf0', 'zi64Hpofz28', 'PXXr78LMkMo', 'd_oHbccoQTA', 'rPh85ekiJAA', 'xbcvIkXhBdM', 'LK4hbnoMHSo', '-o0xXFtD44Q', 'KjvwP1zErXU', 'DR9L5W8bf1I', 'IeMVLCVautw', 'E-dbxW83N7w', 'fxvvMjDCo_4', 'GS7QqjBJDDs', 'KX2ppYAu4OU', '0_XZBDWnngs', 'zNEck4yBj_4', 'uW3p3RLSjMs', 'zJLMdgncaFk', 'nz5l5rKu8sA', 'AOd5k3QwObc', 'jpMBW4GvWXo', '1hSFAZCnH0k', 'l-v_SJzJQNw', 'k3js0i6gS-Y', 'E5EcN__6wjk', 'S-rAng7Qzj8', 'nARngHsFtl0', '1UP6SsHduRA', 'O4p_4wg2kOg', 'eci03eUjErM', '67wgCXeeDgc', 'W987aEnql60', 'lqePRcofY6s', 'O_61udQowzM', 'CP8D1gS8--E', 'jMNuuFijlMU', 'kyyMCr3IQuU', '32zfJJycBt4', 'vXyoWUMAcaA', 'rpX4aGdqgjo', 'xS2Kqhm7UiM', 'Ks4QPWfgBbk', 'KDj4sGnljFs', 'R12ybh5122w', 'Tj8aeORtrCk', 'q-bbH-5P4-4', 'ldxt3h4yA3s', 'yn8CV5O4nrA', 'NfBSQ0Sbtwo', 'qR7xFprYnF0', 'yIxJvSEG4bg', 'JogR7eChkqM', 'h2NNrH2aMZc', 'XlROAkWOgSg', 'gGa25J1Ulzs', 'c7yqHirmXDg', '-Jp9zh8-3BM', 'hxyV0_u56rU', 'dPned7FYl6I', 'VemSiDcvTJI', 'ebsMvLl6EyI', 'jhKtFzxXul4', 'sUVrRU6g8F4', 'sajv3BJJMd0', 'k6cGiP2rHrM', 'XAe7M6s-iRw', '1gFoGX1f1V8', 'UQyL0tbxBG4', 'mrJE5AnEzTc', 'dSE1gZKQ0D0', 'ZATa3PgnyYI', 'iuG9R6bzm14', 'dsvd87HpkFs', 'WtPPrhrsSgk', 'jHKAXah09Qk', 'Hw4DN2xW_lY', '6eBbTw-Tjdc', 'KZ6Qhin7yso', 'CrEtxYhLvTA', '1DRJKRbuqDY', 'D_DyF84ED8I', 'UGAqSiGqHQI', 'yuPtnxke5fo', '6Ni_AaxTV04', 'q0q2QGxnR6s', 'G01LUrzWYI4', 'nXQ8zY5hSZU', 'aqbcm09iRIg', 'FLBYwYkgMRM', 'nnPLeJ-xLLk', '0eTRK-8o0hA', 'DMN1GCmS-Io', 'hjwHZxlOJBg', 'M8BdXyENjTI', 'MemJZW8LVxo', 'N2owPpUaNTY', 'uPZ-NFGRoRQ', 'izs_H-PxiZs', 'TmAaCOW-i5w', '1c2af7jKCMs', 'mXJBddRKvZE', 'cnOnfpAgaGA', '4P25SJ3zk9k', 'u4-78si3Xg8', 'YjCKz6DlP5o', 't0Ww0XCK9Vw', 'amkrgR10sBw', 'nSyDWTA4I24', 'MV13wCoHMms', 'cqLUz8wR-24', '_eTVzm45yNg', 'WqecIGbqVxA', '61FbqcpY-L8', 'zmXEI7b3_Pc', 'brWo4oKt444', 'kiIcA4eJcHg', 'z6h0_uHiWhA', 'o042nX8NBFU', 'nYQm9GpDteQ', 'gJ0kw37IfA0', 'vb0nlSY_n0c', '8clmzAbuu3A', 'xwWx1jzKKmQ', 'YN-UgSJHwrg', 'CcK-GmypeP0', 'vUOhFPqWa7c', 'Do2GSz9su4k', 'WB68kcHEkOs', 'A_7KRWjN-bA', 'gat3lQZNmu0', 'lQFs0m35bhA', 'Qt1LaTHwTJk', 'Z23caov09Zk', 'NpRet0Mj_Fc', 'AB6Nnj-lCR0', 'iqY4kkB-RTs', 'UulqaPpXsBM', 'LevsIJHm9CU', 'i_gdUnz8H60', 'oqP1ptAfrlY', 'iR5rZc2cZ94', 'PMzaEaYVRr0', 'mavS3NrJU74', 'lXbctp5eT7k', 'ELuyxNszTg0', 'CC-NKnQ54QE', 'kakHT8Nv-Vw', 'D4Qn7SShjQw', 'gOZ8ZbpwYtI', 'UtO2CK0r1ss', 'eOULJeSPF5c', '5IN1n_hiX8E', 'zoM7iIyp9wQ', 'lu0Rw114R2E', 'IkBF0_7GTzc', 'ben1_3j8SU4', 'PhM-DNXYhCM', 'FY5LQWjVrhI', 'pIebwGUtz0w', 's0GwM71DJ7s', 'DiWSX-CUP_4', 'eAzC1-FVeME', 'eYHr8GQ4p50', '4qwZvWssc9o', 'M5-uYZhvuOI', '8rK-USZ51TQ', 'xnbENUJay6U', 'oPvZSO3tYKo', 'MILzEUDqU0A', 'w6Erv0y_W_g', 'fjT_MIoWrl8', 'hEMafUgDY88', 'DBFjDbljjVk', 'SWaELRZFEGM', 'YThGtUwq5ck', 'Qz_xRU6TaeM', 's_-JkLR68Do', 'yqC-8wy_cOA', 'u7B7xWlsQTI']



        list_of_video_ids = []
        
        st.image(img)
        
        st.write("")
        option = st.selectbox(
     'What YouTube channel do you want to search?',
     ('ChubbyEmu', 'Veritasium', 'Kurzgesagt', '3Blue1Brown', 'Leeroy', 'MrWissen2Go', 'SahraWagenknecht', 'yKollektiv', 'Simplicissimus'))
        if option == 'ChubbyEmu':
                   list_of_video_ids = cubby_Emu
        elif option == 'Veritasium':
                    list_of_video_ids = veritasium
        elif option == 'Kurzgesagt':
                        list_of_video_ids = kurzgesagt
        elif option == '3Blue1Brown':
                        list_of_video_ids = blue_brown                
        elif option == 'Leeroy':
                        list_of_video_ids = leeroy
        elif option == 'MrWissen2Go':
                        list_of_video_ids = mrWissen
        elif option == 'SahraWagenknecht':
                        list_of_video_ids = sahrawagenknecht
        elif option == 'yKollektiv':
                        list_of_video_ids = yKollektiv
        elif option == 'Simplicissimus':
                        list_of_video_ids = simpli




        st.write(option)
        st.write("")





#Loop videos:

def main():
        
        global all_transcripts
        
        for VideoID in list_of_video_ids:

                try:

                        params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % VideoID}
                        url = "https://www.youtube.com/oembed"
                        query_string = urllib.parse.urlencode(params)
                        url = url + "?" + query_string

                        with urllib.request.urlopen(url) as response:
                            response_text = response.read()
                            data = json.loads(response_text.decode())
                            #print('Title: ' + data['title'])

                        # Separator
                        print(' ')

                        # retrieve the available transcripts
                        transcript_list = YouTubeTranscriptApi.list_transcripts(VideoID)

                        # iterate over all available transcripts
                        for transcript in transcript_list: 
                          # fetch the actual transcript data
                          #print(transcript.fetch())
                          data = transcript.fetch()

                          #data = transcript.fetch() # [{'text': "i'm gonna attempt to collect 30 million", 'start': 0.0, 'duration': 4.16}, {'text': '...
                          #print(type(data)) # <class 'list'>

                          # Add "video_id" for recover it later: 
                          data.insert(0, {'video_id': VideoID})

                          # Add the fetched data to the "all_transcripts" global variable.
                          all_transcripts += data

                except:
                        st.write('Error: For the following video there is no transcript available' + '...' + 'https://www.youtube.com/watch?v=' + VideoID)
                        pass






with col3:
        
        #add a search bar
        user_input = st.text_input("Type in the words/sentences you want to search", "")
        user_input = user_input.lower()
        st.write(' ')

        if len(user_input) > 60:
                        st.write("Your sentence is too long. Try shorter ones.")                
        
        
        # We use here the global list "all_transcripts": 
        dictionary = all_transcripts

        # Function to loop all transcripts and search the captions that contains the 
        # user input.
        # TO-DO: Validate when no data is found.
        
        def search_dictionary(user_input, dictionary): 
                


                link = 'https://youtu.be/'

                # Get the video_id: 
                v_id  = ""

                # I add here the debbuged results: 
                lst_results = []

                # string body:
                matched_line = ""

                # You're really looping a list of dictionaries: 
                for i in range(len(dictionary)): # <= this is really a "list".
                        

                        try:
                #print(type(dictionary[i])) # <= this is really a "dictionary".
                #print(dictionary[i])

                # now you can iterate here the "dictionary": 
                                for x, y in dictionary[i].items():
        
                                        if (x == "video_id"): 
                                                v_id = y
                                        if (user_input in str(y) and len(v_id) > 0):
                                                matched_line = str(dictionary[i]['text']) + '...' + str(dictionary[i]['start']) + ' min und ' + str(dictionary[i]['duration']) + ' sec :: ' + link + v_id + '?t=' + str(int(dictionary[i]['start'] - 1)) + 's'
                
          
                        # Check if line does not exists in the list of results: 
                                        if len(lst_results) == 0:
                                                lst_results.append(matched_line)
                                        if matched_line not in lst_results: 
                                                lst_results.append(matched_line)

                        except Exception as err: 
                                st.write('Unexpected error - see details below:')
                                st.write(err)

                        # Just an example for show "no results":
                if (len(lst_results) == 0):
                        st.write("No results found with input (" + user_input + ")")
                else: 
                        st.write("All time stamps: ")
                        st.write("__________________")

                        #st.write("\n".join(lst_results)) # <= this is for show the results with a line break.
                        
                        #make a new line after each https link:
                        new_lst_results = []
                        for i in range(len(lst_results)):
                                new_lst_results.append(lst_results[i] + '\n')
                        st.write("\n".join(new_lst_results)) # <= this is for show the results with a line break.
                        # Function ends here.
        


        if st.button("Search"):
               
                main()
                search_dictionary(user_input, dictionary)


                
        





      
  







        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#whitespace
with col1:
        st.write("")
           


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
<p>Developed with ❤️  by <a style='display: block; text-align: center;' href="https://www.instagram.com/max_mnemo/" target="_blank">Max Mnemo </a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
