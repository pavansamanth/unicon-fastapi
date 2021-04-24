from .test_database import app
from fastapi.testclient import TestClient

client = TestClient(app)



def test_wrong_names():

    response = client.post(

        "/api/v1/signup",

        json={

            "accountType": "CLIENT",

            "firstName": "test1",

            "lastName": "test1",

            "email": "test@gmail.com",

            "password": "Pavan@1234",

        },

    )

    assert response.status_code == 418

    print(response.text)



def test_valid_email():

    response = client.post(

        "/api/v1/signup",

        json={

            "accountType": "CLIENT",

            "firstName": "test ex",

            "lastName": "test ex",

            "email": "test/sai@gmail.com",

            "password": "Pavan@1234",

        },

    )

    assert response.status_code == 420

    print(response.text)



def test_valid_password():

    response = client.post(

        "/api/v1/signup",

        json={

            "accountType": "CLIENT",

            "firstName": "test ex",

            "lastName": "test ex",

            "email": "test.sai@gmail.com",

            "password": "pavan@1234",

        },

    )


    assert response.status_code == 400

    print(response.text)



def test_signup():

    response = client.post(

        "/api/v1/signup",

        json={

            "accountType": "CLIENT",

            "firstName": "test ex",

            "lastName": "test ex",

            "email": "test.sai@gmail.com",

            "password": "Pavan@1234",

        },

    )

    assert response.status_code == 200, response.text

    print(response.text)