# 09_분할정복



#### 거듭 제곱 1

```python
def Power(Base, Exponent):
    if Base == 0:
        return 1
    result = 1 
    for i in range(Exponent):
        result *= Base
    return result
```



#### 거듭제곱 2(분할정복)

```python
def Power(Base, Exponent):
    if Exponent == 0 or Base == 0:
        return 1
    
    if Exponent % 2 == 0:
        NewBase = Power(Base, Exponent/2)
        return NewBase * NewBase
   	else:
        NewBase = Power(Base, (Exponent-1)/2)
        return (NewBase * NewBase) * Base
```

