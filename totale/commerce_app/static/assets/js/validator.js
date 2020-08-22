
function validateAdmission(){
  var phone = document.forms['admission-form']['phone'].value;
  var course = document.forms['admission-form']['course'].value;

  if (phone.length != 10){
    alert("Please enter a 10 digit phone number.");
    return false;
  }
  if (course == "w"){
    alert("Please enter a valid course name.");
    return false;
  }

  return true;

}
