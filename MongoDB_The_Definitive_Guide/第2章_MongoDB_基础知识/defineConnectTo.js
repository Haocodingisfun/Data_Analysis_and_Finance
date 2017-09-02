// defineConnectTo.js

/** 
 * 连接到指定数据库，并且将 db 指向这个连接
 */

var connectTo = function(port, dbname) {
	if (!port) {
		port = 27017;
	}

	if (!dbname) {
		dbname = 'test';
	}

	db = connect('localhost:' + port + '/' + dbname);
	return db;
};