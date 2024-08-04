#copy file and write it into it again
# change size
def write_into(root_path, champion, skin_number, scale): #TODO
    lines = []
    with open(r"D:\Riot Games\League of Legends\Game\DATA\FINAL\Champions\data\characters\akali\skins\skin0.py", "r") as file:
        for line in file:
            lines.append(line)
            if line.strip() == "skinMeshProperties: embed = SkinMeshDataProperties {":
                break
        for _ in range(3):
            line = file.readline()
            lines.append(line)
        lines.append("\t \t \tskinScale: f32 = " + str(scale)+ "\n")
        for line in file:
            if line.__contains__("skinScale"):
                continue
            lines.append(line)

    output = "".join(lines)
    print(output)
    with open(r"D:\Riot Games\League of Legends\Game\DATA\FINAL\Champions\data\characters\akali\skins\skin0.py", "w") as file:
        file.write(output)