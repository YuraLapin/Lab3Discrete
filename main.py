def CheckMatrix(matrix):
	outerLength = len(matrix)
	for arr in matrix:
		if outerLength != len(arr):
			return False
	return True

def PrintMatrixPosition(num, matrixSize):
	spaces = len(str(matrixSize)) - len(str(num)) + 1
	print(num, end = spaces * " ")

def PrintMatrix(matrix):
	if CheckMatrix(matrix):
		size = len(matrix)
		for i in range(size + 1):
			PrintMatrixPosition(i, size)
		print()
		for i in range(size):
			PrintMatrixPosition(i + 1, size)
			for j in range(size):
				PrintMatrixPosition(matrix[i][j], size)
			print()

def CheckInt(str):
	if str == None or str == "":
		return False
	for char in str:
		if char not in "-0123456789":
			return False
	return True

def GetInt(message):
	print(message)
	ans = input()
	while not CheckInt(ans):
		print("Число должно состоять только из цифр и быть целым")
		print(message)
		ans = input()
	return int(ans)

def GetIntPositive(message):
	ans = GetInt(message)
	while ans <= 0:		
		print("Число должно быть положительным ")
		ans = GetInt(message)		
	return ans	

def GetIntLowerThan(message, max):
	ans = GetIntPositive(message)
	while ans > max:		
		print("Число не может быть больше ", max)
		ans = GetIntPositive(message)		
	return ans	

def ZeroMatrix(size):
	ans = [[0 for i in range(size)] for j in range(size)]
	return ans

def MultiplyMatrix(matrix1, matrix2):
	size = len(matrix1)
	ans = ZeroMatrix(size)
	if CheckMatrix(matrix1) and CheckMatrix(matrix2) and len(matrix1) == len(matrix2):
			size = len(matrix1)
			for i in range(size):
				for j in range(size):
					for k in range(size):
						ans[i][j] += matrix1[k][j] * matrix2[i][k]
					ans[i][j] = min(1, ans[i][j])
	return ans

def PowerMatrix(matrix, power):
	size = len(matrix)
	ans = ZeroMatrix(size)
	if CheckMatrix(matrix):
		if power == 0:
			for i in range(size):
				ans[i][i] = 1
		elif power == 1:
			ans = matrix	
		elif power > 1:
			ans = matrix
			for i in range(power - 1):
				ans = MultiplyMatrix(ans, matrix)
	return ans

def SumMatrix(matrix1, matrix2):
	size = len(matrix1)
	ans = ZeroMatrix(size)
	if CheckMatrix(matrix1) and CheckMatrix(matrix2) and len(matrix1) == len(matrix2):
		for i in range(size):
			for j in range(size):
				ans[i][j] = matrix1[i][j] + matrix2[i][j]
				ans[i][j] = min(1, ans[i][j])
	return ans

def LineSumMatrix(matrix, count):
	size = len(matrix)
	ans = ZeroMatrix(size)
	for i in range(count + 1):
		ans = SumMatrix(ans, PowerMatrix(matrix, i))
	return ans

def Transponate(matrix):
	size = len(matrix)
	ans = ZeroMatrix(size)
	if CheckMatrix(matrix):
		for i in range(size):
			for j in range(size):
				ans[i][j] = matrix[j][i]
	return ans

def And(matrix1, matrix2):
	size = len(matrix)
	ans = ZeroMatrix(size)
	if CheckMatrix(matrix1) and CheckMatrix(matrix2) and len(matrix1) == len(matrix2):
		for i in range(size):
			for j in range(size):
				if matrix1[i][j] == matrix2[i][j] == 1:
					ans[i][j] = 1
				else:
					ans[i][j] = 0
	return ans

def Count(list):
	ans = 0
	for arr in list:
		for elem in arr:
			ans += 1
	return ans

def GetAns(matrix, list):
	if CheckMatrix(matrix):
		size = len(matrix)
		curComp = []
		toDelete = []
		for i in range(size):
			if matrix[0][i] == 1:
				curComp.append(i + 1 + Count(list))
				toDelete.append(i)
		toDelete.reverse()
		for i in toDelete:
			matrix.pop(i)
			for arr in matrix:
				arr.pop(i)
		list.append(curComp)		
		if len(matrix) > 0:
			return GetAns(matrix, list)
		else:
			return list
		
def ConnectionComponents(matrix):
	if CheckMatrix(matrix):
		print(LINE, "\nR:")
		r = LineSumMatrix(matrix, size)
		PrintMatrix(r)

		print(LINE, "\nR^T:")
		rT = Transponate(r)
		PrintMatrix(rT)

		print(LINE, "\nR&R^T")
		fin = And(r, rT)
		PrintMatrix(fin)

		print(LINE, "\nANSWER:")
		print(GetAns(fin, []))

		
if __name__ == "__main__":
	LINE = "-------------------------------------------" 

	size = GetIntPositive("Введите размер матрицы: ")
	matrix = ZeroMatrix(size)

	goOn = True
	while goOn:
		print(LINE)
		PrintMatrix(matrix)
		print(LINE)
		print("1 - Добавить связь")
		print("2 - Найти компоненты связности")
		print("3 - Выход")
		ans = GetInt("Выберите действие [1-3]: ")
		if ans == 1:
			n1 = GetIntLowerThan("Введите номер вершины отправления: ", size)
			n2 = GetIntLowerThan("Введите номер вершины прибытия: ", size)
			matrix[n1 - 1][n2 - 1] = 1			
		elif ans == 2:
			ConnectionComponents(matrix)
			goOn = False
		elif ans == 3:
			goOn = False
		else:
			print("Введено неверное число")