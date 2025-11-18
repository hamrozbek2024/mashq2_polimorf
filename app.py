import hashlib

class User:
    def __init__(self, username):
        self.__username = username
        self.__password_hash = None
    
    def set_password(self, parol):
        """Parolni hash qilib saqlash"""
        # Parolni hash ga aylantirish (SHA-256)
        self.__password_hash = hashlib.sha256(parol.encode()).hexdigest()
        print(f"Parol muvaffaqiyatli o'rnatildi!")
    
    def check_password(self, parol):
        """Parolni tekshirish"""
        if self.__password_hash is None:
            print("Parol hali o'rnatilmagan!")
            return False
        
        # Kiritilgan parolni hash qilib solishtirish
        kiritilgan_hash = hashlib.sha256(parol.encode()).hexdigest()
        
        if kiritilgan_hash == self.__password_hash:
            print("Parol to'g'ri! Kirish ruxsat etildi.")
            return True
        else:
            print("Parol noto'g'ri! Kirish rad etildi.")
            return False
    
    @property
    def username(self):
        """Foydalanuvchi nomini ko'rish"""
        return self.__username
    
    def get_info(self):
        """Foydalanuvchi haqida ma'lumot"""
        parol_holat = "O'rnatilgan" if self.__password_hash else "O'rnatilmagan"
        return f"Foydalanuvchi: {self.__username}\nParol holati: {parol_holat}"


# Test qilish
print("=== FOYDALANUVCHI TIZIMI ===\n")

# Yangi foydalanuvchi yaratish
user1 = User("Alijon")

print(f"Foydalanuvchi: {user1.username}")
print(user1.get_info())
print()

# Parol o'rnatish
print("--- Parol o'rnatish ---")
user1.set_password("mening_parolim123")
print()

# To'g'ri parol bilan kirish
print("--- To'g'ri parol ---")
user1.check_password("mening_parolim123")
print()

# Noto'g'ri parol bilan kirish
print("--- Noto'g'ri parol ---")
user1.check_password("noto'g'ri_parol")
print()

# Parol hash ko'rinmaydi
print("--- Xavfsizlik ---")
print(user1.get_info())
# print(user1.__password_hash)  # AttributeError - ko'rib bo'lmaydi!
print()

# Ikkinchi foydalanuvchi
print("=== IKKINCHI FOYDALANUVCHI ===")
user2 = User("Nodira")
print(user2.get_info())
print()

# Parolsiz kirish urinishi
print("--- Parol o'rnatilmagan ---")
user2.check_password("biror_parol")
