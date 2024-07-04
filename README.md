# Conway's Game of Life
A Python Script That Makes The Conway's Game of Life!

## How It Works

### Instaling The Libraries

First of all get the libraries needed by using `pip install -r requirements.txt` in your terminal! Then just open **main.py** and run it!  
  
### Creating a **venv**

I recommend creating a **venv** for this project, you can do so by using this command `python -m venv myenv` and then activate it by using this command `myenv\Scripts\activate`! Now you can use this **venv** to **install the libraries on this project!**

### Understanding The Code

First we create a grid of squares that we will call cells! For each cell if it's alive the color of the cell will be white, if it's dead then the color of the cell will be black!  
To create the celluar automaton the scripts uses the Conway's Rules:
* A live cell dies if it has fewer than two live neighbors.
* A live cell with two or three live neighbors lives on to the next generation.
* A live cell with more than three live neighbors dies.
* A dead cell will be brought back to live if it has exactly three live neighbors.


## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

### Compliance with License

If you use or distribute this project, you agree to comply with the terms of the above-mentioned license. Specifically, you must:

- Include the original copyright notice in any copy of the project or substantial portion of it.
- Indicate any changes made to the project.
- Provide a copy of the license with the project.

Please refer to the [LICENSE](./LICENSE) file for more information on your rights and obligations under the terms of the MIT License.

## From The Creator

### Why I Did Make This Project

Like many of you guys I like to challenge my self and make cool projects!  
In this case I specifically made this project because I was inspired by the way Conway's Game of Life works!

### How To Make This Project Cooler

If you want to make **more features** to this code I recommend trying to make an mostly infinite grid, for this you would really need to optimize my code, because this code was made to be small and easy to understand! You could also make tools to move the camera, zoom in and zoom out!

### **Made by Dauwt**

### Copyright (c) 2024 Dauwt
