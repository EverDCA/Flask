// initialize constants with some values. We'll use them in our toggle function
const DARK_MODE = 'dark';
const LIGHT_MODE = 'light';
const THEME = 'mode';

// a callout function will be called as soon as the page DOM loads
document.addEventListener('DOMContentLoaded', (event) => {
  applyTheme(); 
  const toggleSwitch = document.getElementById('toggle-switch');
  toggleSwitch.onclick = function() {
    let currentMode = localStorage.getItem(THEME);
    localStorage.setItem(THEME, currentMode === DARK_MODE ? LIGHT_MODE : DARK_MODE);
    applyTheme();
  }
});

// this function implements the switch between light and dark mode
function applyTheme() {
  let html = document.documentElement; // this selects the html element
  let currentMode = localStorage.getItem(THEME);
  if (currentMode === DARK_MODE) {
    html.classList.add(DARK_MODE);
    document.getElementById('toggle-switch').innerHTML = '<i class="fas fa-sun"></i>';
  } else {
    html.classList.remove(DARK_MODE);
    document.getElementById('toggle-switch').innerHTML = '<i class="fas fa-moon"></i>';
  }
}