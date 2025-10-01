# Basics of Kubernetes
## Defined
- An external secrets manager is a must
- in the k8s doc, there's a one-page API ref page under Reference in the docs
- K8s is more like a framework than a platform; it's very extensible

## Login Information
Control Plane: 34.139.184.182
Worker Node:   35.245.187.82

key file path: ~/.ssh/live-cka-key.pem

## Installation and Configuration
kubeadm is the official tool for installing kubernetes
- generates a default ~/.kube/config file
    - if kubectl is giving a network error, it's usually b/c it can't find the config file

## Architecture
Operators
- operate controllers
- informer: watches for events and puts them in queues
Containers
- not managed directly
- usage limits don't typically work well irl because linux doesn't manage memory allocation well. So, don't schedule too many things on one instance
    - limits are in place to keep processes from running away. They should be fairly high
- the requests are the amount of reserved space that should be used; info for the scheduler
Init Containers
- execute something before the main container runs. Can run an array of them; they must end before the next can run. Once all of them successfully run, the main container can run
- status will show 'init' if the init process has stalled

## Scheduling
scheduler doesn't monitor the cluster; it responds to events
it figures out where it can't run, then picks the best choice by balancing the workload across the cluster

## Troubleshooting
There is a skill req'd in troubleshooting and identifying certain things (documenting what you've done helps!). Also requires knowing the system and how it works. And still need info to work with (events, logs) to make informed decisions
- Also need to identify what IS working
- if useful errors can't be found, it's probably security-related

## Exam tips
### Tasks
- They don't care the order you do it in. Skip the difficult things and come back to them later. Questions are weighted differently
- There may be a question to install k8s on the control plane
- Get a free retake with each voucher purchase

### Misc
There's a notepad available digitally to use
Know how to get to the quick-reference page (which has the shell modifications in it)
- https://kubernetes.io/docs/reference/kubectl/quick-reference/

### Questions
able to use own office/desk? In context of AWS exams where you have to have clear desk and everything

### shell modifications
kubectl tab complete
case insensitive tab completion
if needed, how difficult is it to add \y \p for copy/pasting?
also vim for line numbers all the time

# Labs
wget https://cm.lf.training/LFS458/LFS458_V1.33.1_SOLUTIONS.tar.xz --user=LFtraining --password=Penguin2014
- more stuff to try: https://github.com/alijahnas/CKA-practice-exercises
- $40 for two practice exams https://killer.sh/pricing
- https://www.reddit.com/r/devops/comments/1hr0mjw/passed_cka_exam_two_days_ago_some_tidbits/
- https://deloittedevelopment.udemy.com/course/certified-kubernetes-administrator-with-practice-tests/
    - multiple people recommended Mumshad's course + practicals


# Questions
- difference between replicasets and deployments?
