struct Image {
    1: binary data,
    2: i32 width,
    3: i32 height,
    4: i32 channel
}

service PicSim {
    list<Image> get_sim_pics(1: Image img)
}
