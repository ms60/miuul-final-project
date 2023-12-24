import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, cross_validate, validation_curve
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import joblib

df = pd.read_excel("/home/msel/Desktop/MIUUL_13/miuul-13/miuul-13/final-project/miuul-final-project/veriler.xlsx")
dforig = pd.read_excel("/home/msel/Desktop/MIUUL_13/miuul-13/miuul-13/final-project/miuul-final-project/veriler.xlsx")

ohe_cols = ['NEW_LOVE', 'NEW_EDUCATION', 'NEW_ECO_SIM', 'NEW_AGE_GAP', 'NEW_SOC_SIM', 'NEW_CUL_SIM', 'NEW_SOCIAL_GAP',
            'NEW_COMM_INT', 'NEW_REL_COMP', 'CHILD_NUM_BEFORE', 'NEW_ENG_TIME', 'NEW_REL_FAM', 'NEW_ADD', 'NEW_LOY',
            'NEW_INCOME', 'SPOUSE_BEF_MARR', 'NEW_SOCIAL']


def one_hot_encoder(dataframe, categorical_cols):
    dataframe = pd.get_dummies(dataframe, columns=categorical_cols)
    return dataframe


df = one_hot_encoder(dforig, ohe_cols)

num_cols = ['Desire_to_Marry', 'Independency', 'Trading_in', 'Commitment', 'Mental_Health',
            'The_Sense_of_Having_Children', 'Previous_Trading', 'Previous_Marriage', 'The_Proportion_of_Common_Genes',
            'Height_Ratio', 'Self_Confidence', 'Spouse_Confirmed_by_Family', 'Divorce_in_the_Family_of_Grade_1',
            ]

Scaler = MinMaxScaler()
df[num_cols] = Scaler.fit_transform(df[num_cols])

y = df["Divorce_Class"]
X = df.drop("Divorce_Class", axis=1)

X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.20, random_state=17)

log_model = LogisticRegression().fit(X_train, y_train)

log_final = log_model.set_params(max_iter=10).fit(X_train, y_train)

# from sklearn.metrics import accuracy_score, roc_auc_score, confusion_matrix, classification_report, RocCurveDisplay
#
# y_pred = log_final.predict(X_test)
# print(classification_report(y_test, y_pred))

# random_user = X.sample(5)

# log_final.predict(random_user)

# model.feature_names_in_

model_filename = "/miuul-13/final-project/miuul-final-project/model_train_all2.joblib"
joblib.dump(log_final, model_filename)
print(f"Model save as {model_filename}")


