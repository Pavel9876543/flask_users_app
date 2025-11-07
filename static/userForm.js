export function setupUserForm(onAdd) {
  const form = document.getElementById('userForm');
  const msg = document.getElementById('message');

  form.addEventListener('submit', async e => {
    e.preventDefault();
    msg.innerHTML = '';

    const user = {
      name: document.getElementById('name').value.trim(),
      email: document.getElementById('email').value.trim()
    };

    try {
      await onAdd(user);
      msg.innerHTML = `<div class="alert alert-success">Пользователь добавлен!</div>`;
      form.reset();
    } catch (err) {
      msg.innerHTML = `<div class="alert alert-danger">${err.message}</div>`;
    }
  });
}
