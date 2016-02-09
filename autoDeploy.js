var http = require('http')
var createHandler = require('github-webhook-handler')
var handler = createHandler({ path: '/incoming/site', secret: '12345678' })

http.createServer(function (req, res) {
  console.log(req);
  handler(req, res, function (err) {
    console.log(err);
    res.statusCode = 404
    res.end('no such location')
  })
}).listen(8086)

// handler.on('error', function (err) {
//   console.error('Error:', err.message)
// })

// handler.on('push', function (event) {
//   console.log('Received a push event for %s to %s',
//     event.payload.repository.name,
//     event.payload.ref)
// })

// handler.on('issues', function (event) {
//   console.log('Received an issue event for %s action=%s: #%d %s',
//     event.payload.repository.name,
//     event.payload.action,
//     event.payload.issue.number,
//     event.payload.issue.title)
// })
   
handler.on('*', function (event) {
  console.log('Received an  event for %s action=%s',
    event.payload.repository.name,
    event.payload.action)
    
})