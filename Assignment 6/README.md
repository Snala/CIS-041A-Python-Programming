Design and implement a program to draw x/y plots. Your program will read a file of X/Y coordinates and plot them on the window frame. The files to plot are in the DataFiles folder on Canvas: Sin.csv, Cos.csv, Square.csv, Cube.csv, Polynomial.csv and your program should be able to read and plot any of the files.  At the intersection of each line, draw the shape of your choice (like a circle, triangle or rectangle).  You may find that overloading of some operators makes plotting techniques easier.
Your program will design and implement several classes to do the plotting.  Suggested classes:
* Write a UDT (user defined type) that manages the files. 
* Write a UDT that manages X and Y Cartesian coordinate pairs.
* Write a UDT that draws a line between two points.
* Write a UDT that draws a Plot Graph

See the PlotFunc.py and Geometry.py examples for guidelines on creating the classes.  Some of the classes can be used as-is, or even refactored.  Use comprehensions where applicable.
The data will need to be scaled to fit the screen. Here is a data file excerpt:
        
        (0,1)
        (5,0.996195)
        (10,0.984808)
        (15,0.965926)
        (20,0.939693)
        (25,0.906308)
        (30,0.866026)
        (35,0.819152)
        (40,0.766045)
        (45,0.707107)
        (50,0.642788)
        (55,0.573577)
        (60,0.500001)
        (65,0.422619)
        (70,0.342021)
        (75,0.25882)
        (80,0.173649)
        (85,0.087157)
        (90,0)
        
Notice in this excerpt the Y coordiates are, while the X coordiates are between 0 and 90. If the Y coordinates were plotted without scaling, a flat line would be drawn.  Note the X coordinates will require some scaling to fit the screen.