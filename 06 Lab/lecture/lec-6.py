'''
class Vehicle:
    pass
class LandVehicle(Vehicle):
    pass
class TrackedVehicle(LandVehicle):
    pass
my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()

for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()

'''
'''
class SampleClass:
    def __init__ (self, val):
        self.val = val
        
object_1 = SampleClass (0)
object_2 = SampleClass (2)
object_3 = object_1
object_3.val += 1

print(object_1 is object_2)
print(object_2 is object_3)
print(object_3 is object_1)
print(object_1.val, object_2.val, object_3.val)

string_1 = "Mary had a little "
string_2 = "Mary had a little lamb"
string_1 += "lamb"

print(string_1 == string_2, string_1 is string_2)
'''
'''
#yeild
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2

for v in powers_of_2(3):
    print(v)

'''
'''
def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power
fsqr = make_closure(2)
fcub = make_closure(3)
for i in range(5):
    print(i, fsqr(i), fcub(i))
'''
'''
st = open ("lab6.txt" , mode = 'r', encoding = None)
print (st.read())
st.close()
'''
'''
from os import strerror

try:
    bf = open('d1.bin', 'rb')
    data = bytearray(bf.read())
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
        print("I/O error occurred:", strerror(e.errno))
'''
