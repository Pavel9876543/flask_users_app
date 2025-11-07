import { Api } from './api.js';
import { renderUsersTable } from './usersTable.js';
import { showUserModal } from './userModal.js';
import { setupUserForm } from './userForm.js';

async function loadUsers() {
  const users = await Api.getUsers();
  renderUsersTable(users, async id => {
    const user = await Api.getUser(id);
    showUserModal(user);
  });
}

async function addUser(user) {
  await Api.addUser(user);
  await loadUsers();
}

setupUserForm(addUser);
loadUsers();
