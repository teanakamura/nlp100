"""
77. 正解率の計測
76の出力を受け取り，予測の正解率，正例に関する適合率，再現率，F1スコアを求めるプログラムを作成せよ．
"""


from mymodule.path_helpers import get_rel_path_from_working_directory
import numpy as np
from nlp100_73 import sigmoid, create_x_y_data


if __name__ == '__main__':
    features_file = get_rel_path_from_working_directory(__file__, '../data/features.txt')
    source_file = get_rel_path_from_working_directory(__file__, '../data/sentiment.txt')
    theta_file = get_rel_path_from_working_directory(__file__, '../data/theta.npy')
    with open(features_file) as f:
        features = f.read().split()
    with open(source_file) as f:
        sentences = f.readlines()
    theta = np.load(theta_file)
    X, Y = create_x_y_data(sentences, features)
    predictions = sigmoid(X, theta)
    predicted_values = np.round(predictions)
    accuracy = np.sum((Y - predicted_values) == 0) / len(Y)
    # precision = np.sum(np.logical_and(Y == 1, predicted_values == 1)) / np.sum(predicted_values == 1)
    precision = np.sum((Y + predicted_values) == 2) / np.sum(predicted_values == 1)
    recall = np.sum((Y + predicted_values) == 2) / np.sum(Y == 1)
    f_value = 2 * recall * precision / (recall + precision)
    print('accuracy: %f \tprecision: %f \trecall: %f \tFvalue: %f' % (accuracy, precision, recall, f_value))
