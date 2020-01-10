import folium
m = folium.Map(location=[-38, 145])
m.save('index.html')

folium.Marker([-38, 145], popup='<b>Home</b>', tooltip='Home').add_to(m)
