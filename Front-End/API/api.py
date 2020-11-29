import eazyml


test_file_path = 'test.csv'

# To authenticate and retrieve an authentication token to be used for

# all API calls


auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIxOTUzMGFlOS04MTllLTQwZDMtYWY3MC05MDk4MDY2OTYxZWYiLCJleHAiOjE2MDY2OTI5NDEsImZyZXNoIjpmYWxzZSwiaWF0IjoxNjA2NjA2NTQxLCJ0eXBlIjoiYWNjZXNzIiwibmJmIjoxNjA2NjA2NTQxLCJpZGVudGl0eSI6InRlZXQ1ODU4QGdtYWlsLmNvbSJ9.f9o1BMzIG4boBqb1ftpLgKrN3wtZ0zoY2WEvMuDQxqI"


# To initialize machine learning model parameters.

model_id = "12469"


options = {

    "model_name": "Boosted Decision Trees"

}
prediction_dataset_id = str(eazyml.ez_predict(auth_token, model_id, test_file_path, options))

print(prediction_dataset_id)