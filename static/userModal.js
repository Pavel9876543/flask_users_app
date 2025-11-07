export function showUserModal(user) {
  document.getElementById('userDetails').innerHTML = `
    <p><b>№</b> ${user.id}</p>
    <p><b>Имя:</b> ${user.name}</p>
    <p><b>Email:</b> ${user.email}</p>
  `;
  const modal = new bootstrap.Modal(document.getElementById('userModal'));
  modal.show();
}
