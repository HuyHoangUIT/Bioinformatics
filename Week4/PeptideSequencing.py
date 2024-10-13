import numpy as np

_amino_acid_by_mass_ = {57:"G", 71:"A", 87:"S", 97:"P", 99:"V", 101:"T", 103:"C", 113:"L", 114:"N", 115:"D", 128:"Q", 129:"E", 131:"M", 137:"H", 147:"F", 156:"R", 163:"Y", 186:"W"}
_mass_by_amino_acid_ = {"G":57, "A":71, "S":87, "P":97, "V":99, "T":101, "C":103, "L":113, "N":114, "D":115, "Q":128, "E":129, "M":131, "H":137, "F":147, "R":156, "Y":163, "W":186, "I":113, "K":128}
def _input():
    with open('input.txt', 'r') as fi:
        data = fi.read().strip().split()
    spectralVector = list(map(int, data))
    spectralVector.insert(0, 0)
    return spectralVector

# spectralVector: Đây là vector phổ, chứa các giá trị cường độ của các đỉnh phổ tại các vị trí khác nhau
# _amino_acid_by_mass_: Đây là bảng ánh xạ giữa khối lượng và ký hiệu axit amin
def findPeptide(spectralVector, _amino_acid_by_mass_):
    l = len(spectralVector)
    adj = [[] for _ in range(l)]
    for i in range(l):
        for j in range(i, l):
            # nếu khoảng cách j - i tồn tại trong _amino_acid_by_mass_, thì j sẽ được thêm vào danh sách kề của i
            if j-i in _amino_acid_by_mass_:
                adj[i].append(j)
    
    # Bellman-Ford algorithm
    dist = [-np.inf] * l # đại diện cho giá trị điểm số tốt nhất có thể đạt được tại mỗi đỉnh
    parent = [None] * l # dùng để lưu lại đỉnh cha của mỗi đỉnh trên đường đi tốt nhất
    dist[0] = 0
    updated = True  

    # Vòng lặp tiếp tục cho đến khi không có đỉnh nào được cập nhật nữa (điều này được kiểm tra bởi biến updated)
    for i in range(l-1):
        if not updated:
            break
        updated = False
        for u in range(l):
            for v in adj[u]:
                if dist[u] + spectralVector[v] > dist[v]:
                    dist[v] = dist[u] + spectralVector[v]
                    parent[v] = u
                    updated = True
                    
    u = l-1
    path = [u]
    while 0 != u:
        u = parent[u]
        path.insert(0, u)

    peptide = ''.join([_amino_acid_by_mass_[path[i+1]-path[i]] for i in range(len(path)-1)])
    return peptide

if __name__ == "__main__":
    spectralVector = _input()

    peptide = findPeptide(spectralVector, _amino_acid_by_mass_)
    # print(peptide)
    f = open('output.txt', 'w')
    f.write(peptide)
    f.close()