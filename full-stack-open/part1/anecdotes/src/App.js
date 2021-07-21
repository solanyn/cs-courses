import { React, useState } from 'react'

const Button = ({ text, handleClick }) => {
    return (
        <button onClick={handleClick}>{text}</button>
    )
}

const MostVotes = ({ text }) => {
    console.log(text)
    return (
        <div>
            <h1>Anecdote with most votes</h1>
            <p>{text}</p>
        </div>
    )
}

const App = () => {
    const anecdotes = [
        'If it hurts, do it more often',
        'Adding manpower to a late software project makes it later!',
        'The first 90 percent of the code accounts for the first 90 percent of the development time...The remaining 10 percent of the code accounts for the other 90 percent of the development time.',
        'Any fool can write code that a computer can understand. Good programmers write code that humans can understand.',
        'Premature optimization is the root of all evil.',
        'Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it.',
        'Programming without an extremely heavy use of console.log is same as if a doctor would refuse to use x-rays or blod tests when dianosing patients'
    ]
   
    const [selected, setSelected] = useState(0)
    const [points, setPoints] = useState(Array(anecdotes.length).fill(0))

    const selectNext = () => setSelected(Math.floor(Math.random() * anecdotes.length))
    const addVote = () => {
        const copy = [...points]
        copy[selected] += 1
        console.log(copy)
        setPoints(copy)
    }

    return (
        <div>
            <p>{anecdotes[selected]}</p>
            <p>Has {points[selected]} votes</p>
            <Button text="vote" handleClick={addVote} />
            <Button text="next anecdote" handleClick={selectNext} />
            <MostVotes text={anecdotes[points.indexOf(Math.max.apply(Math, points))]} />
        </div>
    )
}

export default App
