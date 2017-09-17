* ### Compromized primary will keep sending old unchanged md5sums every t units of time.
__Solution__: salted hashes of files. Random salts generated at secondary, sent every time to primary just before calculation of md5sums.  
__Why is this a solution?__  
It forces primary to recalculate hashes, which means it proves existance of files at this instant.
