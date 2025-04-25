linnanimi = "Warssav"
print(linnanimi[6])

linnanimed = ['Warssav', 'Tallinn', 'Helsingi','Kyoto','Kuala Lumpur']

kohukesemaitsed = ['maasika', 'vanilli', 'kakao','kondendspiim','marmelaadi']

print(linnanimed[0:2])
print(linnanimed[:2])
print(linnanimed[1:4])
print(linnanimed[3:5])
print(linnanimed[3:])

print(kohukesemaitsed[-1:])

teavitus = "Palun tee töö ära"
print(teavitus[10:14])

print(min([1,2,3,4,5,6,7]))
print(min([1,1,2,2,5,3,5,5,6.9,7.1]))
print(max([1,2,5,5,6,7]))
print(max([1.1,2.2,5.3,5.5,6.9,7.1]))

print(3 in [6,2,4,5,9.0])
print(3 in [6,3,4,6,9.1])
print(3 in [6,2,4,5,9.0,1,2,5,5,6,7])

for i in range(4):
    print(i)
