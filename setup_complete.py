#!/usr/bin/env python3
"""
Complete setup script for the Calorie App
This script will:
1. Initialize the database
2. Create sample food items
3. Set up proper configurations
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from server import app, db
from models import FoodItem, Nutrients

def create_sample_foods():
    """Create sample food items with nutrition data"""
    
    sample_foods = [
        # Fruits
        {"name": "Apple", "brand": "Generic", "serving_qty": 1, "serving_unit": "medium (182g)", 
         "calories": 95, "protein_g": 0.5, "fat_g": 0.3, "carbs_g": 25, "fiber_g": 4.4},
        {"name": "Banana", "brand": "Generic", "serving_qty": 1, "serving_unit": "medium (118g)", 
         "calories": 105, "protein_g": 1.3, "fat_g": 0.4, "carbs_g": 27, "fiber_g": 3.1},
        {"name": "Orange", "brand": "Generic", "serving_qty": 1, "serving_unit": "medium (154g)", 
         "calories": 62, "protein_g": 1.2, "fat_g": 0.2, "carbs_g": 15, "fiber_g": 3.1},
        
        # Vegetables
        {"name": "Broccoli", "brand": "Generic", "serving_qty": 1, "serving_unit": "cup (91g)", 
         "calories": 31, "protein_g": 2.6, "fat_g": 0.3, "carbs_g": 6, "fiber_g": 2.4},
        {"name": "Chicken Breast", "brand": "Generic", "serving_qty": 100, "serving_unit": "grams", 
         "calories": 165, "protein_g": 31, "fat_g": 3.6, "carbs_g": 0, "fiber_g": 0},
        {"name": "Brown Rice", "brand": "Generic", "serving_qty": 1, "serving_unit": "cup (195g)", 
         "calories": 216, "protein_g": 5, "fat_g": 1.8, "carbs_g": 45, "fiber_g": 3.5},
        
        # Proteins
        {"name": "Eggs", "brand": "Generic", "serving_qty": 2, "serving_unit": "large", 
         "calories": 140, "protein_g": 12, "fat_g": 10, "carbs_g": 1, "fiber_g": 0},
        {"name": "Greek Yogurt", "brand": "Generic", "serving_qty": 1, "serving_unit": "cup (227g)", 
         "calories": 130, "protein_g": 22, "fat_g": 0, "carbs_g": 9, "fiber_g": 0},
        
        # Grains
        {"name": "Whole Wheat Bread", "brand": "Generic", "serving_qty": 2, "serving_unit": "slices", 
         "calories": 140, "protein_g": 8, "fat_g": 2, "carbs_g": 24, "fiber_g": 4},
        {"name": "Oatmeal", "brand": "Generic", "serving_qty": 1, "serving_unit": "cup cooked", 
         "calories": 145, "protein_g": 5, "fat_g": 2.5, "carbs_g": 25, "fiber_g": 4},
        
        # Snacks
        {"name": "Almonds", "brand": "Generic", "serving_qty": 1, "serving_unit": "ounce (28g)", 
         "calories": 164, "protein_g": 6, "fat_g": 14, "carbs_g": 6, "fiber_g": 3.5},
        {"name": "Protein Bar", "brand": "Generic", "serving_qty": 1, "serving_unit": "bar (60g)", 
         "calories": 200, "protein_g": 20, "fat_g": 8, "carbs_g": 15, "fiber_g": 3},
        
        # Beverages
        {"name": "Milk", "brand": "Generic", "serving_qty": 1, "serving_unit": "cup (240ml)", 
         "calories": 103, "protein_g": 8, "fat_g": 2.4, "carbs_g": 12, "fiber_g": 0},
        {"name": "Protein Shake", "brand": "Generic", "serving_qty": 1, "serving_unit": "scoop (30g)", 
         "calories": 120, "protein_g": 24, "fat_g": 1, "carbs_g": 3, "fiber_g": 1},
    ]
    
    with app.app_context():
        # Clear existing food items
        FoodItem.query.delete()
        Nutrients.query.delete()
        db.session.commit()
        
        # Add sample foods
        for food_data in sample_foods:
            # Create food item
            food = FoodItem(
                name=food_data["name"],
                brand=food_data["brand"],
                serving_qty=food_data["serving_qty"],
                serving_unit=food_data["serving_unit"],
                source="custom"
            )
            db.session.add(food)
            db.session.flush()  # Get the ID without committing
            
            # Create nutrients
            nutrients = Nutrients(
                food_id=food.id,
                calories=food_data["calories"],
                protein_g=food_data["protein_g"],
                fat_g=food_data["fat_g"],
                carbs_g=food_data["carbs_g"],
                fiber_g=food_data["fiber_g"]
            )
            db.session.add(nutrients)
        
        db.session.commit()
        print(f"✅ Created {len(sample_foods)} sample food items")

def main():
    """Main setup function"""
    print("🍽️  Setting up Calorie App...")
    
    with app.app_context():
        # Create all tables
        db.create_all()
        print("✅ Database tables created")
        
        # Create sample foods
        create_sample_foods()
        
        print("🎉 Setup complete! Your app is ready to use.")
        print("\n📱 Features now available:")
        print("• User registration and login")
        print("• Profile management with body analysis")
        print("• Food logging with 15+ sample foods")
        print("• Calorie tracking and daily progress")
        print("• Real-time food detection (with webcam)")
        print("• AI-powered nutrition advice")
        print("• Advanced RAG chat system")
        print("• Exercise recommendations")

if __name__ == "__main__":
    main()
