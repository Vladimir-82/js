def cyclic_shift(numbers: list[int], step: int) -> None:
    if step > 0:
        numbers[:] = numbers[-step:] + numbers[:-step]
    else:
        numbers[:] = numbers[abs(step):] + numbers[:abs(step)]