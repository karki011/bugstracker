# GitHub to dotCMS

### **Running Impulse Locally** 

The problem with running locally is you typically do not have Impulse running on a domain.  It solve this you can use NGROK

### **Start ngrok**

ngrok allows us to tunnel our running Impulse application in order to expose it to the GitHub webhooks, it should expose whatever port is being exposed for Impulse/Janus. By default that is 8080.   
**`cd <ngrok installation folder>  
./ngrok http 8080  
ngrok by @inconshreveable                                                                                                                                                                                                  (Ctrl+C to quit)                                                                                                                                                                                                                                      
Session Status                online                                                                                                                                                                                                        
Account                       <Account Owner> (Plan: Free)                                                                                                                                                                                   
Version                       2.3.35                                                                                                                                                                                                        
Region                        United States (us)                                                                                                                                                                                            
Web Interface                 http://127.0.0.1:4040                                                                                                                                                                                         
Forwarding                    http://95dbf01d.ngrok.io -> http://localhost:8080                                                                                                                                                             
Forwarding                    https://95dbf01d.ngrok.io -> http://localhost:8080                                                                                                                                                            
                                                                                                                                                                                                                                            
Connections                   ttl     opn     rt1     rt5     p50     p90                                                                                                                                                                   
                              0       0       0.00    0.00    0.00    0.00`**  
   
After starting ngrok you will see on the output after running the command your tunnel URLs, one with http and the other for https \(for this example  http://95dbf01d.ngrok.io and https://95dbf01d.ngrok.io\), we will be using the http tunnel URL.  
  
Visit  ``[`http://localhost:4040/`](http://localhost:4040/) once you have ngrok running to see live requests on your tunnels. Quickly inspect the headers and responses, or replay a request to speed up your development process.   
 

