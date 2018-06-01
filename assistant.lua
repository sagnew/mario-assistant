function read_file(file)
    local input = io.open(file, 'r')

    if input ~= nil then
        io.input(input)
        local content = io.read()
        io.close(input)

        return content
    end

    return nil
end

prev_address = ''
prev_value = ''

while true do
    address = read_file('address.txt')
    value = read_file('value.txt')

    if address ~= nil and value ~= nil then
        hex_address = tonumber(address, 16)
        hex_value = tonumber(value, 16)

        if hex_value ~= nil and hex_address ~= nil then
            emu.message(address .. ': ' .. value)
            memory.writebyte(hex_address, hex_value)
            os.remove('address.txt')
            os.remove('value.txt')
        end
    end

    if address ~= nil and value ~= nil then
        prev_address = address
        prev_value = value
    end
    emu.frameadvance()
end
