c = 1 #Stores count of the solutions.
d = 1

class SolveNqueen() :
    #Initialize the variables of class that is board and board size.
    def __init__(self,n) :
        self.size = n
        self.board = [[0 for i in range(0,n)] for j in range(0,n)]
    
    #When a solution is found, this function is called to print it.
    def myPrintSolution(self) :
        global c,d
        print("solution number - ",c,"\n")
        c = c + 1
        for i in range(0,self.size) :
            for j in range(0,self.size) :
                print(self.board[i][j], end = " ")
            print("\n")
        #This part checks if the found out solution is toroidal solution or not.
        if self.CheckToroidal() == True :
            print("This is also a toroidal solution, solution number - ",d)
            d = d + 1
        print("\n")
    
    #We adopt approach of placing queen from leftmost column. 
    #So we check via this function, whether any constraint is violated while placing the new queen.
    def myQueenSafe(self, row, column) :
        #Check that row on the left side for violation.
        for p in range(0,column) :
            if self.board[row][p] == 1 :
                return False

        #Check lower diagonal on left side for violation.
        k = row
        l = column
        while l >= 0 and k < self.size :
            if self.board[k][l] == 1 :
                return False
            k = k + 1
            l = l - 1

        #Check upper diagonal on left side.
        k = row
        l = column
        while k >= 0 and l >= 0 :
            if self.board[k][l] == 1 :
                return False
            k = k - 1
            l = l - 1

        #If none of the above returns False, then it is safe to place the queen.
        return True

    def mySolveNqueen(self, column) :
        #This part means all queens are placed and you can print the solution obtained.
        if column == self.size :
            self.myPrintSolution()
            return True

        result = False
        for i in range(0,self.size) :
            if self.myQueenSafe(i, column) == True :
                self.board[i][column] = 1
                result = self.mySolveNqueen(column + 1) or result       #Checks recursively one level further.
                self.board[i][column] = 0   #Here the backtracking occurs on the state-tree.

        return result

    def mySolve(self) :
        if self.mySolveNqueen(0) == False :
            print("Solution does not exist for this board size")
            return 

    #This function does the actual checking part that whether an obtained solution is toroidal or not.
    def CheckToroidal(self) :
        p = self.size % 6
        if p == 0 or p == 2 or p == 3 or p == 4 :
            return False
        else :
            for i in range(0,self.size) :
                j = (self.board[i]).index(1)
                p = i
                q = j
                #Checks right-to-left spiral extended diagonal.
                for k in range(0, self.size - 1) :
                    p = (p + 1) % self.size
                    q = (q + 1) % self.size
                    if self.board[p][q] == 1 :
                        return False
                p = i
                q = j
                #Checks left-to-right spiral extended diagonal.
                for k in range(0, self.size - 1) :
                    p = (p + 1) % self.size
                    q = (q - 1) % self.size
                    if self.board[p][q] == 1 :
                        return False
            return True

if __name__ == "__main__" :
    n = int(input("Enter Size of the board\n"))     #Take board size as user input.
    NQ = SolveNqueen(n)
    NQ.mySolve()
