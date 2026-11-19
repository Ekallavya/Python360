from fastapi import FastAPI

restapi = FastAPI()

@restapi.get("/welcome")
def  welcome():
    print("Welcome to P11 RestAPI")
    return "Welcome to P11 RestAPI"