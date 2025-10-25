import random
import matplotlib.pyplot as plt

def generate_maze(w, h, seed=-1):
    if seed!=-1:
        random.seed(seed)
    else:
        random.seed()
    W,H=w*2+1,h*2+1
    maze=[[1]*W for _ in range(H)] # 1 meaning wall, 0 meaning passage
    def carve(x, y):
        dirs=[(0,2),(0,-2),(2,0),(-2,0)]
        random.shuffle(dirs)
        for dx,dy in dirs:
            nx,ny=x+dx, y+dy
            if 0<nx<W-1 and 0<ny<H-1 and maze[ny][nx]==1:
                maze[y+dy//2][x+dx//2] = 0
                maze[ny][nx] = 0
                carve(nx,ny) #recursive structure
    #start at random cell need to ensure odd coords
    sx,sy=random.randrange(1,W,2),random.randrange(1,H,2)
    maze[sy][sx]=0
    carve(sx,sy) #first call
    #opening for start and exit
    maze[1][0] = 0
    maze[H-2][W-1] = 0
    ascii_maze=[]
    for y in range(H):
        row=[]
        for x in range(W):
            if(y,x)==(1,0):
                row.append('S')
            elif (y,x)==(H-2, W-1):
                row.append('E')
            else:
                row.append('#' if maze[y][x] else ' ')
        ascii_maze.append(''.join(row))
    print("ASCII Maze:\n")
    for r in ascii_maze:
        print(r)
    print()
    #display in matplotlib for visually cleaner output
    plt.figure(figsize=(w/2.5,h/2.5))
    plt.axis('off')
    plt.title(f"ASCII Maze ({w}x{h})",fontsize=10,pad=10)
    plt.text(
        0.5, 0.5,
        "\n".join(ascii_maze),
        fontfamily='monospace',
        fontsize=8,
        va='center',
        ha='center',
        color='black',
        linespacing=0.6,
        wrap=True,
    )
    plt.gca().set_facecolor("white")
    plt.show()
if __name__=="__main__":
    w=int(input("Enter width: "))
    h=int(input("Enter height: "))
    s=int(input("Enter seed or -1 if random: "))
    generate_maze(w,h,s)
