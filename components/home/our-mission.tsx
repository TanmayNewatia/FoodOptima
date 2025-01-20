import styles from "../../public/home.module.css";
import Image from "next/image";
import Mission from "../../public/our-mission.svg";

export default function OurMission() {
  return (
    <section className={styles.hero}>
      <div className={styles.content}>
        <div className={styles.hero_text_content + " flex flex-col gap-4"}>
          <h2 className="font-bold text-4xl text-black">Our Mission</h2>
          <p className={styles.hero_secondary + " font-semibold"}>
            To revolutionize food waste management at the consumer & Management
            level, leveraging AI to empower individuals and organizations to
            make informed choices for a sustainable future.
          </p>
        </div>
        <Image src={Mission} alt="hero" width="400" />
      </div>
    </section>
  );
}
