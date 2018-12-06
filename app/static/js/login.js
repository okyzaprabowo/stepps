$(document).ready(function(){


    $("#a-login").click(function(e) {
      e.preventDefault();
      var user = $('#username').val();
      var pass = $('#password').val();
  
      if(user=="admin" && pass=="12345") {
        window.location.href = "http://192.168.10.10:8000/dashboard/";
      } else {
        alert("Username atau Password salah");
      }
    });

    $('#password').keypress(function (e) {
        if (e.which == 13) {
            var user = $('#username').val();
            var pass = $('#password').val();
            if(user=="admin" && pass=="12345") {
                window.location.href = "http://192.168.10.10:8000/dashboard/";
            } else {
                alert("Username atau Password salah");
            }
            return false;    //<---- Add this line
        }
        
      });
});