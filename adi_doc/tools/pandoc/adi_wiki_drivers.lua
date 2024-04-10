-- Pandoc filter to handle ADI mediawiki syntax for driver pages
local logging = require 'logging'


-- #############################################################################
-- Change Headings levels to make sure there is 1 level 1 heading and all other
-- headings are shifted up by 1
function Pandoc(el)
    logging.info('Updating header')
    -- Count number of header levels at each level
    local header_levels = {0, 0, 0, 0, 0, 0}
    local header_levels_new = {0, 0, 0, 0, 0, 0}
    local header_levels_max = 6
    local header_levels_min = 1
    for i = 1, #el.blocks do
        if el.blocks[i].t == 'Header' then
            local level = el.blocks[i].level
            header_text = pandoc.utils.stringify(el.blocks[i].content)
            logging.info('Header: ' .. header_text .. ' | Level: ' .. level)
            header_levels[level] = header_levels[level] + 1
        end
    end

    if header_levels[1] > 1 then
        logging.info('More than one level 1 header')
        -- Move all headers down one level
        for i = 1, #el.blocks do
            if el.blocks[i].t == 'Header' then
                el.blocks[i].level = el.blocks[i].level + 1
            end
        end
        -- Move first header to level 1
        for i = 1, #el.blocks do
            if el.blocks[i].t == 'Header' then
                el.blocks[i].level = 1
                break
            end
        end
    elseif header_levels[1] == 0 then
        logging.info('No level 1 header')
        shift_up_needed = 0
        for i = 2, #header_levels do
            if header_levels[i] > 0 then
                logging.info('Found header at level ' .. i)
                shift_up_needed = i - 2
                break
            end
        end
        -- Move all headers up by shift_up_needed
        for i = 1, #el.blocks do
            if el.blocks[i].t == 'Header' then
                header = pandoc.utils.stringify(el.blocks[i].content)
                level = el.blocks[i].level
                logging.info('Header: ' .. header)
                logging.info('Moving header from level ' .. level .. ' to ' .. level - shift_up_needed)
                el.blocks[i].level = el.blocks[i].level - shift_up_needed
            end
        end
        -- Move first header to level 1
        for i = 1, #el.blocks do
            if el.blocks[i].t == 'Header' then
                el.blocks[i].level = 1
                break
            end
        end
        
    end


  
    return el
end
