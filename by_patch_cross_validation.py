import numpy as np
def cross_patch(xmin,xmax,ymin,ymax,df_merged):
    test_area_dim=[int(xmin),int(xmax),int(ymin),int(ymax)]
    well_test_loc=df_merged[['X','Y']].values
    X=well_test_loc[:,0].astype(float).copy()
    Y=well_test_loc[:,1].astype(float).copy()
    X=np.round((X-25)/50).astype(int)
    Y=np.round((Y-25)/50).astype(int)
    # well data
    train_id=((X>test_area_dim[2])*(X<test_area_dim[3])*(Y>test_area_dim[0])*(Y<test_area_dim[1])).astype(bool)
    return train_id

if __name__ == "__main__":
    test_id=cross_patch(100,199,100,199,df_merged)
    train_id=~test_id
    X_test = df_merged[[ "Porosity",'sand prp.', 'bottom to woc']].values[train_id==True]
    X_train = df_merged[[ "Porosity",'sand prp.', 'bottom to woc']].values[train_id==False]
    y_train = df_merged['Cumoil3'].values[train_id==False]
    y_test = df_merged['Cumoil3'].values[train_id==True]
    regressor = RandomForestRegressor(n_estimators=200, max_depth=25, min_samples_leaf=2,min_samples_split= 2, max_features= 'sqrt', bootstrap =False )
    regressor.fit(X_train, y_train)
    y_pred_test = regressor.predict(X_test)
    error=metrics.mean_squared_error(y_test,y_pred_test)    
    print('MSE:'+str(error))