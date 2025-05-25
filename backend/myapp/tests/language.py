from rest_framework.test import APIClient
from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from myapp.models import Language

#TEST GET
class LanguageGetAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        self.language1 = Language.objects.create(
            name = "Ingles",
            code = "es",
            flag = SimpleUploadedFile("flag.jpg", b"", content_type="image/jpeg"),
            active = True
        )
        
        self.detail_url = reverse("myapp:language-list-create")
        self.response = self.client.get(self.detail_url)
        
    def test_status_code(self):
        #verificar si devuelve el codigo de estado correcto
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_response_structure(self):
        data = self.response.json()
        
        #verificar si la data no esta vacia
        self.assertGreater(len(data), 0)
        
        #verificar que los campos requeridos si esten en la respuesta
        for field in ["name", "code", "flag", "active"]:
            self.assertIn(field, data[0])
            
        #verificar que los datos de la respuesta correspodan con el objeto creado para la prueba
        for field in ["name", "code", "flag", "active"]:
            if field == "flag":
                #como la respuesta "data" devuelve la URL completa, se quita la parte en replace() para poder comparar con lo que obtenemos de "language1.flag.url"
                self.assertEqual(data[0][field].replace("http://testserver", ""), self.language1.flag.url) 
            else:
                self.assertEqual(data[0][field], getattr(self.language1, field))
                
        #verificar en db
        language = Language.objects.get(id=self.language1.id)
        
        for field in ["name", "code", "flag", "active"]:
            if field == "flag":
                self.assertEqual(language.flag.url, self.language1.flag.url)
            else:
                self.assertEqual(getattr(language, field), getattr(self.language1, field))
                
    def test_field_types(self):
        data = self.response.json()
        
        #verificar que los tipos de campos de la respuesta sean los esperados
        for field, type in {"name":str, "code":str, "flag":str, "active":bool}.items():
            self.assertIsInstance(data[0][field], type)
        
#TEST GET DETAIL
class LanguageGetDetailAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        self.language1 = Language.objects.create(
            name = "Ingles",
            code = "es",
            flag = SimpleUploadedFile("flag.jpg", b"", content_type="image/jpeg"),
            active = True
        )
        
        self.detail_url = reverse("myapp:language-detail", kwargs={"id":self.language1.id})
        self.response = self.client.get(self.detail_url)
        
    def test_status_code(self):
        #verificar si devuelve el codigo de estado correcto
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_response_status(self):
        data = self.response.json()
        
        #verificar que los campos requeridos si esten en la respuesta
        for field in ["name", "code", "flag", "active"]:
            self.assertIn(field, data)

        #verificar que los datos de la respuesta correspodan con el objeto creado para la prueba
        for field in ["name", "code", "flag", "active"]:
            if field == "flag":
                self.assertEqual(data[field].replace("http://testserver", ""), self.language1.flag.url)
            else:
                self.assertEqual(data[field], getattr(self.language1, field))
        
        #verificar en db
        language = Language.objects.get(id=self.language1.id)

        for field in ["name", "code", "flag", "active"]:
            if field == "flag":
                self.assertEqual(language.flag.url, self.language1.flag.url)
            else:
                self.assertEqual(getattr(language, field), getattr(self.language1, field))
    
    def test_field_types(self):
        data = self.response.json()
        
        for field, type in {"name":str, "code":str, "flag":str, "active":bool}.items():
            self.assertIsInstance(data[field], type)
        
#TEST POST
class LanguagePostAPITest(TestCase):
    def setUp(self):  
        self.client = APIClient()
        
        #archivo de 1x1 pixel con la estructura completa de un Gif
        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )
        
        self.language_post_data = {
            "name": "Ingles",
            "code": "es",
            "flag": SimpleUploadedFile(name="flag.gif", content=small_gif, content_type="image/gif"),
            "active": True
        }
        
        self.detail_url = reverse("myapp:language-list-create")
        self.response = self.client.post(self.detail_url, self.language_post_data)
        
    def test_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        
    def test_response_structure(self):
        data = self.response.json()
        
        #verificar que los campos requeridos si esten en la respuesta
        for field in ["name", "code", "flag", "active"]:
            self.assertIn(field, data)
    
        #verificar que los datos de la respuesta correspodan con la data de la solicitud
        for field in ["name", "code", "flag", "active"]:
            if field == "flag":
                self.assertTrue(data[field].endswith(".gif"))
            else:
                self.assertEqual(data[field], self.language_post_data[field])
                
        #verificar que los datos del objeto en db correspondan con la data de la solicitud
        language = Language.objects.get(name=self.language_post_data["name"])
        
        print(language.flag.name)
        
        for field in ["name", "code", "flag", "active"]:
            if field == "flag":
                self.assertTrue(language.flag.name.endswith(".gif"))
            else:
                self.assertEqual(getattr(language, field), self.language_post_data[field])
                
    def test_field_types(self):
        data = self.response.json()
        
        for field, type in {"name":str, "code":str, "flag":str, "active":bool}.items():
            self.assertIsInstance(data[field], type)
    
#TEST DELETE
class LanguageDeleteAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        self.language1 = Language.objects.create(
            name = "Español",
            code = "es",
            flag = SimpleUploadedFile(name="flag.gif", content=b"", content_type="image/gif"), 
            active = True
        )
    
        self.detail_url = reverse("myapp:language-detail", kwargs={"id":self.language1.id})
        self.response = self.client.delete(self.detail_url)
        
    def test_status_code(self):
        #verificar si devuelve el codigo de estado correcto
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_objects_delete(self):
        #verificar que el objeto no exista en la db
        self.assertFalse(Language.objects.filter(id=self.language1.id).exists())
        
#TEST PUT
class LanguagePutAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )
        
        self.language1 = Language.objects.create(
            name = "Español",
            code = "es",
            flag = SimpleUploadedFile(name="flag.gif", content=small_gif, content_type="image/gif"), 
            active = True
        )
      
        self.language_put_data = {
            "name": "Ingles",
            "code": "es",
            "flag": SimpleUploadedFile(name="flag.gif", content=small_gif, content_type="image/gif"),
            "active": True
        }
        
        self.detail_url = reverse("myapp:language-detail", kwargs={"id":self.language1.id})
        self.response = self.client.put(self.detail_url, self.language_put_data, format="multipart")
        
    def test_status_code(self):
        print(self.response.json())
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_response_structure(self):
        data = self.response.json()
        
        #verificar que los campos requeridos si esten en la respuesta
        expected_fields = ["id", "name", "code", "flag","active"]
        
        for field in expected_fields:
            self.assertIn(field, data)
            
        #verificar que los datos de la respuesta correspodan con la data de la solicitud
        expected_fields = ["name", "code", "flag","active"]
        
        for field in expected_fields:
            if field == "flag":
                self.assertTrue(data[field].endswith(".gif"))
            else:  
                self.assertEqual(data[field], self.language_put_data[field])
    
        #verificar que los datos del objeto en db correspondan con la data de la solicitud
        language = Language.objects.get(id=self.language1.id)
        
        for field in expected_fields:
            if field == "flag":
                self.assertTrue(data[field].endswith(".gif"))
            else:
                self.assertEqual(getattr(language, field), self.language_put_data[field])
                
    def test_fields_type(self):
        data = self.response.json()        

        for field, type in {"name":str, "code":str, "flag":str, "active":bool}.items():
            self.assertIsInstance(data[field], type)

        
    
#TEST METODO PATCH
class LanguagePatchAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )
        
        self.language1 = Language.objects.create(
            name = "Español",
            code = "es",
            flag = SimpleUploadedFile(name="flag.gif", content=small_gif, content_type="image/gif"), 
            active = True
        )
        
        self.language_patch_data = {
            "name": "Ingles",
            "code": "es",
            "flag": SimpleUploadedFile(name="flag.gif", content=small_gif, content_type="image/gif"),
            "active": True
        }
        
        self.detail_url = reverse("myapp:language-detail", kwargs={"id":self.language1.id})
        self.response = self.client.patch(self.detail_url, self.language_patch_data, format="multipart")
        
    def test_status_code(self):
        #verificar si devuelve el codigo de estado correcto
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_response_structure(self):
        data = self.response.json()
        
        #verificar que los campos requeridos si esten en la respuesta
        expected_fields = ["id", "name", "code", "flag","active"]
        
        for field in expected_fields:
            self.assertIn(field, data)
            
        #verificar que los datos de la respuesta correspodan con la data de la solicitud
        expected_fields = ["name", "code", "flag","active"]
        
        for field in expected_fields:
            if field == "flag":
                self.assertTrue(data[field].endswith(".gif"))
            else:  
                self.assertEqual(data[field], self.language_patch_data[field])
    
        #verificar que los datos del objeto en db correspondan con la data de la solicitud
        language = Language.objects.get(id=self.language1.id)
        
        for field in expected_fields:
            if field == "flag":
                self.assertTrue(data[field].endswith(".gif"))
            else:
                self.assertEqual(getattr(language, field), self.language_patch_data[field])
                
    def test_fields_type(self):
        data = self.response.json()        

        for field, type in {"name":str, "code":str, "flag":str, "active":bool}.items():
            self.assertIsInstance(data[field], type)