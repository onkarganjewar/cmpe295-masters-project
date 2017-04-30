$(document).ready(function () {

$('.upload-btn').on('click', function (){
    $('#upload-input').click();
    $('.progress-bar').text('0%');
    $('.progress-bar').width('0%');
});

$('#upload-input').on('change', function(){

  var files = $(this).get(0).files;
  if (files.length > 0){
    // create a FormData object which will be sent as the data payload in the
    // AJAX request
    var formData = new FormData();

    // loop through all the selected files and add them to the formData object
    //for (var i = 0; i < files.length; i++) {
      var file = files[0];
      var filename = file.name
      var filetype = filename.substring((filename.indexOf(".")) + 1);
      if(filetype != 'jpg' && filetype != 'jpeg' && filetype != 'png' && filetype != 'avi' && filetype != 'mp4' && filetype != 'mov'){
	alert("Invalid file type");
	return;	
      }

     //code to display input file when selected
      if(filetype === 'jpg' || filetype === 'jpeg' || filetype === 'png'){
	var reader = new FileReader();
	
	reader.onload = function (e) {
                var inputImg = $('<img>');
                inputImg.attr("width","500px");
                inputImg.attr("height","400px");
		inputImg.css("margin-top","20px");
                inputImg.attr("src",e.target.result);
                inputImg.appendTo('.jumbotron');

            };
	reader.readAsDataURL(this.files[0]);

      }

      if(filetype === 'mp4' || filetype === 'avi' || filetype === 'mov'){
        var reader = new FileReader();

        reader.onload = function (e) {
                var inputVid = $('<video controls>');
                inputVid.attr("width","500px");
                inputVid.attr("height","400px");
		//inputVid.css("margin-top","20px");
                inputVid.attr("src",e.target.result);
                inputVid.appendTo('.jumbotron');

            };
        reader.readAsDataURL(this.files[0]);

      }


      // add the files to formData object for the data payload
      formData.append('uploads[]', file, file.name);
    }
	
    $.ajax({
      url: '/upload',
      type: 'POST',
      data: formData,
      processData: false,
      contentType: false,
      success: function(data){
          //console.log('upload successful!\n' + data);
          //var b64Response = btoa(unescape(encodeURIComponent(data)));
	  //console.log(b64Response);
	  $('#loader').hide();
	  $('#notify').hide();
	  if(filetype === 'jpg'|| filetype === 'png' || filetype === 'jpeg' ){
          	var outputImg = $('<img>');
          	outputImg.attr("width","500px");
	  	outputImg.attr("height","400px");
		outputImg.css("margin-left","20px");
		outputImg.css("margin-top","20px");
	        outputImg.attr("src","data:image/jpeg;base64, " + data);
          	outputImg.appendTo('.jumbotron');
	  }else if(filetype === 'mp4' || filetype === 'avi' || filetype === 'mov'){
	  	var outputVid = $('<video controls>');
	  	outputVid.attr("width","500px");
          	outputVid.attr("height","400px");
		outputVid.css("margin-left","20px");
		//outputVid.css("margin-top","20px");
          	outputVid.attr("src","data:video/mp4;base64, " + data);
          	outputVid.appendTo('.jumbotron');
	  }else{
		alert("Invalid file type");
		//break;
	  }
      },
      xhr: function() {
        // create an XMLHttpRequest
        var xhr = new XMLHttpRequest();

        // listen to the 'progress' event
        xhr.upload.addEventListener('progress', function(evt) {

          if (evt.lengthComputable) {
            // calculate the percentage of upload completed
            var percentComplete = evt.loaded / evt.total;
            percentComplete = parseInt(percentComplete * 100);

            // update the Bootstrap progress bar with the new percentage
            $('.progress-bar').text(percentComplete + '%');
            $('.progress-bar').width(percentComplete + '%');

            // once the upload reaches 100%, set the progress bar text to done
            if (percentComplete === 100) {
              $('.progress-bar').html('Done');
	      $('#loader').show();
	      $('#notify').show();
            }

          }

        }, false);

        return xhr;
      }
    });

});


});
