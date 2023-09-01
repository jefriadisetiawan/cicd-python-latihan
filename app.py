import streamlit as st 


st.title('aplikasi sederhana dengan streamlit')

st.write('dibuat oleh jefri adi setiawan')
bangun_datar=['silahkan pilih','persegi','segitiga','persegi panjang']

pilih=st.selectbox('',bangun_datar)



if pilih=='persegi':
	st.subheader('Luas Persegi')
	sisi=st.number_input('masukkan panjang sisi (cm)')
	proses=st.button('cari luas persegi')
	if proses:
		luas=sisi**2
		st.write(f'luas persegi adalah {luas} cm^2')

if pilih=='segitiga':
	st.subheader('Luas Segitiga')
	alas=st.number_input('masukkan panjang alas(cm)')
	tinggi=st.number_input('masukkan tinggi(cm)')
	proses=st.button('cari luas segitiga')
	if proses:
		luas=0.5*alas*tinggi
		st.write(f'luas segitiga adalah {luas} cm2')

if pilih=='persegi panjang':
	st.subheader('Luas Persegi Panjang')
	panjang=st.number_input('masukkan panjang (cm)')
	lebar=st.number_input('masukkan lebar (cm)')
	proses=st.button('cari luas persegi panjang')
	if proses:
		luas=panjang*lebar
		st.write(f'luas persegi panjang adalah {luas} cm2')
