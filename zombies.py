# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import random
import time

if 'start' not in st.session_state:
    st.session_state['start'] = False
if 'contador_zombies' not in st.session_state:
    st.session_state['contador_zombies'] = 0
if 'contador_fallos' not in st.session_state:
    st.session_state['contador_fallos'] = 0





h1,h2,h3 = st.columns(3)
h2.header(':rainbow[ZOMBIES]')
b_start = h1.button('START')
b0 = h1.button('RESTART')
if b_start:
    st.session_state.start = True
if b0:
    st.session_state['contador_zombies'] = 0
    st.session_state['contador_fallos'] = 0
    st.session_state['start'] = False
cont = st.empty()
tablero = cont.container()
c1,c2,c3,c4,c5,c6 = tablero.columns(6)
k1 = c1.empty()
k2 = c2.empty()
k3 = c3.empty()
k4 = c4.empty()
k5 = c5.empty()
k6 = c6.empty()

botones = [':zombie:',':man:', ':boy:',':woman:', ':girl:', ':car:']
keys = {':zombie:':1, ':man:':2, ':boy:':3, ':woman:':4, ':girl:':5, ':car:':6}
iconos = random.sample(botones, len(botones))
b1 = k1.button(iconos[0], key=keys[iconos[0]],use_container_width=True )
b2 = k2.button(iconos[1], key=keys[iconos[1]],use_container_width=True )
b3 = k3.button(iconos[2], key=keys[iconos[2]],use_container_width=True )
b4 = k4.button(iconos[3], key=keys[iconos[3]],use_container_width=True )
b5 = k5.button(iconos[4], key=keys[iconos[4]],use_container_width=True )
b6 = k6.button(iconos[5], key=keys[iconos[5]],use_container_width=True )

resultado = 'Dispara'
if b1: 
    if iconos[0] == ':zombie:':
        resultado = ':zombie: Muerto'
        
    elif iconos[0] == ':car:':
        resultado = 'Fallaste'
    else:
        resultado = 'Te has cargado un humano'
if b2:
    if iconos[1] == ':zombie:':
        resultado = ':zombie: Muerto'
    elif iconos[1] == ':car:':
        resultado = 'Fallaste'
    else:
        resultado = 'Te has cargado un humano'
if b3:
    if iconos[2] == ':zombie:':
        resultado = ':zombie: Muerto'
    elif iconos[2] == ':car:':
        resultado = 'Fallaste'
    else:
        resultado = 'Te has cargado un humano'
if b4:
    if iconos[3] == ':zombie:':
        resultado = ':zombie: Muerto'
    elif iconos[3] == ':car:':
        resultado = 'Fallaste'
    else:
        resultado = 'Te has cargado un humano'
if b5:
    if iconos[4] == ':zombie:':
        resultado = ':zombie: Muerto'
    elif iconos[4] == ':car:':
        resultado = 'Fallaste'
    else:
        resultado = 'Te has cargado un humano'
if b6:
    if iconos[5] == ':zombie:':
        resultado = ':zombie: Muerto'
    elif iconos[5] == ':car:':
        resultado = 'Fallaste'
    else:
        resultado = 'Te has cargado un humano'
if 'contador' not in st.session_state:
    st.session_state.contador = 0
if st.session_state['contador_fallos'] > 9:
    st.write('TE HAN CONVERTIDO EN ZOMBI')
    st.write('Tu puntuación: ', st.session_state.contador_zombies)
    st.stop()
if (b1 or b2 or b3 or b4 or b5 or b6) and resultado == ':zombie: Muerto':
    st.session_state.contador_zombies += 1
if (b1 or b2 or b3 or b4 or b5 or b6) and resultado != ':zombie: Muerto':
    st.session_state.contador_fallos += 1
st.write(resultado)
try:
    st.write('Zombies muertos',st.session_state.contador_zombies)
    st.write('Fallos',st.session_state.contador_fallos)
except:
    pass
if st.session_state.start==True:
    if st.session_state['contador_fallos'] < 20:
        time.sleep(1.8)
    elif st.session_state['contador_fallos'] < 50:
        time.sleep(1.6)
    elif st.session_state['contador_fallos'] < 75:
        time.sleep(1.4)
    elif st.session_state['contador_fallos'] < 100:
        time.sleep(1.2)    
    elif st.session_state['contador_fallos'] < 150:
        time.sleep(1)
    st.session_state['contador_fallos'] += 1
    st.rerun()
