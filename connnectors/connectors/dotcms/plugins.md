# Plugins

Cache Buster

With the way that the dotCMS cache and reindexer works, occasionally when updating a piece of content, the reindexer is unable to complete its job because the cache is not up to date. The solution is to clear the appropriate caches so that the reindexer is able to index the content. The cache buster plugin works in tandem with the write adapter to clear the identifier and contentlet caches.   


The write adapter creates files in the dotCMS assets folder at the paths

```text
motiv-adapter/buster/identifiercache and motiv-adapter/buster/contentletcache
```

The cache buster scans for those files along those paths and removes the content from the appropriate cache. This allows the reindex process to finish and reindex the updated content.   
 

