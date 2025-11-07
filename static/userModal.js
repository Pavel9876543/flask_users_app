export class UserModal {
    constructor(modalId) {
        this.modalElement = document.getElementById(modalId);
        this.modalBody = this.modalElement.querySelector('#modalBody');
        this.bsModal = new bootstrap.Modal(this.modalElement);
    }

    show(user) {
        if (user) {
            this.modalBody.innerHTML = `
                <p><strong>ID:</strong> ${user.id}</p>
                <p><strong>Имя:</strong> ${user.name}</p>
                <p><strong>Email:</strong> ${user.email}</p>
            `;
        } else {
            this.modalBody.innerHTML = `<p class="text-danger">Ошибка загрузки пользователя</p>`;
        }
        this.bsModal.show();
    }
}
