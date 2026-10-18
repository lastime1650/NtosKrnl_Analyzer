# PopNetSetResiliencyPhaseBias

- RVA: `0x00ABD9F0`–`0x00ABDA1E` (길이 `46` bytes)
- VA: `0x0000000140ABD9F0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BD8`
- 디코드: `15`개 명령, `46/46` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00ABD9F8` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (function, `0x00B78410`)
- `0x00ABDA09` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (function, `0x00B783C0`)
- `0x00ABDA17` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [PopNetEvaluationWorkerCallback](../../text/4B/PopNetEvaluationWorkerCallback_function_004BE0B0.md) at `0x004BE12D`
- [sub_006FCAE6](../../text/6F/Unknown_function_006FCAE6.md) at `0x006FCB12`
- [PopNetDisengageNetworkRefresh](../76/PopNetDisengageNetworkRefresh_function_00768B88.md) at `0x00768BB9`
- [PopNetRefreshTimerWorkerCallback](../76/PopNetRefreshTimerWorkerCallback_function_00768D10.md) at `0x00768D52`

### Static image references
- `0x00ABD9FD` → RVA `0x00E677C0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00ABD9F8` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (`PAGE` → `PAGELK`)
  - `0x00ABDA09` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (`PAGE` → `PAGELK`)
  - `0x00ABDA17` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00ABD9F0  40 53                           push rbx
00ABD9F2  48 83 EC 20                     sub rsp, 0x20
00ABD9F6  8A D9                           mov bl, cl
00ABD9F8  E8 13 AA 0B 00                  call 0x140b78410
00ABD9FD  48 8B 05 BC 9D 3A 00            mov rax, qword ptr [rip + 0x3a9dbc]
00ABDA04  48 85 C0                        test rax, rax
00ABDA07  75 0C                           jne 0x140abda15
00ABDA09  E8 B2 A9 0B 00                  call 0x140b783c0
00ABDA0E  48 83 C4 20                     add rsp, 0x20
00ABDA12  5B                              pop rbx
00ABDA13  C3                              ret
00ABDA14  CC                              int3
00ABDA15  8A CB                           mov cl, bl
00ABDA17  E8 B4 D0 BF FF                  call 0x1406baad0
00ABDA1C  EB EB                           jmp 0x140abda09
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopNetSetResiliencyPhaseBias(unsigned __int8 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = PopReleasePolicyLock(a1, a2, a3, a4);
    if (*(unsigned __int64 *)(v_rip + 3841468) != 0) goto loc_00ABDA15;
loc_00ABDA09:
    result = PopAcquirePolicyLock(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
loc_00ABDA15:
    result = guard_dispatch_icall(a1, a2, a3, a4);
    goto loc_00ABDA09;
}
```

## 5. (Beta) C Style

```c
int64_t PopNetSetResiliencyPhaseBias(uint8_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = PopReleasePolicyLock(Arg1, a2, a3, a4);
    if (*(uint64_t *)(v_rip + 0x3A9DBC) != 0) goto loc_00ABDA15;
loc_00ABDA09:
    result = PopAcquirePolicyLock(Arg1, a2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
loc_00ABDA15:
    result = guard_dispatch_icall(Arg1, a2, a3, a4);
    goto loc_00ABDA09;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00ABD9F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00ABD9F0[BB_00ABD9F0]
  bb_00ABDA09[BB_00ABDA09]
  bb_00ABDA14[BB_00ABDA14]
  bb_00ABDA15[BB_00ABDA15]
  bb_00ABD9F0 -->|branch| bb_00ABDA15
  bb_00ABD9F0 -->|fallthrough| bb_00ABDA09
  bb_00ABDA14 -->|flow| bb_00ABDA15
  bb_00ABDA15 -->|branch| bb_00ABDA09
```
