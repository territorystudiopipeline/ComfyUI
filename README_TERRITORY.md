# Territory

This is a fork of the main ComfyUI repo. The intention is to povide modifications 
for ease of use in Territory, while keeping the changes as minimal as possible to 
ensure that keeping up to date is easy.

# REZ

We've added some files to the repo to make this releasable as a rez package.

The rez_install_deps.bat file parses the requirements.txt file and installs all 
requirements listed. THIS TAKES A LONG TIME, and generally won't be required for 
every release, but if you encounter issues with dependencies, then you may need to
re-run this script to install the latest versions.

# Other Territory customizations.

Currently our only customization is configuring the image output directory location
to go to the user folder for the current show. 

Also updated the configuration so that models are pulled from the network so all 
models are shared.

# Updating ComfyUI

This is fairly easy - We are maintaining a separate ts_main branch. To update to 
the latest version of ComfyUI, simply rebase our ts_main branch onto their master
branch. We have minimal change so merge conflicts should be rare.
Once the rebase is complete, push the changes, and then release a new version using 
release. 
`release -r -v <comfyUI_version>`
where `<comfyUI_version>` is their latest version + `.ts#` where # is the number 
of custom updates we've made.

So the complete version should look like:
`0.11.0.ts1`
Then after an update from us, it would look like this:
`0.11.0.ts2`
Then after an update from ComfyUI, it would look like this:
`0.12.0.ts2`

# Torch and GPU specific dependencies.

AI image generation is very GPU dependent, and the dependencies rely heavily on our hardware. 
See their README:
https://github.com/Comfy-Org/ComfyUI?tab=readme-ov-file#nvidia

The version of Torch we use is important. As of writing this, we are predominately
using RTXA5000 on the farm, and so we've downloaded Torch-2.9.1+cu126 (see 
requirements.txt for specific versions of all torch packages). Newer hardware will 
require newer versions of Torch + cu (cuda?). View the ComfyUI installation docs
+ google for more information for which versions of Torch to use with which hardware. 
NOTE: We may need to create GPU specific variants for Torch, so that the version 
    resolved is automatically the version which works best for the current machines 
    hardware. We can do this be determining the gpu in the rezconfig.py file, and 
    then adding an implicit package for the GPU. (And then the implicit package 
    can be used as a variant in the torch install location)

If an incorrect Torch version is installed, ComfyUI will get partly the way through
loading, and then suddenly crash with no error message. This is due to a `torch.device`
method call which causes a crash. See the comfy.model_management.get_torch_device() 
method to test if this is the cause of your crash.
