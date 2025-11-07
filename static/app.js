import { UserModal } from './userModal.js';
import { UsersTable } from './usersTable.js';

document.addEventListener('DOMContentLoaded', () => {
    const modal = new UserModal('userModal');
    const table = new UsersTable('usersTableContainer', modal);
    table.render();
});