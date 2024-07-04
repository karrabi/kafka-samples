To store time series data in Redis, you can use various data structures and commands that Redis provides. Here’s a simple guide on how to do it:

### Using Redis Sorted Sets for Time Series Data

Redis Sorted Sets are a good fit for time series data because they allow you to store data with a score, which can be a timestamp, and retrieve it in a sorted order.

#### Steps to Store and Retrieve Time Series Data

1. **Add Data to a Sorted Set**:
   - Use the `ZADD` command to add data to a sorted set. The score will be the timestamp, and the member will be the data point.
   ```sh
   ZADD timeseries 1622547800 "data_point_1"
   ZADD timeseries 1622547900 "data_point_2"
   ```

2. **Retrieve Data by Time Range**:
   - Use the `ZRANGEBYSCORE` command to retrieve data points within a specific time range.
   ```sh
   ZRANGEBYSCORE timeseries 1622547800 1622547900
   ```

3. **Retrieve All Data**:
   - Use the `ZRANGE` command to retrieve all data points.
   ```sh
   ZRANGE timeseries 0 -1 WITHSCORES
   ```

### Example Commands

Here are some basic commands to work with time series data in Redis:

1. **Add Data**:
   ```sh
   ZADD timeseries 1622547800 "temperature:25.3"
   ZADD timeseries 1622547900 "temperature:25.7"
   ZADD timeseries 1622548000 "temperature:26.1"
   ```

2. **Retrieve Data by Time Range**:
   ```sh
   ZRANGEBYSCORE timeseries 1622547800 1622548000
   ```

3. **Retrieve All Data**:
   ```sh
   ZRANGE timeseries 0 -1 WITHSCORES
   ```

4. **Remove Old Data**:
   - Use the `ZREMRANGEBYSCORE` command to remove data points older than a certain timestamp.
   ```sh
   ZREMRANGEBYSCORE timeseries 0 1622547800
   ```

### Using Redis Streams for Time Series Data

Redis Streams are another powerful data structure for handling time series data, especially when you need to handle complex event processing.

#### Steps to Store and Retrieve Time Series Data

1. **Add Data to a Stream**:
   - Use the `XADD` command to add data to a stream. The `*` symbol auto-generates a unique ID based on the current timestamp.
   ```sh
   XADD mystream * temperature 25.3
   XADD mystream * temperature 25.7
   ```

2. **Retrieve Data**:
   - Use the `XRANGE` command to retrieve data within a specific range.
   ```sh
   XRANGE mystream - +
   ```

3. **Retrieve Data by ID**:
   - Use the `XREAD` command to read data starting from a specific ID.
   ```sh
   XREAD COUNT 2 STREAMS mystream 0
   ```

### Example Commands

Here are some basic commands to work with time series data using Redis Streams:

1. **Add Data**:
   ```sh
   XADD mystream * temperature 25.3
   XADD mystream * temperature 25.7
   XADD mystream * temperature 26.1
   ```

2. **Retrieve All Data**:
   ```sh
   XRANGE mystream - +
   ```

3. **Retrieve Data by ID**:
   ```sh
   XREAD COUNT 2 STREAMS mystream 0
   ```

4. **Trim Stream**:
   - Use the `XTRIM` command to trim the stream to a specific length.
   ```sh
   XTRIM mystream MAXLEN 1000
   ```

### Conclusion

Redis provides flexible and powerful data structures like Sorted Sets and Streams to handle time series data efficiently. Depending on your specific use case, you can choose the appropriate data structure and commands to store, retrieve, and manage your time series data in Redis.

Citations:
[1] https://en.wikipedia.org/wiki/Redis_%28data_store%29
[2] https://github.com/redis/redis
[3] https://www.ibm.com/topics/redis
[4] https://github.com/SOHU-Co/kafka-node/issues/1403
[5] https://www.oreilly.com/library/view/kafka-the-definitive/9781491936153/ch04.html