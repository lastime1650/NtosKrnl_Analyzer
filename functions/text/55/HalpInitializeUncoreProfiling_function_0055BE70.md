# HalpInitializeUncoreProfiling

- RVA: `0x0055BE70`–`0x0055BE92` (길이 `34` bytes)
- VA: `0x000000014055BE70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `34/34` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0055BE87` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [HalpHwPerfCntInitSystem](../../pagelk/B5/HalpHwPerfCntInitSystem_function_00B5C590.md) at `0x00B5C5C5`

### Static image references
- `0x0055BE74` → RVA `0x00E03B20` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0055BE70  48 83 EC 28                     sub rsp, 0x28
0055BE74  48 8B 05 A5 7C 8A 00            mov rax, qword ptr [rip + 0x8a7ca5]
0055BE7B  48 8B 80 98 00 00 00            mov rax, qword ptr [rax + 0x98]
0055BE82  48 85 C0                        test rax, rax
0055BE85  74 05                           je 0x14055be8c
0055BE87  E8 44 EC 15 00                  call 0x1406baad0
0055BE8C  48 83 C4 28                     add rsp, 0x28
0055BE90  C3                              ret
0055BE91  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpInitializeUncoreProfiling(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9075877) + 152);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9075877) + 152) != 0) {
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void HalpInitializeUncoreProfiling(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = *(uint64_t *)(*(uint64_t *)(v_rip + 0x8A7CA5) + 0x98);
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x8A7CA5) + 0x98) != 0) {
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0055BE70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0055BE70[BB_0055BE70]
  bb_0055BE87[BB_0055BE87]
  bb_0055BE8C[BB_0055BE8C]
  bb_0055BE91[BB_0055BE91]
  bb_0055BE70 -->|branch| bb_0055BE8C
  bb_0055BE70 -->|fallthrough| bb_0055BE87
  bb_0055BE87 -->|flow| bb_0055BE8C
```
