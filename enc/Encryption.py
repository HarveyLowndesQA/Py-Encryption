#inFile, outFile = input("Enter input file name: "), input("Enter output file name: ")
inFile, outFile = "abc.txt", "abc1.txt"

arr, arrC = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","Z","Y"," ", "Z"),("p","h","G","H","I","J","K","B","C","D","q","g","i","u","y","A","E","F","L","M","N","V","W","X","O","P","m","e","a","Q","R","S","T","U","Y","Z","l","n","o","f","d","x","j","k","r","c","v","s","t","z","w","b", "_")
for x in open(inFile, "r").read(): open(outFile, "a").write(arrC[arr.index(x)] if(arr.__contains__(x)) else x)
for y in open(outFile, "r").read(): print((arr[arrC.index(y)] if(arrC.__contains__(y)) else y), end="")