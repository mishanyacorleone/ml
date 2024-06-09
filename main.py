import streamlit as st
import pickle
import numpy as np

# Загрузка модели


def load_model():
    with open('model.pkl', 'rb') as f:
        model_ = pickle.load(f)
    return model_


model = load_model()

# Заголовок
st.title('Классификация профиля студента')

# Поля для ввода данных
HOURS_DATASCIENCE = st.number_input('Количество часов, потраченных на изучение курсов по DataScience', min_value=0)
HOURS_BACKEND = st.number_input('Количество часов, потраченных на изучение курсов по Backend', min_value=0)
HOURS_FRONTEND = st.number_input('Количество часов, потраченных на изучение курсов по Frontend', min_value=0)

NUM_COURSES_BEGINNER_DATASCIENCE = st.number_input('Количество пройденных начальных курсов по DataScience', min_value=0)
NUM_COURSES_BEGINNER_BACKEND = st.number_input('Количество пройденных начальных курсов по Backend', min_value=0)
NUM_COURSES_BEGINNER_FRONTEND = st.number_input('Количество пройденных начальных курсов по Frontend', min_value=0)

NUM_COURSES_ADVANCED_DATASCIENCE = st.number_input('Количество пройденных курсов для продвинутых по DataScience', min_value=0)
NUM_COURSES_ADVANCED_BACKEND = st.number_input('Количество пройденных курсов для продвинутых по Backend', min_value=0)
NUM_COURSES_ADVANCED_FRONTEND = st.number_input('Количество пройденных курсов для продвинутых по Frontend', min_value=0)

AVG_SCORE_DATASCIENCE = st.number_input('Средний балл по DataScience, набранный учеником', min_value=0.0, max_value=100.0)
AVG_SCORE_BACKEND = st.number_input('Средний балл по Backend, набранный учеником', min_value=0.0, max_value=100.0)
AVG_SCORE_FRONTEND = st.number_input('Средний балл по Frontend, набранный учеником', min_value=0.0, max_value=100.0)

# Преобразование данных в массив
input_data = np.array([
    HOURS_DATASCIENCE,
    HOURS_BACKEND,
    HOURS_FRONTEND,
    NUM_COURSES_BEGINNER_DATASCIENCE,
    NUM_COURSES_BEGINNER_BACKEND,
    NUM_COURSES_BEGINNER_FRONTEND,
    NUM_COURSES_ADVANCED_DATASCIENCE,
    NUM_COURSES_ADVANCED_BACKEND,
    NUM_COURSES_ADVANCED_FRONTEND,
    AVG_SCORE_DATASCIENCE,
    AVG_SCORE_BACKEND,
    AVG_SCORE_FRONTEND
]).reshape(1, -1)

# Кнопка для предсказания
if st.button('Предсказать профиль'):
    prediction = model.predict(input_data)
    labels_to_keys = {0: 'beginner_front_end',
     1: 'advanced_front_end',
     2: 'beginner_data_science',
     3: 'beginner_backend',
     4: 'advanced_data_science',
     5: 'advanced_backend'}
    st.write(f'Предсказанный профиль: {labels_to_keys[prediction[0]]}')

# Запуск: сохраните файл как app.py и выполните команду `streamlit run app.py`
