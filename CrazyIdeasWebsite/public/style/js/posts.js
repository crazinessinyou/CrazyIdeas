function getPosts(posts) {
	for(post in posts) {
		if(post.hasOwnProperty("type")) {
			postType = post.type;
			if(postType == 'image') {
				<% import  image-post.ejs%>
			} else if(postType == 'video') {
				<% import  video-post.ejs%>
			}
		}
	}
}