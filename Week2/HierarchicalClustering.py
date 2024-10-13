import numpy as np

def Davg(D, C1, C2, C, sizes):
    # Tính khoảng cách trung bình giữa cụm mới (C1 và C2) và cụm C
    return (D[C1, C] * sizes[C1] + D[C2, C] * sizes[C2]) / (sizes[C1] + sizes[C2])

def HierarchicalClustering(n, D):
    # Khởi tạo các cụm, ban đầu mỗi phần tử là một cụm đơn
    clusters = {i: [i] for i in range(n)}  # lưu các cụm dưới dạng danh sách các phần tử
    sizes = {i: 1 for i in range(n)}  # lưu kích thước của mỗi cụm
    current_cluster = n  # chỉ số cụm mới sau khi gộp
    merge_order = []  # lưu trật tự gộp cụm
    
    while len(clusters) > 1:
        # Tìm hai cụm gần nhất C1 và C2
        min_dist = float('inf')
        closest_pair = None
        for C1 in clusters:
            for C2 in clusters:
                if C1 < C2:  # tránh so sánh lặp và so sánh chính nó
                    if D[C1, C2] < min_dist:
                        min_dist = D[C1, C2]
                        closest_pair = (C1, C2)
        
        # Lấy hai cụm gần nhất là C1 và C2
        C1, C2 = closest_pair
        new_cluster = current_cluster  # chỉ số của cụm mới
        current_cluster += 1  # tăng chỉ số cho lần gộp cụm tiếp theo
        
        # Gộp C1 và C2 vào cụm mới Cnew
        clusters[new_cluster] = clusters[C1] + clusters[C2]  # gộp các phần tử của C1 và C2
        sizes[new_cluster] = sizes[C1] + sizes[C2]  # cập nhật kích thước cho cụm mới
        merge_order.append(clusters[new_cluster])  # lưu trật tự gộp cụm
        
        # Cập nhật ma trận khoảng cách với cụm mới
        for C in clusters:
            if C != C1 and C != C2:  # tránh tính khoảng cách cho chính cụm mới
                D[new_cluster, C] = Davg(D, C1, C2, C, sizes)  # tính khoảng cách mới
                D[C, new_cluster] = D[new_cluster, C]  # đối xứng khoảng cách mới
        
        # Xóa cụm cũ C1 và C2 sau khi gộp
        del clusters[C1]
        del clusters[C2]
    
    # In kết quả trật tự các cụm được gộp
    for cluster in merge_order:
        print(" ".join(str(x + 1) for x in sorted(cluster)))  # in danh sách cụm theo thứ tự tăng dần

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        n = int(f.readline().strip())  # đọc số lượng phần tử n
        D = np.zeros((2*n-1, 2*n-1))  # khởi tạo ma trận khoảng cách mở rộng
        for i in range(n):
            D[i, :n] = list(map(float, f.readline().split()))  # đọc ma trận khoảng cách từ file

    HierarchicalClustering(n, D)  # chạy thuật toán
