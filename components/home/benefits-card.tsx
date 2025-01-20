import styles from "../../public/home.module.css";
import Image from "next/image";

export default function BenefitsCard({
  img,
  title,
  subTitle,
}: {
  img: number;
  title: string;
  subTitle: string;
}) {
  return (
    <div className={styles.card}>
      <div className={styles.card_image}>
        <Image src={`/${img}.svg`} alt={title} width={125} height={125} />
      </div>
      <p className="text-black font-bold text-[1rem]">{title}</p>
      <p className="text-black font-normal text-[0.875rem]">{subTitle}</p>
    </div>
  );
}
