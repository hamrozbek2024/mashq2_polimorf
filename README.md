# mashq2_polimorf
# 🔐 User Klassi - Parol Himoyasi

Parol bilan himoyalangan foydalanuvchi klassi.

## Nima qiladi?

- Foydalanuvchi ma'lumotlarini saqlaydi
- Parolni hash shaklida saqlaydi (xavfsiz)
- Parolni tekshiradi
- Hech qayerda ochiq parol ko'rinmaydi

## Ishlatish

### Foydalanuvchi yaratish
```python
user = User("Alijon")
```

### Parol o'rnatish
```python
user.set_password("mening_parolim123")
```

### Parolni tekshirish
```python
user.check_password("mening_parolim123")  # To'g'ri
user.check_password("noto'g'ri")          # Noto'g'ri
```

### Ma'lumot olish
```python
print(user.username)    # Foydalanuvchi nomi
print(user.get_info())  # To'liq ma'lumot
```

## Xavfsizlik

- Parol **hash** (SHA-256) shaklida saqlanadi
- Ochiq parol hech qayerda ko'rinmaydi
- Private ma'lumotlarga tashqaridan kirish mumkin emas

## Nimalar ishlatilgan?

- **Inkapsulyatsiya** - Ma'lumotlarni yashirish
- **Hashing** - Parolni shifrlash (hashlib)
- **Property** - Username uchun getter
- **Metodlar** - Parol bilan ishlash

---

O'quv maqsadida yaratilgan loyiha.
