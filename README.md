The following are important commands to run

To copy from local to remote:

`kubectl cp {local_file_path} {remote_pod_name}:/{persitent_storage}/{remote_file_path}`

To copy from remote to local:

`kubectl cp {remote_pod_name}:/{persistent_storage}/{remote_file_path}`

By default our persistent storage is called `birdvol`

To exec/SSH onto a pod use:

`kubectl exec -it {pod_name} -- /bin/bash`

To see running instances use:

`kubectl get {instance_type}`

Kubernetes Instances:

- Pods: Most basic intance type, think of them as a virtual machine. When created manually they are killed after 6-8 hours
- Deployments: Controllers for "deploying" pods. These create pods and facilitate them, so if one dies, it will attempt to bring the pod back up. Pods created via deployment are **NEVER** killed, however we will get a nasty email if we leave a pod/deployment active for over 2 weeks.
- Jobs: A controller for running a set of commands. This will create a pod and run a set of commands. When the commands are finished executing the job will shutdown the pod. Never put `sleep infinity` in a job (this will get your account banned) as pods created by jobs are never shutdown due to a timelimit.
- Persistent Volume Claims (PVCs): These are our persistent storage systems. All data not stored on PVCs are temporary and will be lost when the pod dies. You must mount a PVC to a pod to be able to use it.

To create an instance use:

`kubectl create -f {filename}`

To delete an instance use:

`kubectl delete {instance_type} {instance_name}` or `kubectl delete -f {filename}`

To check logs (std:out/err) of a pod use:

`kubectl logs {pod_name}`

To debug instances you can use:

`kubectl describe {instance_type} {instance_name}` and `kubectl status {instance_type} {instance_name}`

You must be added to the namespace to be able to see everything ask Coen or Luca to give you access via the Nautilus Namespace Manager. Once added, you will have to install `kubectl` which you can find online resources for. To connect your local machine with the cluster, you need to download the `config` file from the Nautilus Portal and place it in your `.kube` directory in your home directory (create `.kube` if it doesn't exist already). Documentation can be found [here](https://docs.nationalresearchplatform.org/) and the Nautilus Homepage can be found [here](https://portal.nrp-nautilus.io/) 

Within the yamls provided, there is a section for commands to be run on the pod (on startup) seperated by `&&`. It is currently set up to be able to run the default ecoscape version as defined in the paper reproduction repo. This has been tested with a modified python file from the [`Connectivity_US_Conform.ipynb`](https://github.com/ecoscape-earth/ecoscape-connectivity-paper-reproduction/blob/main/Connectivity_US_Conform.ipynb) notebook and requires the files from [stejay](https://drive.google.com/drive/folders/1milnRMypGaOA8gJIwmusVIfb1kg0yrxM) in Google Drive.

