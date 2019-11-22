var page = require('webpage').create();

page.viewportSize = { width: 1024, height: 768}
page.clipRect = { top: 0, left: 0, width: 512, height: 216}

page.open('http://www.cnblogs.com/qiyeboy/', function(status) {
  console.log('Status: ' + status);
  if (status == 'success') {
    page.render('qiye.png');
  }
  phantom.exit();
});