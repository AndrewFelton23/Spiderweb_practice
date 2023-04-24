import React from 'react'
import type { NextPage } from 'next';
import styles from "../styles/home.module.css"
import Link from 'next/link';
import Router from 'next/router';

const Home: NextPage = () => {
  const name = "John Doe";
  const age = "27";
  const job = "Software Developer"
  const company = "Google";

  function sendProps(){
    Router.push({
      pathname:"/userProfile",
      query:{
        name,
        age,
        job,
        company
      }
    })
  }

  return(
    <div className={styles.home_container}>
      <div className={styles.home_card}>
        <h1 className={styles.h1}>Using a router</h1>
        <button onClick={() => sendProps()}>send</button>
      </div>
    </div>
  );
};



export default Home;