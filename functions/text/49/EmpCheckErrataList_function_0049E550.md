# EmpCheckErrataList

- RVA: `0x0049E550`–`0x0049E554` (길이 `4` bytes)
- VA: `0x000000014049E550`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `2`개 명령, `4/4` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **89**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [SymCryptInjectError](../4A/SymCryptInjectError_function_004A4FCC.md) at `0x004A4FD0`
- [strupr](../4F/strupr_function_004FEEE0.md) at `0x004FEEF7`
- [vsnwprintf_l](../4F/vsnwprintf_l_function_004FEF50.md) at `0x004FF026`
- [vsnprintf_l](../4F/vsnprintf_l_function_004FF070.md) at `0x004FF111`
- [strtoxlX](../4F/strtoxlX_function_004FF130.md) at `0x004FF32B`
- [strtoxq](../4F/strtoxq_function_004FF3F8.md) at `0x004FF5F2`
- [snprintf](../4F/snprintf_function_004FFB80.md) at `0x004FFC1E`
- [snwprintf](../4F/snwprintf_function_004FFC40.md) at `0x004FFD15`
- [swprintf](../4F/swprintf_function_004FFED0.md) at `0x004FFF7D`
- [vswprintf_l](../4F/vswprintf_l_function_004FFFBC.md) at `0x00500057`
- [wcslwr](../50/wcslwr_function_005000E0.md) at `0x005000F7`
- [wcslwr_s](../50/wcslwr_s_function_00500140.md) at `0x0050016B`
- [wcsnset_s](../50/wcsnset_s_function_00500260.md) at `0x00500285`
- [wcsset_s](../50/wcsset_s_function_00500340.md) at `0x00500383`
- [bsearch](../50/bsearch_function_00500430.md) at `0x00500512`
- [bsearch_s](../50/bsearch_s_function_00500540.md) at `0x00500630`
- [sub_00500D66](../50/Unknown_function_00500D66.md) at `0x00500D77`
- [sub_0050118E](../50/Unknown_function_0050118E.md) at `0x0050119F`
- [sprintf](../50/sprintf_function_00501230.md) at `0x005012B8`
- [vsprintf_l](../50/vsprintf_l_function_00501928.md) at `0x0050199E`
- [wcstoxlX](../50/wcstoxlX_function_00502214.md) at `0x00502408`
- [wctomb_s_l](../50/wctomb_s_l_function_005024D4.md) at `0x0050251B`
- [wcstoxq](../50/wcstoxq_function_00502674.md) at `0x005028AB`
- [woutput_l](../50/woutput_l_function_0050293C.md) at `0x0050320F`
- [output_l](../50/output_l_function_00503368.md) at `0x00503BA4`
- [_call_matherr](../50/_call_matherr_function_00503E90.md) at `0x00503EED`
- [handle_error](../50/handle_error_function_00503FE0.md) at `0x00504119`
- [handle_errorf](../50/handle_errorf_function_00504160.md) at `0x005042A5`
- [fputwc_nolock](../50/fputwc_nolock_function_005044B4.md) at `0x005044CA`
- [vswprintf_s](../50/vswprintf_s_function_00504B50.md) at `0x00504B8E`
- [x64toa_s](../50/x64toa_s_function_00504C4C.md) at `0x00504CA6`
- [x64toa_s](../50/x64toa_s_function_00504C4C.md) at `0x00504D53`
- [xtoa_s](../50/xtoa_s_function_00504D80.md) at `0x00504DDF`
- [xtoa_s](../50/xtoa_s_function_00504D80.md) at `0x00504E81`
- [x64tow_s](../50/x64tow_s_function_00504F4C.md) at `0x00504FAA`
- [x64tow_s](../50/x64tow_s_function_00504F4C.md) at `0x00505064`
- [xtow_s](../50/xtow_s_function_00505090.md) at `0x005050F1`
- [xtow_s](../50/xtow_s_function_00505090.md) at `0x005051A2`
- [makepath_s](../50/makepath_s_function_005051D0.md) at `0x005052E9`
- [makepath_s](../50/makepath_s_function_005051D0.md) at `0x0050530D`
- [vsnprintf_s](../50/vsnprintf_s_function_00505360.md) at `0x005053CC`
- [snscanf_s](../50/snscanf_s_function_00505400.md) at `0x0050541F`
- [vsnwprintf_s](../50/vsnwprintf_s_function_00505470.md) at `0x005054E2`
- [snwscanf_s](../50/snwscanf_s_function_00505520.md) at `0x0050553F`
- [splitpath_s](../50/splitpath_s_function_00505560.md) at `0x005057CE`
- [strnset_s](../50/strnset_s_function_00505800.md) at `0x00505825`
- [strset_s](../50/strset_s_function_00505890.md) at `0x005058CE`
- [wmakepath_s](../50/wmakepath_s_function_005058F0.md) at `0x00505A34`
- [wmakepath_s](../50/wmakepath_s_function_005058F0.md) at `0x00505A57`
- [wsplitpath_s](../50/wsplitpath_s_function_00505A80.md) at `0x00505D0F`
- [memcpy_s](../50/memcpy_s_function_00505D40.md) at `0x00505DB4`
- [memmove_s](../50/memmove_s_function_00505DE0.md) at `0x00505E2A`
- [vsprintf_s](../50/vsprintf_s_function_00505E70.md) at `0x00505EA9`
- [sscanf_s](../50/sscanf_s_function_00505EC0.md) at `0x00505EE6`
- [strcat_s](../50/strcat_s_function_00505F20.md) at `0x00505F60`
- [strcat_s](../50/strcat_s_function_00505F20.md) at `0x00505F98`
- [strcpy_s](../50/strcpy_s_function_00505FB0.md) at `0x00506002`
- [strcpy_s](../50/strcpy_s_function_00505FB0.md) at `0x0050601E`
- [strncat_s](../50/strncat_s_function_00506040.md) at `0x0050606F`
- [strncat_s](../50/strncat_s_function_00506040.md) at `0x00506122`
- [strncpy_s](../50/strncpy_s_function_00506140.md) at `0x00506168`
- [strncpy_s](../50/strncpy_s_function_00506140.md) at `0x0050621F`
- [strtok_s](../50/strtok_s_function_00506240.md) at `0x00506373`
- [swscanf_s](../50/swscanf_s_function_005063B0.md) at `0x005063D6`
- [wcscat_s](../50/wcscat_s_function_00506410.md) at `0x00506453`
- [wcscat_s](../50/wcscat_s_function_00506410.md) at `0x0050648F`
- [wcscpy_s](../50/wcscpy_s_function_005064B0.md) at `0x00506507`
- [wcscpy_s](../50/wcscpy_s_function_005064B0.md) at `0x00506523`
- [wcsncat_s](../50/wcsncat_s_function_00506540.md) at `0x00506574`
- [wcsncat_s](../50/wcsncat_s_function_00506540.md) at `0x00506635`
- [wcsncpy_s](../50/wcsncpy_s_function_00506650.md) at `0x0050667A`
- [wcsncpy_s](../50/wcsncpy_s_function_00506650.md) at `0x00506742`
- [wcstok_s](../50/wcstok_s_function_00506754.md) at `0x00506835`
- [output_s](../50/output_s_function_00506854.md) at `0x0050706E`
- [safecrt_wctomb_s](../50/safecrt_wctomb_s_function_005070A8.md) at `0x00507101`
- [soutput_s](../50/soutput_s_function_00507184.md) at `0x00507253`
- [swoutput_s](../50/swoutput_s_function_00507278.md) at `0x00507380`
- [woutput_s](../50/woutput_s_function_005073AC.md) at `0x00507CBE`
- [input_s](../50/input_s_function_00508090.md) at `0x005088FE`
- [input_s](../50/input_s_function_00508090.md) at `0x00508912`
- [sinput_s](../50/sinput_s_function_00508938.md) at `0x0050899A`
- [swinput_s](../50/swinput_s_function_00508DA4.md) at `0x00508E0B`
- [winput_s](../50/winput_s_function_00508E78.md) at `0x005097D2`
- [winput_s](../50/winput_s_function_00508E78.md) at `0x00509800`
- [ungetc_nolock](../50/ungetc_nolock_function_00509824.md) at `0x0050989D`
- [fgetwc_nolock](../50/fgetwc_nolock_function_005098B4.md) at `0x005098CB`
- [ungetwc_nolock](../50/ungetwc_nolock_function_00509900.md) at `0x0050991A`
- [SymCryptFatalEnvWindowsKernelmodeWin8_1nLater](../51/SymCryptFatalEnvWindowsKernelmodeWin8_1nLater_function_0051C914.md) at `0x0051C91C`
- [SymCryptFdefIntMulMixedSize](../52/SymCryptFdefIntMulMixedSize_function_0052D88C.md) at `0x0052D8C8`
- [SymCryptFdefIntToDivisor](../52/SymCryptFdefIntToDivisor_function_0052DB04.md) at `0x0052DB30`
- [SymCryptFdefRawDivMod](../52/SymCryptFdefRawDivMod_function_0052DC30.md) at `0x0052DCCF`
- [SymCryptFdefModAddGeneric](../53/SymCryptFdefModAddGeneric_function_00534200.md) at `0x0053423E`
- [SymCryptFdefModElementGetValue](../53/SymCryptFdefModElementGetValue_function_005344FC.md) at `0x00534539`
- [SymCryptFdefModElementSetValueGeneric](../53/SymCryptFdefModElementSetValueGeneric_function_00534638.md) at `0x00534685`
- [SymCryptFdefModElementSetValueNegUint32](../53/SymCryptFdefModElementSetValueNegUint32_function_005346F4.md) at `0x0053472E`
- [SymCryptFdefModElementSetValueUint32Generic](../53/SymCryptFdefModElementSetValueUint32Generic_function_005347C0.md) at `0x005347F3`
- [SymCryptFdefModElementToIntGeneric](../53/SymCryptFdefModElementToIntGeneric_function_00534844.md) at `0x0053489F`
- [SymCryptFdefModMulGeneric](../53/SymCryptFdefModMulGeneric_function_00534DA0.md) at `0x00534DEE`
- [SymCryptFdefModNegGeneric](../53/SymCryptFdefModNegGeneric_function_00534F70.md) at `0x00534FA9`
- [SymCryptFdefModSetRandomGeneric](../53/SymCryptFdefModSetRandomGeneric_function_00535180.md) at `0x005351C1`
- [SymCryptFdefModSquareGeneric](../53/SymCryptFdefModSquareGeneric_function_005352C0.md) at `0x00535300`
- [SymCryptFdefModSubGeneric](../53/SymCryptFdefModSubGeneric_function_00535450.md) at `0x0053548E`
- [SymCryptFdef369ModAddGeneric](../53/SymCryptFdef369ModAddGeneric_function_005373C0.md) at `0x005373FE`
- [SymCryptFdef369ModSubGeneric](../53/SymCryptFdef369ModSubGeneric_function_005376C0.md) at `0x005376FE`
- [MiDeleteVadBitmap](../../page/A4/MiDeleteVadBitmap_function_00A45F18.md) at `0x00A45F7B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0049E550  C2 00 00                        ret 0
0049E553  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall EmpCheckErrataList(void)
{
    return;
}
```

## 5. (Beta) C Style

```c
void EmpCheckErrataList(void)
{
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0049E550&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0049E550[BB_0049E550]
  bb_0049E553[BB_0049E553]
```
