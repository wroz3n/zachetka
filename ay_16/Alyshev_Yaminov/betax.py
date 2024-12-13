import numpy  as np;import random;from PIL import Image
# # Задание 1
# ab= np.array(list(range(1,6)))
# print(ab)
# print(type(ab))
# for i in ab:
#     print(i)
# print("Второе состояние массива", ab*3)
# print(f"Общая сумма: {sum(ab)}")
# print(f"Общая длина: {len(ab)}")
# print(f"Общая сумма*3: {sum(ab*3)}")
# print(f"Общая длина*3: {len(ab*3)}")
# # Задание 2
# start = int(input("Введите начальное число: "))
# end = int(input("Введите конечное число: "))
# b = [i for i in range(start,end+1)]
# print(b)

# # Задание 3
# mat = np.array([[1,2,8],[3,4,6],[5,3,1]])
# betax = [b for b in mat]
# print(f"Matrix:\n{np.array(betax)}")
# start_index = int(input("Начало отрезка: "))
# end_index = int(input("Конец отрезка: "))
# print(f"Matrix_list :{(betax)[start_index:end_index]}")
# print(mat[start_index:end_index])
# print(len(betax[start_index:end_index]))

# # Задание 4
# A = np.random.randint(1, 10, size=(2, 3))
# B = np.random.randint(1, 10, size=(3, 2))
# math1x = np.dot(A, B)
# print("A*B:",math1x)

# Задание 5
img = np.array(Image.open('pelmeshek.jpg'))
img_R = img.copy()
img_R[:, :, (1, 2)] = 0
img_B = img.copy()
img_B[:, :, (0, 1)] = 0
img_1 = Image.fromarray(img_R)
img_2 = Image.fromarray(img_B)
result = Image.new("RGB", (img.shape[1]*2, img.shape[0]*2))
result.paste(img_1, (0,0))
result.paste(img_2, (img.shape[1],0))
result_name = input("" + ".png")
result.save(result_name, format="PNG")

