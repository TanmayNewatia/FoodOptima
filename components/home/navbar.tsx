"use client";

import Image from "next/image";
import styles from "../../public/home.module.css";
import Logo from "../../public/logo.svg";
import Link from "next/link";

export default function Navbar() {
  return (
    <>
      <header className={styles.navbar + " !bg-white/35 backdrop-blur-xl"}>
        <div className={styles.navbar_content}>
          <Link href="/">
            <Image src={Logo} alt="hero" width="150" />
          </Link>
          <div className={styles.navbar_menu}>
            <p className="font-bold text-black p-2">Home</p>
            <p className="font-bold text-black p-2">Mission</p>
            <p className="font-bold text-black p-2">Vision</p>
            <p className="font-bold text-black p-2">Features</p>
          </div>
          <div className="text-black flex items-center gap-8">
            <p className="text-primary font-bold border-2 rounded-full border-primary py-2 px-4">
              Register
            </p>
            <p className="bg-primary text-white font-bold border-2 rounded-full border-primary py-2 px-4">
              Login
            </p>
          </div>
        </div>
      </header>
    </>
  );
}
