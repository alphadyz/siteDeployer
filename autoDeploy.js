var http = require('http')
var createHandler = require('github-webhook-handler')
var handler = createHandler({ path: '/incoming/site', secret: '12345678' })
var process = require('child_process');
var fs=require('fs');

if(!fs.existsSync("./public")){
  pullAndGen();
}

http.createServer(function (req, res) {
  handler(req, res, function (err) {
    console.log(err);
    res.statusCode = 404
    res.end('no such location')
  })
}).listen(8086)
console.log('github hook listening...');
handler.on('error', function (err) {
  console.error('Error:', err.message)
})

// handler.on('push', function (event) {
//   console.log('Received a push event for %s at %s',
//     event.payload.repository.name,
//     Date.now());
//     pullAndGen();
    
// })

handler.on('*',function(event){
  if(event.event=="push"){
     console.log('Received a push event for %s at %s',
     event.payload.repository.name,
     Date.now());
     pullAndGen();
  }
})

function pullAndGen(){
  var cmd=process.exec("git pull && hexo generate");
    cmd.on('err',function(err){
      console.log(err);
    });
    cmd.on('exit', function(code) {
      if (code != 0) {
        console.log('Failed: ' + code);
      }else{
        console.log("deployed!");
      }
    });
}