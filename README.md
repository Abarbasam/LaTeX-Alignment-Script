# LaTeX-Alignment-Script
Python Script that allows you to easily create great looking equations in a LaTeX align environment. This script is specifically designed to allow you to align multiple different equations alongside each other.

If you want to have multiple different equations beside each other, it can be frusturating and confusing to have to write the 1st line of the first equation, then the 1st line of the second equation, and so on. With this script, you can write each equation and its solution(s) in "blocks." The script will align these blocks beside each other, making easy to read text and a good-looking LaTeX document

# How to use it
To use this, you need Python (2.7+ is fine). To run it, type, "align_tool.py <file>"
Here is an example of how the <file> should look

<begin> (Don't include this)
	a)    &
	y & = 3(x + 5)^2 - 8
	y &= 3((x + 5)(x + 5)) - 8
	y &= 3(x^2 + 10x + 25) - 8
	y &= 3x^2 + 30x + 75 - 8
	y &= 3x^2 + 30x + 67
    
& b)    &
& x &= \frac{-b}{2a}
& x &= \frac{-4}{2(-2)}
& x &= \frac{-4}{-4}
& x &= 1  
& &
    
& & \\ 
& y &= -2x^2 + 4x + 7 \\
& y &= -2(1)^2 + 4(1) + 7 \\
& y &= -2 + 4 + 7 \\
& y &= 9 \\
& & 
<end> (Don't include this)

The blocks must ALL be the same length, or else the script will not work. You can have as many blocks as you like, but remember the first block is always indented, and subsequent blocks should have an & at the start of every line. If you need the blocks to be the same length, just add an "& &" as filler. 

Here is what the output of the above example should look like:

<begin>
	a)    &                        & b)    &                   & & \\                    
	y & = 3(x + 5)^2 - 8           & x &= \frac{-b}{2a}        & y &= -2x^2 + 4x + 7 \\        
	y &= 3((x + 5)(x + 5)) - 8     & x &= \frac{-4}{2(-2)}     & y &= -2(1)^2 + 4(1) + 7 \\    
	y &= 3(x^2 + 10x + 25) - 8     & x &= \frac{-4}{-4}        & y &= -2 + 4 + 7 \\            
	y &= 3x^2 + 30x + 75 - 8       & x &= 1                    & y &= 9 \\                     
	y &= 3x^2 + 30x + 67           & &                         & &       
<end>
