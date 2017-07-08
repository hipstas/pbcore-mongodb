  function newWindow(filename){
    myWindow = window.open(filename ,"photo","width=550,height=450,left=0,top=0,resizable=no,scrollbars=auto,status=no,menubar=no,directories=no,toobar=no");
  }

  function photopop(filename) {
    var myPhotopop;
    myPhotopop = window.open(filename ,'photo','width=750,height=580,left=0,top=0,resizable=no,scrollbars=auto,status=no,menubar=no,directories=no,toolbar=no');
    myPhotopop.focus();
  }
