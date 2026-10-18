# HalpHvInvokeWheaErrorNotificationCallback

- RVA: `0x0054CE74`–`0x0054CE98` (길이 `36` bytes)
- VA: `0x000000014054CE74`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `11`개 명령, `36/36` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0054CE86` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [HalpMemoryErrorDeferredHandler](../55/HalpMemoryErrorDeferredHandler_function_0055686C.md) at `0x005568DD`
- [HalpPmemErrorDeferredHandler](../55/HalpPmemErrorDeferredHandler_function_00556A30.md) at `0x00556AF1`

### Static image references
- `0x0054CE78` → RVA `0x00FC1D18` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0054CE74  48 83 EC 28                     sub rsp, 0x28
0054CE78  48 8B 05 99 4E A7 00            mov rax, qword ptr [rip + 0xa74e99]
0054CE7F  48 85 C0                        test rax, rax
0054CE82  74 09                           je 0x14054ce8d
0054CE84  B2 01                           mov dl, 1
0054CE86  E8 45 DC 16 00                  call 0x1406baad0
0054CE8B  EB 05                           jmp 0x14054ce92
0054CE8D  B8 01 00 00 C0                  mov eax, 0xc0000001
0054CE92  48 83 C4 28                     add rsp, 0x28
0054CE96  C3                              ret
0054CE97  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpHvInvokeWheaErrorNotificationCallback(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (*(unsigned __int64 *)(v_rip + 10964633) == 0) goto loc_0054CE8D;
    result = guard_dispatch_icall(a1, 1, a3, a4);
    goto loc_0054CE92;
loc_0054CE8D:
loc_0054CE92:
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(0xC0000001ULL);
}
```

## 5. (Beta) C Style

```c
void HalpHvInvokeWheaErrorNotificationCallback(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (*(uint64_t *)(v_rip + 0xA74E99) == 0) goto loc_0054CE8D;
    result = guard_dispatch_icall(a1, 1, a3, a4);
    goto loc_0054CE92;
loc_0054CE8D:
loc_0054CE92:
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(0xC0000001ULL);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0054CE74&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0054CE74[BB_0054CE74]
  bb_0054CE84[BB_0054CE84]
  bb_0054CE8D[BB_0054CE8D]
  bb_0054CE92[BB_0054CE92]
  bb_0054CE97[BB_0054CE97]
  bb_0054CE74 -->|branch| bb_0054CE8D
  bb_0054CE74 -->|fallthrough| bb_0054CE84
  bb_0054CE84 -->|branch| bb_0054CE92
  bb_0054CE8D -->|flow| bb_0054CE92
```
