import eazyml


#Login Credentials
username = 'api_demo'
password = 'api_demo'

#File paths for training and test data
filepath_train = "Titanic - Training Data.csv"
filepath_test = "Titanic - Test Data.csv"

outcome = "Survived"
global auth_token
global dataset_id
global model_id
global prediction_dataset_id

def ez_auth():

    '''
    This function calls the API which allows the user to authenticate with EazyML and returns a token
    '''
    try:
        global auth_token
    
        #Calling the eazyml library function for authentication
        response = eazyml.ez_auth(username, password)
        auth_token = response["token"]
        print("Output of ez_auth function is", response)
    except Exception as e:
        print('The function ez_auth was not executed properly', e)
    

def ez_load():

    '''
    This function calls the API which allows the user to upload training data in a file.
    The accepted file formats are .csv and .xlsx.
    '''
    try: 
        global auth_token
        global dataset_id

        #The options dictionary that is to be provided as part of the request payload. 
        #Please check the API guide for more parameters
        options = {"accelerate":"no"}
        
        #Calling the eazyml library function for loading data
        response = eazyml.ez_load(auth_token, filepath_train, options)
        dataset_id = response['dataset_id']
        print("Output of ez_load function is", response)
    except Exception as e:
        print('The function ez_load was not executed properly', e)


def ez_impute():

    '''
    This function calls the API which allows you to impute missing values in the
    training dataset and then optionally fetch all those records with values imputed.
    '''
    try:
        global auth_token
        global dataset_id

        #The options dictionary that is to be provided as part of the request payload. 
        #Please check the API guide for more parameters
        options = {}

        #Calling the eazyml library function for imputation
        response = eazyml.ez_impute(auth_token, dataset_id, options)
        print("Output of ez_impute function is", response)
    except Exception as e:
        print('The function ez_impute was not executed properly', e)

def ez_outlier():

    '''
    This function calls the API which allows you to detect and remove outliers in the
    training dataset and then optionally fetch all those outlier records
    '''
    try:
        global auth_token
        global dataset_id

        #The options dictionary that is to be provided as part of the request payload. 
        #Please check the API guide for more parameters
        options = {}

        #Calling the eazyml library function for outlier removal
        response = eazyml.ez_outlier(auth_token, dataset_id, options)
        print("Output of ez_outlier function is", response)
    except Exception as e:
        print('The function ez_outlier was not executed properly', e)


def ez_set_outcome():

    '''
    This function calls the API which allows you to specify the outcome
    variable and optionally it's data type
    '''
    try:
        global auth_token
        global dataset_id

        #The options dictionary that is to be provided as part of the request payload. 
        #Please check the API guide for more parameters
        options = {}

        #Calling the eazyml library function for setting the outcome
        response = eazyml.ez_set_outcome(auth_token, dataset_id, outcome, options)
        print("Output of ez_set_outcome function is", response)
    except Exception as e:
        print('The function ez_set_outcome was not executed properly', e)


def ez_init_model():

    '''
    This function calls the API which allows you to initialize machine learning
    model parameters. It provides the user with various options on model building
    such as type of the model, dependency removal, derivation from numeric or
    text predictors derivations and many more.
    '''
    try:
        global auth_token
        global dataset_id
        global model_id

        #The options dictionary that is to be provided as part of the request payload. 
        #Please check the API guide for more parameters
        options = {"accelerate":"no"}    
    
        #Calling the eazyml library function for initializing model
        response = eazyml.ez_init_model(auth_token, dataset_id, options)
        model_id = response['model_id']
        print("Output of ez_init_model function is", response)
    except Exception as e:
        print('The function ez_init_model was not executed properly', e)


def ez_remove_dependent():

    '''
    This function calls the API which allows users to remove dependent
    predictors after model initialization.
    '''
    try:
        global auth_token
        global model_id

        #The options dictionary that is to be provided as part of the request payload. 
        #Please check the API guide for more parameters
        options = {}   

        #Calling the eazyml library function for removing dependent predictors
        response = eazyml.ez_remove_dependent(auth_token, model_id, options)
        print("Output of ez_remove_dependent function is", response)
    except Exception as e:
        print('The function ez_remove_dependent was not executed properly', e)


def ez_derive_numeric():

    '''
    This function calls the API which allows users to derive new predictors from native numeric predictors
    '''
    try:
        global auth_token
        global model_id

        #The options dictionary that is to be provided as part of the request payload. 
        #Please check the API guide for more parameters
        options = {"return_dataset":"yes"}

        #Calling the eazyml library function for deriving numeric predictors
        response = eazyml.ez_derive_numeric(auth_token, model_id, options)
        print("Output of ez_derive_numeric function is", response)
    except Exception as e:
        print('The function ez_derive_numeric was not executed properly', e)
    

def ez_select_features():

    '''
    This function calls the API which allows the users to perform feature selection
    algorithms on training data and then retrieve all selected features.
    '''
    try:
        global auth_token
        global model_id

        #The options dictionary that is to be provided as part of the request payload. 
        #Please check the API guide for more parameters
        options = {}

        #Calling the eazyml library function for selecting features
        response = eazyml.ez_select_features(auth_token, model_id)
        print("Output of ez_select_features function is", response)
    except Exception as e:
        print('The function ez_select_features was not executed properly', e)


def ez_build_models():

    '''
    This feature calls the API which allows users to build machine learning
    models after training data has been uploaded and preprocessed.
    '''
    try:
        global auth_token
        global model_id

        #The options dictionary that is to be provided as part of the request payload. 
        #Please check the API guide for more parameters
        options = {}

        #Calling the eazyml library function for building models
        response = eazyml.ez_build_models(auth_token, model_id)
        print("Output of ez_build_models function is", response)
    except Exception as e:
        print('The function ez_build_models was not executed properly', e)


def ez_predict():

    '''
    This function calls the API which allows you to predict the outcome variable
    for each record in the given prediction (or test) dataset
    '''
    try:
        global auth_token
        global model_id
        global prediction_dataset_id

        #The options dictionary that is to be provided as part of the request payload. 
        #Please check the API guide for more parameters
        options = {}

        #Calling the eazyml library function for prediction
        response = eazyml.ez_predict(auth_token, model_id, filepath_test, options)
        prediction_dataset_id = response['prediction_dataset_id']
        print("Output of ez_predict function is", response)
    except Exception as e:
        print('The function ez_predict was not executed properly', e)


def ez_explain():
    
    '''
    This function calls the API which allows you to fetch an explanation for
    the predicted outcome for any record or multiple records of the test dataset.
    '''
    try:
        global auth_token
        global model_id
        global prediction_dataset_id

        #The options dictionary that is to be provided as part of the request payload. 
        #Please check the API guide for more parameters
        options = {}

        #Calling the eazyml library function for explanation
        response = eazyml.ez_explain(auth_token, model_id, prediction_dataset_id, options)
        print("Output of ez_explain function is", response)
    except Exception as e:
        print('The function ez_explain was not executed properly', e)

if __name__ == '__main__':
    ez_auth()
    ez_load()
    ez_impute()
    ez_outlier()
    ez_set_outcome()
    ez_init_model()
    ez_remove_dependent()
    ez_derive_numeric()
    ez_select_features()
    ez_build_models()
    ez_predict()
    ez_explain()


