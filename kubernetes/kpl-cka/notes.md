# Notes for KPL course 
## Starting to use kubectl
- download kube config file from digital ocean portal once the cluster is running
- in the same dir as the file is, use it to connect to the cluster
    `kubectl --kubeconfig "k8s-1-30-2-do-0-sfo2-1721170047117-kubeconfig.yaml" get nodes` 
- easier way to do is to store the config file in `~/.kube/config`, then it'll auto pull it 
## Pods 
- always runs on a node
- node is a vm w/n k8s
- each node managed by master
- node can have multiple pods 

### Docker Commands
- run docker container with `docker run --name <name> nginx` nginx = image
- `docker ps`
- `docker exec -it mywebserver bash`
- `docker stop mywebserver` then `docker rm mysebserver` 

### Kubernetes Commands
- run kubernetes pod with `kubectl run mywebserver --image=nginx` 
- `kubectl get pods`
- `kubectl exec -it mywebserver -- bash`
- kubectl delete pod mywebserver`

## K8s objects
- k8 object (K8O) = record of intent passed into k8s cluster 
  - k8s will constantly work to ensure object exists 
- can configure w kubectl commands
- can config w file written in yaml 
  - `kubectl apply -f pod.yaml` to apply (in same dir as pod.yaml) 

## Architecture Overview
- kubernetes master
  - kube-apiserver, kube-scheduler, kube-controller-manager, cloud-controller-manager, etcd
    - kube-apiserver: gateway of cluster; accepts input 
    - etcd: database where config stored; key-value store (separate product; not dev'd by k8s community) 
    - kube-scheduler: selects nodes for pods to run on 
    - kube-controller-manager: node controller, logic if node goes down
    - cloud-controller-manager: interacts w underlying cloud provider 
- node components
  - kubelet: receives messages from kube-apiserver; agent on each node in cluster
  - kube-proxy: network proxy; enables pod comms
  - container runtime (prereq, not component): software that runs containers 

### etcd
- inspired by /etc dir in linux where config files are stored and d = distributed 
- definition: distrubted reliable key-value store 
  - stores configuration data of k8s cluster (all data of k8s cluster stored in etcd) 

### kube-apiserver
- gateway to k8s cluster (interact via api/cli/gui) 
  - responsible for authentication/authorization
- only k8s component that connects to etcd. Everything else connects to KAS which then connects to etcd 

### API Primitives Overview
- there's a number of APIs available to do things with the cluster (interact via gui/cli calls)  
- `kubectl api-resources` to view apis in terminal 
- Levels
  - alpha level (may be buggy); disabled by default
  - beta level: well-tested, enabled by default - recommended for non-business-critical use cases
  - stable: recommended for use in prod 
