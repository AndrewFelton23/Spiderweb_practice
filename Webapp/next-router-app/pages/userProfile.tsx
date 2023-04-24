import type { NextPage } from "next";
import styles from "../styles/user.module.css"
import { useRouter } from "next/router";

function userProfile() {
    const router = useRouter();
    const {
        query: {name, age, job, company},
    } = router

    const props = {
        name,
        age,
        job,
        company
    }

  return (
    <div className={styles.user_container}>
        <div className={styles.user_card}>
            <h1>User Profile</h1>
            <section>
                <p>Name <span>{props.name}</span></p>
                <p>Age <span>{props.age}</span></p>
                <p>Job Title <span>{props.job}</span></p>
                <p>Company <span>{props.company}</span></p>
            </section>
        </div>
    </div>
  )
}

export default userProfile;