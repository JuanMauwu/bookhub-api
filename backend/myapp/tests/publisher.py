from django.test import TestCase
from rest_framework import status # type: ignore
from django.urls import reverse
from myapp.models import Publisher, Book
from decimal import Decimal

#TEST GET
class PublisherGetAPITest(TestCase):
    def setUp(self):        
        self.publisher1 = Publisher.objects.create(
            name="Example Publisher",
            founded="1990-05-15",
            website="https://www.examplepublisher.com",
            address={"street": "123 Main St", "city": "Booktown", "country": "USA"},
            active=True,
            email="contact@examplepublisher.com",
            revenue=Decimal("5000000.00")
        )
        
        self.book1 = Book.objects.create(
            title="The Catcher",
            author="J.D. Salinger",
            summary="A story about teenage rebellion.",
            pos_date="1951-07-16",
            active=True,
        )
        
        self.book2 = Book.objects.create(
            title="The",
            author="J.D.",
            summary="A story about teenage",
            pos_date="1951-07-14",
            active=True,
        )
        
        self.publisher1.books.add(self.book1, self.book2) #el metodo add() nos sirve para añadir relaciones manytomany entre campos
        
        self.detail_url = reverse("myapp:publisher-list-create")
        self.response = self.client.get(self.detail_url)
        
    def test_status_code(self):
        #
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        print(self.response.json())

    def test_response_structure(self):
        data = self.response.json() 
        
        #
        self.assertGreater(len(data), 0, "No data")
        
        #
        expected_fields = ["id", "name", "founded", "website", "books", "address", "active", "email", "revenue"]

        for field in expected_fields:
            self.assertIn(field, data[0])
            
        #
        expected_fields = ["name", "founded", "website", "address", "active", "email", "revenue"]
        
        for field in expected_fields:
            if field == "revenue":
                self.assertEqual(data[0][field], str(getattr(self.publisher1, field)))
            else:
                self.assertEqual(data[0][field], getattr(self.publisher1, field))
                
        #
        self.assertEqual(len(data[0]["books"]), self.publisher1.books.count()) #sabemmos que la respuesta en el campo nos devuelve una lista con los ids de los objetos relacionados [1,2]
                                                                               #metodo count() para contar los objetos relacionados 
                                                                               
        #
        expected_books = list(self.publisher1.books.values_list("id", flat=True)) #esta variable contendra una lista con los libros asociados a publisher
                                                                                  #values_list genera una lista de tuplas las cuales contendran las ids de los books
                                                                                  #usamos flat=True para aplanar la estructura y quitar las tuplas para que quede una lista normal
                                                                                  #list convierte el resultado(queryset) en una lista explicita 

        self.assertListEqual(data[0]["books"], expected_books) #y comparamos las listas
        
        #como extra verificamos que las claves del dict que devuelve el campo address si esten correctas
        address_expected_keys = ["street", "city", "country"]
        
        for key in address_expected_keys:
            self.assertIn(key, data[0]["address"])
        
    def test_field_types(self):
        data = self.response.json() 
        
        field_types = {
            "id":int,
            "name":str,
            "founded":str,
            "website":str,
            "books":list,
            "address":dict,
            "active":bool,
            "email":str,
            "revenue":str
        }
        #
        for field, type in field_types.items():
            self.assertIsInstance(data[0][field], type)
            
#TEST GET DETAIL
class PublisherGetDetailAPITest(TestCase):
    def setUp(self):
        self.publisher1 = Publisher.objects.create(
            name="Example Publisher",
            founded="1990-05-15",
            website="https://www.examplepublisher.com",
            address={"street": "123 Main St", "city": "Booktown", "country": "USA"},
            active=True,
            email="contact@examplepublisher.com",
            revenue=Decimal("5000000.00")
        )
        
        self.book1 = Book.objects.create(
            title="The Catcher",
            author="J.D. Salinger",
            summary="A story about teenage rebellion.",
            pos_date="1951-07-16",
            active=True,
        )
        
        self.book2 = Book.objects.create(
            title="The",
            author="J.D.",
            summary="A story about teenage",
            pos_date="1951-07-14",
            active=True,
        )
        
        self.publisher1.books.add(self.book1, self.book2)
        
        self.detail_url = reverse("myapp:publisher-detail", kwargs={"id":self.publisher1.id})
        self.response = self.client.get(self.detail_url)
        
    def test_status_code(self):
        #print(self.response.json())
        #
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_response_structure(self):
        data = self.response.json()
        
        #
        expected_fields = ["id", "name", "founded", "website", "books", "address", "active", "email", "revenue"]

        for field in expected_fields:
            self.assertIn(field, data)
            
        #
        expected_fields = ["name", "founded", "website", "address", "active", "email", "revenue"]
        
        for field in expected_fields:
            if field == "revenue":
                self.assertEqual(data[field], str(getattr(self.publisher1, field)))
            else:
                self.assertEqual(data[field], getattr(self.publisher1, field))
                
        #
        self.assertEqual(len(data["books"]), self.publisher1.books.count())
        
        #
        expected_books = list(self.publisher1.books.values_list("id", flat=True))
        
        self.assertEqual(data["books"], expected_books)
        
        #
        address_expected_keys = ["street", "city", "country"]
        
        for key in address_expected_keys:
            self.assertIn(key, data["address"])
            
    def test_field_types(self):
        data = self.response.json()
        
        field_types = {
            "id":int,
            "name":str,
            "founded":str,
            "website":str,
            "books":list,
            "address":dict,
            "active":bool,
            "email":str,
            "revenue":str
        }
        #
        for field, type in field_types.items():  
            self.assertIsInstance(data[field], type)
            
#TEST POST
class PublisherPostAPITest(TestCase):
    def setUp(self):
        self.book1 = Book.objects.create(
            title="The Catcher",
            author="J.D. Salinger",
            summary="A story about teenage rebellion.",
            pos_date="1951-07-16",
            active=True,         
        )
        
        self.book2 = Book.objects.create(
            title="The",
            author="J.D.",
            summary="A story about teenage",
            pos_date="1951-07-14",
            active=True,
        )
        
        self.publisher_post_data = {
            "name": "New Publisher",
            "founded": "2000-01-01",
            "website": "https://www.newpublisher.com",
            "books": [self.book1.id, self.book2.id],
            "address": {"street": "456 Second St", "city": "Readville", "country": "USA"},
            "active": True,
            "email": "contact@newpublisher.com",
            "revenue": "3000000.00"
        }
        
        self.detail_url = reverse("myapp:publisher-list-create")
        self.response = self.client.post(self.detail_url, self.publisher_post_data, content_type="application/json")
        
    def test_status_code(self):
        #
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        
    def test_response_structure(self):
        data = self.response.json()
        
        #
        expected_fields = ["id", "name", "founded", "website", "books", "address", "active", "email", "revenue"]
        
        for field in expected_fields:
            self.assertIn(field, data)
            
        #
        expected_fields = ["name", "founded", "website", "books", "address", "active", "email", "revenue"]
        
        for field in expected_fields:
            self.assertEqual(data[field], self.publisher_post_data[field])
            
        #
        publisher = Publisher.objects.get(id=data["id"])
        
        expected_books = list(publisher.books.values_list("id", flat=True))
        
        self.assertEqual(data["books"], expected_books)
        
        #
        expected_fields = ["name", "founded", "website", "address", "active", "email", "revenue"]
        
        for field in expected_fields:
            if field == "founded" or field == "revenue" :
                self.assertEqual(str(getattr(publisher, field)), self.publisher_post_data[field])
            else:
                self.assertEqual(getattr(publisher, field), self.publisher_post_data[field])
                
        #
        address_expected_keys = ["street", "city", "country"]         
        for key in address_expected_keys:
            self.assertIn(key, data["address"])       

    def test_field_types(self):
        data = self.response.json()
        
        #
        field_types = {
            "id":int,
            "name":str,
            "founded":str,
            "website":str,
            "books":list,
            "address":dict,
            "active":bool,
            "email":str,
            "revenue":str
        }
        
        for field, type in field_types.items():
            self.assertIsInstance(data[field], type)
            
#TEST DELETE 
class PublisherDeleteAPITest(TestCase):
    def setUp(self):
        self.publisher1 = Publisher.objects.create(
            name="Example Publisher",
            founded="1990-05-15",
            website="https://www.examplepublisher.com",
            address={"street": "123 Main St", "city": "Booktown", "country": "USA"},
            active=True,
            email="contact@examplepublisher.com",
            revenue=Decimal("5000000.00")
        )        
        
        self.book1 = Book.objects.create(
            title="The Catcher",
            author="J.D. Salinger",
            summary="A story about teenage rebellion.",
            pos_date="1951-07-16",
            active=True,
        )
        
        self.book2 = Book.objects.create(
            title="The",
            author="J.D.",
            summary="A story about teenage",
            pos_date="1951-07-14",
            active=True,
        )
        
        self.publisher1.books.add(self.book1, self.book2)
        
        self.detail_url = reverse("myapp:publisher-detail", kwargs={"id":self.publisher1.id})
        self.response = self.client.delete(self.detail_url)
        
    def test_response_status(self):
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)
        #print(self.publisher1.id)
        
    def test_object_delete(self):
        self.assertFalse(Publisher.objects.filter(id=self.publisher1.id).exists())
        
#TEST PUT (actualizar pero se deben pasar todos los campos)
class PublisherPutAPITest(TestCase):
    def setUp(self):
        self.publisher1 = Publisher.objects.create(
            name="Example Publisher",
            founded="1990-05-15",
            website="https://www.examplepublisher.com",
            address={"street": "123 Main St", "city": "Booktown", "country": "USA"},
            active=True,
            email="contact@examplepublisher.com",
            revenue=Decimal("5000000.00")  
        )
        
        self.book1 = Book.objects.create(
            title="The Catcher",
            author="J.D. Salinger",
            summary="A story about teenage rebellion.",
            pos_date="1951-07-16",
            active=True,
        )
        
        self.book2 = Book.objects.create(
            title="The",
            author="J.D.",
            summary="A story about teenage",
            pos_date="1951-07-14",
            active=True,
        )
        
        self.publisher_put_data = {
            "name": "Publisher",
            "founded": "2000-02-01",
            "website": "https://www.new.com",
            "books": [self.book1.id],
            "address": {"street": "1 Second St", "city": "Ville", "country": "Mexico"},
            "active": False,
            "email": "contact@new.com",
            "revenue": "3000000.00"
        }
        
        self.publisher1.books.add(self.book1, self.book2)
        
        self.detail_url = reverse("myapp:publisher-detail", kwargs={"id": self.publisher1.id})
        self.response = self.client.put(self.detail_url, self.publisher_put_data, content_type="application/json")
        
    def test_response_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_response_structure(self):
        data = self.response.json()
        
        #
        expected_fields = ["id", "name", "founded", "website", "books", "address", "active", "email", "revenue"]
        
        for field in expected_fields:
            self.assertIn(field, data)
        
        #
        expected_fields = ["name", "founded", "website", "address", "active", "email", "revenue"]
        
        for field in expected_fields:
            self.assertEqual(data[field], self.publisher_put_data[field])
            
        #
        publisher = Publisher.objects.get(id = self.publisher1.id)
        
        for field in expected_fields:
            if field == "founded" or field == "revenue":
                self.assertEqual(str(getattr(publisher, field)), self.publisher_put_data[field])
            else:
                self.assertEqual(getattr(publisher, field), self.publisher_put_data[field])
                
        #
        expected_books = self.publisher_put_data["books"]
        actual_books = list(publisher.books.values_list("id", flat=True))
        
        self.assertEqual(expected_books, actual_books)
        
        #verificar que el titulo del libro asociado al modelo sea el esperado
        book_title = list(publisher.books.values_list("title", flat=True))
        self.assertEqual(["The Catcher"], book_title)
        
        #verificar que las claves del campo address existanb en la respuesta
        address_expected_keys = ["street", "city", "country"]
        for field in address_expected_keys:
            self.assertIn(field, data["address"])
            
    def test_field_types(self):
        data = self.response.json()
        
        #
        field_types = {
            "id":int,
            "name":str,
            "founded":str,
            "website":str,
            "books":list,
            "address":dict,
            "active":bool,
            "email":str,
            "revenue":str
        }
        
        for field, type in field_types.items():
            self.assertIsInstance(data[field], type)
            
#TEST METODO PATCH (actualizar pero solo se pasa el campo a modificar, puede variar dado como esten definidos los campos en el modelo)
class PublisherPatchAPITest(TestCase):
    def setUp(self):
        self.publisher1 = Publisher.objects.create(
            name="Example Publisher",
            founded="1990-05-15",
            website="https://www.examplepublisher.com",
            address={"street": "123 Main St", "city": "Booktown", "country": "USA"},
            active=True,
            email="contact@examplepublisher.com",
            revenue=Decimal("5000000.00")
        )
        
        self.book1 = Book.objects.create(
            title="The Catcher",
            author="J.D. Salinger",
            summary="A story about teenage rebellion.",
            pos_date="1951-07-16",
            active=True,
        )
        
        self.book2 = Book.objects.create(
            title="The",
            author="J.D.",
            summary="A story about teenage",
            pos_date="1951-07-14",
            active=True,
        )
        
        self.publisher1.books.add(self.book1, self.book2)
        
        self.publisher_patch_data = { #segun definicion de nuestro modelo todos los campos son obligatorios, solo se cambio el dato del campo "name"
            "name":"Example",
            "founded":"1990-05-15",
            "website":"https://www.examplepublisher.com",
            "address":{"street": "123 Main St", "city": "Booktown", "country": "USA"},
            "active":True,
            "email":"contact@examplepublisher.com",
            "revenue":Decimal("5000000.00"),
            "books":[self.book1.id, self.book2.id]
        }
        
        self.detail_url = reverse("myapp:publisher-detail", kwargs={"id":self.publisher1.id})
        self.response = self.client.patch(self.detail_url, self.publisher_patch_data, content_type="application/json")
        
    def test_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_response_structure(self):
        data = self.response.json()
        
        #
        expected_fields = ["id", "name", "founded", "website", "books", "address", "active", "email", "revenue"]
        
        for field in expected_fields:
            self.assertIn(field, data)
            
        #verificar si el cmapo se modifico
        self.assertEqual(data["name"], self.publisher_patch_data["name"])
        
        #verificar si los campos que no se modificaron quedaron igual
        publlisher = Publisher.objects.get(id=self.publisher1.id)
        
        expected_data = ["id","founded", "website", "address", "active", "email", "revenue"]
        
        for field in expected_data:
            if field == "founded" or field == "revenue":
                self.assertEqual(data[field], str(getattr(publlisher, field)))
            else:
                self.assertEqual(data[field], getattr(publlisher, field))
                
        #comparamos los datos del campo "books"
        actual_books = list(self.publisher1.books.values_list("id", flat=True))
        
        self.assertEqual(actual_books, data["books"])
        
        #
        address_expected_keys = ["street", "city", "country"]
        
        for field in address_expected_keys:
            self.assertIn(field, data["address"])
            
    def test_field_types(self):
        data = self.response.json()
        
        field_types = {
           "id":int,
            "name":str,
            "founded":str,
            "website":str,
            "books":list,
            "address":dict,
            "active":bool,
            "email":str,
            "revenue":str
        }
        
        for field, type in field_types.items():
            self.assertIsInstance(data[field], type)