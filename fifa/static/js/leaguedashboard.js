$(document).ready(function () {
  var csrftoken = getCookie('csrftoken');
  alert("in the league .js");
  window.location.href = "/"
  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
        }
  });
});
