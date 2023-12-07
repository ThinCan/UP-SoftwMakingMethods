const cors = require("cors")
const express = require("express")
const app = express();

app.use(cors());
app.use(express.json());

class Book {
    constructor(title, desc, author) {
        this.id = ++Book.bookid;
        this.title = title;
        this.description = desc;
        this.author = author;
    }

    static bookid = 0;
}
let books = [new Book("a", "b", "c")];

app.get("/api/Book/", (req, res) => {
    res.send({
        success: true,
        data: books
    });
})

app.post("/api/Book/", (req, res) => {
    books.push(new Book(req.body.title, req.body.description, req.body.author))
    res.send({
        success: true
    });
})

app.delete("/api/Book/:id", (req, res) => {
    books = books.filter(e => e.id != req.params.id);
    res.send({success: true})
})

app.put("/api/Book/:id", (req, res) => {
    const b = books.find(e => e.id == req.params.id)
    if(b) {
        b.title = req.body.title
        b.description= req.body.description, 
        b.author = req.body.author
    }
    res.send({success: true})
})

app.listen(7230, () => {});