import tkinter as tk, random, tkinter.messagebox as mb

class SlidingPuzzle:
    def __init__(self, master, size=3):
        self.master, self.size = master, size
        self.master.title(f"{size}x{size} Sliding Puzzle")
        self.tiles, self.moves = [], 0
        self.frame = tk.Frame(master); self.frame.pack(pady=10)
        self.info = tk.Label(master, text=f"Moves: {self.moves}", font=("Helvetica",14))
        self.info.pack()
        tk.Button(master,text="Restart",command=self.restart).pack(pady=5)
        self.create_tiles(); self.shuffle_tiles()

    def create_tiles(self):
        nums = list(range(1,self.size*self.size)) + [0]
        self.board = [nums[i*self.size:(i+1)*self.size] for i in range(self.size)]
        self.empty = (self.size-1,self.size-1)
        for i in range(self.size):
            row=[]
            for j in range(self.size):
                n=self.board[i][j]
                btn = tk.Button(self.frame,text=str(n),width=6,height=3,font=("Helvetica",24),
                                command=lambda r=i,c=j:self.move_tile(r,c)) if n else None
                if btn: btn.grid(row=i,column=j,padx=2,pady=2)
                row.append(btn)
            self.tiles.append(row)

    def shuffle_tiles(self):
        for _ in range(1000): self.move_empty(random.choice(['up','down','left','right']))
        self.moves=0; self.info.config(text=f"Moves: {self.moves}")

    def move_empty(self,d):
        ei,ej=self.empty; ni,nj=ei,ej
        if d=='up': ni+=1
        if d=='down': ni-=1
        if d=='left': nj+=1
        if d=='right': nj-=1
        if 0<=ni<self.size and 0<=nj<self.size: self.swap_tiles(ei,ej,ni,nj); self.empty=(ni,nj)

    def swap_tiles(self,i1,j1,i2,j2):
        b1,b2=self.tiles[i1][j1],self.tiles[i2][j2]
        if b1: b1.grid(row=i2,column=j2)
        if b2: b2.grid(row=i1,column=j1)
        self.tiles[i1][j1],self.tiles[i2][j2]=self.tiles[i2][j2],self.tiles[i1][j1]
        self.board[i1][j1],self.board[i2][j2]=self.board[i2][j2],self.board[i1][j1]

    def move_tile(self,i,j):
        ei,ej=self.empty
        if (abs(ei-i)==1 and ej==j) or (abs(ej-j)==1 and ei==i):
            self.swap_tiles(i,j,ei,ej); self.empty=(i,j)
            self.moves+=1; self.info.config(text=f"Moves: {self.moves}")
            if sum(self.board,[])==list(range(1,self.size*self.size))+[0]:
                mb.showinfo("Congrats",f"Puzzle solved in {self.moves} moves!")

    def restart(self):
        for r in self.tiles:
            for b in r: 
                if b: b.destroy()
        self.tiles=[]; self.moves=0; self.info.config(text=f"Moves: {self.moves}")
        self.create_tiles(); self.shuffle_tiles()

if __name__=="__main__":
    root=tk.Tk()
    size=int(input("Enter puzzle size (3 or 4): "))
    SlidingPuzzle(root,size)
    root.mainloop()
