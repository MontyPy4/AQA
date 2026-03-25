import uuid
from datetime import date

from employee import EmployeeApi
from auth import AuthApi

base_url = "http://5.101.50.27:8000"


def create_test_employee_data():
    unique_part = uuid.uuid4().hex[:8]

    return {
        "first_name": "Alex",
        "last_name": "Finder",
        "middle_name": "Test",
        "company_id": 29,
        "email": f"alex_{unique_part}@example.com",
        "phone": f"12345{unique_part[:5]}",
        "birthdate": str(date.today()),
        "is_active": True
    }


def create_employee_and_get_id(api, employee_data):
    create_response = api.create_employee(employee_data)

    assert create_response.status_code == 200, (
        f"Ошибка при создании сотрудника. "
        f"Статус: {create_response.status_code}, тело: {create_response.text}"
    )

    employee_in_list = api.find_employee_in_company_list_by_email(
        employee_data["company_id"],
        employee_data["email"]
    )
    assert employee_in_list is not None, "Сотрудник не найден в списке компании"

    employee_id = api.find_employee_id_by_email(employee_data["email"])
    assert employee_id is not None, "Не удалось найти ID сотрудника"

    return employee_id


def get_user_token():
    auth_api = AuthApi(base_url)

    response = auth_api.login("harrypotter", "expelliarmus")

    assert response.status_code == 200, (
        f"Ошибка авторизации. Статус: {response.status_code}, тело: {response.text}"
    )

    response_data = response.json()
    return response_data["user_token"]


def test_create_employee():
    api = EmployeeApi(base_url)
    employee_data = create_test_employee_data()

    response = api.create_employee(employee_data)

    assert response.status_code == 200, (
        f"Ошибка при создании сотрудника. "
        f"Статус: {response.status_code}, тело: {response.text}"
    )

    employee_in_list = api.find_employee_in_company_list_by_email(
        employee_data["company_id"],
        employee_data["email"]
    )

    assert employee_in_list is not None, "Created employee was not found"
    assert employee_in_list["email"] == employee_data["email"]
    assert employee_in_list["first_name"] == employee_data["first_name"]


def test_get_employee_by_id():
    api = EmployeeApi(base_url)
    employee_data = create_test_employee_data()

    employee_id = create_employee_and_get_id(api, employee_data)

    response = api.get_employee_by_id(employee_id)

    assert response.status_code == 200, (
        "error response by id"
        f"Status: {response.status_code}"
    )

    employee_info = response.json()

    assert employee_info["email"] == employee_data["email"]
    assert employee_info["first_name"] == employee_data["first_name"]
    assert employee_info["last_name"] == employee_data["last_name"]


def test_update_employee():
    api = EmployeeApi(base_url)
    employee_data = create_test_employee_data()

    employee_id = create_employee_and_get_id(api, employee_data)
    user_token = get_user_token()

    updated_data = {
        "last_name": "updated",
        "email": employee_data["email"],
        "phone": employee_data["phone"],
        "is_active": False
    }

    updated_response = api.update_employee(employee_id, user_token, updated_data)

    assert updated_response.status_code == 200, (
        "error by employee updating"
        f"status: {updated_response.status_code}, text: {updated_response.text}"
    )

    employee_info_response = api.get_employee_by_id(employee_id)
    assert employee_info_response.status_code == 200

    employee_info = employee_info_response.json()

    assert employee_info["last_name"] == "updated"
    assert employee_info["is_active"] is False
    assert employee_info["email"] == employee_data["email"]