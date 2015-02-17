
/*
 * GET home page.
 */

exports.index = function(req, res){
  res.render('index1.ejs', {
	  "posts": [
	            
	            {
	            	"type":"image",
	              "thumbnailMetadata": {
	                "text": "Vibhor",
	                "title": "hello",
	                "mediaSrc": "/style/images/art/post1.jpg"
	              },
	              "date": "sampleDate",
	              "likes": 3,
	              "tried" : 2,
	              "challenge" : 3,
	              "comments": 5
	            },
	            {
	            	"type":"video",
	              "thumbnailMetadata": {
	                "text": "Video Text",
	                "title": "video Head",
	                "mediaSrc": "https://www.youtube.com/watch?v=U6mHbXjUVjc"
	              },
	              "date": "sampleDate",
	              "likes": 3,
	              "tried" : 2,
	              "challenge" : 3,
	              "comments": 5
	            },
	            {
	            	"type":"text",
	              "thumbnailMetadata": {
	                "text": "Text Post",
	                "title": "Text Post"	          
	            },
	              "date": "sampleDate",
	              "likes": 3,
	              "tried" : 2,
	              "challenge" : 3,
	              "comments": 5
	            },
	            {
	            	"type":"chat",
	              "thumbnailMetadata": {
	                  "title": "chat Post",
	                  "chat" : [{
	                	"name" : "Barney",
	                	"message" : "Hello"
	                  },
	                  {
	                	  "name" : "Ted",
	                	  "message" : "I am fine. How r u?",
	                  },
	                  {
	                	  "name" : "Barney",
	                	  "message" : "I am good."
		              }]
	               },
	              "date": "sampleDate",
	              "likes": 3,
	              "tried" : 2,
	              "challenge" : 3,
	              "comments": 5
	            }
	          ]
	        });
  
  //http://player.vimeo.com/video/40558553?title=0&byline=0&portrait=0
};