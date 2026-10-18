# HalpCompleteInitializeProfiling

- RVA: `0x00B5EED8`–`0x00B5EEFA` (길이 `34` bytes)
- VA: `0x0000000140B5EED8`
- 실행 섹션: `PAGELK`
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
- `0x00B5EEEF` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [HalpHwPerfCntInitSystem](HalpHwPerfCntInitSystem_function_00B5C590.md) at `0x00B5C5E0`

### Static image references
- `0x00B5EEDC` → RVA `0x00E03B20` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B5EEEF` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B5EED8  48 83 EC 28                     sub rsp, 0x28
00B5EEDC  48 8B 05 3D 4C 2A 00            mov rax, qword ptr [rip + 0x2a4c3d]
00B5EEE3  48 8B 80 80 00 00 00            mov rax, qword ptr [rax + 0x80]
00B5EEEA  48 85 C0                        test rax, rax
00B5EEED  74 05                           je 0x140b5eef4
00B5EEEF  E8 DC BB B5 FF                  call 0x1406baad0
00B5EEF4  48 83 C4 28                     add rsp, 0x28
00B5EEF8  C3                              ret
00B5EEF9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpCompleteInitializeProfiling(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 2772029) + 128);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 2772029) + 128) != 0) {
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void HalpCompleteInitializeProfiling(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = *(uint64_t *)(*(uint64_t *)(v_rip + 0x2A4C3D) + 0x80);
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x2A4C3D) + 0x80) != 0) {
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B5EED8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B5EED8[BB_00B5EED8]
  bb_00B5EEEF[BB_00B5EEEF]
  bb_00B5EEF4[BB_00B5EEF4]
  bb_00B5EEF9[BB_00B5EEF9]
  bb_00B5EED8 -->|branch| bb_00B5EEF4
  bb_00B5EED8 -->|fallthrough| bb_00B5EEEF
  bb_00B5EEEF -->|flow| bb_00B5EEF4
```
