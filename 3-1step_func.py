def step_function(x):
    # 引数に実数しか対応できない(numpy配列を受け付けない)
    if x > 0:
        return 1
    else:
        return 0
