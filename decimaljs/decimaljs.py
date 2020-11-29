import js2py
import os


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Decimal(metaclass=Singleton):
    context = js2py.EvalJs()
    path = os.path.abspath(".")
    with open(f"{path}/decimal.js") as f:
        js_code = f.read()
    context.execute(js_code)

    # methods
    abs = context.Decimal.abs
    acos = context.Decimal.acos
    acosh = context.Decimal.acosh
    add = context.Decimal.add
    asin = context.Decimal.asin
    asinh = context.Decimal.asinh
    atan = context.Decimal.atan
    atanh = context.Decimal.atanh
    atan2 = context.Decimal.atan2
    cbrt = context.Decimal.cbrt
    ceil = context.Decimal.ceil
    clone = context.Decimal.clone
    cos = context.Decimal.cos
    cosh = context.Decimal.cosh
    div = context.Decimal.div
    exp = context.Decimal.exp
    floor = context.Decimal.floor
    hypot = context.Decimal.hypot
    isDecimal = context.Decimal.isDecimal
    ln = context.Decimal.ln
    log = context.Decimal.log
    log2 = context.Decimal.log2
    log10 = context.Decimal.log10
    max = context.Decimal.max
    min = context.Decimal.min
    mod = context.Decimal.mod
    mul = context.Decimal.mul
    noConflict = context.Decimal.noConflict
    pow = context.Decimal.pow
    random = context.Decimal.random
    round = context.Decimal.round
    set = context.Decimal.set
    sign = context.Decimal.sign
    sin = context.Decimal.sin
    sinh = context.Decimal.sinh
    sqrt = context.Decimal.sqrt
    sub = context.Decimal.sub
    tan = context.Decimal.tan
    tanh = context.Decimal.tanh
    trunc = context.Decimal.trunc


if __name__ == "__main__":
    print(Decimal.pow(2, 4))
    print(Decimal.pow(2, 100))