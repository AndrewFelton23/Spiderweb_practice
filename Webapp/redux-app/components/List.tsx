import { store, useAppSelector } from '@/store/store'
import React from 'react'
import { Provider } from 'react-redux'

const List = () => {
    const persons=useAppSelector((state)=>state.person.persons)
  return (
    <div>
        <p>
            This is List component:
        </p>
        <table>
            <thead>
                <tr>
                    <th>
                        ID
                    </th>
                    <th>
                        Name
                    </th>
                </tr>
            </thead>
            <tbody>
                {persons.map(person=>(
                    <tr key={person.id}>
                        <td>
                            {person.id}
                        </td>
                        <td>
                            {person.name}
                        </td>
                    </tr>
                ))}
            </tbody>
        </table>
    </div>
  )
}

export default List