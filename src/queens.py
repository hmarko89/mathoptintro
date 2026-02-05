from ortools.sat.python import cp_model

class QueensSolutionCallback( cp_model.CpSolverSolutionCallback ):
    """
    Solution printer for n-queens.

    Attributes
    ----------
    x : list[IntVar]
        List of variables: x[i] = j if and only if the queen of row i is in column j.
    nsols : int
        Number of found solutions.
    """
    def __init__( self, x ):
        super().__init__()

        self.x = x
        self.nsols = 0

    @property
    def number_of_solutions( self ):
        return self.nsols

    def on_solution_callback( self ):
        """
        Draws solution (called by the solver for each feasible solution found).
        """
        CHARS = '·×' # empty | queen

        self.nsols += 1
        
        print( f'solution #{self.nsols}:' )
        for i in range(len(self.x)):
            print( ' '.join( [ CHARS[1] if self.Value(self.x[i]) == j else CHARS[0] for j in range(len(self.x)) ] ) ) 
        print( '' )

def solve_queens_cp( n:int ) -> None:
    """
    Solves the n-queens puzzle as a CP with Google OR-Tools CP-SAT.

    Args
    ----
    n : int
        The size of the board (and the number of queens).
    """
    # BUILD MODEL
    model = cp_model.CpModel()

    # variables: x[i] = j if and only if the queen of row i is in column j
    # NOTE: by definition, there is only one queen in each row
    x = [ model.new_int_var( 0, n-1, f'x_{i}' ) for i in range(n) ]
 
    # constraints: queens cannot share columns
    model.add_all_different( x )

    # constraints: queens cannot share / diagonals
    model.add_all_different( x[i] + i for i in range(n) )
    
    # constraints: queens cannot share \ diagonals
    model.add_all_different( x[i] - i for i in range(n) )

    # SOLVE PROBLEM
    solver = cp_model.CpSolver()
    solver.parameters.enumerate_all_solutions = True
    cb = QueensSolutionCallback(x)
    status = solver.Solve( model, solution_callback= cb )

    print( f'status: {solver.status_name(status)} | total time: {solver.WallTime():.2f} | number of solutions: {cb.number_of_solutions}' )

def solve_queens_mip( n:int ) -> None:
    """
    Solves the n-queens puzzle as a MIP with Google OR-Tools MathOpt.

    Args
    ----
    n : int
        The size of the board (and the number of queens).
    """
    from ortools.math_opt.python import mathopt
    
    print( 'TODO: implement queens mip solver!' )

if __name__ == '__main__':
    solve_queens_cp( 5 )
