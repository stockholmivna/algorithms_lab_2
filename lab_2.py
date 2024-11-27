import matplotlib.pyplot as plt #import matlib to plot the points

def read_dataset(file_path): #function to read the dataset
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(int, line.strip().split()) #split the points and convert them to integers
            points.append((x, y)) #append the points to the list
    return points

def plot_points(points, canvas_size=(960, 540)): #functiom to make canvas size
    
    plt.figure(figsize=(canvas_size[0]/100, canvas_size[1]/100)) #set the figure size
    x_coords, y_coords = zip(*points)

    plt.scatter(x_coords, y_coords, s=1, color='pink')  #color and size of the points
    plt.title("Graph")
    plt.xlabel("Ox")
    plt.ylabel("Oy")
    plt.grid(True) #to show the grid
    plt.xlim(0, canvas_size[0])  #limit of Ox
    plt.ylim(0, canvas_size[1]) #limit of Oy

    #save a graph as an image
    plt.savefig("ds4.png", dpi=100)
    plt.show()

if __name__ == "__main__":

    dataset_path = "DS4.txt"
    points = read_dataset('DS4.txt')
    plot_points(points)