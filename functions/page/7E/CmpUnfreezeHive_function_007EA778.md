# CmpUnfreezeHive

- RVA: `0x007EA778`–`0x007EA7CE` (길이 `86` bytes)
- VA: `0x00000001407EA778`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00064C80`
- 디코드: `22`개 명령, `86/86` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007EA78E` → [CmpInitializeDelayDerefContext](../../text/42/CmpInitializeDelayDerefContext_function_0042A7F0.md) (function, `0x0042A7F0`)
- `0x007EA7AE` → [CmpDereferenceKeyControlBlockWithLock](../86/CmpDereferenceKeyControlBlockWithLock_function_00862B60.md) (function, `0x00862B60`)
- `0x007EA7C2` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (function, `0x0041B9A0`)

### Direct callers
- [CmpIsHiveAlreadyLoaded](CmpIsHiveAlreadyLoaded_function_007EA594.md) at `0x007EA62F`
- [CmpPerformUnloadKey](../9A/CmpPerformUnloadKey_function_009AFA28.md) at `0x009AFC49`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x007EA78E` → [CmpInitializeDelayDerefContext](../../text/42/CmpInitializeDelayDerefContext_function_0042A7F0.md) (`PAGE` → `.text`)
  - `0x007EA7C2` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007EA778  40 53                           push rbx
007EA77A  48 83 EC 30                     sub rsp, 0x30
007EA77E  48 8B D9                        mov rbx, rcx
007EA781  0F 57 C0                        xorps xmm0, xmm0
007EA784  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
007EA789  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
007EA78E  E8 5D 00 C4 FF                  call 0x14042a7f0
007EA793  48 8B 8B 78 0B 00 00            mov rcx, qword ptr [rbx + 0xb78]
007EA79A  C6 83 80 0B 00 00 00            mov byte ptr [rbx + 0xb80], 0
007EA7A1  48 85 C9                        test rcx, rcx
007EA7A4  74 15                           je 0x1407ea7bb
007EA7A6  45 33 C0                        xor r8d, r8d
007EA7A9  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
007EA7AE  E8 AD 83 07 00                  call 0x140862b60
007EA7B3  48 83 A3 78 0B 00 00 00         and qword ptr [rbx + 0xb78], 0
007EA7BB  33 D2                           xor edx, edx
007EA7BD  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
007EA7C2  E8 D9 11 C3 FF                  call 0x14041b9a0
007EA7C7  48 83 C4 30                     add rsp, 0x30
007EA7CB  5B                              pop rbx
007EA7CC  C3                              ret
007EA7CD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpUnfreezeHive(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (48);
    v_stack_m18 = v_xmm0;
    result = CmpInitializeDelayDerefContext(v_stack_m18, a2, a3, a4);
    *(unsigned __int8 *)(a1 + 2944) = 0;
    if (*(unsigned __int64 *)(a1 + 2936) != 0) {
        a3 = 0;
        a2 = v_stack_m18;
        result = CmpDereferenceKeyControlBlockWithLock(*(unsigned __int64 *)(a1 + 2936), a2, a3, a4);
    }
    a2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_m18, a2, a3, a4);
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpUnfreezeHive(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (48);
    v_stack_m18 = v_xmm0;
    result = CmpInitializeDelayDerefContext(v_stack_m18, Arg2, Arg3, a4);
    *(uint8_t *)(arg1 + 0xB80) = 0;
    if (*(uint64_t *)(arg1 + 0xB78) != 0) {
        Arg3 = 0;
        Arg2 = v_stack_m18;
        result = CmpDereferenceKeyControlBlockWithLock(*(uint64_t *)(arg1 + 0xB78), Arg2, Arg3, a4);
    }
    Arg2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_m18, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xB78` | `64` | `R` |
| `Arg1` | `+ 0xB78` | `64` | `R/W` |
| `Arg1` | `+ 0xB80` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007EA778&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007EA778[BB_007EA778]
  bb_007EA7A6[BB_007EA7A6]
  bb_007EA7BB[BB_007EA7BB]
  bb_007EA7CD[BB_007EA7CD]
  bb_007EA778 -->|branch| bb_007EA7BB
  bb_007EA778 -->|fallthrough| bb_007EA7A6
  bb_007EA7A6 -->|flow| bb_007EA7BB
```
