
    function redirectToPage() {
        var dropdown = document.getElementById("redirectDropdown");
        var selectedOption = dropdown.options[dropdown.selectedIndex].value;
        if (selectedOption !== "") {
            window.location.href = selectedOption;
        }
    }

    function toggleNumber() {
        var numberDisplay = document.getElementById("mobileNumber");
  
        if (numberDisplay.style.display === "none") {
          numberDisplay.style.display = "block";
        } else {
          numberDisplay.style.display = "none";
        }
      }
 