# HvlpMapEarlyPages

- RVA: `0x0058D504`–`0x0058D51F` (길이 `27` bytes)
- VA: `0x000000014058D504`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `7`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0058D514` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [HvlpInitializeBootProcessor](HvlpInitializeBootProcessor_function_00585964.md) at `0x00585A05`
- [HvlpInitializeBootProcessor](HvlpInitializeBootProcessor_function_00585964.md) at `0x00585A4D`
- [HvlpInitializeBootProcessor](HvlpInitializeBootProcessor_function_00585964.md) at `0x00585AC7`
- [HvlpTryConfigureInterface](HvlpTryConfigureInterface_function_0058CABC.md) at `0x0058CC34`
- [HvlpPhase0Enlightenments](HvlpPhase0Enlightenments_function_0058D1B8.md) at `0x0058D2A7`

### Static image references
- `0x0058D508` → RVA `0x00E00980` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0058D504  48 83 EC 28                     sub rsp, 0x28
0058D508  48 8B 05 71 34 87 00            mov rax, qword ptr [rip + 0x873471]
0058D50F  BA 01 00 00 00                  mov edx, 1
0058D514  E8 B7 D5 12 00                  call 0x1406baad0
0058D519  48 83 C4 28                     add rsp, 0x28
0058D51D  C3                              ret
0058D51E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvlpMapEarlyPages(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = guard_dispatch_icall(a1, 1, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void HvlpMapEarlyPages(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = guard_dispatch_icall(a1, 1, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0058D504&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0058D504[BB_0058D504]
  bb_0058D51E[BB_0058D51E]
```
