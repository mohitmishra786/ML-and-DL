# importing required libraries
import pandas as pd
import numpy as np
from catboost import CatBoostClassifier
from catboost import CatBoostRegressor
from sklearn.metrics import accuracy_score

def catboost_classifier(train_data , test_data , number_of_iterations,target_feature):
    
    #printing the shape of train and test data
    print('Shape of training data :',train_data.shape)
    print('Shape of testing data :',test_data.shape)

    # seperate the independent and target variable on training data
    train_x = train_data.drop(columns=[target_feature],axis=1)
    train_y = train_data[target_feature]

    # seperate the independent and target variable on testing data
    test_x = test_data.drop(columns=[target_feature],axis=1)
    test_y = test_data[target_feature]

    # find out the indices of categorical variables
    categorical_var = np.where(train_x.dtypes != np.float)[0]
    print('\nCategorical Variables indices : ',categorical_var)

    # fit the model with the training data
    model = CatBoostClassifier(iterations=number_of_iterations)
    model.fit(train_x,train_y,cat_features = categorical_var,plot=False)
    print('\n Model Trainied')

    # predict the target on the train dataset
    predict_train = model.predict(train_x)
    print('\nTarget on train data',predict_train)

    # Accuray Score on train dataset
    accuracy_train = accuracy_score(train_y,predict_train)
    print('\naccuracy_score on train dataset : ', accuracy_train)

    # predict the target on the test dataset
    predict_test = model.predict(test_x)
    print('\nTarget on test data',predict_test) 

    # Accuracy Score on test dataset
    accuracy_test = accuracy_score(test_y,predict_test)
    print('\naccuracy_score on test dataset : ', accuracy_test)

def catboost_regressor(train_data , test_data , number_of_iterations,target_feature):
    
    #printing the shape of train and test data
    print('Shape of training data :',train_data.shape)
    print('Shape of testing data :',test_data.shape)

    # seperate the independent and target variable on training data
    train_x = train_data.drop(columns=[target_feature],axis=1)
    train_y = train_data[target_feature]

    # seperate the independent and target variable on testing data
    test_x = test_data.drop(columns=[target_feature],axis=1)
    test_y = test_data[target_feature]

    # find out the indices of categorical variables
    categorical_var = np.where(train_x.dtypes != np.float)[0]
    print('\nCategorical Variables indices : ',categorical_var)

    # fit the model with the training data
    model=CatBoostRegressor(iterations=50, depth=3, learning_rate=0.1, loss_function='RMSE')
    model.fit(X_train, y_train,cat_features=categorical_features_indices,eval_set=(X_validation, y_validation),plot=True)
    print('\n Model Trainied')

    # predict the target on the train dataset
    predict_train = model.predict(train_x)
    print('\nTarget on train data',predict_train)

    # Accuray Score on train dataset
    accuracy_train = accuracy_score(train_y,predict_train)
    print('\naccuracy_score on train dataset : ', accuracy_train)

    # predict the target on the test dataset
    predict_test = model.predict(test_x)
    print('\nTarget on test data',predict_test) 

    # Accuracy Score on test dataset
    accuracy_test = accuracy_score(test_y,predict_test)
    print('\naccuracy_score on test dataset : ', accuracy_test)
