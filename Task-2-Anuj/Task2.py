from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    f1_score
)

# --------------------------------------------------
# STEP 1 : LOAD DATASET
# --------------------------------------------------

iris = load_iris()

X = iris.data
y = iris.target

print("=" * 60)
print("IRIS DATASET INFORMATION")
print("=" * 60)
print("Features Shape :", X.shape)
print("Target Shape   :", y.shape)
print("Classes        :", iris.target_names)
print()

# --------------------------------------------------
# STEP 2 : TRAIN TEST SPLIT
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    shuffle=True
)

# --------------------------------------------------
# STEP 3 : FEATURE SCALING
# --------------------------------------------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# --------------------------------------------------
# STEP 4 : KNN MODEL
# --------------------------------------------------

model = KNeighborsClassifier(n_neighbors=5)

model.fit(X_train, y_train)

# --------------------------------------------------
# STEP 5 : PREDICTION
# --------------------------------------------------

y_pred = model.predict(X_test)

# --------------------------------------------------
# STEP 6 : EVALUATION
# --------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

f1 = f1_score(
    y_test,
    y_pred,
    average='weighted'
)

cm = confusion_matrix(y_test, y_pred)

print("=" * 60)
print("MODEL PERFORMANCE")
print("=" * 60)

print(f"Accuracy : {accuracy:.4f}")
print(f"F1 Score : {f1:.4f}")

print("\nConfusion Matrix")
print(cm)

print("\nClassification Report")
print(classification_report(
    y_test,
    y_pred,
    target_names=iris.target_names
))

print("=" * 60)

# --------------------------------------------------
# STEP 7 : TEST WITH NEW FLOWER
# --------------------------------------------------

print("\nCUSTOM PREDICTION")

sample = [[5.1, 3.5, 1.4, 0.2]]

sample_scaled = scaler.transform(sample)

prediction = model.predict(sample_scaled)

flower_name = iris.target_names[prediction[0]]

print("Input Flower Features :", sample[0])
print("Predicted Class       :", flower_name)