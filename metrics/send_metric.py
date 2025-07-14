import statsd

client = statsd.StatsClient('localhost', 8125)
client.incr('notifications.sent')
print("Metric 'notifications.sent' sent to Graphite")
