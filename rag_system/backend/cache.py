import logging
import functools
import hashlib
import json
import pickle
from pathlib import Path
from typing import Any, Callable
from datetime import datetime, timedelta
from config import USE_CACHE, CACHE_TTL, DATA_DIR

logger = logging.getLogger(__name__)

CACHE_DIR = DATA_DIR / "cache"
CACHE_DIR.mkdir(parents=True, exist_ok=True)


class CacheManager:
    """Manage caching for expensive operations"""
    
    @staticmethod
    def _get_cache_key(func_name: str, args: tuple, kwargs: dict) -> str:
        """Generate a cache key from function arguments"""
        key_data = f"{func_name}:{json.dumps(str(args))}{json.dumps(str(kwargs))}"
        return hashlib.md5(key_data.encode()).hexdigest()
    
    @staticmethod
    def _get_cache_file(cache_key: str) -> Path:
        """Get cache file path"""
        return CACHE_DIR / f"{cache_key}.cache"
    
    @staticmethod
    def get(cache_key: str) -> Any:
        """Get cached value"""
        if not USE_CACHE:
            return None
        
        cache_file = CacheManager._get_cache_file(cache_key)
        
        if not cache_file.exists():
            return None
        
        # Check if cache has expired
        file_age = datetime.now() - datetime.fromtimestamp(cache_file.stat().st_mtime)
        if file_age > timedelta(seconds=CACHE_TTL):
            cache_file.unlink()
            return None
        
        try:
            with open(cache_file, 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            logger.warning(f"Error loading cache: {e}")
            return None
    
    @staticmethod
    def set(cache_key: str, value: Any):
        """Set cached value"""
        if not USE_CACHE:
            return
        
        try:
            cache_file = CacheManager._get_cache_file(cache_key)
            with open(cache_file, 'wb') as f:
                pickle.dump(value, f)
        except Exception as e:
            logger.warning(f"Error saving cache: {e}")
    
    @staticmethod
    def clear():
        """Clear all cache"""
        try:
            for cache_file in CACHE_DIR.glob("*.cache"):
                cache_file.unlink()
            logger.info("Cache cleared")
        except Exception as e:
            logger.warning(f"Error clearing cache: {e}")


def cache_result(func: Callable) -> Callable:
    """Decorator to cache function results"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not USE_CACHE:
            return func(*args, **kwargs)
        
        cache_key = CacheManager._get_cache_key(func.__name__, args, kwargs)
        cached_value = CacheManager.get(cache_key)
        
        if cached_value is not None:
            logger.debug(f"Cache hit for {func.__name__}")
            return cached_value
        
        result = func(*args, **kwargs)
        CacheManager.set(cache_key, result)
        return result
    
    return wrapper
