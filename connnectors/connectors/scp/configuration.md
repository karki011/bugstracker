# Configuration

### Taxi-dropoff-scp

1. URL: remote host IP, it has to include the port, for example:  `192.168.68.120:22`
2. Username: is the user that has privileges in the remote host.
3. Private Key: has to be encoded base64, and can't contain newlines. One way to generate it is like this: `base64 -w 0 private-key-motiv.pem > encoded-private-key-motiv.pem` \(pass the content of `encoded-private-key-motiv.pem` make sure you are not copying any end of lines\)

###  Job-depot

Detail: in order to specify the folder path where the user has permissions to SCP the binaries, you need to pass it as location.path 

```text
{
  "name": "github-to-scp-job",
  "type": "manual",
  "description": "GitHub to SCP job",
  "active": true,
  "endpoints": [
    {
      "id": "0e5bf526-4177-4b85-9e4f-3f64a083db5f",
      "type": "source"
    },
    {
      "id": "06a87708-815f-48a8-80d9-d2aaccd855af",
      "type": "destination",
      "detail": "location.path:/home/motiv/github/"
    }
  ]
}

```

