Chapter 8 Plotting and Visualization
======================================
- A Brief matplotlib API Primer
- Plotting Functions in pandas
- Plotting Maps: Visualizing Haiti Earthquake Crisis Data
- Python Visualization Tool Ecosystem

<hr>
- Making plots and static or interactive visualizations is one of the most important tasks
in data analysis. It may be a part of the exploratory process; for example, helping identify
outliers, needed data transformations, or coming up with ideas for models. 
- For
others, building an interactive visualization for the web using a toolkit like ***d3.js*** (http:
//d3js.org/) may be the end goal. Python has many visualization tools (see the end of
this chapter), but I’ll be mainly focused on matplotlib (**http://matplotlib.sourceforge
.net**).
- matplotlib is a (primarily 2D) desktop plotting package designed for creating publication-
quality plots. The project was started by John Hunter in 2002 to enable a MATLAB-
like plotting interface in Python. He, Fernando Pérez (of IPython), and others have
collaborated for many years since then to make IPython combined with matplotlib a
very functional and productive environment for scientific computing. When used in
tandem with a GUI toolkit (for example, within IPython), matplotlib has interactive
features like zooming and panning. 
- It supports many different GUI backends on all operating systems and additionally can export graphics to all of the common vector and raster graphics formats: PDF, SVG, JPG, PNG, BMP, GIF, etc. I have used it to
produce almost all of the graphics outside of diagrams in this book.
matplotlib has a number of add-on toolkits, such as mplot3d for 3D plots and basemap
for mapping and projections. 
- I will give an example using basemap to plot data on a map and to read shapefiles at the end of the chapter.
- To follow along with the code examples in the chapter, make sure you have started
IPython in Pylab mode (ipython --pylab) or enabled GUI event loop integration with
the `%gui` magic.
