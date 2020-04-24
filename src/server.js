const express = require('express')

const app = express()
const port = 7000

app.use(express.json())

app.post('/action', (request, response) => {
    response.send('action!')
})


app.get('/', (request, response) => {
    response.send('Hello world!')
    console.log(request.params)
})

app.listen(port, (err) => {
    if (err) {
        return console.log('something bad happened', err)
    }

    console.log(`server is listening on ${port}`)
})
