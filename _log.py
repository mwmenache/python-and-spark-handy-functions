def _log(thing, logfile):

    """ logs to a file 
    
    _log is nothing but the print() function in which what is printed is redirected to a file.
    This is used for logging: if you run a code, you can use _log() to print in a file and save whatever checks are required
    to ensure the code ran correctly.
    Note that _log() will append the file if it already exists.
    
    Parameters
    ----------
    - thing : Any printable object
    the 'thing' you want to print and log. Can be anything that you'd print with the print() function (string, list, Pandas DataFrame..)
    
    - logfile: String
    the full filename and path of the file where you want to log the results
    
    Returns
    -------
    - nothing is retruned, but 'thing' gets printed to your logfile
    
    Examples
    --------
    f = "./01_Code/01_import_data.log"
    _log("Hello-VS Code!", f)

    """

    f=open(logfile, "a+")
    print(thing, file=f)
    f.close()
