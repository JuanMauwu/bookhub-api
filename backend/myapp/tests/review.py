from django.test import TestCase
from rest_framework import status # type: ignore
from django.urls import reverse
from myapp.models import Review, Book, Label, DetailReview

#TEST GET
class ReviewGetAPITest(TestCase):
    def setUp(self):
        #este modelo tiene tres campos con relaciones de los tres tipos, primero creamos los objetos a relacionar con el modelo principal
        self.book1 = Book.objects.create( 
            title="The Catcher",         
            author="J.D. Salinger",
            summary="A story about teenage rebellion.",
            pos_date="1951-07-16",
            active=True
        )     
        
        self.label1 = Label.objects.create(
            name = "Ficción",
            description = "Lorem ipsum dolor sit amet",
            active = True
        )
        
        self.label2 = Label.objects.create(
            name = "Terror",
            description = "Lorem ipsum dolor sit amet",
            active = True    
        )
        
        self.detail_review1 = DetailReview.objects.create(
            pos_date = "2005-05-29",
            qualification = 10,
            comments = "Lorem ipsum dolor sit amet",
            active = True
        )
        
        #ahora se instancia el modelo principal
        self.review1 = Review.objects.create(
            book = self.book1, #relacion foreignKey: en este caso un libro puede relacionarse con multiples instancias del modelo review
            reviewer = "Juan",
            text = "This is a review text",
            detail = self.detail_review1, #relacion OneToOneField: Un unico DetailReview puede ser relacionado con un unico Review
            active = True
        )
        
        self.review1.labels.add(self.label1, self.label2)
        
        self.detail_url = reverse("myapp:review-list-create")
        self.response = self.client.get(self.detail_url)
        
    def test_status_code(self):
        #verificar si devuelve el codigo de estado correcto
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_response_status(self):
        data = self.response.json()
        
        #verificar si la data no esta vacia
        self.assertGreater(len(data), 0, "No data")
        
        #verificar que los campos requeridos si esten en la respuesta
        expected_fields = ["id", "book", "reviewer", "text", "labels", "detail", "active"]
        for field in expected_fields:
            self.assertIn(field, data[0])
            
        #verificar que los datos de la respuesta correspodan con el objeto creado para la prueba 
        expected_fields = ["id", "reviewer", "text", "active"]
        for field in expected_fields:
            self.assertEqual(data[0][field], getattr(self.review1, field))
            
        #verificamos los valores de lso campos relacionales. La respuesta devuelve los ids de los modelos relacionados
        self.assertEqual(data[0]["book"], self.book1.id)
        self.assertEqual(data[0]["labels"], list(self.review1.labels.values_list("id", flat=True)))
        self.assertEqual(data[0]["detail"], self.detail_review1.id)
        
        #verificar que el campo manytomany tenga el numero correcto de modelos relacionados
        self.assertEqual(len(data[0]["labels"]), self.review1.labels.count())
        
        #verificar en db
        expected_fields = ["id", "book", "reviewer", "text", "labels", "detail", "active"]
        
        review =    Review.objects.get(id=self.review1.id)
        
        for field in expected_fields:
            self.assertEqual(getattr(review, field), getattr(self.review1, field))

    def test_field_types(self):
        data = self.response.json()
        
        field_types = {
            "id":int,
            "book":int,
            "reviewer":str,
            "text":str,
            "labels":list,
            "detail":int,
            "active":bool
        }
        
        #verificar que los tipos de campos de la respuesta sean los esperados
        for field, type in field_types.items():
            self.assertIsInstance(data[0][field], type)
            
#TEST GET DETAIL
class ReviewGetDetailAPITest(TestCase):
    def setUp(self):
        self.book1 = Book.objects.create( 
            title="The Catcher",         
            author="J.D. Salinger",
            summary="A story about teenage rebellion.",
            pos_date="1951-07-16",
            active=True
        )     
        
        self.label1 = Label.objects.create(
            name = "Ficción",
            description = "Lorem ipsum dolor sit amet",
            active = True
        )
        
        self.label2 = Label.objects.create(
            name = "Terror",
            description = "Lorem ipsum dolor sit amet",
            active = True    
        )
        
        self.detail_review1 = DetailReview.objects.create(
            pos_date = "2005-05-29",
            qualification = 10,
            comments = "Lorem ipsum dolor sit amet",
            active = True
        )
        
        self.review1 = Review.objects.create(
            book = self.book1, 
            reviewer = "Juan",
            text = "This is a review text",
            detail = self.detail_review1, 
            active = True
        )
        
        self.review1.labels.add(self.label1, self.label2)
        
        self.detail_url = reverse("myapp:review-detail", kwargs={"id":self.review1.id})
        self.response = self.client.get(self.detail_url)
    
    def test_status_code(self):
        #verificar si devuelve el codigo de estado correcto
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
    
    def test_response_structure(self):
        data = self.response.json()
        
        #verificar que los campos requeridos si esten en la respuesta
        expected_fields = ["id", "book", "reviewer", "text", "labels", "detail", "active"]
        for field in expected_fields:
            self.assertIn(field, data)
            
        #verificar que los datos de la respuesta correspodan con el objeto creado para la prueba
        expected_fields = ["id", "reviewer", "text", "active"]
        for field in expected_fields:
            self.assertEqual(data[field], getattr(self.review1, field))
            
        #verificamos los valores de lso campos relacionales. La respuesta devuelve los ids de los modelos relacionados
        self.assertEqual(data["book"], self.book1.id)
        self.assertEqual(data["labels"], list(self.review1.labels.values_list("id", flat=True)))
        self.assertEqual(data["detail"], self.detail_review1.id)
        
        #verificar que el campo manytomany tenga el numero correcto de modelos relacionados
        self.assertEqual(len(data["labels"]), self.review1.labels.count())
        
        #verificar en db
        expected_fields = ["id", "book", "reviewer", "text", "labels", "detail", "active"]
        
        review =    Review.objects.get(id=self.review1.id)
        
        for field in expected_fields:
            self.assertEqual(getattr(review, field), getattr(self.review1, field))
        
    def test_field_types(self):
        data = self.response.json()
        
        field_types = {
            "id":int,
            "book":int,
            "reviewer":str,
            "text":str,
            "labels":list,
            "detail":int,
            "active":bool
        }
        
        #verificar que los tipos de campos de la respuesta sean los esperados
        for field, type in field_types.items():
            self.assertIsInstance(data[field], type)
        
#TEST POST
class ReviewPostAPITest(TestCase):
    def setUp(self):
        self.book1 = Book.objects.create( 
            title="The Catcher",         
            author="J.D. Salinger",
            summary="A story about teenage rebellion.",
            pos_date="1951-07-16",
            active=True
        )     
        
        self.label1 = Label.objects.create(
            name = "Ficción",
            description = "Lorem ipsum dolor sit amet",
            active = True
        )
        
        self.label2 = Label.objects.create(
            name = "Terror",
            description = "Lorem ipsum dolor sit amet",
            active = True    
        )
        
        self.detail_review1 = DetailReview.objects.create(
            pos_date = "2005-05-29",
            qualification = 10,
            comments = "Lorem ipsum dolor sit amet",
            active = True
        )
        
        #pasamos las ids de los modelos que vamos a relacionar al modelo pirncipal
        self.review_post_data = {
            "book":self.book1.id,
            "reviewer":"Juan",
            "text":"This is a review text",
            "labels":[self.label1.id, self.label2.id],
            "detail":self.detail_review1.id,
            "active":True
        }
        
        self.detail_url = reverse("myapp:review-list-create")
        self.response = self.client.post(self.detail_url, self.review_post_data, content_type="application/json")
        
    def test_status_code(self):
        #verificar si devuelve el codigo de estado correcto
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        
    def test_response_structure(self):
        data = self.response.json()
        
        #verificar que los campos requeridos si esten en la respuesta
        expected_fields = ["id", "book", "reviewer", "text", "labels", "detail", "active"]
        
        for field in expected_fields:
            self.assertIn(field, data)
        
        #verificar que los datos de la respuesta correspodan con la data de la solicitud
        expected_fields = ["book", "reviewer", "text", "labels", "detail", "active"]
        
        for field in expected_fields:
            self.assertEqual(data[field], self.review_post_data[field])
         
        #comparamos los valores que pasamos en la solicitud con lo que hay en db
        review = Review.objects.get(id=data["id"])
        
        self.assertEqual(review.book.id, self.review_post_data["book"])
        self.assertEqual(review.reviewer, self.review_post_data["reviewer"])
        self.assertEqual(review.text, self.review_post_data["text"])
        self.assertEqual(list(review.labels.values_list("id", flat=True)), self.review_post_data["labels"])
        self.assertEqual(review.detail.id, self.review_post_data["detail"])
        self.assertEqual(review.active, self.review_post_data["active"])
        
        #comparacion de los demas valores de los campos relacionales con los de la db
        self.assertEqual(review.book.title, self.book1.title)
        self.assertEqual(review.book.author, self.book1.author)
        self.assertEqual(review.book.summary, self.book1.summary)                           #para book
        self.assertEqual(str(review.book.pos_date), self.book1.pos_date)
        self.assertEqual(review.book.active, self.book1.active)
        
        self.assertEqual(str(review.detail.pos_date), self.detail_review1.pos_date)
        self.assertEqual(review.detail.qualification, self.detail_review1.qualification)    #para detail
        self.assertEqual(review.detail.comments, self.detail_review1.comments)
        self.assertEqual(review.detail.active, self.detail_review1.active)
        
        labels_names = list(review.labels.values_list("name", flat=True))
        self.assertIn(self.label1.name, labels_names)                         
        self.assertIn(self.label2.name, labels_names)
                                                                                           #para labels
        labels_descriptions = list(review.labels.values_list("description", flat=True))
        self.assertIn(self.label1.description, labels_descriptions)                  
        self.assertIn(self.label2.description, labels_descriptions)
        
    def test_field_types(self):
        data = self.response.json()
        
        field_types = {
            "id":int,
            "book":int,
            "reviewer":str,
            "text":str,
            "labels":list,
            "detail":int,
            "active":bool
        }
        
        #verificar que los tipos de campos de la respuesta sean los esperados 
        for field, type in field_types.items():
            self.assertIsInstance(data[field], type)         
            
#TEST DELETE 
class ReviewDeleteAPITest(TestCase):
    def setUp(self):
        self.book1 = Book.objects.create( 
            title="The Catcher",         
            author="J.D. Salinger",
            summary="A story about teenage rebellion.",
            pos_date="1951-07-16",
            active=True
        )     
        
        self.label1 = Label.objects.create(
            name = "Ficción",
            description = "Lorem ipsum dolor sit amet",
            active = True
        )
        
        self.label2 = Label.objects.create(
            name = "Terror",
            description = "Lorem ipsum dolor sit amet",
            active = True    
        )
        
        self.detail_review1 = DetailReview.objects.create(
            pos_date = "2005-05-29",
            qualification = 10,
            comments = "Lorem ipsum dolor sit amet",
            active = True
        )
        
        self.review1 = Review.objects.create(
            book = self.book1, 
            reviewer = "Juan",
            text = "This is a review text",
            detail = self.detail_review1, 
            active = True 
        )
        
        self.review1.labels.add(self.label1, self.label2)
        
        self.detail_url = reverse("myapp:review-detail", kwargs={"id":self.review1.id})
        self.response = self.client.delete(self.detail_url)
        
    def test_status_code(self):
        #verificar si devuelve el codigo de estado correcto
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_object_delete(self):
        #verificar que el objeto no exista en la db
        self.assertFalse(Review.objects.filter(id=self.review1.id).exists())
        
    def test_related_object_status(self):
        #verificar que las isntancias de Book y DetailReview sigan existiendo despues de eliminar la instancia del modelo Review
        self.assertTrue(Book.objects.filter(id=self.book1.id).exists())
        self.assertTrue(DetailReview.objects.filter(id=self.detail_review1.id).exists())
    
#TEST PUT (actualizar pero se deben pasar todos los campos)
class ReviewPutAPITest(TestCase):
    def setUp(self):
        self.book1 = Book.objects.create( 
            title="The Catcher",         
            author="J.D. Salinger",
            summary="A story about teenage rebellion.",
            pos_date="1951-07-16",
            active=True
        )
        
        self.book2 = Book.objects.create( 
            title="The",         
            author="J.D.",
            summary="A story",
            pos_date="2000-07-16",
            active=True
        )  
        
        self.label1 = Label.objects.create(
            name = "Ficción",
            description = "Lorem ipsum dolor sit amet",
            active = True
        )
        
        self.label2 = Label.objects.create(
            name = "Terror",
            description = "Lorem ipsum dolor sit amet",
            active = True    
        )
        
        self.detail_review1 = DetailReview.objects.create(
            pos_date = "2005-05-29",
            qualification = 10,
            comments = "Lorem ipsum dolor sit amet",
            active = True
        )
        
        self.detail_review2 = DetailReview.objects.create(
            pos_date = "2002-05-29",
            qualification = 5,
            comments = "Lorem",
            active = True
        )
        
        self.review1 = Review.objects.create(
            book = self.book1, 
            reviewer = "Juan",
            text = "This is a review text",
            detail = self.detail_review1, 
            active = True
        )

        self.review1.labels.add(self.label1, self.label2)

        self.review_put_data = {
            "book":self.book2.id,
            "reviewer":"Sebas",
            "text":"This is",
            "labels":[self.label1.id],
            "detail":self.detail_review2.id,
            "active":False
        }
        
        self.detail_url = reverse("myapp:review-detail", kwargs={"id":self.review1.id})
        self.response = self.client.put(self.detail_url, self.review_put_data, content_type="application/json")
        
    def test_status_code(self):
        #verificar si devuelve el codigo de estado correcto
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_response_structure(self):
        data = self.response.json()
        
        #verificar que los campos requeridos si esten en la respuesta
        expected_fields = ["id", "book", "reviewer", "text", "labels", "detail", "active"]
        
        for field in expected_fields:
            self.assertIn(field, data)
            
        #verificar que los datos de la respuesta correspodan con la data de la solicitud
        expected_fields = ["book", "reviewer", "text", "labels", "detail", "active"]
        
        for field in expected_fields:
            self.assertEqual(data[field], self.review_put_data[field])
        
        #comparamos los valores que pasamos en la solicitud con lo que hay en db
        review = Review.objects.get(id=self.review1.id)
        
        self.assertEqual(review.book.id, self.review_put_data["book"])
        self.assertEqual(review.reviewer, self.review_put_data["reviewer"])
        self.assertEqual(review.text, self.review_put_data["text"])
        self.assertEqual(list(review.labels.values_list("id", flat=True)), self.review_put_data["labels"])
        self.assertEqual(review.detail.id, self.review_put_data["detail"])
        self.assertEqual(review.active, self.review_put_data["active"])

        #comparacion de los demas valores de los campos relacionales con los de la db
        self.assertEqual(review.book.id, self.book2.id)
        self.assertEqual(review.book.title, self.book2.title)
        self.assertEqual(review.book.author, self.book2.author)
        self.assertEqual(review.book.summary, self.book2.summary)                          #para book
        self.assertEqual(str(review.book.pos_date), self.book2.pos_date)
        self.assertEqual(review.book.active, self.book2.active)
        
        self.assertEqual(str(review.detail.pos_date), self.detail_review2.pos_date)
        self.assertEqual(review.detail.qualification, self.detail_review2.qualification)    #para detail
        self.assertEqual(review.detail.comments, self.detail_review2.comments)
        self.assertEqual(review.detail.active, self.detail_review2.active)
        
        labels_names = list(review.labels.values_list("name", flat=True))
        self.assertIn(self.label1.name, labels_names)                         
                                                                                           #para labels
        labels_descriptions = list(review.labels.values_list("description", flat=True))
        self.assertIn(self.label1.description, labels_descriptions)     
        
    def test_field_types(self):
        data = self.response.json()
        
        field_types = {
            "id":int,
            "book":int,
            "reviewer":str,
            "text":str,
            "labels":list,
            "detail":int,
            "active":bool
        }
        
        #verificar que los tipos de campos de la respuesta sean los esperados
        for field, type in field_types.items():
            self.assertIsInstance(data[field], type)            
        
#TEST METODO PATCH (actualizar pero solo se pasa el campo a modificar, puede variar dado como esten definidos los campos en el modelo)
class ReviewPatchAPITest(TestCase):
    def setUp(self):
        self.book1 = Book.objects.create( 
            title="The Catcher",         
            author="J.D. Salinger",
            summary="A story about teenage rebellion.",
            pos_date="1951-07-16",
            active=True
        )
        
        self.book2 = Book.objects.create( 
            title="The",         
            author="J.D.",
            summary="A story",
            pos_date="2000-07-16",
            active=True
        )  
        
        self.label1 = Label.objects.create(
            name = "Ficción",
            description = "Lorem ipsum dolor sit amet",
            active = True
        )
        
        self.label2 = Label.objects.create(
            name = "Terror",
            description = "Lorem ipsum dolor sit amet",
            active = True    
        )
        
        self.detail_review1 = DetailReview.objects.create(
            pos_date = "2005-05-29",
            qualification = 10,
            comments = "Lorem ipsum dolor sit amet",
            active = True
        )
        
        self.detail_review2 = DetailReview.objects.create(
            pos_date = "2002-05-29",
            qualification = 5,
            comments = "Lorem",
            active = True
        )
        
        self.review1 = Review.objects.create(
            book = self.book1, 
            reviewer = "Juan",
            text = "This is a review text",
            detail = self.detail_review1, 
            active = True
        )
        
        self.review1.labels.add(self.label1, self.label2)
        #aqui termina la creacion

        self.review_put_data = {  #no modificamos campo active, por ende no lo pasamos en la solicitud (el unico no obligatorio), el resto de campos se modifican
            "book":self.book2.id,
            "reviewer":"Sebas",
            "text":"This is",
            "labels":[self.label1.id],
            "detail":self.detail_review2.id,
        }
        
        self.detail_url = reverse("myapp:review-detail", kwargs={"id":self.review1.id})
        self.response = self.client.patch(self.detail_url, self.review_put_data, content_type="application/json")
        
    def test_status_code(self):
        #verificar si devuelve el codigo de estado correcto
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        
    def test_response_structure(self):
        data = self.response.json()
        
        #verificar que los campos requeridos si esten en la respuesta
        expected_fields = ["id", "book", "reviewer", "text", "labels", "detail", "active"]
        
        for field in expected_fields:
            self.assertIn(field, data)
        
        #verificar que los datos de la respuesta correspodan con la data de la solicitud
        expected_fields = ["book", "reviewer", "text", "labels", "detail"]
        
        for field in expected_fields:
            self.assertEqual(data[field], self.review_put_data[field])
        
        self.assertEqual(data["active"], True) #verificar que el campo que no se cambio este igual
        
        #comparamos los valores que pasamos en la solicitud con lo que hay en db
        review = Review.objects.get(id=self.review1.id)
        
        self.assertEqual(review.book.id, self.review_put_data["book"])
        self.assertEqual(review.reviewer, self.review_put_data["reviewer"])
        self.assertEqual(review.text, self.review_put_data["text"])
        self.assertEqual(list(review.labels.values_list("id", flat=True)), self.review_put_data["labels"])
        self.assertEqual(review.detail.id, self.review_put_data["detail"])
        self.assertEqual(review.active, self.review1.active)

        #comparacion de los demas valores de los campos relacionales con los de la db
        self.assertEqual(review.book.id, self.book2.id)
        self.assertEqual(review.book.title, self.book2.title)
        self.assertEqual(review.book.author, self.book2.author)
        self.assertEqual(review.book.summary, self.book2.summary)                          #para book
        self.assertEqual(str(review.book.pos_date), self.book2.pos_date)
        self.assertEqual(review.book.active, self.book2.active)
        
        self.assertEqual(str(review.detail.pos_date), self.detail_review2.pos_date)
        self.assertEqual(review.detail.qualification, self.detail_review2.qualification)    #para detail
        self.assertEqual(review.detail.comments, self.detail_review2.comments)
        self.assertEqual(review.detail.active, self.detail_review2.active)
        
        labels_names = list(review.labels.values_list("name", flat=True))
        self.assertIn(self.label1.name, labels_names)                         
                                                                                           #para labels
        labels_descriptions = list(review.labels.values_list("description", flat=True))
        self.assertIn(self.label1.description, labels_descriptions)     
        
    def test_field_types(self):
        data = self.response.json()
        
        field_types = {
            "id":int,
            "book":int,
            "reviewer":str,
            "text":str,
            "labels":list,
            "detail":int,
            "active":bool
        }
        
        #verificar que los tipos de campos de la respuesta sean los esperados
        for field, type in field_types.items():
            self.assertIsInstance(data[field], type) 