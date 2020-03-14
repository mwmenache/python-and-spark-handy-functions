def _log(thing, logfile):

    """ logs to a file 
    
    _log is nothing but the print() function in which what is printed is redirected to a file.
    This is used for logging: if you run a loing code, you can use _log() to print whatever checks are required
    to ensure the code ran correctly in a file.
    Note that _log() will append the file if it already exists.
    
    Parameters
    ----------
    - thing : Anything printable object
    the 'thing' you want to print and log.
    
    - logfile: String
    the full filename and path of the file where you want to log the results
    
    Returns
    -------
    - nothing is retruned, but 'thing' gets printed to your logfile
    
    Examples
    --------
    logfile = "/projects/loyalty/share/Big_W/201808_Lapsed/01_Code/01_Data_extraction.log"
    # start logging
    _log(datetime.now())
    # Log anything
    _log("Hello!"
    _log(df.shape)
    _proc_contents(df)

    """
    f=open(logfile, "a+")
    print(thing, file=f)
    f.close()
