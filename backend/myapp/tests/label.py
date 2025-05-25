from rest_framework.test import APIClient
from django.test import TestCase
from rest_framework import status 
from django.urls import reverse
from myapp.models import Label

#TEST GET
class LabelGetAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        self.label1 = Label.objects.create(
            name = "Ficción",
            description = "Lorem ipsum dolor sit amet",
            active = True
        )
        
        self.detail_url = reverse("myapp:label-list-create")
        self.response = self.client.get(self.detail_url, content_type="application/json")
        
    def test_status_code(self):
        #verificar si devuelve el codigo de estado correcto
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_response_structure(self):
        data = self.response.json()
        
        #verificar si la data no esta vacia
        self.assertGreater(len(data), 0, "No data")
        
        expected_fields = ["id", "name", "description", "active"]
        
        #verificar que los campos requeridos si esten en la respuesta
        for field in expected_fields:
            self.assertIn(field, data[0])

        #verificar que los datos de la respuesta correspodan con el objeto creado para la prueba         
        for field in expected_fields:
            self.assertEqual(data[0][field], getattr(self.label1, field))
            
        #verificar en db
        expected_fields = ["id", "name", "description", "active"]
        
        label = Label.objects.get(id=self.label1.id)
        
        for field in expected_fields:
            self.assertEqual(getattr(label, field), getattr(self.label1, field))   
        
    def test_field_types(self):
        data = self.response.json()
        
        expected_fields = {
            "id":int,
            "name":str,
            "description":str,
            "active":bool
        }
        
        #verificar que los tipos de campos de la respuesta sean los esperados
        for field, type in expected_fields.items():
            self.assertIsInstance(data[0][field], type)
            
#TEST GET DETAIL
class LabelGetDetailAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        self.label1 = Label.objects.create(
            name = "Ficción",
            description = "Lorem ipsum dolor sit amet",
            active = True
        )
        
        self.detail_url = reverse("myapp:label-detail", kwargs={"id":self.label1.id})
        self.response = self.client.get(self.detail_url, content_type="application/json")
        
    def test_status_code(self):
        #verificar si devuelve el codigo de estado correcto
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_response_structure(self):
        data = self.response.json()

        expected_fields = ["id", "name", "description", "active"]
        
        #verificar que los campos requeridos si esten en la respuesta
        for field in expected_fields:
            self.assertIn(field, data)

        #verificar que los datos de la respuesta correspodan con el objeto creado para la prueba
        for field in expected_fields:
            self.assertEqual(data[field], getattr(self.label1, field))
            
        #verificar en db
        expected_fields = ["id", "name", "description", "active"]
        
        label = Label.objects.get(id=self.label1.id)
        
        for field in expected_fields:
            self.assertEqual(getattr(label, field), getattr(self.label1, field))
            
    def test_field_types(self):
        data = self.response.json()
        
        expected_fields = {
            "id":int,
            "name":str,
            "description":str,
            "active":bool
        }
        
        #verificar que los tipos de campos de la respuesta sean los esperados
        for field, type in expected_fields.items():
            self.assertIsInstance(data[field],type)
            
#TEST POST           
class LabelPostAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.label_post_data = {
            "name": "Ficción",
            "description": "Lorem ipsum dolor sit amet",
            "active": True
        }
        
        self.detail_url = reverse("myapp:label-list-create")
        self.response = self.client.post(self.detail_url, self.label_post_data, content_type="application/json")
        
    def test_status_code(self):
        #verificar si devuelve el codigo de estado correcto
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        
    def test_response_structure(self):
        data = self.response.json()
        
        #verificar que los campos requeridos si esten en la respuesta
        expected_fields = ["id", "name", "description", "active"]
        
        for field in expected_fields:
            self.assertIn(field, data)
        
        #verificar que los datos de la respuesta correspodan con la data de la solicitud
        expected_fields = ["name", "description", "active"]
        
        for field in expected_fields:
            self.assertEqual(data[field], self.label_post_data[field])
            
        #verificar que los datos del objeto en db correspondan con la data de la solicitud
        label = Label.objects.get(name=self.label_post_data["name"])
        
        for field in expected_fields:
            self.assertEqual(getattr(label, field), self.label_post_data[field])
            
        #COMPROBAR EN DB

    def test_field_types(self):
        data = self.response.json()
        
        field_types = {
            "id":int,
            "name": str,
            "description": str,
            "active": bool
        }
           
        #verificar que los tipos de campos de la respuesta sean los esperados   
        for field, type in field_types.items():
            self.assertIsInstance(data[field], type)

#TEST DELETE     
class labelDeleteAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        self.label1 = Label.objects.create(
            name = "Ficción",
            description = "Lorem ipsum dolor sit amet",
            active = True
        )
        
        self.detail_url = reverse("myapp:label-detail", kwargs={"id": self.label1.id})
        self.response = self.client.delete(self.detail_url, content_type="application/json")
        
    def test_status_code(self):
        #verificar si devuelve el codigo de estado correcto
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_object_delete(self):
        #verificar que el objeto no exista en la db
        self.assertFalse(Label.objects.filter(id=self.label1.id).exists())
        
#TEST PUT
class LabelPutAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        self.label1 = Label.objects.create(
            name = "Ficción",
            description = "Lorem ipsum dolor sit amet",
            active = True    
        )
        
        self.label_put_data = {
            "name": "Terror",
            "description": "Ipsum",
            "active": False
        }
        
        self.detail_url = reverse("myapp:label-detail", kwargs={"id": self.label1.id})
        self.response = self.client.put(self.detail_url, self.label_put_data, content_type="application/json")
        
    def test_status_code(self):
        #verificar si devuelve el codigo de estado correcto
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_response_structure(self):
        data = self.response.json()
        
        #verificar que los campos requeridos si esten en la respuesta
        expected_fields = ["id", "name", "description", "active"]
        
        for field in expected_fields:
            self.assertIn(field, data)
            
        #verificar que los datos de la respuesta correspodan con la data de la solicitud
        expected_fields = ["name", "description", "active"]
        for field in expected_fields:
            self.assertEqual(data[field], self.label_put_data[field])
            
        #verificar que los datos del objeto en db correspondan con la data de la solicitud
        label = Label.objects.get(id=self.label1.id)
        
        for field in expected_fields:
            self.assertEqual(getattr(label, field), self.label_put_data[field] )
            
    def test_fields_types(self):
        data = self.response.json()
        
        fields_types = {
            "id": int,
            "name": str,
            "description": str,
            "active": bool,            
        }
        
        #verificar que los tipos de campos de la respuesta sean los esperados
        for field, type in fields_types.items():
            self.assertIsInstance(data[field], type)

#TEST METODO PATCH
class LabelPatchAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        self.label1 = Label.objects.create(
            name = "Ficción",
            description = "Lorem ipsum dolor sit amet",
            active = True   
        )
        
        self.label_patch_data = { 
            "name":"Terror"
        }
        
        self.detail_url = reverse("myapp:label-detail", kwargs={"id": self.label1.id})
        self.response = self.client.patch(self.detail_url, self.label_patch_data, content_type="application/json")
        
    def test_status_code(self):
        #verificar si devuelve el codigo de estado correcto
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_response_structure(self):
        data = self.response.json()
        
        #verificar que los campos requeridos si esten en la respuesta
        expected_fields = ["id", "name", "description", "active"]
        
        for field in expected_fields:
            self.assertIn(field, data)
           
        #verificar si el campo se modifico 
        self.assertEqual(data["name"], self.label_patch_data["name"])
        
        #verificar si los campos que no se modificaron quedaron igual
        label = Label.objects.get(id=self.label1.id)
        
        expected_data = ["id", "description", "active"]
        
        for field in expected_data:
            self.assertEqual(data[field], getattr(label, field))
                
    def test_field_types(self):
        data = self.response.json()
        
        field_types = {
            "id": int,
            "name": str,
            "description": str,
            "active": bool, 
        }
        
        #verificar que los tipos de campos de la respuesta sean los esperados
        for field, type in field_types.items():
            self.assertIsInstance(data[field], type)