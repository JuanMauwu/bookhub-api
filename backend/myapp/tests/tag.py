from django.test import TestCase
from rest_framework import status # type: ignore
from django.urls import reverse
from myapp.models import Tag

#TEST GET
class TagGetAPITest(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(
            name = "Tag name",
            active = True
        )
        
        self.detail_url = reverse("myapp:tag-list-create")
        self.response = self.client.get(self.detail_url)
        
    def test_status_code(self):
        #verificar si devuelve el codigo de estado correcto
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_response_structure(self):
        data = self.response.json()
        
        #verificar si la data no esta vacia
        self.assertGreater(len(data), 0, "No data")
        
        expected_fields = ["id", "name", "active"]
        
        #verificar que los campos requeridos si esten en la respuesta
        for field in expected_fields:
            self.assertIn(field, data[0])

        #verificar que los datos de la respuesta correspondan con el objeto creado para la prueba         
        for field in expected_fields:
            self.assertEqual(data[0][field], getattr(self.tag1, field))
            
        #verificar en db
        expected_fields = ["id", "name", "active"]
        
        tag = Tag.objects.get(id=self.tag1.id)
        
        for field in expected_fields:
            self.assertEqual(getattr(tag, field), getattr(self.tag1, field))
            
    def test_field_types(self):
        data = self.response.json()
        
        expected_fields = {
            "id":int,
            "name":str,
            "active":bool
        }
        #verificar que los tipos de campos de la respuesta sean los esperados
        for field, type in expected_fields.items():
            self.assertIsInstance(data[0][field], type)
    
#TEST GET DETAIL
class TagGetDetailAPITest(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(
            name = "Tag name",
            active = True
        )
        
        self.detail_url = reverse("myapp:tag-detail", kwargs={"id":self.tag1.id})
        self.response = self.client.get(self.detail_url)
        
    def test_status_code(self):
        #verificar si devuelve el codigo de estado correcto
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_response_structure(self):
        data = self.response.json()
        #verificar si la data no esta vacia
        self.assertGreater(len(data), 0, "No data")
        
        expected_fields = ["id", "name", "active"]
        
        #verificar que los campos requeridos si esten en la respuesta
        for field in expected_fields:
            self.assertIn(field, data)

        #verificar que los valores
        for field in expected_fields:
            self.assertEqual(data[field], getattr(self.tag1, field))
            
        #verificar en db
        expected_fields = ["id", "name", "active"]
        
        tag = Tag.objects.get(id=self.tag1.id)
        
        for field in expected_fields:
            self.assertEqual(getattr(tag, field), getattr(self.tag1, field))
            
    def test_field_types(self):
        data = self.response.json()
        
        expected_fields = {
            "id":int,
            "name":str,
            "active":bool
        }
        
        #verificar que los tipos de campos de la respuesta sean los esperados
        for field, type in expected_fields.items():
            self.assertIsInstance(data[field],type) 

#TEST POST
class TagPostAPITest(TestCase):
    def setUp(self):
        self.tag_post_data = {
            "name": "Tag name",
            "active": True
        }
        
        self.detail_url = reverse("myapp:tag-list-create")
        self.response = self.client.post(self.detail_url, self.tag_post_data, content_type="application/json")
        
    def test_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        
    def test_response_structure(self):
        data = self.response.json()
        # print(len(data))
        # print(data)
        
        #
        expected_fields = ["id", "name", "active"]
        
        for field in expected_fields:
            self.assertIn(field, data)
        
        #
        expected_fields = ["name", "active"]
        
        for field in expected_fields:
            self.assertEqual(data[field], self.tag_post_data[field])
            
        #
        tag = Tag.objects.get(name=self.tag_post_data["name"])
        
        for field in expected_fields:
            self.assertEqual(getattr(tag, field), self.tag_post_data[field])
            
    def test_field_types(self):
        data = self.response.json()
        
        field_types = {
            "id":int,
            "name": str,
            "active": bool
        }
        
        #        
        for field, type in field_types.items():
            self.assertIsInstance(data[field], type)
    
#TEST DELETE 
class TagDeleteAPITest(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(
            name = "Tag name",
            active = True
        )
        
        self.detail_url = reverse("myapp:tag-detail", kwargs={"id": self.tag1.id})
        self.response = self.client.delete(self.detail_url)
        
    def test_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_object_delete(self):
        self.assertFalse(Tag.objects.filter(id=self.tag1.id).exists())

#TEST PUT (actualizar pero se deben pasar todos los campos)
class TagPutAPITest(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(
            name = "Tag name",
            active = True    
        )
        
        self.tag_put_data = {
            "name": "xd",
            "active": False
        }
        
        self.detail_url = reverse("myapp:tag-detail", kwargs={"id": self.tag1.id})
        self.response = self.client.put(self.detail_url, self.tag_put_data, content_type="application/json")
        
    def test_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_response_structure(self):
        data = self.response.json()
        
        #
        expected_fields = ["id", "name", "active"]
        
        for field in expected_fields:
            self.assertIn(field, data)
            
        #
        expected_fields = ["name", "active"]
        for field in expected_fields:
            self.assertEqual(data[field], self.tag_put_data[field])
            
        #
        tag = Tag.objects.get(id=self.tag1.id)
        
        for field in expected_fields:
            self.assertEqual(getattr(tag, field), self.tag_put_data[field] )
            
    def test_fields_types(self):
        data = self.response.json()
        
        #verificar que los tipos de campos de la respuesta sean los esperados
        fields_types = {
            "id": int,
            "name": str,
            "active": bool,            
        }
        
        for field, type in fields_types.items():
            self.assertIsInstance(data[field], type)

#TEST METODO PATCH (actualizar pero solo se pasa el campo a modificar, puede variar dado como esten definidos los campos en el modelo)
class TagPatchAPITest(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(
            name = "Tag name",
            active = True   
        )
        
        self.tag_patch_data = { 
            "name":"xd"
        }
        
        self.detail_url = reverse("myapp:tag-detail", kwargs={"id": self.tag1.id})
        self.response = self.client.patch(self.detail_url, self.tag_patch_data, content_type="application/json")
        
    def test_status_code(self):
        #verificar si devuelve el codigo de estado correcto
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_response_structure(self):
        data = self.response.json()
        
        #verificar que los campos requeridos si esten en la respuesta
        expected_fields = ["id", "name", "active"]
        
        for field in expected_fields:
            self.assertIn(field, data)
           
        #verificar si el campo se modifico 
        self.assertEqual(data["name"], self.tag_patch_data["name"])
        
        #verificar si los campos que no se modificaron quedaron igual
        tag = Tag.objects.get(id=self.tag1.id)
        
        expected_data = ["id", "active"]
        
        for field in expected_data:
            self.assertEqual(data[field], getattr(tag, field))
                
    def test_field_types(self):
        data = self.response.json()
        
        #verificar que los tipos de campos de la respuesta sean los esperados
        field_types = {
            "id": int,
            "name": str,
            "active": bool, 
        }
        
        for field, type in field_types.items():
            self.assertIsInstance(data[field], type)