import styles from "../../public/home.module.css";
import BenefitsCard from "./benefits-card";

export default function BeneFitSection() {
  const data = [
    {
      title: "AI-Powered Food Waste Analysis",
      subTitle:
        "Analyze food waste through image-based segmentation and portion estimation.",
    },
    {
      title: "Personalized Recommendations",
      subTitle:
        "Get tailored suggestions to minimize waste, optimize portions, and plan meals effectively.",
    },
    {
      title: "Real-Time Reporting",
      subTitle:
        "Generate comprehensive waste reports directly from captured images.",
    },
    {
      title: "Versatile Applications",
      subTitle:
        "Ideal for households, eateries, and institutions for waste reduction and sustainability.",
    },
    {
      title: "Sustainability Insights",
      subTitle:
        "Track and improve your environmental impact with actionable insights.",
    },
  ];
  const benefitsCard = data.map((text, key) => {
    return (
      <BenefitsCard
        key={key}
        img={key + 1}
        title={text.title}
        subTitle={text.subTitle}
      />
    );
  });
  return (
    <section className={styles.benefits}>
      <div className={styles.content}>
        <h1 className={styles.benefits_content_title}>Features</h1>
        <div className={styles.cards_div}>{benefitsCard}</div>
      </div>
    </section>
  );
}
