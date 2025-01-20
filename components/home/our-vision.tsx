import styles from "../../public/home.module.css";
import Image from "next/image";
import Vision from "../../public/our-vision.svg";

export default function OurVision() {
  return (
    <section className={styles.hero}>
      <div className={styles.content}>
        <Image src={Vision} alt="hero" width="400" />
        <div className={styles.hero_text_content + " flex flex-col gap-4"}>
          <h2 className="font-bold text-4xl text-black text-right flex justify-end w-full">
            Our Vision
          </h2>
          <p className={styles.hero_secondary + " font-semibold text-right"}>
            To create a world where food waste is minimized, sustainability is a
            priority, and technology bridges the gap between resources and
            responsible consumption
          </p>
        </div>
      </div>
    </section>
  );
}
