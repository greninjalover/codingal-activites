basket1={"mango", "apple", "Banana", "pear", "kiwi"}
basket2={"kiwi", "mango", "guava", "kiwi"}
print("Fruits in basket1",basket1)
print("Fruits in basket2",basket2)

basket2.add("nectarine")
basket2.add("orange")
print("basket2 after adding more fruits",basket2)

basket3= basket1.intersection(basket2)
print("common fruits",basket3)

import array as arr
fruitcounts=arr.array("i",[3,5,4,2])
print("fruit counts array:", fruitcounts)

fruitcounts.insert(1,60)
fruitcounts.append(7)
print(fruitcounts)

countof60=fruitcounts.count(60)
print(countof60)
fruitcounts.reverse()
print(fruitcounts)