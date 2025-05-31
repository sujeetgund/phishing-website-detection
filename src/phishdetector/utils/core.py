def extract_clf_name(clf_str):
    if not isinstance(clf_str, str):
        clf_str = str(clf_str)
    if "RandomForestClassifier" in clf_str:
        return "RandomForest"
    elif "KNeighborsClassifier" in clf_str:
        return "KNeighbors"
    elif "SVC" in clf_str:
        return "SVC"
    elif "RidgeClassifier" in clf_str:
        return "Ridge"
    elif "LogisticRegression" in clf_str:
        return "Logistic"
    else:
        return "Unknown"
