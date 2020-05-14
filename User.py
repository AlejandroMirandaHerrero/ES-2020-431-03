class User:

    def __init__(self, nombre_completo, DNI, direccion_postal, num_tel, email ):
        self._nombre_completo = nombre_completo
        self._DNI = DNI
        self._direccion_postal = direccion_postal
        self._num_tel = num_tel
        self._email = email
        
        
    def get_userdata(self):
        return self._nombre_completo, self._DNI, self._direccion_posatal, self._num_tel, self._email
    
    
   
 
       