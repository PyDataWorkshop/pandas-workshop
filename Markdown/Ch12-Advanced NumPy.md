Chapter 12 Advanced NumPy
===========================
- ndarray Object Internals
- Advanced Array Manipulation
- Broadcasting
- Advanced ufunc Usage
- Structured and Record Arrays
- More About Sorting
- NumPy Matrix Class
- Advanced Array Input and Output
- Performance Tips

<hr>
### `ndarray` Object Internals
- The NumPy ndarray provides a means to interpret a block of homogeneous data (either
contiguous or strided, more on this later) as a multidimensional array object. 
- As you’ve seen, the data type, or dtype, determines how the data is interpreted as being floating
point, integer, boolean, or any of the other types we’ve been looking at.
- Part of what makes ndarray powerful is that every array object is a strided view on a
block of data. You might wonder, for example, how the array view `arr[::2, ::-1]` does
not copy any data. 
- Simply put, the `ndarray` is more than just a chunk of memory and
a dtype; it also has striding information which enables the array to move through
memory with varying step sizes.
<hr>
