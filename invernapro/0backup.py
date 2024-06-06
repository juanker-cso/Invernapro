import os
import time

bkname = 'invernapro' + '-bk-' + time.strftime('%Y%m%d')

if not (os.path.exists("backups\\")):
    os.makedirs("backups\\")

cmd = "mysqldump -u '{}' -p{} {} > backups\\{}.sql --no-tablespaces --routines"

print(cmd.format('invernadmin',"****",'invernapro',bkname), end='\t')
os.popen(cmd.format('invernadmin','password','invernapro',bkname))
print("...done")
