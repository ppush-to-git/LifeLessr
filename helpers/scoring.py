def calcScore(distance):
    if distance <= 50:
        return 5000
    elif distance<=500:
        return 4500
    elif distance<=1000:
        return 3000
    elif distance<=2000:
        return 1500
    else:
        return 250
    
# Current scoring bands:
# 0–50 km      -> 5000
# 50–500 km    -> 4500
# 500–1000 km  -> 3000
# 1000–2000 km -> 1500
# 2000+ km     -> 250
# Future: interpolate scores within each band for smoother scaling.