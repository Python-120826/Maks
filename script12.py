fetch('https://jsonplaceholder.typicode.com/posts/1/comments')
  .then((response) => response.json())
  .then((comments) => console.log('Комментарии к посту:', comments));

// 2. Добавить новый комментарий (POST)
fetch('https://jsonplaceholder.typicode.com/comments', {
  method: 'POST',
  body: JSON.stringify({
    postId: 1,
    name: 'Имя автора',
    email: 'user@example.com',
    body: 'Текст моего комментария',
  }),
  headers: {
    'Content-type': 'application/json; charset=UTF-8',
  },
})
  .then((response) => response.json())
  .then((newComment) => console.log('Созданный комментарий:', newComment));

// 3. Удалить комментарий (DELETE)
fetch('https://jsonplaceholder.typicode.com/comments/1', {
  method: 'DELETE',
}).then((response) => {
  if (response.ok) console.log('Комментарий удалён');
});

#чуть чуть  не понял как делать это