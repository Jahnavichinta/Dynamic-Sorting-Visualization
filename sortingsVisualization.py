import tkinter as tk
import time

r = tk.Tk()
r.title("Dynamic Sorting")
r.geometry("1000x600")
r.configure(bg="sky blue")

l = tk.Frame(r, bg="sky blue", pady=2, width=150, height=600, relief="ridge")
l.grid(row=0, column=0)

root = tk.Frame(r, bg="sky blue", pady=2, width=700, height=600, relief="ridge")
root.grid(row=0, column=1)

ri = tk.Frame(r, bg="sky blue", pady=2, width=150, height=600, relief="ridge")
ri.grid(row=0, column=2)

num_frame = tk.Frame(root, bg="sky blue", pady=2, width=150, height=600, relief="ridge")
num_frame.grid(row=0, column=0)

ip_label = tk.Label(num_frame, font="Arial 20 bold", text="Enter number of elements (<=20)  ", bg="sky blue")
ip_label.grid(row=0, column=0)

ip_entry = tk.Entry(num_frame, width=5, font="Arial 15 bold", relief="ridge")
ip_entry.grid(row=0, column=1)

input_label = tk.Label(root, font="Arial 20 bold", text="Enter numbers separated by spaces", bg="sky blue")
input_label.grid(row=1, column=0)

entry = tk.Entry(root, width=50, font="Arial 15 bold", relief="ridge")
entry.grid(row=2, column=0)

s = tk.Frame(root, bg="sky blue", pady=2, width=700, height=40, relief="flat")
s.grid(row=3, column=0)

reason_label = tk.Label(root, text="", font="Arial 15 bold", fg="black", relief="ridge", width=50)
reason_label.grid(row=4, column=0)

visualization = tk.Canvas(root, width=700, height=400, bg='white', relief="ridge")
visualization.grid(row=5, column=0)

def validate_input(entry_text):
    try:
        nums = list(map(int, entry_text.split()))
        num_elements = int(ip_entry.get())
        if num_elements > 20:
            reason_label.config(text="Number of elements should be less than 20")
            return None
        if len(nums) != num_elements:
            reason_label.config(text=f"Please enter {num_elements} elements")
            return None
        return nums

    except ValueError:
        reason_label.config(text="Invalid input. Please enter numbers separated by spaces.")
        return None


# Bubble sort
def sleep(ms):
    root.update()
    time.sleep(ms / 1000)

def animate_swap(nums, idx1, idx2, bar_width, gap, bar_height):
    num1, num2 = nums[idx1], nums[idx2]
    x1 = 10 + (bar_width + gap) * idx1
    x2 = 10 + (bar_width + gap) * idx2
    y = 400

    frames = 10
    dx1 = (x2 - x1) / frames
    dx2 = (x1 - x2) / frames

    for _ in range(frames):
        visualization.delete("swap_animation")
        visualization.create_rectangle(x1, y, x1 + bar_width, y - num2 * bar_height, fill='orange',
                                       tags="swap_animation")
        visualization.create_rectangle(x2, y, x2 + bar_width, y - num1 * bar_height, fill='orange',
                                       tags="swap_animation")
        x1 += dx1
        x2 += dx2
        sleep(50)
        root.update()

    visualization.delete("all")
    x = 10
    for idx, num in enumerate(nums):
        if idx >= len(nums):
            visualization.create_rectangle(x, 400, x + bar_width, 400 - num * bar_height, fill='blue')
        else:
            visualization.create_rectangle(x, 400, x + bar_width, 400 - num * bar_height, fill='cadet blue')
        x += bar_width + gap
    sleep(50)

def Bubble_array():
    global paused, sorting_in_progress
    sorting_in_progress = True
    Bubble_button.config(state=tk.DISABLED)
    Merge_button.config(state=tk.DISABLED)
    Quick_button.config(state=tk.DISABLED)
    Insertion_button.config(state=tk.DISABLED)
    Selection_button.config(state=tk.DISABLED)
    paused = False
    e = entry.get()
    nums = validate_input(e)
    if not nums:
        Bubble_button.config(state=tk.NORMAL)
        Merge_button.config(state=tk.NORMAL)
        Quick_button.config(state=tk.NORMAL)
        Insertion_button.config(state=tk.NORMAL)
        Selection_button.config(state=tk.NORMAL)

    n = len(nums)
    max_num = max(nums)
    bar_width = min(20, (700 // (n + 1)))
    gap = 5
    bar_height = 390 // (max_num + 2)
    count = 0
    reason_label.config(text="Lets perform Bubble sort")
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            while paused:
                root.update()
                time.sleep(0.1)
            visualization.delete("all")
            x = 10
            for idx, num in enumerate(nums):
                bar_actual_height = abs(num) * bar_height
                if idx == j or idx == j + 1:
                    visualization.create_rectangle(x, 400, x + bar_width, 400 - bar_actual_height,
                                                   fill='orange')  # Different color for compared elements
                elif idx >= n - i:
                    visualization.create_rectangle(x, 400, x + bar_width, 400 - bar_actual_height,
                                                   fill='blue')  # Different color for fixed elements
                else:
                    visualization.create_rectangle(x, 400, x + bar_width, 400 - bar_actual_height, fill='cadet blue')
                visualization.create_text(x + bar_width // 2, 400 - bar_actual_height - 10, text=str(num),
                                          font="Arial 12 bold")
                x += bar_width + gap
            sleep(5000)

            if nums[j] > nums[j + 1]:
                reason_label.config(text=f"{nums[j]} > {nums[j + 1]} swapping {nums[j]} and {nums[j + 1]}")
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
                animate_swap(nums, j, j + 1, bar_width, gap, bar_height)
                # reason_label.config(text=f"{nums[j]} > {nums[j+1]} swapping {nums[j]} and {nums[j+1]}")
            else:
                reason_label.config(text=f"{nums[j]} <= {nums[j + 1]} No swapping is needed")
                # animate_swap(nums, j, j + 1, bar_width, gap, bar_height)
                sleep(5000)
        sleep(200)
        count += 1
        if not swapped:
            reason_label.config(text="Array is sorted!")
            visualization.delete("all")
            x = 10
            for idx, num in enumerate(nums):
                bar_actual_height = abs(num) * bar_height
                visualization.create_rectangle(x, 400, x + bar_width, 400 - bar_actual_height, fill='blue')
                visualization.create_text(x + bar_width // 2, 400 - bar_actual_height - 10, text=str(num),
                                          font="Arial 12 bold")
                x += bar_width + gap
            sleep(5000)
            break
        else:
            reason_label.config(text=f"{count} Iteration is completed.Continuing sorting...")
    sorting_in_progress = False
    Bubble_button.config(state=tk.NORMAL)
    Merge_button.config(state=tk.NORMAL)
    Quick_button.config(state=tk.NORMAL)
    Insertion_button.config(state=tk.NORMAL)
    Selection_button.config(state=tk.NORMAL)

# Bubble sort end

#Merge sort start

def draw_bars(nums, color_array):
    visualization.delete("all")
    x = 10
    bar_width = min(20, (700 // (len(nums) + 1)))
    gap = 5
    bar_height = 390 // (max(nums) + 2)
    for i, num in enumerate(nums):
        color = color_array[i]
        visualization.create_rectangle(x, 400, x + bar_width, 400 - num * bar_height, fill=color)
        visualization.create_text(x + bar_width // 2, 400 - num * bar_height - 10, text=str(num), font="Arial 12 bold")
        x += bar_width + gap
    sleep(1000)



def get_color_array(length, left, mid, right, base_colors):
    colorarr = base_colors.copy()
    for i in range(left, mid + 1):
        colorarr[i] = "yellow"
    for i in range(mid + 1, right + 1):
        colorarr[i] = "pink"
    return colorarr

def merge(data, left, mid, right, color_array):
    left_part = data[left:mid + 1]
    right_part = data[mid + 1:right + 1]
    leftIdx = rightIdx = 0
    for dataIdx in range(left, right + 1):
        if leftIdx < len(left_part) and rightIdx < len(right_part):
            color_array[leftIdx + left] = "orange"  # Color left element for comparison
            color_array[rightIdx + mid + 1] = "orange"  # Color right element for comparison
            if left_part[leftIdx] <= right_part[rightIdx]:
                data[dataIdx] = left_part[leftIdx]
                leftIdx += 1
                color_array[leftIdx + left] = "white"  # Reset color after comparison
            else:
                data[dataIdx] = right_part[rightIdx]
                rightIdx += 1
                color_array[rightIdx + mid + 1] = "white"  # Reset color after comparison
        elif leftIdx < len(left_part):
            data[dataIdx] = left_part[leftIdx]
            leftIdx += 1
            color_array[leftIdx + left] = "white"  # No comparison needed, reset color
        else:
            data[dataIdx] = right_part[rightIdx]
            rightIdx += 1
            color_array[rightIdx + mid + 1] = "white"  # No comparison needed, reset color
        draw_bars(data, color_array)  # Update visualization after each element swap


def merge_sort(data, left, right, color_array):
    if left < right:
        mid = (left + right) // 2
        color_array = get_color_array(len(data), left, mid, right, color_array)
        draw_bars(data, color_array)
        sleep(1000)
        merge_sort(data, left, mid, color_array)
        merge_sort(data, mid + 1, right, color_array)
        merge(data, left, mid, right, color_array)
def Merge_array():
    global paused, sorting_in_progress
    sorting_in_progress = True
    Bubble_button.config(state=tk.DISABLED)
    Merge_button.config(state=tk.DISABLED)
    Quick_button.config(state=tk.DISABLED)
    Insertion_button.config(state=tk.DISABLED)
    Selection_button.config(state=tk.DISABLED)
    paused = False
    e = entry.get()
    nums = validate_input(e)
    if not nums:
        Bubble_button.config(state=tk.NORMAL)
        Merge_button.config(state=tk.NORMAL)
        Quick_button.config(state=tk.NORMAL)
        Insertion_button.config(state=tk.NORMAL)
        Selection_button.config(state=tk.NORMAL)
        return

    reason_label.config(text="Let's perform Merge Sort")
    draw_bars(nums, ["pink"] * len(nums))
    sleep(1000)
    color_array = ["white"] * len(nums)
    merge_sort(nums, 0, len(nums) - 1, color_array)
    reason_label.config(text="Array is sorted!")
    draw_bars(nums, ["blue"] * len(nums))

    sorting_in_progress = False
    Bubble_button.config(state=tk.NORMAL)
    Merge_button.config(state=tk.NORMAL)
    Quick_button.config(state=tk.NORMAL)
    Insertion_button.config(state=tk.NORMAL)
    Selection_button.config(state=tk.NORMAL)

# Merge sort end

# Quick sort start

def animate_quick_sort(nums, pivot_idx, left, right, bar_width, gap, bar_height, fixed):
    visualization.delete("all")
    x = 10
    for idx, num in enumerate(nums):
        bar_actual_height = abs(num) * bar_height
        if idx == pivot_idx:
            fill_color = 'green'
        elif idx == left or idx == right:
            fill_color = 'orange'
        elif idx in fixed:
            fill_color = 'blue'
        else:
            fill_color = 'cadet blue'
        visualization.create_rectangle(x, 400, x + bar_width, 400 - bar_actual_height, fill=fill_color)
        visualization.create_text(x + bar_width // 2, 400 - bar_actual_height - 10, text=str(num),
                                  font="Arial 12 bold")
        x += bar_width + gap
    sleep(1000)


def partition(array, low, high, bar_width, gap, bar_height, fixed):
    pivot = array[low]
    start = low + 1
    end = high

    while True:
        while start <= end and array[end] >= pivot:
            end -= 1
            reason_label.config(text=f'Here {array[end + 1]} >= pivot. So decrement right')
            animate_quick_sort(array, low, start, end, bar_width, gap, bar_height, fixed)
            sleep(5000)

        while start <= end and array[start] <= pivot:
            start += 1
            reason_label.config(text=f'Here {array[start - 1]} <= pivot. So increment left')
            animate_quick_sort(array, low, start, end, bar_width, gap, bar_height, fixed)
            sleep(5000)

        if start <= end:
            array[start], array[end] = array[end], array[start]
            reason_label.config(text=f'Swapping elements at positions {start} and {end}')
            animate_quick_sort(array, low, start, end, bar_width, gap, bar_height, fixed)
            sleep(5000)
        else:
            break

    array[low], array[end] = array[end], array[low]
    fixed.append(end)
    animate_quick_sort(array, low, start, end, bar_width, gap, bar_height, fixed)
    reason_label.config(text=f'Placing pivot at end position')
    sleep(5000)
    return end


def quick_sort_visual(nums, low, high, bar_width, gap, bar_height, fixed):
    if low < high:
        pivot_idx = partition(nums, low, high, bar_width, gap, bar_height, fixed)
        quick_sort_visual(nums, low, pivot_idx - 1, bar_width, gap, bar_height, fixed)
        quick_sort_visual(nums, pivot_idx + 1, high, bar_width, gap, bar_height, fixed)


def Quick_array():
    global paused, sorting_in_progress
    sorting_in_progress = True
    Bubble_button.config(state=tk.DISABLED)
    Merge_button.config(state=tk.DISABLED)
    Quick_button.config(state=tk.DISABLED)
    Insertion_button.config(state=tk.DISABLED)
    Selection_button.config(state=tk.DISABLED)
    paused = False
    e = entry.get()
    nums = validate_input(e)
    if not nums:
        Bubble_button.config(state=tk.NORMAL)
        Merge_button.config(state=tk.NORMAL)
        Quick_button.config(state=tk.NORMAL)
        Insertion_button.config(state=tk.NORMAL)
        Selection_button.config(state=tk.NORMAL)
        return
    visualization.delete("all")
    n = len(nums)
    max_num = max(nums)
    bar_width = min(20, (700 // (n + 1)))
    gap = 5
    bar_height = 390 // (max_num + 2)

    reason_label.config(text="Let's perform Quick sort")
    x = 10
    for idx, num in enumerate(nums):
        bar_actual_height = abs(num) * bar_height
        visualization.create_rectangle(x, 400, x + bar_width, 400 - bar_actual_height, fill='cadet blue')
        visualization.create_text(x + bar_width // 2, 400 - bar_actual_height - 10, text=str(num),
                                  font="Arial 12 bold")
        x += bar_width + gap
    sleep(5000)
    reason_label.config(text=f'Here Green -> pivot element \n orange -> left and right pointers \n Blue -> Partition element')
    sleep(2000)
    quick_sort_visual(nums, 0, n - 1, bar_width, gap, bar_height, [])

    reason_label.config(text=f"Array is sorted!")
    visualization.delete("all")
    x = 10
    for idx, num in enumerate(nums):
        bar_actual_height = abs(num) * bar_height
        visualization.create_rectangle(x, 400, x + bar_width, 400 - bar_actual_height, fill='blue')
        visualization.create_text(x + bar_width // 2, 400 - bar_actual_height - 10, text=str(num),
                                  font="Arial 12 bold")
        x += bar_width + gap
    sleep(5000)

    sorting_in_progress = False
    Bubble_button.config(state=tk.NORMAL)
    Merge_button.config(state=tk.NORMAL)
    Quick_button.config(state=tk.NORMAL)
    Insertion_button.config(state=tk.NORMAL)
    Selection_button.config(state=tk.NORMAL)


# Quick sort end

#Selection sort start

def animate_selection_sort(nums, min_idx, current_idx, bar_width, gap, bar_height, sort_idx):
    visualization.delete("all")
    x = 10
    for idx, num in enumerate(nums):
        bar_actual_height = abs(num) * bar_height
        # for i in range(0, idx):
        # fill_color = 'blue'
        if idx == min_idx and idx != sort_idx:
            fill_color = 'red'
        elif idx == current_idx:
            fill_color = 'orange'
        elif idx == sort_idx:
            fill_color = 'green'
        else:
            fill_color = 'cadet blue'
        visualization.create_rectangle(x, 400, x + bar_width, 400 - bar_actual_height, fill=fill_color, tags='swap_animation')
        visualization.create_text(x + bar_width // 2, 400 - bar_actual_height - 10, text=str(num),
                                  font="Arial 12 bold", tags='swap_animation')
        x += bar_width + gap
    sleep(3000)

def Selection_array():
    global paused, sorting_in_progress
    sorting_in_progress = True
    Bubble_button.config(state=tk.DISABLED)
    Merge_button.config(state=tk.DISABLED)
    Quick_button.config(state=tk.DISABLED)
    Insertion_button.config(state=tk.DISABLED)
    Selection_button.config(state=tk.DISABLED)
    paused = False
    e = entry.get()
    nums = validate_input(e)
    if not nums:
        Bubble_button.config(state=tk.NORMAL)
        Merge_button.config(state=tk.NORMAL)
        Quick_button.config(state=tk.NORMAL)
        Insertion_button.config(state=tk.NORMAL)
        Selection_button.config(state=tk.NORMAL)
        return

    n = len(nums)
    max_num = max(nums)
    bar_width = min(20, (700 // (n + 1)))
    gap = 5
    bar_height = 390 // (max_num + 2)

    reason_label.config(text="Let's perform Selection sort,\n Here Green colur -> the element to be swapped \n with corresponding minimum element \n Red -> the minimum value in each iteration(Global minimum) \n Orange -> the current value")
    sleep(2500)
    for i in range(n):
        sort_idx = i
        min_idx = i
        for j in range(i+1, n):
            while paused:
                root.update()
                time.sleep(0.1)
            animate_selection_sort(nums, min_idx, j, bar_width, gap, bar_height, sort_idx)
            if nums[j] < nums[min_idx]:
                reason_label.config(text=f"The element at {j} is less than the element at {min_idx} \n So update global minimum")
                sleep(5000)
                min_idx = j
            else:
                reason_label.config(text=f'Here the current element is not less than global minimum.\n So there is no change in global minimum')
                sleep(5000)

        nums[i], nums[min_idx] = nums[min_idx], nums[i]
        reason_label.config(text=f"Swapping element at index {i} with element at index {min_idx}")
        animate_selection_sort(nums, min_idx, i, bar_width, gap, bar_height, sort_idx)
        sleep(5000)

    reason_label.config(text="Array is sorted!")
    visualization.delete("all")
    x = 10
    for idx, num in enumerate(nums):
        bar_actual_height = abs(num) * bar_height
        visualization.create_rectangle(x, 400, x + bar_width, 400 - bar_actual_height, fill='blue')
        visualization.create_text(x + bar_width // 2, 400 - bar_actual_height - 10, text=str(num),
                                  font="Arial 12 bold")
        x += bar_width + gap
    sleep(5000)

    sorting_in_progress = False
    Bubble_button.config(state=tk.NORMAL)
    Merge_button.config(state=tk.NORMAL)
    Quick_button.config(state=tk.NORMAL)
    Insertion_button.config(state=tk.NORMAL)
    Selection_button.config(state=tk.NORMAL)

# Selection sort end

#Insertion sort start

def animate_insertion_sort(nums, current_idx, bar_width, gap, bar_height, sorted_idx):
    visualization.delete("all")
    x = 10
    for idx, num in enumerate(nums):
        bar_actual_height = abs(num) * bar_height
        if idx == current_idx:
            fill_color = 'orange'
        elif idx <= sorted_idx:
            fill_color = 'blue'
        else:
            fill_color = 'cadet blue'
        visualization.create_rectangle(x, 400, x + bar_width, 400 - bar_actual_height, fill=fill_color, tags='swap_animation')
        visualization.create_text(x + bar_width // 2, 400 - bar_actual_height - 10, text=str(num), font="Arial 12 bold", tags='swap_animation')
        x += bar_width + gap
    root.update()
    sleep(3000)

def Insertion_array():
    global paused, sorting_in_progress
    sorting_in_progress = True
    Bubble_button.config(state=tk.DISABLED)
    Merge_button.config(state=tk.DISABLED)
    Quick_button.config(state=tk.DISABLED)
    Insertion_button.config(state=tk.DISABLED)
    Selection_button.config(state=tk.DISABLED)
    paused = False
    e = entry.get()
    nums = validate_input(e)
    if not nums:
        Bubble_button.config(state=tk.NORMAL)
        Merge_button.config(state=tk.NORMAL)
        Quick_button.config(state=tk.NORMAL)
        Insertion_button.config(state=tk.NORMAL)
        Selection_button.config(state=tk.NORMAL)
        return
    n = len(nums)
    max_num = max(nums)
    bar_width = min(20, (700 // (n + 1)))
    gap = 5
    bar_height = 390 // (max_num + 2)

    reason_label.config(text="Let's perform Insertion sort,\n Here Blue color -> the sorted part of the array \n Orange -> the current value being compared and inserted")
    sleep(2500)

    for i in range(1, n):
        key = nums[i]
        j = i - 1
        sorted_idx = i - 1

        animate_insertion_sort(nums, i, bar_width, gap, bar_height, sorted_idx)

        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key
        reason_label.config(text=f"Inserting the key at its correct position {j + 1}")
        animate_insertion_sort(nums, j + 1, bar_width, gap, bar_height, sorted_idx+1)
        sleep(3000)

    reason_label.config(text="Array is sorted!")
    visualization.delete("all")
    x = 10
    for idx, num in enumerate(nums):
        bar_actual_height = abs(num) * bar_height
        visualization.create_rectangle(x, 400, x + bar_width, 400 - bar_actual_height, fill='blue')
        visualization.create_text(x + bar_width // 2, 400 - bar_actual_height - 10, text=str(num), font="Arial 12 bold")
        x += bar_width + gap
    sleep(5000)
    sorting_in_progress = False
    Bubble_button.config(state=tk.NORMAL)
    Merge_button.config(state=tk.NORMAL)
    Quick_button.config(state=tk.NORMAL)
    Insertion_button.config(state=tk.NORMAL)
    Selection_button.config(state=tk.NORMAL)

# Insertion sort end

Bubble_button = tk.Button(s, text="Bubble Sort", font="Arial 15 bold ", command=Bubble_array)
Bubble_button.grid(row=0, column=0)

Merge_button = tk.Button(s, text="Merge Sort", font="Arial 15 bold ", command=Merge_array)
Merge_button.grid(row=0, column=1)

Quick_button = tk.Button(s, text="Quick Sort", font="Arial 15 bold ")  # , command=Quick_array)
Quick_button.grid(row=0, column=2)

Insertion_button = tk.Button(s, text="Insertion Sort", font="Arial 15 bold ", command=Insertion_array)
Insertion_button.grid(row=0, column=3)

Selection_button = tk.Button(s, text="Selection Sort", font="Arial 15 bold " , command=Selection_array)
Selection_button.grid(row=0, column=4)

root.mainloop()