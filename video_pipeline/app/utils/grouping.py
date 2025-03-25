def associate_faces_with_vehicles(faces, plates, vehicles):
    # Naive implementation: find faces within or near vehicle bounding boxes
    groups = []
    for vehicle in vehicles:
        vx1, vy1, vx2, vy2 = vehicle['bbox']
        group = {'vehicle': vehicle, 'faces': [], 'plates': plates}

        for face in faces:
            fx1, fy1, fx2, fy2 = face['bbox']
            if vx1 - 50 < fx1 < vx2 + 50 and vy1 - 50 < fy1 < vy2 + 50:
                group['faces'].append(face)
        groups.append(group)
    return groups
