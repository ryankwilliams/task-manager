```shell
kubectl create -f task-manager.yml

kubectl port-forward svc/task-manager 9091:9090 -n <namespace>
```
