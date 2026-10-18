# HalpHvEnterSleepState

- RVA: `0x0054CDEC`–`0x0054CE0C` (길이 `32` bytes)
- VA: `0x000000014054CDEC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0054CE01` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [HalpShutdown](HalpShutdown_function_005469AC.md) at `0x00546ABC`
- [HaliAcpiSleep](../56/HaliAcpiSleep_function_0056AD60.md) at `0x0056B061`

### Static image references
- `0x0054CDF0` → RVA `0x00FC1C98` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0054CDEC  48 83 EC 28                     sub rsp, 0x28
0054CDF0  48 8B 15 A1 4E A7 00            mov rdx, qword ptr [rip + 0xa74ea1]
0054CDF7  33 C0                           xor eax, eax
0054CDF9  48 85 D2                        test rdx, rdx
0054CDFC  74 08                           je 0x14054ce06
0054CDFE  48 8B C2                        mov rax, rdx
0054CE01  E8 CA DC 16 00                  call 0x1406baad0
0054CE06  48 83 C4 28                     add rsp, 0x28
0054CE0A  C3                              ret
0054CE0B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpHvEnterSleepState(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = 0;
    if (*(unsigned __int64 *)(v_rip + 10964641) != 0) {
        result = *(unsigned __int64 *)(v_rip + 10964641);
        result = guard_dispatch_icall(a1, *(unsigned __int64 *)(v_rip + 10964641), a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void HalpHvEnterSleepState(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = 0;
    if (*(uint64_t *)(v_rip + 0xA74EA1) != 0) {
        result = *(uint64_t *)(v_rip + 0xA74EA1);
        result = guard_dispatch_icall(a1, *(uint64_t *)(v_rip + 0xA74EA1), a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0054CDEC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0054CDEC[BB_0054CDEC]
  bb_0054CDFE[BB_0054CDFE]
  bb_0054CE06[BB_0054CE06]
  bb_0054CE0B[BB_0054CE0B]
  bb_0054CDEC -->|branch| bb_0054CE06
  bb_0054CDEC -->|fallthrough| bb_0054CDFE
  bb_0054CDFE -->|flow| bb_0054CE06
```
