# HalpHvQueryAssociatedProcessors

- RVA: `0x0054CEC8`–`0x0054CEEF` (길이 `39` bytes)
- VA: `0x000000014054CEC8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `11`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0054CEDD` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [HalpHvInitMcaPcrContext](../4D/HalpHvInitMcaPcrContext_function_004D7D88.md) at `0x004D7E46`
- [HalpHvInitMcaPcrContext](../4D/HalpHvInitMcaPcrContext_function_004D7D88.md) at `0x004D7E9D`

### Static image references
- `0x0054CECC` → RVA `0x00FC1CD0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0054CEC8  48 83 EC 28                     sub rsp, 0x28
0054CECC  48 8B 05 FD 4D A7 00            mov rax, qword ptr [rip + 0xa74dfd]
0054CED3  48 85 C0                        test rax, rax
0054CED6  74 0C                           je 0x14054cee4
0054CED8  B9 FE FF FF FF                  mov ecx, 0xfffffffe
0054CEDD  E8 EE DB 16 00                  call 0x1406baad0
0054CEE2  EB 05                           jmp 0x14054cee9
0054CEE4  B8 01 00 00 C0                  mov eax, 0xc0000001
0054CEE9  48 83 C4 28                     add rsp, 0x28
0054CEED  C3                              ret
0054CEEE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpHvQueryAssociatedProcessors(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (*(unsigned __int64 *)(v_rip + 10964477) == 0) goto loc_0054CEE4;
    result = guard_dispatch_icall((unsigned int)(0xFFFFFFFEULL), a2, a3, a4);
    goto loc_0054CEE9;
loc_0054CEE4:
loc_0054CEE9:
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(0xC0000001ULL);
}
```

## 5. (Beta) C Style

```c
void HalpHvQueryAssociatedProcessors(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (*(uint64_t *)(v_rip + 0xA74DFD) == 0) goto loc_0054CEE4;
    result = guard_dispatch_icall((uint32_t)(0xFFFFFFFEULL), a2, a3, a4);
    goto loc_0054CEE9;
loc_0054CEE4:
loc_0054CEE9:
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(0xC0000001ULL);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0054CEC8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0054CEC8[BB_0054CEC8]
  bb_0054CED8[BB_0054CED8]
  bb_0054CEE4[BB_0054CEE4]
  bb_0054CEE9[BB_0054CEE9]
  bb_0054CEEE[BB_0054CEEE]
  bb_0054CEC8 -->|branch| bb_0054CEE4
  bb_0054CEC8 -->|fallthrough| bb_0054CED8
  bb_0054CED8 -->|branch| bb_0054CEE9
  bb_0054CEE4 -->|flow| bb_0054CEE9
```
