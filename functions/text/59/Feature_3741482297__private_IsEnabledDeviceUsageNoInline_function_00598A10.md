# Feature_3741482297__private_IsEnabledDeviceUsageNoInline

- RVA: `0x00598A10`–`0x00598A42` (길이 `50` bytes)
- VA: `0x0000000140598A10`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00598A37` → [Feature_3741482297__private_IsEnabledFallback](Feature_3741482297__private_IsEnabledFallback_function_00598A48.md) (function, `0x00598A48`)

### Direct callers
- [IopAllocateAndPopulateWriteIrp](../40/IopAllocateAndPopulateWriteIrp_function_004011F4.md) at `0x004014CE`
- [IopFreeCopyObjectsFromIrp](../4E/IopFreeCopyObjectsFromIrp_function_004E8834.md) at `0x004E8870`
- [IopReadFile](../../page/8A/IopReadFile_function_008AEFF0.md) at `0x008AF89B`

### Static image references
- `0x00598A1A` → RVA `0x00FC47E8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00598A10  48 83 EC 28                     sub rsp, 0x28
00598A14  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00598A1A  8B 05 C8 BD A2 00               mov eax, dword ptr [rip + 0xa2bdc8]
00598A20  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00598A24  A8 10                           test al, 0x10
00598A26  74 05                           je 0x140598a2d
00598A28  83 E0 01                        and eax, 1
00598A2B  EB 0F                           jmp 0x140598a3c
00598A2D  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00598A32  BA 03 00 00 00                  mov edx, 3
00598A37  E8 0C 00 00 00                  call 0x140598a48
00598A3C  48 83 C4 28                     add rsp, 0x28
00598A40  C3                              ret
00598A41  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_3741482297__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10665416)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10665416)))) & (16)) == 0) goto loc_00598A2D;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10665416))) & (1));
    goto loc_00598A3C;
loc_00598A2D:
    result = Feature_3741482297__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_00598A3C:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_3741482297__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA2BDC8)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA2BDC8)))) & (16)) == 0) goto loc_00598A2D;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xA2BDC8))) & (1));
    goto loc_00598A3C;
loc_00598A2D:
    result = Feature_3741482297__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_00598A3C:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00598A10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00598A10[BB_00598A10]
  bb_00598A28[BB_00598A28]
  bb_00598A2D[BB_00598A2D]
  bb_00598A3C[BB_00598A3C]
  bb_00598A41[BB_00598A41]
  bb_00598A10 -->|branch| bb_00598A2D
  bb_00598A10 -->|fallthrough| bb_00598A28
  bb_00598A28 -->|branch| bb_00598A3C
  bb_00598A2D -->|flow| bb_00598A3C
```
