# PiUEventHandleUnregisterClient

- RVA: `0x009C3BBC`–`0x009C3BFE` (길이 `66` bytes)
- VA: `0x00000001409C3BBC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006CF28`
- 디코드: `20`개 명령, `66/66` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009C3BD5` → [ExAcquireFastMutex](../../text/20/ExAcquireFastMutex_function_0020E5A0.md) (function, `0x0020E5A0`)
- `0x009C3BE4` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)

### Direct callers
- [PiUEventHandleIoctl](PiUEventHandleIoctl_function_009C2B74.md) at `0x009C2BFD`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x009C3BD5` → [ExAcquireFastMutex](../../text/20/ExAcquireFastMutex_function_0020E5A0.md) (`PAGE` → `.text`)
  - `0x009C3BE4` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009C3BBC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
009C3BC1  57                              push rdi
009C3BC2  48 83 EC 20                     sub rsp, 0x20
009C3BC6  48 8B 79 20                     mov rdi, qword ptr [rcx + 0x20]
009C3BCA  33 DB                           xor ebx, ebx
009C3BCC  48 85 FF                        test rdi, rdi
009C3BCF  74 26                           je 0x1409c3bf7
009C3BD1  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
009C3BD5  E8 C6 A9 84 FF                  call 0x14020e5a0
009C3BDA  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
009C3BDE  88 9F 8C 00 00 00               mov byte ptr [rdi + 0x8c], bl
009C3BE4  E8 D7 DD 88 FF                  call 0x1402519c0
009C3BE9  8B C3                           mov eax, ebx
009C3BEB  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
009C3BF0  48 83 C4 20                     add rsp, 0x20
009C3BF4  5F                              pop rdi
009C3BF5  C3                              ret
009C3BF6  CC                              int3
009C3BF7  BB 0D 00 00 C0                  mov ebx, 0xc000000d
009C3BFC  EB EB                           jmp 0x1409c3be9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiUEventHandleUnregisterClient(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    v_rbx = 0;
    if (*(unsigned __int64 *)(a1 + 32) == 0) goto loc_009C3BF7;
    result = ExAcquireFastMutex(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 16), a2, a3, a4);
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 32) + 140) = 0;
    result = ExReleaseFastMutex(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 16), a2, a3, a4);
loc_009C3BE9:
    v_rsp = (v_rsp) + (32);
    return 0;
loc_009C3BF7:
    goto loc_009C3BE9;
}
```

## 5. (Beta) C Style

```c
int64_t PiUEventHandleUnregisterClient(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    local_rbx = 0;
    if (*(uint64_t *)(arg1 + 0x20) == 0) goto loc_009C3BF7;
    result = ExAcquireFastMutex(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x10), a2, a3, a4);
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8C) = 0;
    result = ExReleaseFastMutex(*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x10), a2, a3, a4);
loc_009C3BE9:
    local_rsp = (local_rsp) + (32);
    return 0;
loc_009C3BF7:
    goto loc_009C3BE9;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009C3BBC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009C3BBC[BB_009C3BBC]
  bb_009C3BD1[BB_009C3BD1]
  bb_009C3BE9[BB_009C3BE9]
  bb_009C3BF6[BB_009C3BF6]
  bb_009C3BF7[BB_009C3BF7]
  bb_009C3BBC -->|branch| bb_009C3BF7
  bb_009C3BBC -->|fallthrough| bb_009C3BD1
  bb_009C3BD1 -->|flow| bb_009C3BE9
  bb_009C3BF6 -->|flow| bb_009C3BF7
  bb_009C3BF7 -->|branch| bb_009C3BE9
```
