import subprocess

p = subprocess.Popen(['git', 'branch', '-a'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = p.communicate()

out2 = out.splitlines()

for i in out2:
    if not i.endswith("master"):
        b = i[17:]
        print b
        p = subprocess.Popen(['git', 'push', 'origin', '--delete', b], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        print out
        print "err", err

