import { configureStore } from "@reduxjs/toolkit";
import { PersonSlice } from "./features/personSlice";
import { TypedUseSelectorHook, useDispatch, useSelector } from "react-redux"


export const store= configureStore({
    reducer:{
        person:PersonSlice.reducer
    }
})

//Especially for typescript
export const useAppDispatch:()=>typeof store.dispatch=useDispatch;
export const useAppSelector:TypedUseSelectorHook<ReturnType<typeof store.getState>>=useSelector;