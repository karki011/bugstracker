# Manual steps

If you don’t want to use the script to bring up Impulse \(or want to know the steps taken to bring up Impulse\) you can do it following these steps. 

It is suggested that you use the google cloud console to create persistent drives, instances, and clusters. 

1. You need 5 persistent drives. 
   1. These persistent drives must be named as follows: 
      1. janus-disk
      2. dotcms-source-plugin
      3. dotcms-source-shared
      4. dotcms-dest-plugin
      5. dotcms-dest-shared
   2. You can create these drives individually and attach them to an instance or you can create an instance on Google Cloud with 5 additional drives.
2. Create a Google Cloud instance. 
3. ssh into the instance and mount persistent drives into instance
   1. [Attach and Mount Disks to VM Instance in Google Cloud](https://www.cloudbooklet.com/attach-and-mount-disks-to-vm-instance-in-google-cloud/%20)
   2. Only janus-disk, dotcms-source-plugin, and dotcms-dest-plugin must be mounted. dotcms-source-shared and dotcms-dest-shared do not need to be mounted. 
   3. If multiple drives are attached to the instance you can tell the order of the drives by viewing details for the instance. View all your VM instances and click the name of the instance with the attached drives. In the middle of the page there will be a list of “Additional disks”. The order of the list matches the order when running `sudo lsblk` inside the instance
4. Use **scp** files into persistent drives through their mount point in the instance**.** 

   1.  ****[https://cloud.google.com/filestore/docs/copying-data](https://cloud.google.com/filestore/docs/copying-data) 

      ```text
      gcloud compute scp ../impulse/janus --recurse "$instance":/janus-disk --zone "$zone" --project "$project"

      gcloud compute scp ../impulse/cms-static-plugins-source1 --recurse "$instance":/dotcms-source-plugin --zone "$zone" --project "$project"

      gcloud compute scp ../impulse/cms-static-plugins-destination1 --recurse "$instance":/dotcms-dest-plugin --zone "$zone" --project "$project"

      ```

   2. Once the files are transferred the plugin drives need a little clean up. You need to remove the lost+found folder, move the plugins outside of their parent directory, and remove the now empty parent directory. You can either do this in the **ssh** or run these commands in your local terminal. 

   ```text
   gcloud compute ssh $instance --zone="$zone" --command="rm -r /dotcms-source-plugin/lost+found"

   gcloud compute ssh $instance --zone="$zone" --command="mv /dotcms-source-plugin/cms-static-plugins-source1/* /dotcms-source-plugin"


   gcloud compute ssh $instance --zone="$zone" --command="rm -r /dotcms-source-plugin/cms-static-plugins-source1"

   gcloud compute ssh $instance --zone="$zone" --command="rm -r /dotcms-dest-plugin/lost+found"

   gcloud compute ssh $instance --zone="$zone" --command="mv /dotcms-dest-plugin/cms-static-plugins-destination1/* /dotcms-dest-plugin"

   gcloud compute ssh $instance --zone="$zone" --command="rm -r /dotcms-dest-plugin/cms-static-plugins-destination1"

   ```

5.  Delete the instance, but leave the additional drives

   1. This is usually the default option when creating an instance through the google cloud console. The terminal command would be as follows: 

   ```text


   gcloud compute instances delete $instance --keep-disks data


   ```

6. Create a Kubernetes cluster
   1. The nodes should be e2-standard-4 machine type. This provides 4VCPU, 16GB memory.
7. Connect to the new cluster in local terminal

   1. When viewing all clusters in the google cloud console there is a connect button. If you press that you can copy the command and run it in your local terminal to connect kubectl to the remote cluster. The command is akin to this: 

   ```text

   gcloud container clusters get-credentials $cluster --zone $zone --project $project 

   ```

8. Create the secrets so that docker images can be pulled

   ```text

   kubectl create secret docker-registry regsecret3 --docker-username=$dockerUser --docker-password=$dockerPass --docker-email=$dockerEmail
   kubectl create secret docker-registry regsecret3 --docker-username=$dockerUser --docker-password=$dockerPass --docker-email=$dockerEmail --namespace=kube-system


   ```

9. Label nodes
   1. Get the name of the nodes by running:
   2. ```text
      kubectl get nodes
      ```
   3. dotCMS

      1. Before starting dotCMS you need to apply 2 labels. It is recommended that you apply them to separate nodes.

      ```text

      kubectl label nodes $node1 dotcms=source
      kubectl label nodes $node2 dotcms=dest

      ```

   4. Fluentd

      1. The Fluentd daemonset uses a node selector to choose what nodes to exist on. This means you need to add a label to every node you want Fluentd to capture Impulse logs from.

      ```text
      kubectl label nodes $node beta.kubernetes.io/fluentd-ds-ready=true
      ```
10. Start up Cassandra 

    ```text

    helm repo add bitnami https://charts.bitnami.com/bitnami
    kubectl apply -f helm/cassandra-init-db-config-map.yaml
    helm install db --set fullnameOverride=db,nameOverride=db -f helm/values-cassandra.yaml bitnami/cassandra

    ```

11. Bring up jaeger operator 

    ```text

    kubectl create -f jaeger/service_account.yaml
    kubectl create -f jaeger/role.yaml
    kubectl create -f jaeger/role_binding.yaml
    kubectl create -f jaeger/operator.yaml

    ```

12. Bring up kafka with helm 

    ```text
    helm install my-confluent helm/cp-helm-charts-0.5.0.tgz -f helm/values.yaml
    ```

13. Bring up jaeger 

    ```text
    kubectl apply -f jaeger/cassandra-jaeger.yaml
    ```

    1. You should wait for the cassandra-jaeger pod to be running before starting Impulse. Check if it’s running with this command:  

    ```text
    kubectl get pods | grep cassandra-jaeger
    ```

14. Bring up Fluentd 

    ```text
    kubectl apply -f fluentd/conf/fluentd-impulse-cluster-configmap.yaml -f fluentd/fluentd-daemonset.yaml -f fluentd/fluentd-daemonset-service.yaml
    ```

15. Bring up diesel 

    ```text
    kubectl apply -f diesel/
    ```

16. Bring up Impulse

    ```text
    kubectl apply -f impulse/ -f dotcms-source/ -f dotcms-destination/
    ```

