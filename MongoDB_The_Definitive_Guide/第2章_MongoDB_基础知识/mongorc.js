// mongorc.js

var compliment = ['attractive', 'intelligent', 'like Batman'];
var index = Math.floor(Math.random() * 3);

print("Hello, you're looking particularly " + compliment[idnex] + "today!");

var no = function() {
	print('Not on my watch.');
}

// 禁止删除数据库
db.dropDatabase = DB.prototype.dropDatabase = no;

// 禁止删除集合
DBCollection.prototype.drop = no;

// 禁止删除索引
DBCollection.prototype.dropIndex = no;