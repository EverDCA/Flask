// Modo oscuro/claro
const toggleButton = document.getElementById('theme-toggle');
const body = document.body;

// Cambiar el tema al presionar el botón
toggleButton.addEventListener('click', () => {
    if (body.classList.contains('light-mode')) {
        body.classList.replace('light-mode', 'dark-mode');
        toggleButton.innerHTML = '<i class="bi bi-brightness-high"></i>'; // Cambia a ícono de sol
        localStorage.setItem('theme', 'dark-mode');
    } else {
        body.classList.replace('dark-mode', 'light-mode');
        toggleButton.innerHTML = '<i class="bi bi-moon"></i>'; // Cambia a ícono de luna
        localStorage.setItem('theme', 'light-mode');
    }
});

// Aplicar tema guardado
const savedTheme = localStorage.getItem('theme');
if (savedTheme) {
    body.classList.add(savedTheme);
    toggleButton.innerHTML = savedTheme === 'dark-mode'
        ? '<i class="bi bi-brightness-high"></i>' // Ícono de sol
        : '<i class="bi bi-moon"></i>'; // Ícono de luna
}
