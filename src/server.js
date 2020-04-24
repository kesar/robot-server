const express = require('express')
const {spawn} = require('child_process')

const app = express()
const port = 3000

app.use(express.json())

app.post('/action', (request, response) => {
    response.send('action!')
    console.log(request.body)

    const motor = spawn('python3', ['lib/motor.py'])
    motor.stdout.on('data', function (data) {
        console.log(data)
    })
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
