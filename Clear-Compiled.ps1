#! powershell
# clear C builds for debugging purposes
$compiled_list = '.\\functions\\import_grid',
'.\\functions\\import_stl',
'.\\functions\\line_generator',
'.\\functions\\m_config',
'.\\functions\\m_parser',
'.\\functions\\m_queue',
'.\\functions\\m_object',
'.\\functions\\m_line',
'.\\functions\\m_stack',
'.\\functions\\obj_merger',
'.\\functions\\writer'

foreach ($file in $compiled_list) {
    try {
        Remove-Item $file".cp311-win_amd64.pyd"
        Remove-Item $file".c"
    }
    catch [System.IO.FileNotFoundException] { 
        pass 
    }
}
