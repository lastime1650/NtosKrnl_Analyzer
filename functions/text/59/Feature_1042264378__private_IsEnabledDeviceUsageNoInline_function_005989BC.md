# Feature_1042264378__private_IsEnabledDeviceUsageNoInline

- RVA: `0x005989BC`–`0x005989EE` (길이 `50` bytes)
- VA: `0x00000001405989BC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005989E3` → [Feature_1042264378__private_IsEnabledFallback](Feature_1042264378__private_IsEnabledFallback_function_005989F4.md) (function, `0x005989F4`)

### Direct callers
- [IopCopyCompleteReadIrp](../4E/IopCopyCompleteReadIrp_function_004E83F0.md) at `0x004E844D`
- [IopCopyCompleteReadRequest](../4E/IopCopyCompleteReadRequest_function_004E8760.md) at `0x004E87B7`

### Static image references
- `0x005989C6` → RVA `0x00FC47F0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005989BC  48 83 EC 28                     sub rsp, 0x28
005989C0  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
005989C6  8B 05 24 BE A2 00               mov eax, dword ptr [rip + 0xa2be24]
005989CC  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
005989D0  A8 10                           test al, 0x10
005989D2  74 05                           je 0x1405989d9
005989D4  83 E0 01                        and eax, 1
005989D7  EB 0F                           jmp 0x1405989e8
005989D9  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
005989DE  BA 03 00 00 00                  mov edx, 3
005989E3  E8 0C 00 00 00                  call 0x1405989f4
005989E8  48 83 C4 28                     add rsp, 0x28
005989EC  C3                              ret
005989ED  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_1042264378__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10665508)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10665508)))) & (16)) == 0) goto loc_005989D9;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10665508))) & (1));
    goto loc_005989E8;
loc_005989D9:
    result = Feature_1042264378__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_005989E8:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_1042264378__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA2BE24)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA2BE24)))) & (16)) == 0) goto loc_005989D9;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xA2BE24))) & (1));
    goto loc_005989E8;
loc_005989D9:
    result = Feature_1042264378__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_005989E8:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005989BC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005989BC[BB_005989BC]
  bb_005989D4[BB_005989D4]
  bb_005989D9[BB_005989D9]
  bb_005989E8[BB_005989E8]
  bb_005989ED[BB_005989ED]
  bb_005989BC -->|branch| bb_005989D9
  bb_005989BC -->|fallthrough| bb_005989D4
  bb_005989D4 -->|branch| bb_005989E8
  bb_005989D9 -->|flow| bb_005989E8
```
