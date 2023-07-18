import subprocess
import re

def check_juicy_potato():
    try:
        command = 'tasklist /v /fo csv'
        output = subprocess.check_output(command, shell=True, universal_newlines=True)
        processes = output.strip().split('\n')[1:]

        for process in processes:
            process_details = re.split('",', process.strip())
            process_name = process_details[0].strip('"')
            process_pid = process_details[1].strip('"')
            process_command = process_details[-2].strip('"')

            if process_name.lower() == 'lsass.exe' and 'nt authority\\system' in process_command.lower():
                print(f"WARNING: Potential Juicy Potato exploit detected!")
                print(f"Process Name: {process_name}")
                print(f"Process PID: {process_pid}")
                print(f"Process Command: {process_command}")
                print("Please take necessary actions to secure your system.")
                return

        print("No potential Juicy Potato exploit detected.")
    except KeyboardInterrupt:
        print("\nProgram execution interrupted.")

check_juicy_potato()
