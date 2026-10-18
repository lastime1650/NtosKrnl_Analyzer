# WheaHwErrorReportAbandonDeviceDriver

- RVA: `0x0065E650`–`0x0065E671` (길이 `33` bytes)
- VA: `0x000000014065E650`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `11`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0065E654` → [WheapErrorHandleIsValid](WheapErrorHandleIsValid_function_0065EC3C.md) (function, `0x0065EC3C`)
- `0x0065E664` → [WheapFreeDriverPacketBuffer](WheapFreeDriverPacketBuffer_function_0065EC58.md) (function, `0x0065EC58`)

### Direct callers
- [WheaReportFatalHwErrorDeviceDriverEx](WheaReportFatalHwErrorDeviceDriverEx_function_0065E910.md) at `0x0065E9AE`
- [WheaReportHwErrorDeviceDriverEx](WheaReportHwErrorDeviceDriverEx_function_0065EA30.md) at `0x0065EACD`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0065E650  48 83 EC 28                     sub rsp, 0x28
0065E654  E8 E3 05 00 00                  call 0x14065ec3c
0065E659  84 C0                           test al, al
0065E65B  75 07                           jne 0x14065e664
0065E65D  B8 08 00 00 C0                  mov eax, 0xc0000008
0065E662  EB 07                           jmp 0x14065e66b
0065E664  E8 EF 05 00 00                  call 0x14065ec58
0065E669  33 C0                           xor eax, eax
0065E66B  48 83 C4 28                     add rsp, 0x28
0065E66F  C3                              ret
0065E670  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WheaHwErrorReportAbandonDeviceDriver(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = WheapErrorHandleIsValid(a1, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0065E664;
    goto loc_0065E66B;
loc_0065E664:
    result = WheapFreeDriverPacketBuffer(a1, a2, a3, a4);
    result = 0;
loc_0065E66B:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void WheaHwErrorReportAbandonDeviceDriver(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = WheapErrorHandleIsValid(a1, a2, a3, a4);
    if ((uint8_t)(result) != 0) goto loc_0065E664;
    goto loc_0065E66B;
loc_0065E664:
    result = WheapFreeDriverPacketBuffer(a1, a2, a3, a4);
    result = 0;
loc_0065E66B:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0065E650&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0065E650[BB_0065E650]
  bb_0065E65D[BB_0065E65D]
  bb_0065E664[BB_0065E664]
  bb_0065E66B[BB_0065E66B]
  bb_0065E670[BB_0065E670]
  bb_0065E650 -->|branch| bb_0065E664
  bb_0065E650 -->|fallthrough| bb_0065E65D
  bb_0065E65D -->|branch| bb_0065E66B
  bb_0065E664 -->|flow| bb_0065E66B
```
