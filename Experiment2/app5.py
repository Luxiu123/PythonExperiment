# -*- coding: UTF-8 -*-
# 编写程序打印九九成法口诀表
print('\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x * y) for y in range(1, x + 1)]) for x in range(1, 10)]))
