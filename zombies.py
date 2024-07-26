# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import random
import time

st.markdown(
    """
    <style>
    div.stButton :nth-child(1)  {background-color: gold !important;}
    """,
    unsafe_allow_html=True
    )

if 'start' not in st.session_state:
    st.session_state['start'] = False
if 'contador_zombies' not in st.session_state:
    st.session_state['contador_zombies'] = 0
if 'contador_fallos' not in st.session_state:
    st.session_state['contador_fallos'] = 0

h1,h2,h3 = st.columns(3)
h2.header(':rainbow[ZOMBIES]')
b_start = h1.button('START',key='b_start')

if b_start:
    st.session_state['contador_zombies'] = 0
    st.session_state['contador_fallos'] = 0
    st.session_state.start = True


cont = st.empty()
tablero = cont.container()
c1,c2,c3, = tablero.columns(3)
c4,c5,c6 = tablero.columns(3)
k1 = c1.empty()
k2 = c2.empty()
k3 = c3.empty()
k4 = c4.empty()
k5 = c5.empty()
k6 = c6.empty()

botones = [':zombie:',':man:', ':boy:',':woman:', ':girl:', ':car:']
keys = {':zombie:':1, ':man:':2, ':boy:':3, ':woman:':4, ':girl:':5, ':car:':6}
iconos = random.sample(botones, len(botones))
b1 = k1.button(iconos[0], key=keys[iconos[0]] )
b2 = k2.button(iconos[1], key=keys[iconos[1]] )
b3 = k3.button(iconos[2], key=keys[iconos[2]] )
b4 = k4.button(iconos[3], key=keys[iconos[3]] )
b5 = k5.button(iconos[4], key=keys[iconos[4]] )
b6 = k6.button(iconos[5], key=keys[iconos[5]] )

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

if st.session_state['contador_fallos'] >= 10:
    st.write('TE HAN CONVERTIDO EN ZOMBI')
    st.write('Tu puntuación: ', st.session_state.contador_zombies)
    st.stop()

if (b1 or b2 or b3 or b4 or b5 or b6) and resultado == ':zombie: Muerto':
    st.session_state.contador_zombies += 1

if (b1 or b2 or b3 or b4 or b5 or b6) and resultado != ':zombie: Muerto':
    st.session_state.contador_fallos += 1



st.write('Zombies muertos',st.session_state.contador_zombies)
st.write('Fallos',st.session_state.contador_fallos)

t1=st.session_state.contador_zombies
tiempo = 40/(t1+0.1)

if st.session_state.start==True:
    
    time.sleep(tiempo)
    st.session_state['contador_fallos'] += 1
    st.rerun()

