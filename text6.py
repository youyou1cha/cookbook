#!/usr/bin/env python
# -*- coding: utf-8 -*-

# round 四舍五入
# format 格式化
# decimal
from decimal import Decimal
from decimal import localcontext

a = Decimal('1.3')
b = Decimal('1.7')
# 上下文
with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)

with localcontext() as ctx:
    ctx.prec = 10
    print(a / b)
