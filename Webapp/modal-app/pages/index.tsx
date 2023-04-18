import { Fragment,useState } from "react";
import styles from "../styles/popup.module.css";

const Popup = () => {
  const [show, setShow] = useState(false);

  const toggle = () => {
    //When the button is pressed either hide or show the form
    setShow(!show)
  };

  return(
    <Fragment>
      <button className={styles.btn}>

      </button>
    </Fragment>
  )
}