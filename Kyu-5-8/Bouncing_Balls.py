def bouncing_ball(h, bounce, window):
    result = -1
    if not (h > 0 and (bounce > 0 and bounce < 1) and window < h):
        return result
    else:
        vistas = 1
        h = h * bounce
        while h > window:
            vistas += 2
            h *= bounce
    return vistas

print(bouncing_ball(3, 0.66, 1.5))