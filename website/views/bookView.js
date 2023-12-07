class BookView {
  render(book, isupdating = false) {
    const container = document.getElementById('book-container');
    const display = `
      <div class="book-row">
        <span>${book.title}</span>
        <span>${book.description}</span>
        <span>${book.author}</span>
        <button onclick=bookUpdate(${book.id})>Update</button>
        <button onclick=bookDelete(${book.id})>Delete</button>
      </div>
    `
    const update = `
      <div class="book-row">
        <input type='text' id='book-update-title-${book.id}'>${book.title}</input>
        <input type='text' id='book-update-desc-${book.id}'>${book.description}</input>
        <input type='text' id='book-update-author-${book.id}'>${book.author}</input>
        <button onclick=bookUpdateCancel(${book.id})>Cancel</button>
        <button onclick=bookUpdateConfirm(${book.id})>Update</button>
      </div>
    `
    container.innerHTML += isupdating ? update : display;
  }
}
