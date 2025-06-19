# Ваш исходный текст
original_text = "Источник"

# Преобразуем текст в байты, а затем в строку с использованием неправильной кодировки
encoded_text = original_text.encode('utf-8')  # Сначала кодируем в UTF-8
faulty_text = encoded_text.decode('latin-1')  # Затем декодируем с использованием latin-1 (или windows-1252)

print(faulty_text)  # Выводит: Ð¡Ð¾Ð±ÑÑÐ¸Ñ Ð² ÑÑÐ°ÑÑÑÑ

# Обратное преобразование (если у вас уже есть 'faulty_text')
faulty_text2 ="ÐÑÑÐ¾ÑÐ½Ð¸ÐºÐ¸:"
fixed_text = faulty_text2.encode('latin-1').decode('utf-8')
print(fixed_text)  # Выводит: События в статьях