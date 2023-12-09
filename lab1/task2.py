volume = 1.44*2**20
pages = 100
rows = 50
chars = 25
cost=4

books = int(volume//(pages*rows*chars*cost))
print("Количество книг, помещающихся на дискету:", books)
