import os
from sklearn.model_selection import train_test_split
import json
import numpy as np
import pandas as pd

#Enum of clusters
CLUSTER_NAME={
    0:"A",
    1:"B",
    2: "C",
    3: "D",
    4:"E",
    5:"F"
}

def make_test_train_files(path):
    seed = 42
    for category in os.listdir(path):
        videos_path =os.path.join(path,category)
        videos=os.listdir(videos_path)
        print("Videos in",category ,":",len(videos))
        train_videos,test_videos=train_test_split(videos,test_size=0.2,shuffle=True,random_state=seed)
        with open("train_videos.txt",'a') as file:
            for v in train_videos:
                file.write(os.path.join(videos_path,v))
                file.write("\n")

        with open("test_videos.txt",'a') as file:
            for v in test_videos:
                file.write(os.path.join(videos_path,v))
                file.write("\n")

def load_features_dataset(json_filename,is_group=False,groups=4):
    with open(json_filename) as f:
        data = json.load(f)
    labels = []
    features=[]
    videos=[]
    print("Found",len(data),"videos")
    for i in range(len(data)):
        video_path=data[i]['video']
        try:
            label =video_path.split("/")[-2]
        except:
            label=0
            pass

        for j in range(len(data[i]["clips"])):
            # if j !=0 and j!= len(data[i]["clips"])-1:
            if True:
                segment_feature=data[i]["clips"][j]
                f=np.array(segment_feature["features"])
                features.append(f)
                videos.append(video_path)
                labels.append(label)

    features=np.array(features)
    if is_group:
        videos, features, labels = group_features(videos, features, labels,groups)
    return videos, features, labels

def group_features(videos,features,labels,padding_thresh=4):
    videos=np.array(videos)
    labels=np.array(labels)
    features=np.array(features)
    grouped_features=[]
    grouped_labels=[]
    grouped_videos=[]

    for v in list(np.unique(videos)):
        idx=np.where(videos==v)
        f=features[idx[0]]
        l=labels[idx[0]][0]
        if f.shape[0]<padding_thresh:
            pad_value = (padding_thresh -f.shape[0]) *512
            f = np.pad(f.flatten(), (0,pad_value), 'constant', constant_values=(0, 0))
        elif f.shape[0]>padding_thresh:
            f=f[0:padding_thresh,:].flatten()
        else:
            f=f.flatten()
        grouped_features.append(f)
        grouped_labels.append(l)
        grouped_videos.append(v)

    return grouped_videos,np.array(grouped_features),np.array(grouped_labels)

        # break


def rename_files(path):
    for category in os.listdir(path):
        videos_path =os.path.join(path,category)
        videos=os.listdir(videos_path)
        for v in videos:
            old_name =v
            old_name=old_name.replace(" ","_")
            old_name=old_name.replace(")","_")
            new_name=old_name.replace("(", "_")
            os.rename(os.path.join(videos_path,v),os.path.join(videos_path,new_name))



