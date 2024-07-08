const hamburger = document.querySelector('.hamburger');
const navLink = document.querySelector('.nav__link');

hamburger.addEventListener('click', () => {
  navLink.classList.toggle('hide');
});


document.addEventListener("DOMContentLoaded", function() {
  var toggleButton = document.querySelector('.toggle-button'); // Adjust this selector to match your HTML
  if (toggleButton) {
      toggleButton.addEventListener('click', function() {
          // Your event handler logic
          console.log('Toggle button clicked!');
      });
  } else {
      console.error('Toggle button not found.');
  }
});
