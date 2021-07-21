import React, { useState } from 'react'

const Button = (props) => (
    <button onClick={props.handleClick}>
        {props.text}
    </button>
)

const StatisticRow = ({ text, value }) => { 
    if (text === "positive") {
        return (
            <tr>
                <td>{text}</td> 
                <td>{value}%</td>
            </tr>
        )
    }
    return (
        <tr>
            <td>{text}</td>
            <td>{value}</td>
        </tr>
    )
}

const Statistics = ({ good, neutral, bad}) => {
    if (good === 0 && neutral === 0 && bad === 0) {
        return (
            <div>
            <h1>statistics</h1>
            <p>No feedback given</p>
            </div>
        )
    }
    return (
        <div>
        <h1>statistics</h1>
        <table>
            <tbody>
            <StatisticRow text="good" value={good} />
            <StatisticRow text="neutral" value={neutral} />
            <StatisticRow text="bad" value={bad} />
            <StatisticRow text="average" value={(good - bad) / (good + bad + neutral)} />
            <StatisticRow text="positive" value={good / (good + bad + neutral) * 100} /> 
            </tbody>
        </table>
        </div>
    )
}
const App = () => {
    const [good, setGood] = useState(0) 
    const [neutral, setNeutral] = useState(0)
    const [bad, setBad] = useState(0)

    const handleGoodClick = () => setGood(good + 1)
    const handleNeutralClick = () => setNeutral(neutral + 1)
    const handleBadClick = () => setBad(bad + 1)

    return (
        <div>
            <h1>give feedback</h1>
            <Button handleClick={handleGoodClick} text='good' /> 
            <Button handleClick={handleNeutralClick} text='neutral' /> 
            <Button handleClick={handleBadClick} text='bad' /> 
            <Statistics good={good} neutral={neutral} bad={bad} />
        </div>
    )
}

export default App
