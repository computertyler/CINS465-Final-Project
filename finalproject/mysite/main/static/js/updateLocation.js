
function confirmHome(){
    if (confirm("Are you sure you want to leave this form")) {
        window.location.replace("");
      } 
}
function confirmUpdate(){
    if (confirm("Are you sure you want to leave this form")) {
        window.location.replace("{% url 'update' %}");
      } 
}
function confirmAbout(){
    if (confirm("Are you sure you want to leave this form")) {
        window.location.replace("{% url 'about' %}" );
      } 
}
function confirmLocation(){
  if (confirm("Are you sure you want to leave this form")) {
      window.location.replace("{% url 'updateLocation' %}");
    } 
}