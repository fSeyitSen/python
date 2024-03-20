


# Bir metinde her harften kaç tane olduğunu gösterip ekrana yazdıran fonksiyon
def frequencyAnalysis(input):
    input=input.strip().lower()
    special_chars=[' ','1','2','3','4','5','6','7','8', '9', '0', '/','*','-','+','@','#','$','%', '.','?',',','(',')' ]

    for char in special_chars:
        input=input.replace(char,'')

    input.split()

    input_len=len(input)
    dictionary={}
    for harf in input:
        if harf in dictionary:
            dictionary[harf]+=1
        else:
            dictionary[harf]=1
    return print(dictionary)

# frequencyAnalysis(user_input)

# Kendisine gönderilen metinde harflerin kullanım sıklığını (yüzdelik oranını) bulan fonksiyon
def harfOran(input):
    input=input.strip().lower()
    special_chars=[' ','1','2','3','4','5','6','7','8', '9', '0', '/','*','-','+','@','#','$','%', '.','?',',','(',')' ]

    for char in special_chars:
        input=input.replace(char,'')

    input.split()

    input_len=len(input)
    dictionary={}

    for harf in input:
        if harf in dictionary:
            dictionary[harf]+=1
        else:
            dictionary[harf]=1

    for harf,sayi in sorted(dictionary.items()):
        p = 100 * sayi / input_len
        p = round(p, 2)
        print(f" {harf}  \t{sayi}  \t {p}%")
    
    
# harfOran(user_input)
    
# Kendisine gelen harfi (büyükse) küçük harfe çeviren bir fonksiyon
    
def lowerLetter(input):
    yeniString=''
    for harf in input:
        if harf.isupper():
            yeniString+=harf.lower()
        else:
            yeniString+=harf
    
    return print(yeniString)

# lowerLetter(user_input)

# Kendisine gönderilen karakterin bir harf olup olmadığını bulan bir fonksiyon

def isHarf(input):
    for harf in input:
        if harf.isalpha():
            return True
        else:
            return False

      
# print(isHarf(user_input))
    
def infoOgr():
    ogrName="Seyit"
    ogrLastname="Sen"
    ogrNo=221220112
    nott="Python programlamaya giriş dersinin 2.ödevi tamamlandı."
    infoOgr=[ogrName,ogrLastname,ogrNo,nott]
    print(infoOgr)

# infoOgr()