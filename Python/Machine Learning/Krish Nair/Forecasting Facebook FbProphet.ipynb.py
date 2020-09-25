#!/usr/bin/env python
# coding: utf-8

# ##### Forecasting Timeseries Data Using Facebook FbProphet
# 
# Steps Required With FbProphet
# 1. Introduction And Installation
# 2. Data Preprocessing With Time Seires
# 3. Model Fitting
# 4. Obtaining The Forecasts
# 5. Plotting The Forecasts
# 6. Cross Validation
# 7. Computing Performance Metrics
# 8. Visualize the Performance MEtrics
# 9. Conclusions
# 

# In[57]:


### pip install pystan
### conda install -c conda-forge fbprophet
import pandas as pd
import fbprophet
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[58]:


df=pd.read_csv('monthly-milk-production-pounds.csv')
df.head()


# In[59]:


df.tail()


# In[60]:


df.drop(168,axis=0,inplace=True)


# In[61]:


df.tail()


# In[62]:


df.columns=["ds","y"]


# In[63]:


df.plot()


# In[64]:


df.head()


# In[65]:


df['ds']=pd.to_datetime(df['ds'])


# In[12]:


df.head()


# In[66]:


df['y'].plot()


# In[ ]:





# In[17]:


df.head()


# In[67]:


df['y'].plot()


# In[68]:


from fbprophet import Prophet


# In[69]:


dir(Prophet)


# In[70]:


df.head()


# In[71]:


### intiialize the Model
model=Prophet()
model.fit(df)


# In[72]:


model


# In[73]:


model.seasonalities


# In[27]:


model.component_modes


# In[74]:


#### Create future dates of 365 days
future_dates=model.make_future_dataframe(periods=365)


# In[75]:


df.tail()


# In[29]:


future_dates


# In[76]:


### Prediction
prediction=model.predict(future_dates)


# In[77]:


prediction.head()


# In[36]:


(8.974783+27.786856)/2


# In[78]:


prediction[['ds','yhat','yhat_lower','yhat_upper']].tail()


# In[79]:


prediction[['ds','yhat','yhat_lower','yhat_upper']].head()


# #### Plotting the Forecasts
#  
# Prophet has an inbuilt feature that enables us to plot the forecasts we just generated. This is achieved using model.plot() and passing in our forecasts as the argument. The blue line in the graph represents the predicted values while the black dots represents the data in our dataset.

# In[80]:


#### plot the predicted projection
model.plot(prediction)


# In[81]:


##### Visualize Each Components[Trends,Weekly]
model.plot_components(prediction)


# #### Cross Validation
#  
# Next let’s measure the forecast error using the historical data. We’ll do this by comparing the predicted values with the actual values. In order to perform this operation we select cut of points in the history of the data and fit the model with data upto that cut off point. Afterwards we compare the actual values to the predicted values. The cross_validation method allows us to do this in Prophet. This method take the following parameters as explained below:
# 
# 1. horizon the forecast horizon
# 2. initial the size of the initial training period
# 3. period the spacing between cutoff dates

# In[82]:


df.shape


# In[83]:


from fbprophet.diagnostics import cross_validation


# In[84]:


df_cv=cross_validation(model,horizon="365 days",period='180 days',initial='1095 days')


# In[87]:


df.head()


# In[88]:


df_cv.head()


# #### Obtaining the Performance Metrics
#  
# We use the performance_metrics utility to compute the Mean Squared Error(MSE), Root Mean Squared Error(RMSE),Mean Absolute Error(MAE), Mean Absolute Percentage Error(MAPE) and the coverage of the the yhat_lower and yhat_upper estimates.

# In[89]:


from fbprophet.diagnostics import performance_metrics
df_performance=performance_metrics(df_cv)
df_performance.head()


# In[90]:


from fbprophet.plot import plot_cross_validation_metric
fig=plot_cross_validation_metric(df_cv,metric='rmse')


# In[ ]:




