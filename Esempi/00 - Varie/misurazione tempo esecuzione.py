# se voglio verificare quanto tempo ci metto a fare qualcosa posso usare la funzione timeit

import timeit

# print(timeit.timeit("""
# x = 2 + 2
# """, number = 1000000))

print(timeit.timeit("text = 'abcdefg'; s = list(text); s[6] = 'W'; ''.join(s)", number=1000000))
print(timeit.timeit("text = 'abcdefg'; text = text[:1] + 'Z' + text[2:]", number=1000000))
# print(timeit.timeit("text = 'abcdefg'; s = bytearray(text); s[1] = 'Z'; str(s)", number=1000000))







# Note By default, timeit() temporarily turns off garbage collection during the timing. The advantage of this approach is that it makes independent timings more comparable. The disadvantage is that GC may be an important component of the performance of the function being measured. If so, GC can be re-enabled as the first statement in the setup string. For example:
# timeit.Timer('for i in range(10): oct(i)', 'gc.enable()').timeit()
