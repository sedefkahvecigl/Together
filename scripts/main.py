#!/usr/bin/env python3
"""
Event Map Analytics & Validation Scripts

Bu script, Event Map projesi için:
- Kullanıcı doğrulama
- Veri analizi
- Veri temizleme
- Raporlama
"""

import os
import logging
from datetime import datetime
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

# Logging konfigürasyonu
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Ortam değişkenlerini yükle
load_dotenv()

class EventMapAnalytics:
    """Event Map Analiz Sınıfı"""
    
    def __init__(self):
        """Initialize Firebase connection"""
        try:
            # Firebase Admin SDK başlat
            if not firebase_admin._apps:
                cred = credentials.Certificate(
                    os.getenv('FIREBASE_KEY_PATH', 'firebase-key.json')
                )
                firebase_admin.initialize_app(cred)
            
            self.db = firestore.client()
            logger.info("Firebase connected successfully")
        except Exception as e:
            logger.error(f"Firebase connection failed: {e}")
            raise
    
    def validate_users(self):
        """Kullanıcı verilerini doğrula"""
        logger.info("Validating user data...")
        try:
            users_ref = self.db.collection('users')
            docs = users_ref.stream()
            
            valid_count = 0
            invalid_count = 0
            
            for doc in docs:
                user = doc.to_dict()
                if self._is_valid_user(user):
                    valid_count += 1
                else:
                    invalid_count += 1
                    logger.warning(f"Invalid user: {doc.id}")
            
            logger.info(f"User validation complete. Valid: {valid_count}, Invalid: {invalid_count}")
            return {'valid': valid_count, 'invalid': invalid_count}
        
        except Exception as e:
            logger.error(f"User validation failed: {e}")
            return None
    
    def _is_valid_user(self, user):
        """Kullanıcı verilerinin geçerli olup olmadığını kontrol et"""
        required_fields = ['email', 'username', 'created_at']
        return all(field in user for field in required_fields)
    
    def get_user_statistics(self):
        """Kullanıcı istatistiklerini al"""
        logger.info("Gathering user statistics...")
        try:
            users_ref = self.db.collection('users')
            total_users = len(users_ref.stream())
            
            logger.info(f"Total users: {total_users}")
            return {'total_users': total_users}
        
        except Exception as e:
            logger.error(f"Failed to get user statistics: {e}")
            return None
    
    def get_event_statistics(self):
        """Etkinlik istatistiklerini al"""
        logger.info("Gathering event statistics...")
        try:
            events_ref = self.db.collection('events')
            total_events = len(events_ref.stream())
            
            logger.info(f"Total events: {total_events}")
            return {'total_events': total_events}
        
        except Exception as e:
            logger.error(f"Failed to get event statistics: {e}")
            return None
    
    def generate_report(self):
        """Genel rapor oluştur"""
        logger.info("Generating report...")
        try:
            report = {
                'timestamp': datetime.now().isoformat(),
                'users': self.get_user_statistics(),
                'events': self.get_event_statistics(),
                'validation': self.validate_users()
            }
            
            logger.info("Report generated successfully")
            return report
        
        except Exception as e:
            logger.error(f"Report generation failed: {e}")
            return None


def main():
    """Ana fonksiyon"""
    try:
        analytics = EventMapAnalytics()
        
        # Rapor oluştur ve yazdır
        report = analytics.generate_report()
        
        if report:
            print("\n=== Event Map Analytics Report ===\n")
            print(f"Generated at: {report['timestamp']}")
            print(f"\nUsers: {report['users']}")
            print(f"Events: {report['events']}")
            print(f"Validation: {report['validation']}")
            print("\n=== End of Report ===\n")
    
    except Exception as e:
        logger.error(f"Main execution failed: {e}")
        raise


if __name__ == "__main__":
    main()
