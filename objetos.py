class Persona():  #El objeto Padre  #Nombres de clase con mayusculas
    def __init__(self, param_nombre, param_email):      
        self.nombre = param_nombre
        self.email = param_email
        self.asistencia = 0

    def cambiar_nombre(self, nuevo_nombre): #Creo un METODO para cambiar el valor de una variable
        self.nombre = nuevo_nombre
    def asistencia_clase(self):
        self.asistencia += 1

#No se si se puede tener 2 herencias, CREO QUE NO DEBERIA
class Profesor(Persona):  #El objeto que hereda
    def __init__(self, param_nombre, param_email):  #self y param_nombre son parametros     
        #para iniciar una variable pongo init - Esto es un CONSTRUCTOR
#el self dice que se agregue cosas a si mismo
        super().__init__(param_nombre, param_email) #el super sobre-escribe lo que hay arriba para llamar a la clase padre

class Materia():  #El objeto
    def __init__(self, nombre_mat, mat_id, profesor, curso):  #self y param_nombre son parametros     
        self.nombre = nombre_mat
        self.id = mat_id #el self dice que se agregue cosas a si mismo
        self.profesor = profesor
        self.curso = curso

class Alumno(Persona):  #El objeto que hereda los metodos
    def __init__(self, param_nombre, param_email, numero_alumno, materianom):  #self y param_nombre son parametros     
        self.numero_alumno = numero_alumno#para iniciar una variable pongo init - Esto es un CONSTRUCTOR
        self.materias_cursando = materianom

        super().__init__ (param_nombre, param_email)
       
    def cursandoeliminar(self, materia): #Creo un METODO para cambiar el valor de una variable
        self.materias_cursando.remove(materia)
    def cursandoagregar(self, materia): #Creo un METODO para cambiar el valor de una variable
        self.materias_cursando.append(materia)


#Alumno y Profesor tiene herencia de una clase llamada persona porque los 2 son personas con nombre y email


#Si agrego otro parametro lo agrego en la misma linea
profesor_pepe = Profesor("Pepe", "jose@email.um")
profesor_maria = Profesor("Maria", "maria@email.um")

print("PROFESOR ") #Profesor

print(id(profesor_pepe))    #id es el lugar de la memoria donde esta guardada la variable
print(profesor_pepe.nombre)  #imprime lo que tiene profesor pepe pegado
print(profesor_pepe.email)

profesor_pepe.cambiar_nombre("Jose") #Cambio el nombre
print("nuevo nombre", profesor_pepe.nombre) #imprimo el nuevo valor del objeto profesor.nombre

print("El profesor fue a clase!!")
profesor_pepe.asistencia_clase()

print("su asistencia es: ", profesor_pepe.asistencia)

print ("MATERIA") #Materia
materia_computacion = Materia("Computacion", 2007, profesor_pepe.nombre, "2II")
print(materia_computacion.nombre)
print(materia_computacion.id)
print(materia_computacion.profesor)
print(materia_computacion.curso)

materia_matematica = Materia("Matematica", 2108, profesor_maria.nombre, "2II")
print(materia_computacion.nombre)
print(materia_computacion.id)
print(materia_computacion.profesor)
print(materia_computacion.curso)

materia_analisis = Materia("Analisis de sistemas", 3004, profesor_maria.nombre, "1II")
print(materia_computacion.nombre)
print(materia_computacion.id)
print(materia_computacion.profesor)
print(materia_computacion.curso)

print ("ALUMNO") #Alumno

alumno_sofia = Alumno("sofia", "s.soler@alumno.um.edu.ar", 62008, [materia_computacion.nombre, materia_matematica.nombre])
print(alumno_sofia.nombre)
print(alumno_sofia.email)
print(alumno_sofia.materias_cursando) #Lo agrego como lista y se agregan todos los de la lista como 1 atributo

alumno_sofia.cursandoeliminar (materia_matematica.nombre)
alumno_sofia.cursandoagregar (materia_analisis.nombre)

print("Las nuevas materias que cursas son: ", alumno_sofia.materias_cursando)





