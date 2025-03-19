import gc

print(gc.get_threshold())  # (700, 10, 10)

"""
Set the garbage collection thresholds (the collection frequency). Setting threshold0 to zero disables collection.

The GC classifies objects into three generations depending on how many collection sweeps they have survived. 
New objects are placed in the youngest generation (generation 0). If an object survives a collection it is moved into 
the next older generation. Since generation 2 is the oldest generation, objects in that generation remain there after 
a collection. In order to decide when to run, the collector keeps track of the number object allocations 
and deallocations since the last collection. When the number of allocations minus the number of deallocations 
exceeds threshold0, collection starts. Initially only generation 0 is examined. If generation 0 has been examined 
more than threshold1 times since generation 1 has been examined, then generation 1 is examined as well. 
With the third generation, things are a bit more complicated, see Collecting the oldest generation for more information.

https://docs.python.org/3/library/gc.html
"""
gc.set_threshold(500, 10, 10)
print(gc.get_threshold())
