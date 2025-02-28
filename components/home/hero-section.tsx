import styles from "../../public/home.module.css";
import Image from "next/image";
import Link from "next/link";
import Hero from "../../public/hero.svg";
import Logo from "../../public/logo.svg";

export default function HeroSection() {
  return (
    <section className={styles.hero}>
      <div className={styles.content}>
        <div className={styles.hero_text_content}>
          <Image src={Logo} alt="hero" width="400" />
          <p className={styles.hero_secondary}>
            Transforming the way we manage food waste—FoodOptima empowers
            smarter choices with AI-driven insights for a sustainable and
            waste-free future.
          </p>
          <Link href="https://xdre8yke6nc2keph4gxd9m.streamlit.app/">
            <button className={"uppercase " + styles.try_now}>
              <span>Try Now</span>
            </button>
          </Link>
        </div>
        <Image src={Hero} alt="hero" width="400" />
      </div>
    </section>
  );
}
