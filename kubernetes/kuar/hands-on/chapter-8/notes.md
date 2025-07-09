- Install Contour Ingress controller
`kubectl apply -f https://projectcontour.io/quickstart/contour.yaml`

- It will create a load balancer that has a public ip. Get that by running
`kubectl get -n projectcontour service envoy -o wide`

### Simple Example
- Add the public IP address to `/etc/hosts` for alpaca.example.com and bandicoot.example.com

- Using ingress; create upstream/backend services
```
kubectl create deployment be-default --image=gcr.io/kuar-demo/kuard-amd64:blue --replicas=3 --port=8080
kubectl expose deployment be-default
kubectl create deployment alpaca --image=gcr.io/kuar-demo/kuard-amd64:green --replicas=3 --port=8080
kubectl expose deployment alpaca
kubectl create deployment bandicoot --image=gcr.io/kuar-demo/kuard-amd64:purple --replicas=3 --port=8080
kubectl expose deployment bandicoot
kubectl get services -o wide
```

- Then create `ingress.yaml` and should be able to get to http://alpaca.example.com

- Clean up with the following commands  
```
kubectl delete ingress host-ingress path-ingress simple-ingress
kubectl delete service alpaca bandicoot be-default
kubectl delete deployment alpaca bandicoot be-default
```

### Serving TLS