"""
73. 学習
72で抽出した素性を用いて，ロジスティック回帰モデルを学習せよ．
"""

from mymodule.path_helpers import get_rel_path_from_working_directory
import numpy as np
from stemming.porter2 import stem
from IPython import embed


def update_theta(eta, x, y, theta):
    return theta + eta * np.dot(y - sigmoid(x, theta), x)

def sigmoid(x, theta):
    return 1 / (1 + np.exp(-np.dot(x, theta)))

def create_x_y_data(sentences, features):
    x_list = []
    y_list = []
    for i, s in enumerate(sentences, 1):
        print('line' + str(i), end='\r')
        words = s.split()
        y_list.append(1 if words[0] == '+1' else 0)
        stemmed_words = [stem(w) for w in words[1:]]
        x_line = [1 if f in stemmed_words else 0 for f in features]
        x_list.append(x_line)
    x = np.array(x_list)
    Y = np.array(y_list)
    X = add_x0_line_for_bias(x)
    return X, Y

def add_x0_line_for_bias(x):
    x0 = np.ones([x.shape[0], 1])
    return np.hstack([x0, x])


if __name__ == '__main__':
    ETA = 1e-3
    EPOCH = 5000
    features_file = get_rel_path_from_working_directory(__file__, '../data/features.txt')
    source_file = get_rel_path_from_working_directory(__file__, '../data/sentiment.txt')
    theta_file = get_rel_path_from_working_directory(__file__, '../data/theta.npy')
    with open(features_file) as f:
        features = f.read().split()
    with open(source_file) as f:
        sentences = f.readlines()
    theta = np.random.rand(len(features) + 1)
    X, Y = create_x_y_data(sentences, features)

    for i in range(EPOCH):
        theta = update_theta(ETA, X, Y, theta)
        print('epoch' + str(i + 1), end='\r')
    np.save(theta_file, theta)
