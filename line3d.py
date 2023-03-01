import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from skspatial.objects import Line, Vector, Point

def main():
    x = input("Enter equation of x: ").lower().strip()
    y = input("Enter equation of y: ").lower().strip()
    z = input("Enter equation of z: ").lower().strip()
    dv = get_direction(t_coefs(x), t_coefs(y), t_coefs(z))
    print(f"Direction vector of a line: <{dv}>")
    p_on_line = get_point(point(x), point(y), point(z))
    print(f"Point on the line: ({p_on_line})")
    visualize(p_on_line,dv)


def t_coefs(d):
    index_t = d.find("t")
    index_add = d.find("+")
    index_sub = d.find("-")
    if "+" in d:
        comp = d[index_add+1:index_t]
        return comp
    elif d[0] == "-" or "-" in d and d[index_sub+1] == "t":
        comp = "-1"
        return comp
    elif "-" in d:
        comp = d[index_sub:index_t]
        return comp
    elif d[index_t-1] == "":
        comp = "1"
        return comp

def point(p):
    index_add = p.rfind("+")
    index_sub = p.rfind("-")
    if "+" in p:
        pcomp = p[:index_add]
        return pcomp
    elif "-" in p:
        pcomp = p[:index_sub]
        return pcomp
    elif "+" and "-" not in p:
        pcomp = "0"

def get_point(p1, p2, p3):
    lst_p = list()
    lst_p.append(p1)
    lst_p.append(p2)
    lst_p.append(p3)
    p_line = ",".join(lst_p)
    return p_line


def get_direction(d1, d2, d3):
    lst_dir = list()
    lst_dir.append(d1)
    lst_dir.append(d2)
    lst_dir.append(d3)
    dir_vec = ",".join(lst_dir)
    return dir_vec

def visualize(p,d):
    lst_pl = list()
    lst_dl = list()
    pl = p.split(",")
    dl = d.split(",")
    for i in pl:
        lst_pl.append(float(i))
    for j in dl:
        lst_dl.append(float(j))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection = "3d")
    ax.set_xlabel("x-axis")
    ax.set_ylabel("y-axis")
    ax.set_zlabel("z-axis")

    line = Line(lst_pl, lst_dl)
    line.plot_3d(ax, c="k")
    line.point.plot_3d(ax, s=100)
    Vector(lst_dl).plot_3d(ax, point=(0,0,0), c="r")
    origin = Point([0,0,0])
    origin.plot_3d(ax, s=100)

    plt.show()


if __name__ == "__main__":
    main()