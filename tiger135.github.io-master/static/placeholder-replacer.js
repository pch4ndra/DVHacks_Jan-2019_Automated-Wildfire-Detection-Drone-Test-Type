
var config = require('./config.json');
var dir = __dirname;
var fs = require('fs');

fs.readdir(dir, (err, files) => {
	if (err) {
		return console.log(err);
	}
	files.forEach(file => {
		if (file.endsWith('.html')) {
   			fs.readFile(file, 'utf8', function (err, data) {
				if (err) {
					return console.log(err);
				}
				data = data.replace(/\${api.key}/gim, config.keys.maps);
				data = data.replace(/\${api.key.search}/gim, config.keys.search);
				data = data.replace(/\${api.key.routing}/gim, config.keys.routing);
				data = data.replace(/\${api.key.traffic}/gim, config.keys.traffic);
				data = data.replace(/\${api.key.trafficFlow}/gim, config.keys.trafficFlow);
				data = data.replace(/\/sdk/gim, config.paths.basePath);
				fs.writeFile(file, data, 'utf8', function (err) {
					if (err) {
						return console.log(err);
					}
				});
			});
		}
	});
})
