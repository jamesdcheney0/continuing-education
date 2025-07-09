BANDICOOT_POD=$(kubectl get pods -l app=bandicoot -o jsonpath='{.items[0].metadata.name}')
kubectl port-forward $BANDICOOT_POD 48858:8080