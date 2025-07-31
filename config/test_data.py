from faker import Faker

fake = Faker()

class TestData:
    VALID_PHRASES = {
        'cyrillic': "Мастер и Маргарита",
        'latin': "Master and Margarita",
        'with_numbers': "123 Мастер и Маргарита 456"
    }
    
    INVALID_PHRASES = {
        'random_chars': fake.pystr(min_chars=10, max_chars=30),
        'emojis': "😂😂😂😂😂😂😂😂😂😂"
    }
    
    INVALID_TOKENS = [
        "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIyMjU1MDAxLCJpYXQiOjE3NDUzNDEwMTEsImV4cCI6MTc0NTM0NDYxMSwidHlwZSI6MjB9.xbT9_lhELZqAFRoy4itVpQuM4nrM_ds8BRcCO98eOzF"
    ]
