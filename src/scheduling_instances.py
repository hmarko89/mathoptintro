import random

def random_single_machine_instance( n:int= 20, seed:int= 0 ) -> tuple[list[int],list[int],list[int],list[int]]:
    """
    Generates random instance for single machine scheduling problems, based on:
    
    Keha, A. B., Khowala, K., & Fowler, J. W. (2009).
    *Mixed integer programming formulations for single machine scheduling problems*.
    Computers & Industrial Engineering, 56(1), 357-367.
    
    Args
    ----
    n: int
        Desired number of jobs. Should be a positive integer (not checked).
    seed: int
        Random seed.

    Returns
    -------
    proc_times: list[int]
        Processing times: proc_times[j] is the processing time of job j (j=0,...,n-1).
    weights: list[int]
        Weights: weights[j] is the weight of job j (j=0,...,n-1).
    due_dates: list[int]
        Due dates: due_dates[j] is the due date of job j (j=0,...,n-1).
    release_times: list[int]
        Release times: release_times[j] is the release time of job j (j=0,...,n-1).
    """
    random.seed(seed)

    N = range(n)
    L = 0.5
    R = 0.8
    Q = 0.4

    # For each job an integer processing time is generated from uniform distribution [1,100],
    # and an integer weight is generated from the uniform distribution [1,10].
    proc_times = [ random.randint(1,100) for _ in N ]
    weights = [ random.randint(1,10) for _ in N ]

    # The due date of a job is an integer generated from the uniform distribution [P(L-R/2),P(L+R/2)],
    # where P is the sum of processing times of all jobs
    # and the two parameters L and R are relative measures of the location and range of the distribution, respectively.
    # We choose L from the set {0.5,0.7}, R is chosen from the set {0.4,0.8,1.4}.
    P = sum( proc_times )
    due_dates = [ random.randint( int(P*(L-R/2)), int(P*(L+R/2)) ) for _ in N ]

    # The release date of a job is an integer generated from the uniform distribution [0,QP],
    # where P is the sum of processing times of all the jobs
    # and the parameter Q defines the range of the distribution.
    # Q is taken as 0.4.
    release_times = [ random.randint( 0, int(P*Q) ) for _ in N ]

    return proc_times, weights, due_dates, release_times

def random_upmsp_instance( n:int= 15, m:int= 5, seed:int= 0 ) -> tuple[list[list[int]],list[list[list[int]]]]:
    """
    Generates random instance for the Unrelated Parallel Machine Scheduling Problem with machine- and sequence-dependent setup times
    based on:
    
    Tran, T. T., Araujo, A., & Beck, J. C. (2016).
    *Decomposition methods for the parallel machine scheduling problem with setups*.
    INFORMS Journal on Computing, 28(1), 83-95.

    Args
    ----
    n: int
        Desired number of jobs. Should be a positive integer (not checked).
    m: int
        Desired number of machines. Should be a positive integer (not checked).
    seed: int
        Random seed.

    Returns
    -------
    proc_times: list[list[int]]
        Processing times: proc_times[i][j] is the processing time of job j (j=0,...,n-1) on machine i (i=0,...,m-1).
    setup_times: list[list[list[int]]]
        Setup times: setup_times[i][j][k] is the setup time of from job j (j=0,...,n) to job k (k = 0,...,n-1) on machine i (i=0,...,m-1),
        where setup_times[i][n][k] refers to the case when job k is the first job to be processed on machine i.
    """
    random.seed(seed)

    JOBS = range(n)
    EXTENDED_JOBS = range(n+1)
    MACHINES = range(m)

    # Processing times for each machine-job pair were generated from a uniform distribution between 5 and 200.
    proc_times = [ [ random.randint(5,200) for j in JOBS ] for i in MACHINES ]

    # To obtain setup times that were sequence dependent and follow the triangular inequality assumption,
    # each job was given two different sets of coordinates on a Cartesian plane for every machine.
    # The coordinates along the x and y axis are chosen using a uniform distribution between [0,50].
    coordinates_1 = [ [ ( random.randint(0,50), random.randint(0,50) ) for _ in EXTENDED_JOBS ] for _ in MACHINES ]
    coordinates_2 = [ [ ( random.randint(0,50), random.randint(0,50) ) for _ in JOBS ] for _ in MACHINES ]

    # The setup times are the Manhattan distances from one job’s coordinates to the others.    
    # Distances between the second set of coordinates are used to provide asymmetric setup times
    # by linearly scaling a distance of 0 to the LB of the setup time distribution and 100 to the upper bound.
    # We set our setup times to be between 25 and 50
    def setup_time( i:int, j:int, k:int ) -> int:
        if j == k:
            return 0
        
        if j < k or j == n:
            return 25 + int(0.25 * (abs(coordinates_1[i][j][0] - coordinates_1[i][k][0]) + abs(coordinates_1[i][j][1] - coordinates_1[i][k][1])))
        
        return 25 + int(0.25 * (abs(coordinates_2[i][j][0] - coordinates_2[i][k][0]) + abs(coordinates_2[i][j][1] - coordinates_2[i][k][1])))

    setup_times = [ [ [ setup_time(i,j,k) for k in JOBS ] for j in EXTENDED_JOBS ] for i in MACHINES ]
    
    return proc_times, setup_times
