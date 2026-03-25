import requests


class EmployeeApi:
    def __init__(self, url):
        self.url = url

    def create_employee(self, employee_data):
        response = requests.post(
            self.url + "/employee/create",
            json=employee_data
        )
        return response

    def get_employee_by_id(self, employee_id):
        response = requests.get(
            self.url + f"/employee/info/{employee_id}"
        )
        return response

    def update_employee(self, employee_id, user_token, updated_data):
        response = requests.patch(
            self.url + f"/employee/change/{employee_id}",
            params={"client_token": user_token},
            json=updated_data
        )
        return response

    def get_company_employee_list(self, company_id):
        response = requests.get(
            self.url + f"/employee/list/{company_id}"
        )
        return response

    def find_employee_in_company_list_by_email(self, company_id, email):
        response = self.get_company_employee_list(company_id)
        assert response.status_code == 200, (
            f"Не удалось получить список сотрудников. "
            f"Статус: {response.status_code}"
        )

        employees = response.json()

        for employee in employees:
            if employee.get("email") == email:
                return employee

        return None

    def get_employee_by_id_if_exists(self, employee_id):
        response = self.get_employee_by_id(employee_id)

        if response.status_code == 200:
            return response.json()

        return None

    def find_employee_id_by_email(self, email):
        search_steps = [100, 300, 1000, 3000]

        for search_limit in search_steps:
            for employee_id in range(1, search_limit + 1):
                employee = self.get_employee_by_id_if_exists(employee_id)

                if employee is None:
                    continue

                if employee.get("email") == email:
                    return employee_id

        return None