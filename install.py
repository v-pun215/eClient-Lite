import wget, os,time,platform
py_ver = platform.python_version()
print('''
           $$$$$$\  $$\ $$\                      $$\           $$\       $$\   $$\                      $$$$$$\             $$\                         
          $$  __$$\ $$ |\__|                     $$ |          $$ |      \__|  $$ |                    $$  __$$\            $$ |                        
 $$$$$$\  $$ /  \__|$$ |$$\  $$$$$$\  $$$$$$$\ $$$$$$\         $$ |      $$\ $$$$$$\    $$$$$$\        $$ /  \__| $$$$$$\ $$$$$$\   $$\   $$\  $$$$$$\  
$$  __$$\ $$ |      $$ |$$ |$$  __$$\ $$  __$$\\_$$  _|        $$ |      $$ |\_$$  _|  $$  __$$\       \$$$$$$\  $$  __$$\\_$$  _|  $$ |  $$ |$$  __$$\ 
$$$$$$$$ |$$ |      $$ |$$ |$$$$$$$$ |$$ |  $$ | $$ |          $$ |      $$ |  $$ |    $$$$$$$$ |       \____$$\ $$$$$$$$ | $$ |    $$ |  $$ |$$ /  $$ |
$$   ____|$$ |  $$\ $$ |$$ |$$   ____|$$ |  $$ | $$ |$$\       $$ |      $$ |  $$ |$$\ $$   ____|      $$\   $$ |$$   ____| $$ |$$\ $$ |  $$ |$$ |  $$ |
\$$$$$$$\ \$$$$$$  |$$ |$$ |\$$$$$$$\ $$ |  $$ | \$$$$  |      $$$$$$$$\ $$ |  \$$$$  |\$$$$$$$\       \$$$$$$  |\$$$$$$$\  \$$$$  |\$$$$$$  |$$$$$$$  |
 \_______| \______/ \__|\__| \_______|\__|  \__|  \____/       \________|\__|   \____/  \_______|       \______/  \_______|  \____/  \______/ $$  ____/ 
                                                                                                                                              $$ |      By v-pun215
                                                                                                                                              $$ |      
                                                                                                                                              \__|                                                             
                                                                                                 
                                                                                                 
''')
if not py_ver == "3.10.0":
    print("You don't have Python 3.10.0 installed. This might result in some bugs.")
    print("Also, you have Python {}. Don't ask me how I know!".format(py_ver))
else:
    pass
def dep():
    os.system("pip install -r requirements.txt")
java = input("Do you have Java 17 installed? (Y/N): ")

if java == "Y":
    print("Installing dependencies...")
    time.sleep(5)
    dep()
    
else:
    wget.download("https://download.bell-sw.com/java/17.0.3+7/bellsoft-jdk17.0.3+7-windows-amd64.msi", bar=wget.bar_adaptive)
    os.system(f"msiexec /i bellsoft-jdk17.0.3+7-windows-amd64.msi")
    time.sleep(5)
    os.remove(f"bellsoft-jdk17.0.3+7-windows-amd64.msi")
    dep()
    
    
