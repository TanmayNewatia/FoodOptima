import HeroSection from "./hero-section";
import BeneFitSection from "./benefit-section";
import OurMission from "./our-mission";
import OurVision from "./our-vision";

export default function HomePage() {
  return (
    <>
      <HeroSection />
      <OurMission />
      <OurVision />
      <BeneFitSection />
    </>
  );
}
