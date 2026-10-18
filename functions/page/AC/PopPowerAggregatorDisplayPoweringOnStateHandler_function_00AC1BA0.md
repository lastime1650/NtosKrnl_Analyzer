# PopPowerAggregatorDisplayPoweringOnStateHandler

- RVA: `0x00AC1BA0`–`0x00AC1BFF` (길이 `95` bytes)
- VA: `0x0000000140AC1BA0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000697A4`
- 디코드: `26`개 명령, `95/95` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00AC1BC1` → [PopPowerAggregatorSetCurrentState](../98/PopPowerAggregatorSetCurrentState_function_0098A3B0.md) (function, `0x0098A3B0`)
- `0x00AC1BD0` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (function, `0x002DFBBC`)
- `0x00AC1BD7` → [PopGetMonitorReasonFromPowerEventId](../../text/4B/PopGetMonitorReasonFromPowerEventId_function_004BB2D8.md) (function, `0x004BB2D8`)
- `0x00AC1BE5` → [PopSleepstudyStartNextSession](PopSleepstudyStartNextSession_function_00AC4720.md) (function, `0x00AC4720`)
- `0x00AC1BF1` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (function, `0x00430B44`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00AC1BC9` → RVA `0x00F09710` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00AC1BD0` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (`PAGE` → `.text`)
  - `0x00AC1BD7` → [PopGetMonitorReasonFromPowerEventId](../../text/4B/PopGetMonitorReasonFromPowerEventId_function_004BB2D8.md) (`PAGE` → `.text`)
  - `0x00AC1BF1` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AC1BA0  40 53                           push rbx
00AC1BA2  48 83 EC 40                     sub rsp, 0x40
00AC1BA6  80 79 48 00                     cmp byte ptr [rcx + 0x48], 0
00AC1BAA  48 8B D9                        mov rbx, rcx
00AC1BAD  74 47                           je 0x140ac1bf6
00AC1BAF  0F 57 C0                        xorps xmm0, xmm0
00AC1BB2  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
00AC1BB7  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00AC1BBC  0F 11 44 24 30                  movups xmmword ptr [rsp + 0x30], xmm0
00AC1BC1  E8 EA 87 EC FF                  call 0x14098a3b0
00AC1BC6  8B 5B 18                        mov ebx, dword ptr [rbx + 0x18]
00AC1BC9  48 8D 0D 40 7B 44 00            lea rcx, [rip + 0x447b40]
00AC1BD0  E8 E7 DF 81 FF                  call 0x1402dfbbc
00AC1BD5  8B CB                           mov ecx, ebx
00AC1BD7  E8 FC 96 9F FF                  call 0x1404bb2d8
00AC1BDC  25 FF FF FF 00                  and eax, 0xffffff
00AC1BE1  33 C9                           xor ecx, ecx
00AC1BE3  8B D0                           mov edx, eax
00AC1BE5  E8 36 2B 00 00                  call 0x140ac4720
00AC1BEA  48 8D 0D 1F 7B 44 00            lea rcx, [rip + 0x447b1f]
00AC1BF1  E8 4E EF 96 FF                  call 0x140430b44
00AC1BF6  33 C0                           xor eax, eax
00AC1BF8  48 83 C4 40                     add rsp, 0x40
00AC1BFC  5B                              pop rbx
00AC1BFD  C3                              ret
00AC1BFE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPowerAggregatorDisplayPoweringOnStateHandler(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;

    v_rsp = (v_rsp) - (64);
    v_rbx = a1;
    if ((*(unsigned __int8 *)(a1 + 72)) != 0) {
        a2 = v_stack_m28;
        v_stack_m28 = v_xmm0;
        v_stack_m18 = v_xmm0;
        result = PopPowerAggregatorSetCurrentState(a1, a2, a3, a4);
        v_rbx = *(unsigned int *)(a1 + 24);
        a1 = v_rip + 4488000;
        result = PopReleaseRwLock(a1, a2, a3, a4);
        a1 = (unsigned int)(v_rbx);
        result = PopGetMonitorReasonFromPowerEventId(a1, a2, a3, a4);
        result = (unsigned int)((result) & (0xFFFFFFULL));
        a1 = 0;
        a2 = (unsigned int)(result);
        result = PopSleepstudyStartNextSession(a1, a2, a3, a4);
        a1 = v_rip + 4487967;
        result = PopAcquireRwLockExclusive(a1, a2, a3, a4);
    }
    result = 0;
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopPowerAggregatorDisplayPoweringOnStateHandler(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;

    local_rsp = (local_rsp) - (64);
    local_rbx = Arg1;
    if ((*(uint8_t *)(arg1 + 0x48)) != 0) {
        a2 = v_stack_m28;
        v_stack_m28 = v_xmm0;
        v_stack_m18 = v_xmm0;
        result = PopPowerAggregatorSetCurrentState(Arg1, a2, a3, a4);
        local_rbx = *(uint32_t *)(arg1 + 0x18);
        Arg1 = v_rip + 4488000;
        result = PopReleaseRwLock(Arg1, a2, a3, a4);
        Arg1 = (uint32_t)(local_rbx);
        result = PopGetMonitorReasonFromPowerEventId(Arg1, a2, a3, a4);
        result = (uint32_t)((result) & (0xFFFFFFULL));
        Arg1 = 0;
        a2 = (uint32_t)(result);
        result = PopSleepstudyStartNextSession(Arg1, a2, a3, a4);
        Arg1 = v_rip + 4487967;
        result = PopAcquireRwLockExclusive(Arg1, a2, a3, a4);
    }
    result = 0;
    local_rsp = (local_rsp) + (64);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x48` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AC1BA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AC1BA0[BB_00AC1BA0]
  bb_00AC1BAF[BB_00AC1BAF]
  bb_00AC1BF6[BB_00AC1BF6]
  bb_00AC1BFE[BB_00AC1BFE]
  bb_00AC1BA0 -->|branch| bb_00AC1BF6
  bb_00AC1BA0 -->|fallthrough| bb_00AC1BAF
  bb_00AC1BAF -->|flow| bb_00AC1BF6
```
