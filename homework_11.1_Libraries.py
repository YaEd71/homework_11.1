import requests
import numpy as np

print('Работа с библиотекой Requests:')
# 1. Выполнение GET-запроса
response = requests.get('https://jsonplaceholder.typicode.com/posts')
# Проверка статуса ответа
if response.status_code == 200:
    print("GET Request Successful!")
else:
    print("GET Request Failed!")

# 2. Вывод первых 3 записей из полученного JSON-ответа
posts = response.json()
for post in posts[:3]:
    print(f"Post ID: {post['id']}")
    print(f"Title: {post['title']}")
    print(f"Body: {post['body']}")
    print('---')

# 3. Выполнение POST-запроса
new_post = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
response_post = requests.post('https://jsonplaceholder.typicode.com/posts', json=new_post)
if response_post.status_code == 201:
    print("POST Request Successful!")
    print("New Post ID:", response_post.json()['id'])
else:
    print("POST Request Failed!")

# 4. Выполнение PUT-запроса для обновления существующего поста
update_post = {
    'id': 1,
    'title': 'updated title',
    'body': 'updated body',
    'userId': 1
}
response_put = requests.put('https://jsonplaceholder.typicode.com/posts/1', json=update_post)
if response_put.status_code == 200:
    print("PUT Request Successful!")
    print("Updated Post:", response_put.json())
else:
    print("PUT Request Failed!")

# 5. Выполнение DELETE-запроса для удаления поста
response_delete = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
if response_delete.status_code == 200:
    print("DELETE Request Successful!")
else:
    print("DELETE Request Failed!")
print('---')

# Работа с библиотекой NumPy
# 1. Создание массива чисел
print('Работа с библиотекой NumPy:')
array = np.array([1, 2, 3, 4, 5])
print("Original Array:", array)

# 2. Выполнение математических операций
# a. Сложение массива с числом
array_plus_10 = array + 10
print("Array + 10:", array_plus_10)

# b. Поэлементное умножение массива
array_squared = array ** 2
print("Array Squared:", array_squared)

# c. Вычисление среднего значения массива
mean_value = np.mean(array)
print("Mean of Array:", mean_value)

# 3. Создание двумерного массива (матрицы)
matrix = np.array([[1, 2], [3, 4]])
print("Original Matrix:\n", matrix)

# a. Транспонирование матрицы
transposed_matrix = np.transpose(matrix)
print("Transposed Matrix:\n", transposed_matrix)

# b. Умножение матриц
matrix_product = np.dot(matrix, transposed_matrix)
print("Matrix Product:\n", matrix_product)

# c. Вычисление определителя матрицы
matrix_determinant = np.linalg.det(matrix)
print("Matrix Determinant:", matrix_determinant)