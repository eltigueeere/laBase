



class Usuario():
    def __init__(self, consulta):
        self.nombre = consulta[1]
        self.apellido = consulta[2]
        self.tipoUsuario = consulta[8]
    