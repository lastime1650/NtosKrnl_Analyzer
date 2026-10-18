# InbvSetScrollRegion

- RVA: `0x005904C0`–`0x005904E4` (길이 `36` bytes)
- VA: `0x00000001405904C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `11`개 명령, `36/36` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005904D9` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [DisplayBootBitmap](../53/DisplayBootBitmap_function_0053B87C.md) at `0x0053B921`

### Static image references
- `0x005904C4` → RVA `0x00E65E58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005904C0  48 83 EC 38                     sub rsp, 0x38
005904C4  48 8B 05 8D 59 8D 00            mov rax, qword ptr [rip + 0x8d598d]
005904CB  48 85 C0                        test rax, rax
005904CE  74 0E                           je 0x1405904de
005904D0  48 8B 40 48                     mov rax, qword ptr [rax + 0x48]
005904D4  48 85 C0                        test rax, rax
005904D7  74 05                           je 0x1405904de
005904D9  E8 F2 A5 12 00                  call 0x1406baad0
005904DE  48 83 C4 38                     add rsp, 0x38
005904E2  C3                              ret
005904E3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall InbvSetScrollRegion(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (56);
    if (*(unsigned __int64 *)(v_rip + 9263501) == 0) goto loc_005904DE;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9263501) + 72);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9263501) + 72) != 0) {
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
void InbvSetScrollRegion(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (56);
    if (*(uint64_t *)(v_rip + 0x8D598D) == 0) goto loc_005904DE;
    result = *(uint64_t *)(*(uint64_t *)(v_rip + 0x8D598D) + 0x48);
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x8D598D) + 0x48) != 0) {
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005904C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005904C0[BB_005904C0]
  bb_005904D0[BB_005904D0]
  bb_005904D9[BB_005904D9]
  bb_005904DE[BB_005904DE]
  bb_005904E3[BB_005904E3]
  bb_005904C0 -->|branch| bb_005904DE
  bb_005904C0 -->|fallthrough| bb_005904D0
  bb_005904D0 -->|branch| bb_005904DE
  bb_005904D0 -->|fallthrough| bb_005904D9
  bb_005904D9 -->|flow| bb_005904DE
```
