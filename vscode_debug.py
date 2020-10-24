# configuration for vscode remote attach and debug
import ptvsd
import sys
ip_address = ('0.0.0.0', 6789)
print("Process: " + " ".join(sys.argv[:]))
print("Is waiting for attach at address: %s:%d" % ip_address, flush= True)
# Allow other computers to attach to ptvsd at this IP address and port.
ptvsd.enable_attach(address=ip_address)
# Pause the program until a remote debugger is attached
ptvsd.wait_for_attach()
print("Process attached, start running into experiment...", flush= True)
ptvsd.break_into_debugger()
# the next line will be stopped by a breakpoint where you can start your debugging

