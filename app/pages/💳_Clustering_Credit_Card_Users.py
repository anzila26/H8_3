import streamlit as st
from pathlib import Path
import pandas as pd
import pickle

st.title('💳 Clustering Credit Card Users')

with open(str(Path(__file__).parents[1]) + '/models/cc_users_clusterer.pkl', 'rb') as file:
  model = pickle.load(file)
    
@st.cache
def predict(balance, balance_frequency, purchases, one_off_purchases, installment_purchases, cash_advance, purchases_frequency, one_off_purchases_frequency, installment_purchases_frequency, cash_advance_frequency, cash_advance_trx, purchases_trx, credit_limit, payments, minimum_payments, full_payment, tenure):
  return model.predict(pd.DataFrame([[balance, balance_frequency/100, purchases, one_off_purchases, installment_purchases, cash_advance, purchases_frequency/100, one_off_purchases_frequency/100, installment_purchases_frequency/100, cash_advance_frequency/100, cash_advance_trx, purchases_trx, credit_limit, payments, minimum_payments, full_payment/100, tenure]],
                                    columns=('BALANCE', 'BALANCE_FREQUENCY', 'PURCHASES', 'ONEOFF_PURCHASES', 'INSTALLMENTS_PURCHASES', 'CASH_ADVANCE', 'PURCHASES_FREQUENCY', 'ONEOFF_PURCHASES_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY', 'CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_TRX', 'PURCHASES_TRX', 'CREDIT_LIMIT', 'PAYMENTS', 'MINIMUM_PAYMENTS', 'PRC_FULL_PAYMENT', 'TENURE')))

balance = st.number_input('Balance ($):', min_value=0.0)
balance_frequency = st.slider('Balance Frequncy:', 0, 100, format='%f%%')
purchases = st.number_input('Purchases ($):', min_value=0.0)
one_off_purchases = st.number_input('One Off Purchases ($):', min_value=0.0)
installment_purchases = st.number_input('Installment Purchases ($):', min_value=0.0)
cash_advance = st.number_input('Cash Advance ($):', min_value=0.0)
purchases_frequency = st.slider('Purchases Frequncy:', 0, 100, format='%f%%')
one_off_purchases_frequency = st.slider('One Off Purchases Frequncy:', 0, 100, format='%f%%')
installment_purchases_frequency = st.slider('Installment Purchases Frequncy:', 0, 100, format='%f%%')
cash_advance_frequency = st.slider('Cash Advance Frequncy:', 0, 100, format='%f%%')
cash_advance_trx = st.number_input('Cash Advance Transactions:', min_value=0)
purchases_trx = st.number_input('Purchases Transactions:', min_value=0)
credit_limit = st.number_input('Credit Limit ($):', min_value=0.0)
payments = st.number_input('Payments ($):', min_value=0.0)
minimum_payments = st.number_input('Minimum Payments ($):', min_value=0.0)
full_payment = st.slider('Percent of Full Payment:', 0, 100, format='%f%%')
tenure = st.number_input('Tenure:', min_value=0)

if st.button('Cluster'):
  prediction = predict(balance, balance_frequency, purchases, one_off_purchases, installment_purchases, cash_advance, purchases_frequency, one_off_purchases_frequency, installment_purchases_frequency, cash_advance_frequency, cash_advance_trx, purchases_trx, credit_limit, payments, minimum_payments, full_payment, tenure)
  
  if prediction[0]:
    st.warning('You belong to a cluster of credit card users with low purchases.')
  else:
    st.success('You belong to a cluster of credit card users with high purchases.')