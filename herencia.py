class Persona:
    def __init__(self, nombre:str, apellido:str, anno:int)-> None:
        self.nombre = nombre
        self.apellido = apellido
        self.anno = anno

    def __str__(self):
        return f"nombre: {self.nombre}; apellido: {self.apellido}; año: {self.anno}"

class Departamento:
    def __init__(self, nombre_depto:str, nombre_corto_depto:str)-> None:
        self.nombre_depto =  nombre_depto
        self.nombre_corto_depto = nombre_corto_depto
    
    def __str__(self):
        return f"nombre del departamento: {self.nombre_depto}; diminutivo del departamento: {self.nombre_corto_depto}"
    
class Trabajador(Persona, Departamento): 
    def __init__(self, nombre:str, apellido:str, anno:int, nombre_depto:str, nombre_corto_depto:str, salario:int)->None:
        Persona.__init__(self, nombre, apellido, anno)
        Departamento.__init__(self, nombre_depto, nombre_corto_depto)
        self.salario = salario
        
    def __str__(self):
        return f"{Persona.__str__(self)}; {Departamento.__str__(self)}; el salario es {self.salario}"

trabajador = Trabajador("Juan", "Pérez", 2005, "ingeniería de software", "IS", 20000)

print(trabajador)


print("Es trabajador instancia de Persona: ",  isinstance(trabajador, Persona))
print("Es trabajador instancia de Departamento: ", isinstance(trabajador, Departamento))
print("Es trabajador instancia de Trabajador: ", isinstance(trabajador, Trabajador))
