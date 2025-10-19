import random, os, msvcrt

WIDTH, HEIGHT = 25, 15
DIRS = [(-1,0),(1,0),(0,-1),(0,1)]

def make_maze(w,h):
    maze=[[1]*w for _ in range(h)]
    stack=[(1,1)]; maze[1][1]=0
    while stack:
        x,y=stack[-1]; neighbors=[]
        for dx,dy in DIRS:
            nx,ny=x+dx*2, y+dy*2
            if 0<nx<w-1 and 0<ny<h-1 and maze[ny][nx]==1:
                neighbors.append((nx,ny,dx,dy))
        if neighbors:
            nx,ny,dx,dy=random.choice(neighbors)
            maze[y+dy][x+dx]=0; maze[ny][nx]=0
            stack.append((nx,ny))
        else:
            stack.pop()
    maze[h-2][w-2]=9
    return maze

def draw_maze(maze, player_pos):
    os.system('cls')
    for i,row in enumerate(maze):
        line=""
        for j,c in enumerate(row):
            if [i,j]==player_pos: line+="P"
            elif c==1: line+="█"
            elif c==9: line+="G"
            else: line+="."
        print(line)

maze = make_maze(WIDTH, HEIGHT)
player_pos = [1,1]

while True:
    draw_maze(maze, player_pos)
    if maze[player_pos[0]][player_pos[1]]==9:
        print("🎉 You reached the goal!")
        break
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8').lower()
            x,y = player_pos
            if key=='w': nx,ny=x-1,y
            elif key=='s': nx,ny=x+1,y
            elif key=='a': nx,ny=x,y-1
            elif key=='d': nx,ny=x,y+1
            else: nx,ny=x,y
            if 0<=nx<HEIGHT and 0<=ny<WIDTH and maze[nx][ny]!=1:
                player_pos=[nx,ny]
            break
