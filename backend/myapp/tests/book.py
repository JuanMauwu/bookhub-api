from django.test import TestCase
from rest_framework import status # type: ignore
from django.urls import reverse
from myapp.models import Book


#TEST GET
class BookGetAPITest(TestCase): 
    
    def setUp(self):
        self.book1 = Book.objects.create( #.objects es el manager usado en django para interactuar con la db, permite hacer consultas y operar con los registros de cada modelo propiamente
            title="The Catcher",          #con el manager podemos usar operaciondes CRUD (Create, Read, Update, Delete) con los modelos. create() es uno de estos metodos
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
        
        self.detail_url = reverse("myapp:book-list-create")
        self.response = self.client.get(self.detail_url, format="json") #tener en cuenta que el self.client se usa para simular un cliente web que interactua con la API  
        
    def test_status_code(self):
        """Comprueba que el endpoint devuelva un código de estado 200"""
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_response_structure(self):
        data = self.response.json()
     
        self.assertGreater(len(data), 0, "No data")  #comprobar que la lista no este vacia        
        
        expected_fields = ["id", "title", "author", "summary", "pos_date", "active"]
        
        for field in expected_fields:
            self.assertIn(field, data[0])  #assertin: verificar que la calve "id" este dentro del diccionario
        
        # self.assertIn("id", data[0]) 
        # self.assertIn("title", data[0])
        # self.assertIn("author", data[0])
        # self.assertIn("summary", data[0])
        # self.assertIn("pos_date", data[0])
        # self.assertIn("active", data[0]) getattr
         
        for field in expected_fields:                                    
            self.assertEqual(data[0][field], getattr(self.book1, field)) #funcion getattr, buscamos en este caso la clave field dentro de self.book1
        
        # self.assertEqual(data[0]["id"], self.book1.id) 
        # self.assertEqual(data[0]["title"], self.book1.title)
        # self.assertEqual(data[0]["author"], self.book1.author)
        # self.assertEqual(data[0]["summary"], self.book1.summary)
        # self.assertEqual(data[0]["pos_date"], self.book1.pos_date)
        # self.assertEqual(data[0]["active"], self.book1.active)
    
    def test_field_types(self):
        data = self.response.json()
        
        self.assertGreater(len(data), 0, "No data")
       
        field_types = {
            "id":int,
            "title":str,
            "author":str,
            "summary":str,
            "pos_date":str,
            "active":bool,
        }
        
        for field, type in field_types.items():
            self.assertIsInstance(data[0][field], type)
       
        # self.assertIsInstance(data[0]["id"], int)
        # self.assertIsInstance(data[0]["title"], str)
        # self.assertIsInstance(data[0]["author"], str)
        # self.assertIsInstance(data[0]["summary"], str)
        # self.assertIsInstance(data[0]["pos_date"], str)
        # self.assertIsInstance(data[0]["active"], bool)
            
#TEST GET DETAIL (detalles del Get)
class BookGetDetailApiTest(TestCase):
    
    def setUp(self):
        
        #crear el libro en la db de prueba
        self.book1 = Book.objects.create(
            title="The Catcher",
            author="J.D. Salinger",
            summary="A story about teenage rebellion.",
            pos_date="1951-07-16",
            active=True,            
        )
        
        self.detail_url = reverse("myapp:book-detail",kwargs = {"id": self.book1.id}) #obtiene/construye la URL para el endpoint y asi poderlo usar abajo
        self.response = self.client.get(self.detail_url, format="json") #hace la solicitud get al endpoint anteriormente conseguido
        
    def test_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_response_structure(self):
        data = self.response.json()             #recordar que en caso de los detalles no devuelve una lista de dict, solo devuelve un dict
        #print(data)
        
        expected_fields = ["id", "title", "author", "summary", "pos_date", "active"]
        
        for field in expected_fields:
            self.assertIn(field, data)
        
        # self.assertIn("id", data)  
        # self.assertIn("title", data)
        # self.assertIn("author", data)
        # self.assertIn("summary", data)
        # self.assertIn("pos_date", data)
        # self.assertIn("active", data)
        
        for field in expected_fields:
            self.assertEqual(data[field], getattr(self.book1, field))
        
        # self.assertEqual(data["id"], self.book1.id)
        # self.assertEqual(data["title"], self.book1.title)
        # self.assertEqual(data["author"], self.book1.author)
        # self.assertEqual(data["summary"], self.book1.summary)
        # self.assertEqual(data["pos_date"], self.book1.pos_date)
        # self.assertEqual(data["active"], self.book1.active)
        
    def test_field_type(self):
        data = self.response.json()
        
        field_types = {
            "id":int,
            "title":str,
            "author":str,
            "summary":str,
            "pos_date":str,
            "active":bool,
        }
        
        for field, type in field_types.items():  
            self.assertIsInstance(data[field], type) 
    
        # self.assertIsInstance(data["id"], int)
        # self.assertIsInstance(data["title"], str)
        # self.assertIsInstance(data["author"], str)
        # self.assertIsInstance(data["summary"], str)
        # self.assertIsInstance(data["pos_date"], str)
        # self.assertIsInstance(data["active"], bool)
                    
#TEST POST
class BookPostAPITest(TestCase):

    def setUp(self):

        self.post_book_data = {
            "title": "El tunel",
            "author": "Pepito",
            "summary": "ooo",
            "pos_date": "2023-10-26",
            "active": True
        }
        
        self.url_book = reverse("myapp:book-list-create")
        self.response = self.client.post(self.url_book, self.post_book_data, format="json")

    def test_status_code(self):    
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
      
    def test_response_structure(self):
        data = self.response.json()
        
        expected_fields = ["id", "title", "author", "summary", "pos_date", "active"]
        
        for field in expected_fields:
            self.assertIn(field, data)
        
        # self.assertIn("id", data)
        # self.assertIn("title", data)
        # self.assertIn("author", data)
        # self.assertIn("summary", data)
        # self.assertIn("pos_date", data)
        # self.assertIn("active", data)
        
        expected_fields = ["title", "author", "summary", "pos_date", "active"] #en estecaso no comparamos el id ya que no se encuentra en post book data
        # Compara los datos enviados con los datos devueltos
        for field in expected_fields:
            self.assertEqual(self.post_book_data[field], data[field])
        
        # self.assertEqual(self.post_book_data["title"], data["title"])
        # self.assertEqual(self.post_book_data["author"], data["author"])
        # self.assertEqual(self.post_book_data["summary"], data["summary"])
        # self.assertEqual(self.post_book_data["pos_date"], data["pos_date"])
        # self.assertEqual(self.post_book_data["active"], data["active"])
        
        # Verifica que el libro ha sido creado en la base de datos
        expected_fields = ["title", "author", "summary", "pos_date", "active"]
        book = Book.objects.get(title=self.post_book_data["title"])
        
        for field in expected_fields:
            if field == "pos_date":  
                self.assertEqual(str(getattr(book, field)), self.post_book_data[field])
            else:
                self.assertEqual(getattr(book, field), self.post_book_data[field])
        
        # self.assertEqual(book.title, self.post_book_data["title"])
        # self.assertEqual(book.author, self.post_book_data["author"])
        # self.assertEqual(book.summary, self.post_book_data["summary"])
        # self.assertEqual(str(book.pos_date), self.post_book_data["pos_date"])
        # self.assertEqual(book.active, self.post_book_data["active"])
        
    def test_fields_types(self):
        data = self.response.json()
        # Verifica los tipos de datos
        
        field_types = {
            "id":int,
            "title":str,
            "author":str,
            "summary":str,
            "pos_date":str,
            "active":bool,
        }
        
        for field, type in field_types.items():
            self.assertIsInstance(data[field], type)
        
        # self.assertIsInstance(data["title"], str)
        # self.assertIsInstance(data["author"], str)
        # self.assertIsInstance(data["summary"], str)
        # self.assertIsInstance(data["pos_date"], str)
        # self.assertIsInstance(data["active"], bool)
 
#TEST METODO DELETE       
class BookDeleteAPITest(TestCase):
    def setUp(self):
        self.book1 = Book.objects.create(
            title="The Catcher",
            author="J.D. Salinger",
            summary="A story about teenage rebellion.",
            pos_date="1951-07-16",
            active=True,         
        )
        
        self.detail_url = reverse("myapp:book-detail", kwargs={"id":self.book1.id})
        self.response = self.client.delete(self.detail_url, format="json")
        
    def test_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_object_deleted(self):
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())
            
#METODO PUT (actualizar pero se deben pasar todos los campos)
class BookPutAPITest(TestCase):
    def setUp(self):
         
        self.book1 = Book.objects.create(
            title="The Catcher",
            author="J.D. Salinger",
            summary="A story about teenage rebellion.",
            pos_date="1951-07-16",
            active=True, 
        )
        
        self.put_book_data = {
            "title":"The",
            "author":"J.D.",
            "summary":"A story",
            "pos_date":"2000-07-16",
            "active":False,            
        }
        
        self.detail_url = reverse("myapp:book-detail", kwargs={"id":self.book1.id})
        self.response = self.client.put(self.detail_url, self.put_book_data, content_type="application/json") #revisar(diferencia en content type)
        
    def test_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_response_structure(self):
        data = self.response.json()

        expected_fields = ["id", "title", "author", "summary", "pos_date", "active"]
        
        for field in expected_fields:
            self.assertIn(field, data)
        
        # self.assertIn("id", data)
        # self.assertIn("title", data)
        # self.assertIn("author", data)
        # self.assertIn("summary", data)
        # self.assertIn("pos_date", data)
        # self.assertIn("active", data)
        
        #que la respuesta sea lo que se modifico
        
        expected_fields = ["title", "author", "summary", "pos_date", "active"]
        
        for field in expected_fields:
            self.assertEqual(data[field], self.put_book_data[field])
        
        # self.assertEqual(data["title"], self.put_book_data["title"])
        # self.assertEqual(data["author"], self.put_book_data["author"])
        # self.assertEqual(data["summary"], self.put_book_data["summary"])
        # self.assertEqual(data["pos_date"], self.put_book_data["pos_date"])
        # self.assertEqual(data["active"], self.put_book_data["active"])
        
        #verificar cambio en db
        update_book = Book.objects.get(id=self.book1.id) #objects.get para oobtener un objeto de la db
        
        for field in expected_fields:
            if field == "pos_date":
                self.assertEqual(str(getattr(update_book, field)), self.put_book_data[field])
            else: 
                self.assertEqual(getattr(update_book, field), self.put_book_data[field])
            
        # self.assertEqual(update_book.title, self.put_book_data["title"]) notar en este caso como accedemos al dato title(estamos accediendo directamente al modelo)
        # self.assertEqual(update_book.author, self.put_book_data["author"])
        # self.assertEqual(update_book.summary, self.put_book_data["summary"])
        # self.assertEqual(str(update_book.pos_date), self.put_book_data["pos_date"]) recordar el tipo de este campo, pos_date = models.DateField(), esto genera problema al compararlo con una cadena
        # self.assertEqual(update_book.active, self.put_book_data["active"])
        
    def test_field_types(self):
        data = self.response.json()
        
        field_types = {
            "id":int,
            "title":str,
            "author":str,
            "summary":str,
            "pos_date":str,
            "active":bool,
        }
        
        for field, type in field_types.items():
            self.assertIsInstance(data[field], type)
        
        # self.assertIsInstance(data["title"], str)
        # self.assertIsInstance(data["author"], str)
        # self.assertIsInstance(data["summary"], str)
        # self.assertIsInstance(data["pos_date"], str)
        # self.assertIsInstance(data["active"], bool)

#TEST METODO PATCH (actualizar pero solo se pasa el campo a modificar, puede variar dado como esten definidos los campos en el modelo)
class BookPatchAPITest(TestCase):
    def setUp(self):
        
        self.post_book_data = {
            "title": "El tunel",
            "author": "Pepito",
            "summary": "ooo",
            "pos_date": "2023-10-26",
            "active": True            
        }
        
        self.patch_book_data = {         #se modificara el titulo
            "title": "El",               #segun el planteamiento del modelo es obligatorio poner la info para title, author y pos_date
            "author": "Pepito",
            "pos_date": "2023-10-26",            
        }
        
        #primero hacemos una solicitud post apra crear un libro en al db (otra forma)
        self.post_detail_url = reverse("myapp:book-list-create")
        self.post_response = self.client.post(self.post_detail_url, self.post_book_data, format="json")
        
        
        #segundo hacemos la solicitud del metodo patch con el objeto anteriormente creado
        self.detail_url = reverse("myapp:book-detail", kwargs={"id":self.post_response.json().get("id")}) #aqui usamos el metodo de los dic para obtener un valor o podemos usar #self.post_response.json()["id"]
        self.response = self.client.patch(self.detail_url, self.patch_book_data, content_type="application/json")
        
    def test_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_response_structure(self):
        data = self.response.json()
        #print(data)
        
        expected_fields = ["id", "title", "author", "summary", "pos_date", "active"]
        
        for field in expected_fields:
            self.assertIn(field, data)
        
        # self.assertIn("id", data)
        # self.assertIn("title", data)
        # self.assertIn("author", data)
        # self.assertIn("summary", data)
        # self.assertIn("pos_date", data)
        # self.assertIn("active", data)
        
        #verificar que el cambio si se haya efectuado
        self.assertEqual(data["title"], self.patch_book_data["title"])
        
        #verificar que el resto de campos no se hayan modificado
        
        expected_fields = ["author", "summary", "pos_date", "active"]
        
        for field in expected_fields:
            self.assertEqual(data[field], self.post_book_data[field])
        
        # self.assertEqual(data["author"], self.post_book_data["author"])
        # self.assertEqual(data["summary"], self.post_book_data["summary"])
        # self.assertEqual(data["pos_date"], self.post_book_data["pos_date"])
        # self.assertEqual(data["active"], self.post_book_data["active"])
    
        #verificar que en la db se haya modificado el titulo correctamente        
        expected_fields = ["author", "summary", "pos_date", "active"]
        update_book = Book.objects.get(id=data["id"])

        self.assertEqual(update_book.title, self.patch_book_data["title"])
        
        #verificar que en la db el resto de datos no se hayan modificado
        for field in expected_fields:
            if field == "pos_date":
                self.assertEqual(str(getattr(update_book, field)), self.post_book_data[field])
            else:
                self.assertEqual(getattr(update_book, field), self.post_book_data[field])
        
        
        # self.assertEqual(update_book.author, self.post_book_data["author"])
        # self.assertEqual(update_book.summary, self.post_book_data["summary"])
        # self.assertEqual(str(update_book.pos_date), self.post_book_data["pos_date"])
        # self.assertEqual(update_book.active, self.post_book_data["active"]) 
        
    def test_fields_types(self):
        data = self.response.json()
        
        field_types = {
            "id":int,
            "title":str,
            "author":str,
            "summary":str,
            "pos_date":str,
            "active":bool,
        }
        
        for field, type in field_types.items():
            self.assertIsInstance(data[field], type)
        
        # self.assertIsInstance(data["title"], str)
        # self.assertIsInstance(data["author"], str)
        # self.assertIsInstance(data["summary"], str)
        # self.assertIsInstance(data["pos_date"], str)
        # self.assertIsInstance(data["active"], bool)