# Running Impulse

Once minikube and Kafka have been started you can then decide how you want to start Impulse. Make sure Janus is mounted before spinning up Impulse.   
Once Impulse is running, use the “`minikube ip`” command to get the domain to access all the pods. 

If you so choose, you can label this domain in your Ubuntu machine by adding to the `/etc/hosts` file. Add “&lt;`minikube’s ip`&gt; &lt;`personal label`&gt;“ to the `/etc/hosts` file. 

1. **Impulse Only**

   ```text
   kubectl apply -f impulse/
   ```

2. **Impulse and Source dotCMS**  
   To run source dotCMS you will need to mount the plugins. Open a new terminal and run: 

   ```text
   minikube mount <checkout location>/impulse/cms-static-plugins-source1:/dotcms-source/plugins
   ```

3. **Then spin up dotCMS.** 

   ```text
   kubectl apply -f impulse/ -f dotcms-source/
   ```

4. **Impulse and Destination dotCMS**  
   To run destination dotCMS you will need to mount the plugins. Open a new terminal and run:  

   ```text
   minikube mount <checkout location>/impulse/cms-static-plugins-destination1:/dotcms-dest/plugins
   ```

   ```text
   kubectl apply -f impulse/ -f dotcms-destination/
   ```

5. **Impulse, Source dotCMS and Destination dotCMS**  
   Make sure Janus, dotCMS source plugins, and dotCMS destination plugins are all mounted. 

   ```text
   kubectl apply -f impulse/ -f dotcms-source/ -f dotcms-destination/
   ```

\*\*\*\*

