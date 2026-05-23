from scripts.validators import check_barrier_ratio
from scripts.engine import BarrieEngine
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger("Barrie")

def main():
    # Setup
    target_ph = 5.2
    ingredient = "Ceramide_NP"
    
    # 1. Macro Check
    is_valid, status = check_barrier_ratio(3, 1, 1)
    
    if is_valid:
        # 2. Micro Inference
        engine = BarrieEngine()
        results, status = engine.predict_kinetics(ingredient, target_ph)
        
        if results:
            logger.info(f"Analysis for {ingredient}:")
            logger.info(f"Target Enzyme: {results['enzyme']}")
            logger.info(f"Km (Affinity): {results['km']}")
            logger.info(f"Adjusted kcat (Activity): {results['adjusted_kcat']}")
            logger.info(f"Status: {results['status']}")
        else:
            logger.error(status)
    else:
        logger.warning("Skipped AI Analysis due to Macro-check failure.")

if __name__ == "__main__":
    main()
