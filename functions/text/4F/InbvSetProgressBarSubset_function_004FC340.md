# InbvSetProgressBarSubset

- RVA: `0x004FC340`–`0x004FC364` (길이 `36` bytes)
- VA: `0x00000001404FC340`
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
- `0x004FC359` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [Phase1Initialization](../../page/70/Phase1Initialization_function_007062C0.md) at `0x007062EE`
- [Phase1InitializationIoReady](../../init/C7/Phase1InitializationIoReady_function_00C70458.md) at `0x00C70527`

### Static image references
- `0x004FC344` → RVA `0x00E65E58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004FC340  48 83 EC 28                     sub rsp, 0x28
004FC344  48 8B 05 0D 9B 96 00            mov rax, qword ptr [rip + 0x969b0d]
004FC34B  48 85 C0                        test rax, rax
004FC34E  74 0E                           je 0x1404fc35e
004FC350  48 8B 40 70                     mov rax, qword ptr [rax + 0x70]
004FC354  48 85 C0                        test rax, rax
004FC357  74 05                           je 0x1404fc35e
004FC359  E8 72 E7 1B 00                  call 0x1406baad0
004FC35E  48 83 C4 28                     add rsp, 0x28
004FC362  C3                              ret
004FC363  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall InbvSetProgressBarSubset(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (*(unsigned __int64 *)(v_rip + 9870093) == 0) goto loc_004FC35E;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9870093) + 112);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9870093) + 112) != 0) {
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void InbvSetProgressBarSubset(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (*(uint64_t *)(v_rip + 0x969B0D) == 0) goto loc_004FC35E;
    result = *(uint64_t *)(*(uint64_t *)(v_rip + 0x969B0D) + 0x70);
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x969B0D) + 0x70) != 0) {
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004FC340&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004FC340[BB_004FC340]
  bb_004FC350[BB_004FC350]
  bb_004FC359[BB_004FC359]
  bb_004FC35E[BB_004FC35E]
  bb_004FC363[BB_004FC363]
  bb_004FC340 -->|branch| bb_004FC35E
  bb_004FC340 -->|fallthrough| bb_004FC350
  bb_004FC350 -->|branch| bb_004FC35E
  bb_004FC350 -->|fallthrough| bb_004FC359
  bb_004FC359 -->|flow| bb_004FC35E
```
