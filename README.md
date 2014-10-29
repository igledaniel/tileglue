tileglue
========

This package contains the mapzen specifics to integrate the other tile
packages. This helps eliminate dependencies from tilequeue on
tilestache-providers, and keeps the mapzen specific glue out of that
package.

Down the road, the tile rendering logic may be moved out of tilequeue
into this package as well, and perhaps tilequeue would not depend on
TileStache and would only manage the queue pipeline.

Custom Cache Provider
---------------------

A custom tilestache cache is created, which is the caching provider
that Mapzen uses to stitch the pieces together. It uses a wrapper
around the S3 cache (to add appropriate caching headers), wrapped by a
notifier cache. Upon cache save, the tile coordinate is inserted into
a redis datastore. The redis datastore interactions are located in
[tilequeue](https://www.github.com/mapzen/tilequeue).
