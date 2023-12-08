import mlflow
import mlflow.sklearn
from urllib.parse import urlparse
def calculate(x,y):
    return (x+y)
if __name__=='__main__':
    x=1000
    y=2000
    mlflow.set_registry_uri("MLFLOW_TRACKING_URI=https:\
                            //dagshub.com/LataData/mlrun_prac.mlflow ")
            
    tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
            
    print(tracking_url_type_store)
    with mlflow.start_run():
        result=calculate(x,y)
        mlflow.log_param('x',x)
        mlflow.log_param('y',y)
        mlflow.log_param('result',result)
        '''if tracking_url_type_store != "file":
            mlflow.sklearn.log_model(, "model", registered_model_name="ml_model")
        else:
            mlflow.sklearn.log_model(model, "model")'''
