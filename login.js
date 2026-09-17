const loginForm = document.getElementById('loginForm');
const message = document.getElementById('message');

loginForm.addEventListener('submit', function (event) {
  event.preventDefault();

  const username = document.getElementById('username').value.trim();
  const password = document.getElementById('password').value.trim();

  message.className = 'message';

  if (!username || !password) {
    message.textContent = 'Debes completar usuario y contraseña.';
    message.classList.add('error');
    return;
  }

  if (username.length < 3) {
    message.textContent = 'El usuario debe tener al menos 3 caracteres.';
    message.classList.add('error');
    return;
  }

  if (password.length < 4) {
    message.textContent = 'La contraseña debe tener al menos 4 caracteres.';
    message.classList.add('error');
    return;
  }

  message.textContent = `Bienvenido, ${username}. Acceso correcto.`;
  message.classList.add('success');

  localStorage.setItem('usuario', username);

  setTimeout(() => {
    window.location.href = 'index.html';
  }, 1000);
});
