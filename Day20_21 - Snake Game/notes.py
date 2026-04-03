# inheritance related
# always use self

class Animal:
    def __init__(self):
        self.whoami = 'an animal'
    
    def imwho(self):
        print(self.whoami)

    def breathe(self):
        print("i breathe like this: ")

class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.type = 'water'
    
    def intro(self):
        self.imwho()
        print("i live in ", self.type)

    def breathe(self):
        super().breathe()
        print("blubub blubub")

nemo = Fish()
nemo.intro()
nemo.breathe()

"""
====================================================
PYTHON SLICING – COMPLETE POC (COPY & RUN)
====================================================
This file demonstrates ALL slicing concepts in Python
with examples and printed outputs.
====================================================
"""

print("\n===== 1. BASIC SETUP =====")
text = "PYTHON"
nums = [0, 1, 2, 3, 4, 5, 6]

print("text =", text)
print("nums =", nums)

# --------------------------------------------------

print("\n===== 2. BASIC SLICING =====")
print("text[0:3]  ->", text[0:3])   # PYT
print("text[2:5]  ->", text[2:5])   # THO
print("text[:4]   ->", text[:4])    # PYTH
print("text[3:]   ->", text[3:])    # HON
print("text[:]    ->", text[:])     # PYTHON (copy)

# --------------------------------------------------

print("\n===== 3. STEP (STRIDE) SLICING =====")
print("text[::1]  ->", text[::1])   # normal
print("text[::2]  ->", text[::2])   # PTO
print("text[1::2] ->", text[1::2])  # YHN

# --------------------------------------------------

print("\n===== 4. NEGATIVE INDEXING =====")
print("text[-1]   ->", text[-1])    # N
print("text[-3:]  ->", text[-3:])   # HON

# --------------------------------------------------

print("\n===== 5. REVERSE SLICING =====")
print("text[::-1]    ->", text[::-1])     # reverse
print("text[5:2:-1] ->", text[5:2:-1])    # NOH
print("nums[::-1]   ->", nums[::-1])      # reverse list

# --------------------------------------------------

print("\n===== 6. LIST SLICING =====")
print("nums[2:5] ->", nums[2:5])    # [2,3,4]
print("nums[:3]  ->", nums[:3])     # [0,1,2]
print("nums[::2] ->", nums[::2])    # [0,2,4,6]

# --------------------------------------------------

print("\n===== 7. SLICING CREATES A COPY =====")
a = [1, 2, 3, 4]
b = a[:]          # copy list
b[0] = 99

print("Original a ->", a)
print("Copied b   ->", b)

# --------------------------------------------------

print("\n===== 8. SLICE ASSIGNMENT (LIST ONLY) =====")
nums2 = [1, 2, 3, 4, 5]

# Replace part of list
nums2[1:4] = [20, 30, 40]
print("Replace slice ->", nums2)

# Replace with fewer elements
nums2[1:3] = [9]
print("Fewer elements ->", nums2)

# Replace with more elements
nums2[1:2] = [7, 8, 9]
print("More elements ->", nums2)

# --------------------------------------------------

print("\n===== 9. DELETE USING SLICING =====")
nums3 = [1, 2, 3, 4, 5]
del nums3[1:4]
print("After delete ->", nums3)

# --------------------------------------------------

print("\n===== 10. INDEXING VS SLICING =====")
s = "ABC"
print("s[1]   ->", s[1])     # single element
print("s[1:2] ->", s[1:2])   # slice (still string)

# --------------------------------------------------

print("\n===== 11. OUT-OF-RANGE SAFETY =====")
print("text[0:100] ->", text[0:100])  # safe
print("text[100:]  ->", text[100:])   # empty string

# --------------------------------------------------

print("\n===== 12. RANGE SLICING =====")
r = range(10)
print("list(r[2:8:2]) ->", list(r[2:8:2]))

# --------------------------------------------------

print("\n===== 13. SLICE OBJECT =====")
sl = slice(1, 5, 2)
print("text[slice(1,5,2)] ->", text[sl])

# --------------------------------------------------

print("\n===== 14. COMMON IDIOMS =====")
print("Reverse sequence ->", nums[::-1])
print("Copy list ->", nums[:])
print("Skip every other ->", nums[::2])
print("Remove first & last ->", nums[1:-1])

# --------------------------------------------------

print("\n===== END OF SLICING DEMO =====")
