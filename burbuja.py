import flet as ft
import random as rm
import time

def main(page: ft.Page):
    def create_containers(number):
        container_list = []
        for _ in range(number):
             container_list.append(
              ft.Container(
              content=ft.Text(value=rm.randint(1,100), color=ft.colors.BLACK, size=25),
              alignment=ft.alignment.center,
              width=50,
              height=50,
              bgcolor=ft.colors.ORANGE,
              border_radius=25,
                )
              )
        return container_list
    
    
    row = ft.Row(controls=create_containers(10))
    
    page.add(row)

    time.sleep(5)
    
    arr = row.controls
    
    nv = len(arr)
    for i in range(nv):
        for j in range(0, nv-i-1):
            arr[j].bgcolor = ft.colors.WHITE
            arr[j+1].bgcolor = ft.colors.WHITE
            time.sleep(0.5)
            page.update()
            if int(arr[j].content.value) > int(arr[j + 1].content.value):
                arr[j], arr[j + 1] = arr[j+1], arr[j]
            arr[j].bgcolor = ft.colors.ORANGE
            arr[j+1].bgcolor = ft.colors.ORANGE
        arr[nv-i-1].bgcolor = ft.colors.GREEN
    page.update()

ft.app(target=main)
