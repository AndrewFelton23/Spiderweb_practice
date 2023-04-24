import { configureStore } from "@reduxjs/toolkit";
import { PersonSlice } from "./features/personSlice";

export function makeStore(){
    return configureStore({
        reducer:{
            person:PersonSlice.reducer
        }
    });
}

export const store = makeStore();

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;