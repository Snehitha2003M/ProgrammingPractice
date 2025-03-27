def count_warnings(filename):
    warnings_Count=0
    file=open(filename,"r")
    for line in file:
        if "warning" in line.lower():
            warnings_Count+=1
    file.close()
    return warnings_Count
def build():
    old_log="logfile1.txt"
    new_log="logfile2.txt"
    c1=count_warnings(old_log)
    c2=count_warnings(new_log)
    print(f"old warning count{old_log}:{c1}")
    print(f"new warning count{new_log}:{c2}")
    if c2>c1:
        print("build is not promoted")
    else:
        print("Build is promoted")
if __name__=="__main__":
    build()