from fastapi.testclient import TestClient
from main import app


client = TestClient(app)



def test_create_establishment():
    data = {
        "name": "Product",
        "description": "Productdesc",
        "locations": "EstablishmentLoc",
        "opening_hours": "09:00",
    }

    response = client.post("/establishments/", json=data)
    assert response.status_code == 201
    response_data = response.json()
    assert response_data["id"] is not None
    assert response_data["name"] == data["name"]
    assert response_data["description"] == data["description"]
    assert response_data["locations"] == data["locations"]
    assert response_data["opening_hours"] == data["opening_hours"]


def test_get_establishment():
    establishment_id = 'ab93b601-3e91-45fb-847d-8c937d95c393'
    
    data = {
        "id": establishment_id,
        "name": "Product",
        "description": "Productdesc",
        "locations": "EstablishmentLoc",
        "opening_hours": "09:00",
    }
    response = client.get(f"/establishments/{establishment_id}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == data["id"]
    assert response_data["name"] == data["name"]
    assert response_data["description"] == data["description"]
    assert response_data["locations"] == data["locations"]
    assert response_data["opening_hours"] == data["opening_hours"]



def test_update_establishment():
    establishment_id ='ab93b601-3e91-45fb-847d-8c937d95c393'
    
    data = {
        "id": establishment_id,
        "name": "NewProduct",
        "description": "NewProductdesc",
        "locations": "NewEstablishmentLoc",
        "opening_hours": "10:00",
    }
    response = client.put(f"/establishments/{establishment_id}")
    assert response.status_code == 202
    response_data = response.json()
    assert response_data["id"] == data["id"]
    assert response_data["name"] == data["name"]
    assert response_data["description"] == data["description"]
    assert response_data["locations"] == data["locations"]
    assert response_data["opening_hours"] == data["opening_hours"]    

def test_delete_establishment():
    establishment_id ='ab93b601-3e91-45fb-847d-8c937d95c393'
    response = client.delete(f"/products/{establishment_id}")
    assert response.status_code == 204



