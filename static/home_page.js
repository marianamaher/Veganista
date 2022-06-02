$(document).ready(function() {
    
    $(".form-control").focus();
    
    $("#myform").submit(function(event) {
      
        

        if ($.trim($(".form-control").val()) === "") {
          $(".form-control").focus();
          return false;
        }

        else{
            let new_entry = $(".form-control").val()
            let newvar = new_entry.toLowerCase();
            console.log(newvar)
            window.location.href = ("/results_page/" + newvar)
        }
        
        event.preventDefault();

        
    });

                   

})