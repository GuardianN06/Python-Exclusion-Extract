import subprocess, sys, os


if not sys.argv[-1] == 'admin':
    # Re-launch the script with administrative privileges
    script_path = os.path.abspath(sys.argv[0])
    params = ' '.join(sys.argv[1:])
    subprocess.run(['powershell.exe', '-Command', f'Start-Process "{sys.executable}" -ArgumentList "{script_path} {params} admin" -Verb RunAs'])
    sys.exit()
powershell_cmd = 'Get-MpPreference | Select-Object -ExpandProperty ExclusionPath'
p = subprocess.Popen(["powershell.exe", "-Command", powershell_cmd], stdout=subprocess.PIPE)
stdout, _ = p.communicate()

filename = 'Exclusions.txt'

with open(filename, 'w') as file:
    file.write(stdout.decode())