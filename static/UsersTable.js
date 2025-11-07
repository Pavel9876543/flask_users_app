export function renderUsersTable(users, onUserClick) {
  const container = document.getElementById('usersContainer');
  if (!users.length) {
    container.innerHTML = '<p class="text-muted">Пока нет пользователей 😢</p>';
    return;
  }

  const rows = users.map(u => `
    <tr data-id="${u.id}" class="user-row" style="cursor:pointer;">
      <td>${u.id}</td>
      <td>${u.name}</td>
      <td>${u.email}</td>
    </tr>`).join('');

  container.innerHTML = `
    <table class="table table-hover">
      <thead><tr><th>ID</th><th>Имя</th><th>Email</th></tr></thead>
      <tbody>${rows}</tbody>
    </table>`;

  document.querySelectorAll('.user-row').forEach(row =>
    row.addEventListener('click', () => onUserClick(row.dataset.id))
  );
}
