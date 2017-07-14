# IPython log file

a = get_ipython().getoutput('ipython')
a
y
a
a y
foo = 'test*)
foo = 'test*'
get_ipython().system('ls $foo')
get_ipython().magic('cd d')
get_ipython().magic('bookmark d /Users/wonderful/Desktop')
get_ipython().magic('cd d')
get_ipython().magic('bookmark -d d')
get_ipython().magic('cd d')
get_ipython().magic('bookmark d /Users/wonderful/Desktop')
get_ipython().magic('cd d')
get_ipython().magic('cd d')
get_ipython().magic('bookmark -l')
strings = ['foo', 'foobar', 'baz', 'qux', 'python', 'Gui Van Rossum'] * 100000
method1 = [x for x in strings if x.startswith('foo')]
method2 = [x for x in strings if x[:3] == 'foo']
get_ipython().magic("time method1 = [x for x in strings if x.startswith('foo')]")
get_ipython().magic("time method2 = [x for x in strings if x[:3] == 'foo']")
get_ipython().magic("timeit method1 = [x for x in strings if x.startswith('foo')]")
get_ipython().magic("timeit method2 = [x for x in strings if x[:3] == 'foo']")
x = 'foobar'
y = 'foo
y = 'foo'
get_ipython().magic('timeit x.startswith(x)')
get_ipython().magic('timeit x[:3] == y')
python -m cProfile /Users/wonderful/Desktop/cprof_example.py 
python -m cProfile /Users/wonderful/Desktop/cprof_example.py
get_ipython().magic('prun -l 7 -s cumulative /Users/wonderful/Desktop/cprof_example.py')
get_ipython().magic('cd d')
get_ipython().magic('prun -l 7 -s cumulativecprof_example.p')
get_ipython().magic('prun -l 7 -s cumulative cprof_example.py')
get_ipython().magic('run /Users/wonderful/Desktop/cprof_example.py')
get_ipython().magic('run /Users/wonderful/Desktop/cprof_example.py')
get_ipython().magic('run /Users/wonderful/Desktop/cprof_example.py')
get_ipython().magic('prun -l 7 -s cumulative /Users/wonderful/Desktop/cprof_example.py')
get_ipython().magic('prun -l 7 -s cumulative /Desktop/cprof_example.py')
get_ipython().magic('prun -l 7 -s cumulativec prof_example.py')
get_ipython().magic('cpaste')
get_ipython().magic('prun -l 7 -s cumulativec run_expereiment()')
get_ipython().magic('prun -l 7 -s cumulative run_expereiment()')
get_ipython().magic('run -p -s cumulative /Users/wonderful/Desktop/cprof_example.py')
get_ipython().magic('log')
get_ipython().magic('logstart')
get_ipython().magic('logstop')
