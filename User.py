class User:

    def __init__(self, nombre_completo, DNI, direccion_postal, num_tel, email ):
        self.nombre_completo = nombre_completo
        self.DNI = DNI
        self.direccion_postal = direccion_postal
        self.num_tel = num_tel
        self.email = email
        
        
    def get_userdata(self):
        return self.nombre_completo, self.DNI, self.direccion_postal, self.num_tel, self.email
    
    
   
 
       