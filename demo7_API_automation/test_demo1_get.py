import requests
from assertpy import assert_that


class TestPetStoreAPI:
    END_POINT = "https://petstore.swagger.io/v2"

    """def test_find_valid_pet_by_id(self):
        pet_id = 1001
        resource = f"/pet/{pet_id}"
        print(resource)

        response = requests.get(TestPetStoreAPI.END_POINT+resource)
        print(response)
        print(response.status_code)
        print(response.json())"""

    def test_find_valid_pet_by_id(self):
        pet_id = 5001
        resource = f"/pet/{pet_id}"
        response = requests.get(TestPetStoreAPI.END_POINT + resource)
        assert_that(200).is_equal_to(response.status_code)
