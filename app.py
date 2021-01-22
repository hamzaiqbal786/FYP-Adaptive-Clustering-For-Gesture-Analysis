from my_utils.dataset_utils import  *
import os
from sklearn import svm,neighbors
from sklearn.metrics import accuracy_score

import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,classification_report
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def most_frequent(List):
    return max(set(List), key = List.count)

def trainKNN( X_train, X_test, y_train, y_test, K):
    knn_clf = neighbors.KNeighborsClassifier(n_neighbors=K, weights='distance')
    knn_clf.fit(X_train, y_train)
    # p = knn_clf.predict(X_train)

    with open("knn.pkl", 'wb') as f:
        pickle.dump(knn_clf, f)
    # print("Train Accuracy :", accuracy_score(y_train, p) * 100)
    p = knn_clf.predict(X_test)
    print("Test Accuracy :", accuracy_score(y_test, p) * 100)
    return knn_clf

def loadModel(model_file="knn.pkl"):
    with open(model_file, 'rb') as file:
        model = pickle.load(file)
    return model

def train_cluster_model(X_train, clusters):
    kmeans = KMeans(n_clusters=clusters).fit(X_train)
    with open("clustering_model.pkl", 'wb') as f:
        pickle.dump(kmeans, f)
    return kmeans

def get_video_level_predictions(videos, features_truth, features_preds, output_file=None, is_evaluation=False):
    df=pd.DataFrame({
        "videos":videos,
        "truth":features_truth,
        "preds":features_preds
    })
    if output_file is not None:
        if os.path.exists(output_file):
            os.remove(output_file)
    f = open(output_file, "w")
    f.write("Video,prediction\n")
    video_truth_list=[]
    video_predictions_list=[]

    for v in list(np.unique(df['videos'])):
        g=(df.loc[df["videos"]==v])
        p=(most_frequent(list(g["preds"])))
        if is_evaluation:
            vid_truth=(list(g["truth"])[0])
            video_truth_list.append(vid_truth)
        video_predictions_list.append(p)
        if output_file is not None:
            f = open(output_file, "a")
            f.write(v+","+str(p)+"\n")
            f.close()
    print("Results saved in",output_file)
    if is_evaluation:
        c_mat = confusion_matrix(video_truth_list, video_predictions_list)
        report = classification_report(video_truth_list, video_predictions_list)
        print("Video level Accuracy:", accuracy_score(video_truth_list, video_predictions_list) * 100)
        print(report)
        CLASSES=list(np.unique(np.array(video_truth_list)))
        df_cm = pd.DataFrame(c_mat,index=CLASSES,columns=CLASSES)
        plt.figure(figsize=(12, 12))
        sns.heatmap(df_cm,annot=True)
        plt.show()



def predict_from_json(json_filename,group_features=1):
    videos, X_test, y_test = load_features_dataset(json_filename=json_filename,is_group=True,groups=group_features)
    try:
        os.mkdir("Output")
    except:
        pass


    output_file = "predictions.csv"
    clf1=loadModel("knn.pkl")
    clf2=loadModel("clustering_model.pkl")
    output_file = os.path.join("Output", output_file)
    cluster_preditcs = clf2.predict(X_test)

    ####
    name_predicts = []
    for index in cluster_preditcs:
        name_predicts.append(CLUSTER_NAME.get(index))
    ####

    preds = clf1.predict(X_test)
    df = pd.DataFrame({
        "videos": videos,
        "truth": y_test,
        "predictions": preds,
        "clusters":name_predicts
    })

    df.to_csv(output_file)

def train(feature_group=1):
    train_videos, X_train, y_train = load_features_dataset("Extracted_Features/train_features.json")
    train_videos, X_train, y_train = group_features(train_videos, X_train, y_train,feature_group)
    test_videos, X_test, y_test = load_features_dataset("Extracted_Features/test_features.json")
    test_videos, X_test, y_test = group_features(test_videos, X_test, y_test,feature_group)
    print("Training data", X_train.shape)
    print("Testing data", X_test.shape)
    trainKNN(X_train, X_test, y_train, y_test, 1)
    train_cluster_model(X_train,6)


# if __name__ == '__main__':
#    # predict_from_json("Extracted_Features/test_videos_features.json")

#     train_videos, X_train, y_train = load_features_dataset("Extracted_Features/train_features.json")
#     train_videos, X_train, y_train=group_features(train_videos, X_train, y_train)
#     test_videos, X_test, y_test = load_features_dataset("Extracted_Features/test_features.json")
#     test_videos, X_test, y_test=group_features(test_videos, X_test, y_test)
#
#     print("Training data", X_train.shape)
#     print("Testing data", X_test.shape)
#     clf=train_cluster_model(X_train, 6)
#     preds=clf.fit_predict(X_train)
#     df = pd.DataFrame({
#         "videos": train_videos,
#         "truth": y_train,
#         "predictions": preds
#     })
#     df.to_csv("output.csv")