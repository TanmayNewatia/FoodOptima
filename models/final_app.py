# import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import tensorflow
from tensorflow import keras
from keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing import image
import torch
import cv2
import numpy as np
from google.colab.patches import cv2_imshow # Import cv2_imshow

model = pickle.load(open('food_detection.sav','rb'))
tokenizer = pickle.load(open('food_waste_tokenizer.pkl','rb'))
solution_model = pickle.load(open('food_waste_model.pkl','rb'))
allFoodItems={0: 'adhirasam', 1: 'aloo_gobi', 2: 'aloo_matar', 3: 'aloo_methi', 4: 'aloo_shimla_mirch', 5: 'aloo_tikki', 6: 'anarsa', 7: 'ariselu', 8: 'bandar_laddu', 9: 'basundi', 10: 'bhatura', 11: 'bhindi_masala', 12: 'biryani', 13: 'boondi', 14: 'butter_chicken', 15: 'chak_hao_kheer', 16: 'cham_cham', 17: 'chana_masala', 18: 'chapati', 19: 'chhena_kheeri', 20: 'chicken_razala', 21: 'chicken_tikka', 22: 'chicken_tikka_masala', 23: 'chikki', 24: 'daal_baati_churma', 25: 'daal_puri', 26: 'dal_makhani', 27: 'dal_tadka', 28: 'dharwad_pedha', 29: 'doodhpak', 30: 'double_ka_meetha', 31: 'dum_aloo', 32: 'gajar_ka_halwa', 33: 'gavvalu', 34: 'ghevar', 35: 'gulab_jamun', 36: 'imarti', 37: 'jalebi', 38: 'kachori', 39: 'kadai_paneer', 40: 'kadhi_pakoda', 41: 'kajjikaya', 42: 'kakinada_khaja', 43: 'kalakand', 44: 'karela_bharta', 45: 'kofta', 46: 'kuzhi_paniyaram', 47: 'lassi', 48: 'ledikeni', 49: 'litti_chokha', 50: 'lyangcha', 51: 'maach_jhol', 52: 'makki_di_roti_sarson_da_saag', 53: 'malapua', 54: 'misi_roti', 55: 'misti_doi', 56: 'modak', 57: 'mysore_pak', 58: 'naan', 59: 'navrattan_korma', 60: 'palak_paneer', 61: 'paneer_butter_masala', 62: 'phirni', 63: 'pithe', 64: 'poha', 65: 'poornalu', 66: 'pootharekulu', 67: 'qubani_ka_meetha', 68: 'rabri', 69: 'ras_malai', 70: 'rasgulla', 71: 'sandesh', 72: 'shankarpali', 73: 'sheer_korma', 74: 'sheera', 75: 'shrikhand', 76: 'sohan_halwa', 77: 'sohan_papdi', 78: 'sutar_feni', 79: 'unni_appam'}

def process_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    predictions = model.predict(img_array,verbose=False)
    predicted_class_index = np.argmax(predictions)
    fooditem=allFoodItems[predicted_class_index]
    return fooditem

def calculate_food_area(image_path="OIP (2).jpg"):
    # Step 1: Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not read the image.")
        return None

    # Get image dimensions (height × width)
    height, width, _ = image.shape
    total_image_area = height * width  # Total pixels in the image

    # Step 2: Preprocess the image
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Thresholding to get a binary mask
    _, binary_mask = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY_INV)

    # Step 3: Find contours
    contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Step 4: Calculate the area of each contour
    total_area = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        total_area += area

    # Optionally, display the results
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)  # Draw contours on the original image
    # cv2.putText(image, f"Total Food Area: {total_area} pixels", (10, 30),
    #             cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Show the image with contours
    cv2_imshow(image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return [total_area,total_image_area]

# Example usage
food_item = process_image("OIP (2).jpg")
food_area = calculate_food_area()
area_of_food_wasted=food_area[0]
area_of_plate_total_area=food_area[1]
percentage_of_food_wasted=total_area/total_image_area*100
query=f"Total Food Area: {total_area} pixels, Total Image Area: {total_image_area}, Total Wastage Percentage: {total_wastage_percentage}"
input_tokens = tokenizer(test_query, return_tensors="pt", max_length=512, truncation=True)
print(input_tokens)