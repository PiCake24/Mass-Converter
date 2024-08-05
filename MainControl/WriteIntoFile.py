
def write_into(root_path, champion, skin_number, scale):
    lines = []
    path = root_path + "0WADS\\data\\characters\\" + champion + "\\skins\\skin" + skin_number + ".bin"
    with open(path, "r") as file:
        for line in file:
            lines.append(line)
            if line.strip() == "skinMeshProperties: embed = SkinMeshDataProperties {":
                break
        for _ in range(3):
            line = file.readline()
            lines.append(line)
        lines.append("\t \t \tskinScale: f32 = " + str(scale) + "\n")
        for line in file:
            if line.__contains__("skinScale"):
                continue
            lines.append(line)

    output = "".join(lines)
    print(output)
    with open(path, "w") as file:
        file.write(output)
