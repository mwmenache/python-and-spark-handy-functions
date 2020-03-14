def _logtime(start, comment):

    """ measures and prints the elapsed time 

   Print the elapsed time (in seconds) between 'now' and 'start', and reurns 'now', where :
   - 'now' is the time _log_logtime is calles
   - 'start' is a parameter to the function
   Example:
    "Real Time : Start Spark Session took : 5 seconds"
    This can be used to optimize a long runngin code by identifying which step of the code is time consuming
    Use cases :  
        - call _logtime() rigtht before and after a bit of code you want to measure the duration of
        - create start_time = time.time() at the beginning of your code, and call _logtime() at the ends
        to print the total duration of your code

    Parameters
    ----------
    start : DateTime
        The moment since when you want to measure how much time elapsed.
        e.g : time.time() or the result returnned by a previous call of _logtime()
    comment : String
         A comment you want to see printed, describing the step you want to measure the duration of
         e.g "Start Spark Session"
        
    Returns
    -------
    now : DateTime
        The tiem when _logtime() was called


    Examples
    --------
    start_time = time.time()
        
    features = spark.read.parquet("/projects/loyalty/share/Big W SOW/Feature files/explanatory varibles/ALL_features.parquet")
    ctime = _logtime(start_time, 'Load Features_ini file')
    
    features.count()
    ctime = _logtime(x, 'Count CRNs')    

    """
    now = time.time()
    print("Real Time : " + comment + " took : " + str(math.trunc(now - start)) + " seconds")

    return now