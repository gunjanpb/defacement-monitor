## Definitions
- Primary server:  
	Server containing `website data` and `md5sums` and script `p`
- website data:  
	anything stored at /var/www/html
- backup server:  
	Server containing script `s`
- md5sums:  
	Contains md5sums of all files in website data
- t:  
	monitor interval

## Steps
1. Start execution of `p` first.
1. `p` sees no md5sums, ∴ generates one. (p is capable of generating md5sums)
1. Start execution of `s`
1. `s` connects to `p`
1. `s` sees no md5sums with itself, ∴ requests one.
1. `md5sums` transferred `p` ⇨ `s`
7. Wait for `t` units of time.
1. `p` resends `md5sums` to `s`
1. * if new file received and all sums (except sums marked for change) in both files (old and new) match:  
   	ALL OK.  
   	Replace old `md5sums` with new.
   * else:  
   	### ***Unauthorized change detected:***
1. * if unauthorized change detected:  
   	send emails, raise errors, evacuate city.
   * else:  
   	Go to step 7
