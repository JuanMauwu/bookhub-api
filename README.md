# django-benniger

Comandos para iniciar el proyecto:
- Abrir terminal
- Abrir docker
- docker compose up backend (inicializa el contenedor)


Abrir sitio administrativo:
- http://localhost:8000/admin/


Hacer migraciones:
- docker-compose exec backend python manage.py makemigrations myapp
- docker-compose exec backend python manage.py migrate myapp


Endpoint o rutas de APIs:
- http://localhost:8000/api/v1/books
- http://localhost:8000/api/v1/tags


Hacer migraciones(despues de crear o modificar un modelo):
- docker compose exec backend python manage.py makemigrations myapp
- docker compose exec backend python manage.py migrate myapp


Crear super usuario (inicio de proyecto):
- docker compose exec backend python manage.py createsuperuser


Abrir la db en terminal y visualizar tablas:
- docker-compose exec backend python manage.py dbshell
- .tables (listar todas las tablas en la db)
- .mode table (para ponerlo en formato bonito)
- SELECT column FROM nombre de la tabla; (ejem: SELECT title FROM book;) (ejem: SELECT * FROM book;) "selecciona todos los campos")


Tipos de Campos en Django (clases):
    Campos Numéricos:
    - IntegerField
    - FloatField
    - DecimalField(max_digits=X, decimal_places=Y)

    Campos de Texto:
    - CharField(max_length=X)
    - TextField

    Campos de Fecha y Hora:
    - DateField(auto_now=False, auto_now_add=False)
    - TimeField(auto_now=False, auto_now_add=False)
    - DateTimeField(auto_now=False, auto_now_add=False)

    Campos Booleanos:
    - BooleanField

    Campos de Relación:
    - ForeignKey(to, on_delete=models.CASCADE) "Uno a muchos" Elijo uno y Puedo repetir en otro modelo la elección
    - ManyToManyField(to) "Muchos a muchos" Elijo los que quiera y puedo repetir en otro modelo la elección
    - OneToOneField(to, on_delete=models.CASCADE) "Uno a uno" Elijo uno sin repetir 
 
    Campos de Archivos y Multimedia:
    - FileField(upload_to='path/')
    - ImageField(upload_to='path/')

    Campos Misceláneos:
    - EmailField
    - URLField
    - UUIDField
    - SlugField
    - JSONField
    - IPAddressField
    - GenericIPAddressField(protocol='both')

Comando para el test:
- docker compose exec backend python manage.py test myapp.tests


Metodos de asserts (unittest):

- assertEqual(a, b)
Verifica que a y b sean iguales.

- assertNotEqual(a, b)
Verifica que a y b no sean iguales.

- assertTrue(expr)
Verifica que expr sea verdadero (True).

- assertFalse(expr)
Verifica que expr sea falso (False).

- assertIs(a, b)
Verifica que a y b sean el mismo objeto (misma referencia en memoria).

- assertIsNot(a, b)
Verifica que a y b no sean el mismo objeto.

- assertIsNone(expr)
Verifica que expr sea None.

- assertIsNotNone(expr)
Verifica que expr no sea None.

- assertIn(member, container)
Verifica que member esté presente en container.

- assertNotIn(member, container)
Verifica que member no esté presente en container.

- assertIsInstance(obj, cls)
Verifica que obj sea una instancia de la clase cls.

- assertNotIsInstance(obj, cls)
Verifica que obj no sea una instancia de la clase cls.

- assertGreater(a, b)
Verifica que a sea mayor que b.

- assertGreaterEqual(a, b)
Verifica que a sea mayor o igual que b.

- assertLess(a, b)
Verifica que a sea menor que b.

- assertLessEqual(a, b)
Verifica que a sea menor o igual que b.

- assertListEqual(list1, list2)
Verifica que list1 y list2 sean listas iguales.

- assertDictEqual(dict1, dict2)
Verifica que dict1 y dict2 sean diccionarios iguales.

- assertCountEqual(seq1, seq2)
Verifica que seq1 y seq2 tengan los mismos elementos, sin importar el orden.

- assertRegex(text, regex)
Verifica que text coincida con el patrón de expresión regular regex.
Ejemplo: self.assertRegex(email, r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

- assertNotRegex(text, regex)
Verifica que text no coincida con el patrón de expresión regular regex.
Ejemplo: self.assertNotRegex(username, r'\s')

- assertRaises(exc, callable, *args, **kwargs)
Verifica que callable lanza una excepción del tipo exc.
Ejemplo: self.assertRaises(ValueError, func, arg1, arg2)

- assertRaisesRegex(exc, regex, callable, *args, **kwargs)
Verifica que la excepción lanzada coincide con el patrón regex.
Ejemplo: self.assertRaisesRegex(ValueError, "invalid input", func, arg)

- assertWarns(warning, callable, *args, **kwargs)
Verifica que callable emita una advertencia del tipo warning.
Ejemplo: self.assertWarns(DeprecationWarning, func)

- assertWarnsRegex(warning, regex, callable, *args, **kwargs)
Verifica que la advertencia emitida coincida con el patrón regex.
Ejemplo: self.assertWarnsRegex(UserWarning, "deprecated", func)

- assertLogs(logger, level)
Verifica que un mensaje de log se emita con un nivel específico.
Ejemplo: self.assertLogs('myapp', 'INFO')

- assertAlmostEqual(a, b, places)
Verifica que a y b sean casi iguales, hasta un número de decimales.
Ejemplo: self.assertAlmostEqual(3.14159, 3.14, places=2)

- assertNotAlmostEqual(a, b, places)
Verifica que a y b no sean casi iguales.
Ejemplo: self.assertNotAlmostEqual(3.14159, 3.13, places=2)