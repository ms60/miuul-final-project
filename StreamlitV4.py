import streamlit as st
import pandas as pd
import joblib
import time

st.set_page_config(page_title="DATA2İZDİVAÇ 2023",
                   page_icon=":smile:",
                   layout="wide")
def get_model():
    model = joblib.load("model_train_all2.joblib")
    return model


model = get_model()
dforig = pd.read_excel("veriler.xlsx")

tab_home, tab_oneri = st.tabs(["Hoşgeldiniz", "Aşk Testi"])

a1,a2,a3,a4= tab_home.columns(4)
a2.image("seda.PNG", width=600)


def main():
    # Düğmeyi oluştur
    play_button = tab_home.button("Arka Plan Müziğini Çal/Durdur")

    # Müzik dosyasını okut
    audio_file = open("music.mp3", "rb").read()

    # Düğme tıklandığında müziği çal veya durdur
    if play_button:
        tab_home.audio(audio_file, format="audio/mp3", start_time=0)
    else:
        tab_home.audio(audio_file, format="audio/mp3", start_time=0)


if __name__ == "__main__":
    main()

c1, c2, c3 = tab_oneri.columns(3)
c2.header(":red[❤️AŞK UYUMU TAHMİNİ❤️]")

tab_oneri.markdown("**Lütfen burada filtreleyin:**")

# Giriş

c1, c2 = tab_oneri.columns(2)

# st.dataframe(data=dforig, width=2500)

love_tr = {"❤️❤️": "so_so_love", "❤️": "no_love", "❤️❤️❤️": "like_heaven"}
unique_team1 = love_tr.keys()
NEW_LOVE = c1.selectbox("**Aşk Durumunuzu Seçiniz**", unique_team1)


new_education_tr = {"ilköğretim": "low_educated", "lise": "middle_educated", "üniversite": "high_educated"}
unique_team2 = new_education_tr.keys()
NEW_EDUCATION = c1.selectbox("**Eğitim Durumunuzu Seçiniz**", unique_team2)


# unique_team3 = dforig["NEW_ECO_SIM"].unique()
# NEW_ECO_SIM = tab_oneri.selectbox("Ekonumik durumunuzu seçiniz", unique_team3)
new_age_gap_tr = {"<=3": "low_age_gap", "3-6": "midle_age_gap", ">6": "high_age_gap"}
unique_team4 = new_age_gap_tr.keys()
NEW_AGE_GAP = c1.selectbox("**Yaş Farkını Seçiniz**", unique_team4)


new_soc_sım_tr={"yakın": "low_soc_sim", "uzak": "high_soc_sim"}
unique_team5 = new_soc_sım_tr.keys()
NEW_SOC_SIM = c1.selectbox("**Sosyal Uyumu Seçiniz**", unique_team5)


new_ıncome_tr={"💰💰💰": "high_inc", "💰💰": "medium_inc","💰": "low_inc"}
unique_team6 = new_ıncome_tr.keys()
NEW_INCOME = c2.selectbox("**Gelir Seviyesini Seçiniz**", unique_team6)


new_socıal_tr={"<20": "very_social", "20-30": "mid_social","=>30": "low_social"}
unique_team7 = new_socıal_tr.keys()
NEW_SOCIAL = c2.selectbox("**İlk Flört Yaş Aralığını Seçiniz**", unique_team7)


new_loy_tr={"❣️❣️❣️❣️": "high_loy", "❣️❣️❣️": "medium_loy","❣️❣️": "low_loy","❣️": "very_low_loy"}
unique_team8 = new_loy_tr.keys()
NEW_LOY = c2.selectbox("**Bağlılık Seviyesini Seçiniz** ", unique_team8)

new_eng_tıme_tr={"0-2": "0-2", "3-4": "2-4","5-6": "4-6","7-8": "6-8","9-10": "8-10"}
unique_team9 = new_eng_tıme_tr.keys()
NEW_ENG_TIME = c2.selectbox("**Nişanlı Kalma Sürenizi Seçiniz**", unique_team9)

# dtm = tab_oneri.number_input("Desire_to_Marry")
# scf = tab_oneri.number_input("Spouse_Confirmed_by_Family")


scf = c1.slider(label="**Aile Onayını Seçiniz**", min_value=dforig['Spouse_Confirmed_by_Family'].min(),
                max_value=dforig['Spouse_Confirmed_by_Family'].max())

dtm = c2.slider(label="**İlişki İsteğini Seçiniz**", min_value=dforig['Desire_to_Marry'].min(),
                max_value=dforig['Desire_to_Marry'].max())

cat_cols = ['NEW_LOVE', 'NEW_EDUCATION', 'NEW_ECO_SIM', 'NEW_AGE_GAP', 'NEW_SOC_SIM', 'NEW_CUL_SIM', 'NEW_SOCIAL_GAP',
            'NEW_COMM_INT', 'NEW_REL_COMP', 'CHILD_NUM_BEFORE', 'NEW_ENG_TIME', 'NEW_REL_FAM', 'NEW_ADD', 'NEW_LOY',
            'NEW_INCOME', 'SPOUSE_BEF_MARR', 'NEW_SOCIAL']
num_cols = ['Desire_to_Marry', 'Independency', 'Trading_in', 'Commitment', 'Mental_Health',
            'The_Sense_of_Having_Children', 'Previous_Trading', 'Previous_Marriage', 'The_Proportion_of_Common_Genes',
            'Height_Ratio', 'Self_Confidence', 'Spouse_Confirmed_by_Family', 'Divorce_in_the_Family_of_Grade_1',
            'Divorce_Probability']
user_input_list = {}

for col in model.feature_names_in_:
    for cat in cat_cols:
        if cat in col:
            user_input_list[col] = [False]
    for num in num_cols:
        if num == col:
            user_input_list[col] = [0]

user_input_list["NEW_LOVE" + "_" + love_tr[NEW_LOVE]] = [True]
user_input_list["NEW_EDUCATION" + "_" + new_education_tr[NEW_EDUCATION]] = [True]
# user_input_list["NEW_ECO_SIM" + "_" + NEW_ECO_SIM] = [True]
user_input_list["NEW_AGE_GAP" + "_" + new_age_gap_tr [NEW_AGE_GAP]] = [True]
user_input_list["NEW_SOC_SIM" + "_" + new_soc_sım_tr[NEW_SOC_SIM]] = [True]
user_input_list["NEW_INCOME" + "_" + new_ıncome_tr[NEW_INCOME]] = [True]
user_input_list["NEW_SOCIAL" + "_" + new_socıal_tr[NEW_SOCIAL]] = [True]
user_input_list["NEW_LOY" + "_" + new_loy_tr[NEW_LOY]] = [True]
user_input_list["NEW_ENG_TIME" + "_" + new_eng_tıme_tr[NEW_ENG_TIME]] = [True]
user_input_list['Desire_to_Marry'] = [dtm]
user_input_list['Spouse_Confirmed_by_Family'] = [scf]

# user_input = pd.DataFrame({"NEW_LOVE": NEW_LOVE}, index=[0])
user_input = pd.DataFrame(user_input_list, index=[0])


# tab_oneri.write(user_input)

# Assume you have a model.predict function
def predict(user_input):
    # Your prediction logic here
    return 1  # Replace this with the actual prediction result


def main():
    b1, b2, b3 = tab_oneri.columns(3)
    # Check if the button in the second column is clicked
    if tab_oneri.button("Aşk uyumum!", key="ask_uyumu_button"):

        with tab_oneri.status("Veriler yükleniyor...", expanded=True) as status:
            tab_oneri.write("Veriler taranıyor...")
            time.sleep(2)
            tab_oneri.write("Uyumlar eşleştiriliyor")
            time.sleep(1)
            tab_oneri.write("Tahmin sonucu hesaplanıyor...")
            time.sleep(1)
            status.update(label="Tahmin sonucu hesaplandı!", state="complete", expanded=False)
        tab_oneri.button('Rerun')

        # Make a prediction
        prediction = model.predict(user_input)
        # Display result based on the prediction
        if prediction == 0:
            tab_oneri.success(f"Tahmin edilen aşk uyumu: {prediction} Başarılı! ")
            tab_oneri.balloons()
        else:
            tab_oneri.error(f"Tahmin edilen aşk uyumu: {prediction} Başarısız😢.")
            tab_oneri.snow()


if __name__ == "__main__":
    main()

# b1, b2, b3 = tab_oneri.columns(3)
# if b2.button("Aşk uyumum!", key="ask_uyumu_button"):
#    prediction = model.predict(user_input)
#    b2.success(f"Tahmin edilen aşk uyumu: {prediction}")
#    if prediction == 1:
#        b2.balloons()
