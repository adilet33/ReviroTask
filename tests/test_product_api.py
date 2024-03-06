from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_create_product():
    data = {
        "name": "Product",
        "description": "Productdesc",
        "price": 100.0,
        "quantity_in_stock": 100,
    }

    response = client.post("/products/", json=data)
    assert response.status_code == 201
    response_data = response.json()
    assert response_data["id"] is not None
    assert response_data["name"] == data["name"]
    assert response_data["description"] == data["description"]
    assert response_data["price"] == data["price"]
    assert response_data["quantity_in_stock"] == data["quantity_in_stock"]


def test_get_product():
    product_id ='74a99f48-085a-4239-af5e-c7d141144a6f'
    data = {
        "id": product_id,
        "name": "Product",
        "description": "Productdesc",
        "price": 100.0,
        "quantity_in_stock": 100,
    }
    response = client.get(f"/products/{product_id}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == data["id"]
    assert response_data["name"] == data["name"]
    assert response_data["description"] == data["description"]
    assert response_data["price"] == data["price"]
    assert response_data["quantity_in_stock"] == data["quantity_in_stock"]

def test_update_product():
    product_id ='b0d89b84-c7a7-4bab-b518-c4ab5e5936e4'
    data = {
        "id": product_id,
        "name": "New_Product",
        "description": "New_Productdesc",
        "price": 200.0,
        "quantity_in_stock": 200,
    }
    response = client.put(f"/products/{product_id}", json=data)
    assert response.status_code == 202
    response_data = response.json()
    assert response_data["id"] == data["id"]
    assert response_data["name"] == data["name"]
    assert response_data["description"] == data["description"]
    assert response_data["price"] == data["price"]
    assert response_data["quantity_in_stock"] == data["quantity_in_stock"]


def test_delete_product():
    product_id ='b0d89b84-c7a7-4bab-b518-c4ab5e5936e4'
    response = client.delete(f"/products/{product_id}")
    assert response.status_code == 204