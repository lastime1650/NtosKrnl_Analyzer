# WheaPrmTranslatePhysicalAddress

- RVA: `0x00660AD0`–`0x00660B05` (길이 `53` bytes)
- VA: `0x0000000140660AD0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `13`개 명령, `53/53` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00660AFA` → [WheapPrmTranslatePhysicalAddressIntel](WheapPrmTranslatePhysicalAddressIntel_function_00660D98.md) (function, `0x00660D98`)

### Direct callers
- [HalpAddPrmAddressTranslationToMemoryExtIntelSection](../54/HalpAddPrmAddressTranslationToMemoryExtIntelSection_function_00544DC8.md) at `0x00544DFF`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00660AD0  48 83 EC 28                     sub rsp, 0x28
00660AD4  65 4C 8B 04 25 20 00 00 00      mov r8, qword ptr gs:[0x20]
00660ADD  B8 BB 00 00 C0                  mov eax, 0xc00000bb
00660AE2  41 80 78 41 00                  cmp byte ptr [r8 + 0x41], 0
00660AE7  75 07                           jne 0x140660af0
00660AE9  B8 01 00 00 C0                  mov eax, 0xc0000001
00660AEE  EB 0F                           jmp 0x140660aff
00660AF0  41 80 B8 8D 00 00 00 02         cmp byte ptr [r8 + 0x8d], 2
00660AF8  75 05                           jne 0x140660aff
00660AFA  E8 99 02 00 00                  call 0x140660d98
00660AFF  48 83 C4 28                     add rsp, 0x28
00660B03  C3                              ret
00660B04  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WheaPrmTranslatePhysicalAddress(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 65)) != 0) goto loc_00660AF0;
    goto loc_00660AFF;
loc_00660AF0:
    result = (unsigned int)(0xC0000001ULL);
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 141)) == 2) {
        result = WheapPrmTranslatePhysicalAddressIntel(a1, a2, *(unsigned __int64 *)(gs_base + (0 + 32)), a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void WheaPrmTranslatePhysicalAddress(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x41)) != 0) goto loc_00660AF0;
    goto loc_00660AFF;
loc_00660AF0:
    result = (uint32_t)(0xC0000001ULL);
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8D)) == 2) {
        result = WheapPrmTranslatePhysicalAddressIntel(a1, a2, *(uint64_t *)(gs_base + (0 + 0x20)), a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00660AD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00660AD0[BB_00660AD0]
  bb_00660AE9[BB_00660AE9]
  bb_00660AF0[BB_00660AF0]
  bb_00660AFA[BB_00660AFA]
  bb_00660AFF[BB_00660AFF]
  bb_00660B04[BB_00660B04]
  bb_00660AD0 -->|branch| bb_00660AF0
  bb_00660AD0 -->|fallthrough| bb_00660AE9
  bb_00660AE9 -->|branch| bb_00660AFF
  bb_00660AF0 -->|branch| bb_00660AFF
  bb_00660AF0 -->|fallthrough| bb_00660AFA
  bb_00660AFA -->|flow| bb_00660AFF
```
