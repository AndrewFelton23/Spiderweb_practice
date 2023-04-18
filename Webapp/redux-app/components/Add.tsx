import { addPerson } from '@/store/features/personSlice';
import { store, useAppDispatch } from '@/store/store'
import React, { useRef } from 'react'
import { Provider } from 'react-redux';

const Add = () => {
    const name=useRef<string>("")
    const dispatch = useAppDispatch();


  return (
    <form>
        <label htmlFor=''>
            Person Name
        </label>
        <input onChange={e=>name.current=e.target.value}/>
        <button onClick={()=>dispatch(addPerson({name:name.current}))}>
            Add
        </button>
    </form>
  )
}

export default Add;