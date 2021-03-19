# Table of contents

* [🚀 Introduction](README.md)

## Example Sync Use Cases <a id="example-sync-use-cases-1"></a>

* [GitHub to dotCMS](example-sync-use-cases-1/example-sync-use-cases.md)
* [dotCMS File\|Content Type](example-sync-use-cases-1/dotcms-file-or-content-type.md)

## Installation

* [Google Cloud](installation/google-cloud/README.md)
  * [Bring up Impulse](installation/google-cloud/bring-up-impulse.md)
  * [Manual steps](installation/google-cloud/manual-steps.md)
  * [Single vs. Multi Cluster](installation/google-cloud/single-vs.-multi-cluster/README.md)
    * [Taxi/adapter communication](installation/google-cloud/single-vs.-multi-cluster/taxi-adapter-communication.md)
    * [Jaeger](installation/google-cloud/single-vs.-multi-cluster/jaeger.md)
    * [Fluentd & Cassandra](installation/google-cloud/single-vs.-multi-cluster/fluentd-and-cassandra.md)
* [Docker-Compose](installation/docker-compose/README.md)
  * [Local Install](installation/docker-compose/local-install.md)
  * [Running Impulse](installation/docker-compose/running-impulse.md)
* [minikube](installation/minikube/README.md)
  * [Starting kafka](installation/minikube/starting-kafka.md)
  * [Running Impulse](installation/minikube/running-impulse.md)
  * [Known Issues](installation/minikube/known-issues.md)

## Config

* [Impulse Pieces](config/untitled.md)

## Concepts

* [Jobs/Endpoints](concepts/untitled.md)

## Connnectors

* [Connectors](connnectors/connectors/README.md)
  * [gGitHub](connnectors/connectors/ggithub.md)
  * [SCP](connnectors/connectors/scp/README.md)
    * [Configuration](connnectors/connectors/scp/configuration.md)
  * [dotCMS](connnectors/connectors/dotcms/README.md)
    * [Plugins](connnectors/connectors/dotcms/plugins.md)
    * [Options](connnectors/connectors/dotcms/options.md)
    * [Not supported / Known errors](connnectors/connectors/dotcms/not-supported-known-errors.md)
  * [Strapi](connnectors/connectors/strapi/README.md)
    * [Taxi](connnectors/connectors/strapi/taxi.md)
    * [Adapters](connnectors/connectors/strapi/adapters.md)
    * [Job-&gt;Endpoint-&gt;Details Option](connnectors/connectors/strapi/options.md)
    * [Combining details Option](connnectors/connectors/strapi/combining-details-option.md)
    * [Not supported / Known errors](connnectors/connectors/strapi/not-supported-known-errors.md)
  * [Global Connector Options](connnectors/connectors/global-connector-options.md)
  * [Implement a Connector](connnectors/connectors/implement-a-connector/README.md)
    * [Kafka Topics](connnectors/connectors/implement-a-connector/kafka-topics/README.md)
      * [Rest Endpoints](connnectors/connectors/implement-a-connector/kafka-topics/rest-endpoints.md)
      * [JSON produced or consumed](connnectors/connectors/implement-a-connector/kafka-topics/json-produced-or-consumed.md)
      * [Sync-Manager configuration](connnectors/connectors/implement-a-connector/kafka-topics/sync-manager-configuration.md)
      * [PickupTaxi configuration](connnectors/connectors/implement-a-connector/kafka-topics/pickuptaxi.md)
      * [Transformer-In configuration](connnectors/connectors/implement-a-connector/kafka-topics/transformer-in-configuration.md)
      * [DropOffTaxi configuration](connnectors/connectors/implement-a-connector/kafka-topics/dropofftaxi-configuration.md)
      * [Transformer-Out configuration](connnectors/connectors/implement-a-connector/kafka-topics/transformer-out-configuration.md)

---

* [Transactions](transactions.md)
* [Adapters](adapters.md)
* [Notifications & Alerts](notifications-and-alerts.md)

## APIs

* [Janus Gateway](apis/janus-gateway.md)
* [List of APIs](apis/list-of-apis.md)

## How To

* [GitHub to dotCMS](how-to/github-to-dotcms/README.md)
  * [Impulse Config](how-to/github-to-dotcms/impulse-config.md)
  * [dotCMS Config](how-to/github-to-dotcms/dotcms-config.md)
  * [GitHub Config](how-to/github-to-dotcms/github-config.md)
  * [Sync GitHub - dotCMS 5.2.7](how-to/github-to-dotcms/sync-github-dotcms-5.2.7.md)
* [dotCMS \(folder\) to dotCMS \(folder\)](how-to/dotcms-folder-to-dotcms-folder/README.md)
  * [Job Depot](how-to/dotcms-folder-to-dotcms-folder/job-depot.md)
  * [Pick up taxi](how-to/dotcms-folder-to-dotcms-folder/pick-up-taxi.md)
  * [dotCMS 5.2.7 adapter IN / Read](how-to/dotcms-folder-to-dotcms-folder/dotcms-5.2.7-adapter-in-read.md)
  * [Drop off taxi](how-to/dotcms-folder-to-dotcms-folder/drop-off-taxi.md)
  * [Start Sync](how-to/dotcms-folder-to-dotcms-folder/start-sync.md)
* [dotCMS \(content\) to dotCMS \(content\)](how-to/dotcms-content-to-dotcms-content/README.md)
  * [Job Depot](how-to/dotcms-content-to-dotcms-content/job-depot.md)
  * [Pick up taxi](how-to/dotcms-content-to-dotcms-content/pick-up-taxi.md)
  * [dotCMS 5.2.7 adapter IN / Read](how-to/dotcms-content-to-dotcms-content/dotcms-5.2.7-adapter-in-read.md)
  * [Drop off taxi](how-to/dotcms-content-to-dotcms-content/drop-off-taxi.md)
  * [Start Sync](how-to/dotcms-content-to-dotcms-content/start-sync.md)

---

* [Shutdown Impulse](shutdown-impulse.md)
* [Logger](logger.md)
* [Report](report.md)

## Impulse UI

* [Concepts](impulse-ui/concepts.md)
* [⚙️ Start Impulse UI](impulse-ui/how-to.md)
* [Dashboard](impulse-ui/dashboard.md)
* [➕ Add Endpoints](impulse-ui/add-endpoints.md)
* [➕ Add Job](impulse-ui/add-job-1.md)
* [​📈 Sync-Man report](impulse-ui/sync-man-report.md)
* [Logger](impulse-ui/logger.md)

---

* [Jaeger UI](untitled.md)
* [Fluentd](fluentd.md)
* [Glossary](glossary.md)

