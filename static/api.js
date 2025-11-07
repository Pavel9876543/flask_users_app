export const Api = {
  getUsers: () => fetch('/users').then(r => r.json()),
  getUser: (id) => fetch(`/users/${id}`).then(r => r.json()),
  addUser: (user) =>
    fetch('/users', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(user)
    }).then(async res => {
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'Ошибка при добавлении');
      return data;
    })
};
