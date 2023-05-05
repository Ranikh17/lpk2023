import streamlit as st
from PIL import Image
st.set_page_config(page_title="Concentration Machine", page_icon=":fire:",layout="wide")

#Cover
image=Image.open('coverr.jpeg')
st.image(image, width=500)

st.title('Aplikasi Penentuan Konsentrasi Larutan')
st.write('Oleh Kelompok 6 :')
st.write('Aldo Floristo Parasian Pardede (2219029)')
st.write('Achmed Zakky Zamani (2219024)')
st.write('Rani Khoerunnisa (2219152)')
st.write('Rayna Anggita Ramadhani (2219154)')

#tab
tab1,tab2=st.tabs(['Konsentrasi', 'Penentuan Konsentrasi'])

#tab 1
with tab1:
    st.header('Konsentrasi')
    st.write('Konsentrasi larutan adalah jumlah zat yang terlarut dalam setiap satuan larutan atau pelarut. Konsentrasi larutan dapat dinyatakan dalam beberapa satuan, yaitu molaritas (M), molalitas (m), fraksi mol (X), dan kadar (%).')
    st.subheader(':blue[A. Molaritas]')
    st.write('Molaritas dalam konsentrasi larutan dikenal dengan istilah konsentrasi molar. Molaritas adalah satuan yang menyatakan jumlah mol suatu zat dalam satu liter larutan. Satuan molaritas disimbolkan dengan huruf M atau disebut juga Molar.')
    st.write('Rumus :')
    image=Image.open('Molaritas.png')
    st.image(image, width=100)
    st.write('Keterangan :')
    st.write('M = Molaritas zat (molar)')
    st.write('n = Mol suatu zat (mol)')
    st.write('V = Volume larutan (liter)')
    st.subheader(':blue[B. Molalitas]')
    st.write('Molalitas adalah satuan konsentrasi larutan yang menyatakan jumlsh mol suatu zat dalam satu kilogram larutan. Satuan molalitas disimbolkan dengan huruf m.')
    st.write('Rumus :')
    image=Image.open('Molalitas.png')
    st.image(image, width=100)
    st.write('Keterangan :')
    st.write('m = Molalitas zat (molal)')
    st.write('n = Mol suatu zat (mol)')
    st.write('p = Massa pelarut (gram)')
    st.subheader(':blue[C. Fraksi Mol]')
    st.write('Fraksi mol adalah perbandingan jumlah mol suatu zat terlarut atau zat pelarut dengan jumlah mol total yang ada dalam sebuah larutan. Simbol dari fraksi mol ini adalah huruf X.')
    st.write('Rumus :')
    image=Image.open('Xt.jpeg')
    st.image(image, width=200)
    image=Image.open('Xp.jpeg')
    st.image(image, width=200)
    st.write('Keterangan :')
    st.write('Xt = Fraksi mol zat terlarut')
    st.write('Xp = Fraksi mol zat pelarut')
    st.write('nt = Mol zat terlarut')
    st.write('np = Mol zat pelarut')
    st.subheader(':blue[D. Kadar]')
    st.write('Konsentrasi dalam persen dapat dinyatakan menjadi dua bentuk, yaitu persen berat (%b/b) dan persen berat volume (%b/v).')
    st.write('Rumus :')
    image=Image.open('bb.jpeg')
    st.image(image, width=350)
    image=Image.open('bv.jpeg')
    st.image(image, width=350)
    
#tab 2
with tab2:
    st.header('Penentuan Konsentrasi Larutan')
    option=st.selectbox(
    'Silahkan pilih satuan konsentrasi yang ingin dicari ',
    ('Molaritas (M)','Molalitas (m)','Normalitas (N)','Fraksi mol terlarut (Xt)','Fraksi mol pelarut (Xp)','Kadar (%b/b)','Kadar (%b/v)'))
        
    if option=='Molaritas (M)':
        mol=st.number_input('Masukkan mol zat')
        volume=st.number_input('Masukkan volume larutan')
        if st.button('Hitung'):
            Molaritas=mol/volume
            st.success(f'Molaritas larutan sebesar {Molaritas} M')
    elif option=='Molalitas (m)':
        mol=st.number_input('Masukkan mol zat')
        p=st.number_input('Masukkan massa pelarut')
        if st.button('Hitung'):
            Molalitas=mol/p
            st.success(f'Molaritas larutan sebesar {Molalitas} molal')
    elif option=='Normalitas (N)':
        M=st.number_input('Masukkan molaritas zat')
        a=st.number_input('Masukkan valensi(banyaknya ion)')
        if st.button('Hitung'):
            Normalitas=M*a
            st.success(f'Normalitas larutan sebesar {Normalitas} N')
    elif option=='Fraksi mol terlarut (Xt)':
        t=st.number_input('Masukkan mol terlarut')
        p=st.number_input('Masukkan mol pelarut')
        if st.button('Hitung'):
            FraksiMol=t/(p+t)
            st.success(f'Fraksi mol terlarut sebesar {FraksiMol} ')
    elif option=='Fraksi mol pelarut (Xp)':
        p=st.number_input('Masukkan mol terlarut')
        t=st.number_input('Masukkan mol pelarut')
        if st.button('Hitung'):
            FraksiMol=p/(p+t)
            st.success(f'Fraksi mol pelarut sebesar {FraksiMol} ')
    elif option=='Kadar (%b/b)':
        m=st.number_input('Masukkan massa zat terlarut')
        mt=st.number_input('Masukkan massa zat total')
        if st.button('Hitung'):
            Kadar=m/mt
            st.success(f'Kadar (%b/b) sebesar {Kadar} %(b/b) ')
    elif option=='Kadar (%b/v)':
        m=st.number_input('Masukkan massa zat terlarut')
        vt=st.number_input('Masukkan volume zat total')
        if st.button('Hitung'):
            Kadar=m/vt
            st.success(f'Kadar (%b/v) sebesar {Kadar} %(b/v) ')
