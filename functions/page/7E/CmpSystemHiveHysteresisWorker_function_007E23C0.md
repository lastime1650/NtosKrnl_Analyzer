# CmpSystemHiveHysteresisWorker

- RVA: `0x007E23C0`–`0x007E23EF` (길이 `47` bytes)
- VA: `0x00000001407E23C0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `12`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x007E23C6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007E23E4` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x007E23CB` → RVA `0x00EEFBB8` (`.data`; read)
- `0x007E23D7` → RVA `0x00EEFBB0` (`.data`; read)
- `0x007E23DD` → RVA `0x00EEFBC0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x007E23C6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007E23E4` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007E23C0  48 83 EC 28                     sub rsp, 0x28
007E23C4  33 D2                           xor edx, edx
007E23C6  E8 A5 04 3A 00                  call 0x140b82870
007E23CB  48 8B 05 E6 D7 70 00            mov rax, qword ptr [rip + 0x70d7e6]
007E23D2  48 85 C0                        test rax, rax
007E23D5  74 12                           je 0x1407e23e9
007E23D7  8B 15 D3 D7 70 00               mov edx, dword ptr [rip + 0x70d7d3]
007E23DD  48 8B 0D DC D7 70 00            mov rcx, qword ptr [rip + 0x70d7dc]
007E23E4  E8 E7 86 ED FF                  call 0x1406baad0
007E23E9  48 83 C4 28                     add rsp, 0x28
007E23ED  C3                              ret
007E23EE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpSystemHiveHysteresisWorker(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = 0;
    result = ExFreePoolWithTag(a1, a2, a3, a4);
    result = *(unsigned __int64 *)(v_rip + 7395302);
    if (*(unsigned __int64 *)(v_rip + 7395302) != 0) {
        a2 = *(unsigned int *)(v_rip + 7395283);
        a1 = *(unsigned __int64 *)(v_rip + 7395292);
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpSystemHiveHysteresisWorker(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg2 = 0;
    result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
    result = *(uint64_t *)(v_rip + 0x70D7E6);
    if (*(uint64_t *)(v_rip + 0x70D7E6) != 0) {
        Arg2 = *(uint32_t *)(v_rip + 0x70D7D3);
        Arg1 = *(uint64_t *)(v_rip + 0x70D7DC);
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007E23C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007E23C0[BB_007E23C0]
  bb_007E23D7[BB_007E23D7]
  bb_007E23E9[BB_007E23E9]
  bb_007E23EE[BB_007E23EE]
  bb_007E23C0 -->|branch| bb_007E23E9
  bb_007E23C0 -->|fallthrough| bb_007E23D7
  bb_007E23D7 -->|flow| bb_007E23E9
```
