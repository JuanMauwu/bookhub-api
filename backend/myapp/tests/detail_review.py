from django.test import TestCase
from rest_framework import status 
from django.urls import reverse
from myapp.models import DetailReview

#TEST GET
class DetailReviewGetAPITest(TestCase):
    def setUp(self):
        self.detail_review1 = DetailReview.objects.create(
            pos_date = "2005-05-29",
            qualification = 10,
            comments = "Lorem ipsum dolor sit amet",
            active = True
        )
        
        self.detail_url = reverse("myapp:detail-review-list-create")
        self.response = self.client.get(self.detail_url, content_type="application/json")
     
    def test_status_code(self):
        #verificar si devuelve el codigo de estado correcto
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_response_structure(self):
        data = self.response.json()

        #verificar si la data no esta vacia
        self.assertGreater(len(data), 0, "No data")

        expected_fields = ["id", "pos_date", "qualification", "comments", "active"]

        #verificar que los campos requeridos si esten en la respuesta
        for field in expected_fields:
            self.assertIn(field, data[0])
        
        #verificar que los datos de la respuesta correspodan con el objeto creado para la prueba
        for field in expected_fields:
            self.assertEqual(data[0][field], getattr(self.detail_review1, field))
        
        #verificar en db
        expected_fields = ["id", "pos_date", "qualification", "comments", "active"]
        
        detail_review = DetailReview.objects.get(id=self.detail_review1.id)
        for field in expected_fields:
            if field == "pos_date":
                self.assertEqual(str(getattr(detail_review, field)), getattr(self.detail_review1, field))
            else:
                self.assertEqual(getattr(detail_review, field), getattr(self.detail_review1, field))
        
    def test_field_types(self):
        data = self.response.json()
        
        expected_types = {
            "id":int,
            "pos_date":str,
            "qualification":int,
            "comments":str,
            "active":bool,
        }
        
        #verificar que los tipos de campos de la respuesta sean los esperados
        for field, type in expected_types.items():
            self.assertIsInstance(data[0][field], type)

#TEST GET DETAIL
class DetailReviewGetDetailAPITest(TestCase):
    def setUp(self):
        self.detail_review1 = DetailReview.objects.create(
            pos_date = "2005-05-29",
            qualification = 10,
            comments = "Lorem ipsum dolor sit amet",
            active = True        
        )
        
        self.detail_url = reverse("myapp:detail-review-detail", kwargs={"id":self.detail_review1.id})
        self.response = self.client.get(self.detail_url, format ="json")
        
    def test_status_code(self):
        #verificar si devuelve el codigo de estado correcto
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_response_tructure(self):
        data = self.response.json()
        
        expected_fields = ["id", "pos_date", "qualification", "comments", "active"]
        
        #verificar que los campos requeridos si esten en la respuesta
        for field in expected_fields:
            self.assertIn(field, data)
        
        #verificar que los datos de la respuesta correspodan con el objeto creado para la prueba
        for field in expected_fields:
            self.assertEqual(data[field], getattr(self.detail_review1, field))
    
        #verificar en db
        expected_fields = ["id", "pos_date", "qualification", "comments", "active"]
        
        detail_review = DetailReview.objects.get(id=self.detail_review1.id)
        for field in expected_fields:
            if field == "pos_date":
                self.assertEqual(str(getattr(detail_review, field)), getattr(self.detail_review1, field))
            else:
                self.assertEqual(getattr(detail_review, field), getattr(self.detail_review1, field))
    
    def test_field_types(self):
        data = self.response.json()
        
        expected_types = {
            "id":int,
            "pos_date":str,
            "qualification":int,
            "comments":str,
            "active":bool,
        }
        
        #verificar que los tipos de campos de la respuesta sean los esperados
        for field, type in expected_types.items():
            self.assertIsInstance(data[field], type)

#TEST POST
class DetailReviewPostAPITest(TestCase):
    def setUp(self):
        self.detail_review_post_data = {
            "pos_date": "2005-05-29",
            "qualification": 10,
            "comments": "Lorem ipsum dolor sit amet",
            "active": True            
        }
        
        self.detail_url = reverse("myapp:detail-review-list-create")
        self.response = self.client.post(self.detail_url, self.detail_review_post_data, content_type="application/json")
        
    def test_status_code(self):
        #verificar si devuelve el codigo de estado correcto
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
    
    def test_response_structure(self):
        data = self.response.json()
        
        #verificar que los campos requeridos si esten en la respuesta
        expected_fields = ["id", "pos_date", "qualification", "comments","active"]
        
        for field in expected_fields:
            self.assertIn(field, data)
            
        #verificar que los datos de la respuesta correspodan con la data de la solicitud
        expected_fields = ["pos_date", "qualification", "comments","active"]
        
        for field in expected_fields:
            self.assertEqual(self.detail_review_post_data[field], data[field])
        
        #verificar que los datos del objeto en db correspondan con la data de la solicitud
        detail_review = DetailReview.objects.get(pos_date=self.detail_review_post_data["pos_date"])
        
        for field in expected_fields:
            if field == "pos_date":
                self.assertEqual(str(getattr(detail_review, field)), self.detail_review_post_data[field])
            else:
                self.assertEqual(getattr(detail_review, field), self.detail_review_post_data[field])
    
    def test_fields_types(self):
        data = self.response.json()
        
        fields_types = {
            "id": int,
            "pos_date": str,
            "qualification": int,
            "comments": str,
            "active": bool            
        }
        
        #verificar que los tipos de campos de la respuesta sean los esperados
        for field, type in fields_types.items():
            self.assertIsInstance(data[field], type)
      
#TEST DELETE
class DetailReviewDeleteAPITest(TestCase):
    def setUp(self):
        self.detail_review1 = DetailReview.objects.create(
            pos_date = "2005-05-29",
            qualification = 10,
            comments = "Lorem ipsum dolor sit amet",
            active = True
        )
        
        self.detail_url = reverse("myapp:detail-review-detail", kwargs={"id":self.detail_review1.id})
        self.response = self.client.delete(self.detail_url, content_type="application/json")
        
    def test_status_code(self):
        #verificar si devuelve el codigo de estado correcto
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_object_detele(self): 
        #verificar que el objeto no exista en la db
        self.assertFalse(DetailReview.objects.filter(id=self.detail_review1.id).exists()) 

#TEST PUT (actualizar pero se deben pasar todos los campos)
class DetailReviewPutAPITest(TestCase):
    def setUp(self):
        self.detail_review1 = DetailReview.objects.create(
            pos_date = "2005-05-29",
            qualification = 10,
            comments = "Lorem ipsum dolor sit amet",
            active = True             
        )
        
        self.detail_review_put_data = {
            "pos_date": "2004-05-29",
            "qualification": 5,
            "comments": "Lorem",
            "active": False
        }
        
        self.detail_url = reverse("myapp:detail-review-detail", kwargs={"id":self.detail_review1.id})
        self.response = self.client.put(self.detail_url, self.detail_review_put_data, content_type="application/json")
        
    def test_status_code(self):
        #verificar si devuelve el codigo de estado correcto
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_response_structure(self):
        data = self.response.json()
        
        #verificar que los campos requeridos si esten en la respuesta
        expected_fields = ["id", "pos_date", "qualification", "comments","active"]
        
        for field in expected_fields:
            self.assertIn(field, data)
        
        #verificar que los datos de la respuesta correspodan con la data de la solicitud
        expected_fields = ["pos_date", "qualification", "comments","active"]
        
        for field in expected_fields:
            self.assertEqual(data[field], self.detail_review_put_data[field])
        
        #verificar que los datos del objeto en db correspondan con la data de la solicitud
        detail_review = DetailReview.objects.get(id=self.detail_review1.id) 
        
        for field in expected_fields:
            if field == "pos_date":
                self.assertEqual(str(getattr(detail_review, field)), self.detail_review_put_data[field])
            else:
                self.assertEqual(getattr(detail_review, field), self.detail_review_put_data[field])
    
    def test_fields_types(self):
        data = self.response.json()
        
        fields_types = {
            "id": int,
            "pos_date": str,
            "qualification": int,
            "comments": str,
            "active": bool            
        }
        
        #verificar que los tipos de campos de la respuesta sean los esperados
        for field, type in fields_types.items():
            self.assertIsInstance(data[field], type)

#TEST METODO PATCH (actualizar pero solo se pasa el campo a modificar, puede variar dado como esten definidos los campos en el modelo)
class DetailReviewPatchAPITest(TestCase):
    def setUp(self):
        self.detai_review1 = DetailReview.objects.create(
            pos_date = "2005-05-29",
            qualification = 10,
            comments = "Lorem ipsum dolor sit amet",
            active = True   
        )
        
        self.detail_review_patch_data = { #en este modelo los campos pos_date y qualification son obligatorios, en esta prueba se modificara "comments"
            "pos_date": "2005-05-29",
            "qualification": 10,
            "comments": "Lorem",
        }
        
        self.detail_url = reverse("myapp:detail-review-detail", kwargs={"id": self.detai_review1.id})
        self.response = self.client.patch(self.detail_url, self.detail_review_patch_data, content_type="application/json")
        
    def test_status_code(self):
        #verificar si devuelve el codigo de estado correcto
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_response_structure(self):
        data = self.response.json()
        
        #verificar que los campos requeridos si esten en la respuesta
        expected_data = ["id", "pos_date", "qualification", "comments","active"]
        
        for field in expected_data:
            self.assertIn(field, data)
           
        #verificar si el campo se modifico 
        self.assertEqual(data["comments"], self.detail_review_patch_data["comments"])
        
        #verificar si los campos que no se modificaron quedaron igual
        detail_review = DetailReview.objects.get(id=self.detai_review1.id)
        
        expected_data = ["id", "pos_date", "qualification","active"]
        
        for field in expected_data:
            if field == "pos_date":
                self.assertEqual(data[field], str(getattr(detail_review, field)))
            else:
                self.assertEqual(data[field], getattr(detail_review, field))
                
    def test_field_types(self):
        data = self.response.json()
        
        field_types = {
            "id": int,
            "pos_date": str,
            "qualification": int,
            "comments": str,
            "active": bool
        }
        
        #verificar que los tipos de campos de la respuesta sean los esperados
        for field, type in field_types.items():
            self.assertIsInstance(data[field], type)