import streamlit as st
import cv2
import numpy as np
import face_recognition

# Fonction pour téléverser et afficher une image
def load_image(image_file):
    img = cv2.imdecode(np.fromstring(image_file.read(), np.uint8), 1)
    return img

st.title("Détection de Visages et Extraction de Caractéristiques")
uploaded_file = st.file_uploader("Choisissez une image...", type=["jpeg", "jpg", "png", "bmp", "tiff"])

if uploaded_file is not None:
    # Charger l'image
    image = load_image(uploaded_file)
    st.image(image, channels="BGR", caption="Image Téléversée", use_column_width=True)
    
    # Convertir BGR en RGB
    rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Détection de visage
    face_locations = face_recognition.face_locations(rgb_img)
    face_encodings = face_recognition.face_encodings(rgb_img, face_locations)
    
    st.write(f"Nombre de visages détectés : {len(face_encodings)}")
    
    for i, (top, right, bottom, left) in enumerate(face_locations):
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
        st.image(image, channels="BGR", caption=f"Visage {i+1}", use_column_width=True)
        
        # Afficher les caractéristiques faciales
        st.write(f"Caractéristiques du visage {i+1} : {face_encodings[i]}")

