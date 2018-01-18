import pytest
import app as main
import json

@pytest.fixture
def app():
    app = main.create_app()
    app.debug = True   
    return app.test_client()

def test_Welcome_LauchPad(app):
    res = app.get("/")
    # print(dir(res), res.status_code)
    assert res.status_code == 200
    assert b"Welcome to the LauchPad 2 Team K project" in res.data

def test_user_login(app):
    """Test registered user can login."""
    login_res = app.post('/auth', data={
            'email': 'tracy.tim@cognizant.com',
            'password': 'password'
        },content_type='application/json')    
    assert login_res.status_code == 200
    


    