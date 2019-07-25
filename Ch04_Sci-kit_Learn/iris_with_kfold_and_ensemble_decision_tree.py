from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import (KFold, StratifiedKFold)

iris = load_iris() # Iris 데이터 세트 불러오기
kf = KFold(n_splits = 10, random_state=None, shuffle=True)
kf.get_n_splits(iris)

dt_ens = BaggingClassifier()        # Classification에 사용할 모델 불러오기
dt_clf = DecisionTreeClassifier()   # Classification에 사용할 모델 불러오기

X = iris.data                 # 학습에 사용할 데이터 저장
y = iris.target               # 학습에 사용할 Label 저장


for train_index, test_index in kf.split(X):
    print(f"TRAIN : {train_index}\tTEST : {test_index}")
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    dt_clf.fit(X_train, y_train)     # 학습 진행
    dt_ens.fit(X_train, y_train)     # 학습 진행

    pred_e = dt_ens.predict(X_test)       # 학습된 모델을 검증
    print("Ensemble      정확도(accuracy) : ", accuracy_score(y_test, pred_e))    # 정확도 출력

    pred_c = dt_clf.predict(X_test)       # 학습된 모델을 검증
    print("Decision Tree 정확도(accuracy) : ", accuracy_score(y_test, pred_c))    # 정확도 출력
