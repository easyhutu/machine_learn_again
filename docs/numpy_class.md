shape 属性
对于shape函数，官方文档是这么说明：

the dimensions of the array. This is a tuple of integers indicating the size of the array in each dimension.

直译：数组的维度。这是一个整数的元组，元组中的每一个元素对应着每一维度的大小(size)。
```
import numpy as np
a = np.array([1,2,3])
print(a.shape) # 输出 (3,)
```


用法：zeros(shape, dtype=float, order='C')

返回：返回来一个给定形状和类型的用0填充的数组；