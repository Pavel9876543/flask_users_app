import { Api } from './api.js';

export class UsersTable {
    constructor(containerId, modal) {
        this.container = document.getElementById(containerId);
        this.modal = modal;
    }

    render() {
        this.container.innerHTML = `<table class="table table-striped">
            <thead>
                <tr><th>№</th><th>Имя</th></tr>
            </thead>
            <tbody id="tableBody"></tbody>
        </table>`;

        this.loadUsers();
    }

    loadUsers() {
        const tbody = this.container.querySelector('#tableBody');
        Api.getUsers()
            .then(users => {
                tbody.innerHTML = '';
                users.forEach(user => {
                    const tr = document.createElement('tr');
                    tr.innerHTML = `<td>${user.id}</td><td>${user.name}</td>`;
                    tr.addEventListener('click', () => this.showUserDetails(user.id));
                    tbody.appendChild(tr);
                });
            })
            .catch(err => {
                tbody.innerHTML = `<tr><td colspan="3" class="text-danger">Ошибка: ${err.message}</td></tr>`;
            });
    }

    showUserDetails(userId) {
        Api.getUser(userId)
            .then(user => this.modal.show(user))
            .catch(err => this.modal.show(null));
    }
}
