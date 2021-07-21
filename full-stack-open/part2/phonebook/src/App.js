import React, { useState } from 'react'

const App = () => {
    const [persons, setPersons] = useState([
        { name: 'Arto Hellas' }
    ])
    const [newName, setNewName] = useState('')
    
    const handlePersonChange = (event) => {
        console.log(event.target.value)
        setNewName(event.target.value)
    }
    
    const addPerson = (event) => {
        event.preventDefault()
        const personObject = { name: newName }
        setPersons(persons.concat(personObject))
        setNewName('')
    }

    return (
        <div>
            <h2>Phonebook</h2>
            <form>
                <div>
                    name: <input value={newName} onChange={handlePersonChange} />
                </div>
                <div>
                    <button type="submit" onClick={addPerson}>add</button>
                </div>
            </form>
            <h2>Numbers</h2>
            {persons.map((person) => 
                <p>{person.name}</p>
            )}
        </div>
    )
}

export default App