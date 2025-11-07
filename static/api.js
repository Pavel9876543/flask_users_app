export const Api = {
    getUsers: () => fetch('/users').then(res => res.json()),
    getUser: (id) => fetch(`/users/${id}`)
        .then(res => {
            if (!res.ok) throw new Error('Пользователь не найден');
            return res.json();
        })
};