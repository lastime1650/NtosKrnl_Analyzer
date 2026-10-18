# ExpWorkQueueManagerInitialize

- RVA: `0x007D01D4`–`0x007D02A8` (길이 `212` bytes)
- VA: `0x00000001407D01D4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000794E0`
- 디코드: `54`개 명령, `212/212` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x007D0200` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007D0219` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (function, `0x0040DD10`)
- `0x007D0224` → [KeInitializeTimerEx](../../text/45/KeInitializeTimerEx_function_004563F0.md) (function, `0x004563F0`)
- `0x007D0232` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (function, `0x0040DD10`)
- `0x007D024C` → [KeInitializeTimer2](../../text/3A/KeInitializeTimer2_function_003A30B0.md) (function, `0x003A30B0`)
- `0x007D0260` → [KeQueryNodeActiveAffinity](../../text/43/KeQueryNodeActiveAffinity_function_0043EF80.md) (function, `0x0043EF80`)
- `0x007D028B` → [KeSelectIdealProcessor](../../text/2C/KeSelectIdealProcessor_function_002CE8CC.md) (function, `0x002CE8CC`)

### Direct callers
- [ExpPartitionInitialize](../7C/ExpPartitionInitialize_function_007CFB9C.md) at `0x007CFCA8`

### Static image references
- `0x007D0245` → RVA `0x004C2720` (`ExpWorkQueueManagerReaperTimer`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **7**
  - `0x007D0200` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007D0219` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (`PAGE` → `.text`)
  - `0x007D0224` → [KeInitializeTimerEx](../../text/45/KeInitializeTimerEx_function_004563F0.md) (`PAGE` → `.text`)
  - `0x007D0232` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (`PAGE` → `.text`)
  - `0x007D024C` → [KeInitializeTimer2](../../text/3A/KeInitializeTimer2_function_003A30B0.md) (`PAGE` → `.text`)
  - `0x007D0260` → [KeQueryNodeActiveAffinity](../../text/43/KeQueryNodeActiveAffinity_function_0043EF80.md) (`PAGE` → `.text`)
  - `0x007D028B` → [KeSelectIdealProcessor](../../text/2C/KeSelectIdealProcessor_function_002CE8CC.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007D01D4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
007D01D9  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
007D01DE  57                              push rdi
007D01DF  48 83 EC 30                     sub rsp, 0x30
007D01E3  49 8B F8                        mov rdi, r8
007D01E6  48 8B DA                        mov rbx, rdx
007D01E9  48 8B F1                        mov rsi, rcx
007D01EC  0F 57 C0                        xorps xmm0, xmm0
007D01EF  48 83 C1 10                     add rcx, 0x10
007D01F3  33 D2                           xor edx, edx
007D01F5  41 B8 08 01 00 00               mov r8d, 0x108
007D01FB  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
007D0200  E8 3B 6A EF FF                  call 0x1406c6c40
007D0205  45 33 C0                        xor r8d, r8d
007D0208  48 89 1E                        mov qword ptr [rsi], rbx
007D020B  48 8D 4E 10                     lea rcx, [rsi + 0x10]
007D020F  48 89 7E 08                     mov qword ptr [rsi + 8], rdi
007D0213  41 8D 58 01                     lea ebx, [r8 + 1]
007D0217  8B D3                           mov edx, ebx
007D0219  E8 F2 DA C3 FF                  call 0x14040dd10
007D021E  48 8D 4E 28                     lea rcx, [rsi + 0x28]
007D0222  8B D3                           mov edx, ebx
007D0224  E8 C7 61 C8 FF                  call 0x1404563f0
007D0229  48 8D 4E 68                     lea rcx, [rsi + 0x68]
007D022D  45 33 C0                        xor r8d, r8d
007D0230  8B D3                           mov edx, ebx
007D0232  E8 D9 DA C3 FF                  call 0x14040dd10
007D0237  48 8D 8E 80 00 00 00            lea rcx, [rsi + 0x80]
007D023E  4C 8B C6                        mov r8, rsi
007D0241  44 8D 4B 07                     lea r9d, [rbx + 7]
007D0245  48 8D 15 D4 24 CF FF            lea rdx, [rip - 0x30db2c]
007D024C  E8 5F 2E BD FF                  call 0x1403a30b0
007D0251  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
007D0255  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
007D025A  45 33 C0                        xor r8d, r8d
007D025D  0F B7 09                        movzx ecx, word ptr [rcx]
007D0260  E8 1B ED C6 FF                  call 0x14043ef80
007D0265  F3 48 0F B8 44 24 20            popcnt rax, qword ptr [rsp + 0x20]
007D026C  33 C9                           xor ecx, ecx
007D026E  66 89 8E 14 01 00 00            mov word ptr [rsi + 0x114], cx
007D0275  85 C0                           test eax, eax
007D0277  74 1E                           je 0x1407d0297
007D0279  45 33 C9                        xor r9d, r9d
007D027C  48 8D 96 14 01 00 00            lea rdx, [rsi + 0x114]
007D0283  45 33 C0                        xor r8d, r8d
007D0286  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
007D028B  E8 3C E6 AF FF                  call 0x1402ce8cc
007D0290  66 89 86 14 01 00 00            mov word ptr [rsi + 0x114], ax
007D0297  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
007D029C  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
007D02A1  48 83 C4 30                     add rsp, 0x30
007D02A5  5F                              pop rdi
007D02A6  C3                              ret
007D02A7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpWorkQueueManagerInitialize(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (48);
    a1 = (a1) + (16);
    a2 = 0;
    v_stack_m18 = v_xmm0;
    result = memset(a1, a2, 264, a4);
    a3 = 0;
    *(unsigned __int64 *)(a1) = 0;
    *(unsigned __int64 *)(a1 + 8) = 0;
    result = KeInitializeEvent(a1 + 16, (unsigned int)((unsigned int)(a3 + 1)), a3, a4);
    result = KeInitializeTimerEx(a1 + 40, (unsigned int)((unsigned int)(a3 + 1)), a3, a4);
    a3 = 0;
    result = KeInitializeEvent(a1 + 104, (unsigned int)((unsigned int)(a3 + 1)), a3, a4);
    result = KeInitializeTimer2(a1 + 128, v_rip - 3201836, a1, a3 + 1 + 7);
    a3 = 0;
    result = KeQueryNodeActiveAffinity(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8)), v_stack_m18, a3, a3 + 1 + 7);
    a1 = 0;
    *(unsigned __int16 *)(a1 + 276) = 0;
    if ((unsigned int)(result) != 0) {
        a4 = 0;
        a2 = a1 + 276;
        a3 = 0;
        a1 = v_stack_m18;
        result = KeSelectIdealProcessor(a1, a2, a3, a4);
        *(unsigned __int16 *)(a1 + 276) = (unsigned __int16)(result);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpWorkQueueManagerInitialize(void *Arg1, int64_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (48);
    Arg1 = (Arg1) + (16);
    Arg2 = 0;
    v_stack_m18 = v_xmm0;
    result = memset(Arg1, Arg2, 264, a4);
    Arg3 = 0;
    *(uint64_t *)(arg1) = 0;
    *(uint64_t *)(arg1 + 0x8) = 0;
    result = KeInitializeEvent(Arg1 + 16, (uint32_t)((uint32_t)(Arg3 + 1)), Arg3, a4);
    result = KeInitializeTimerEx(Arg1 + 40, (uint32_t)((uint32_t)(Arg3 + 1)), Arg3, a4);
    Arg3 = 0;
    result = KeInitializeEvent(Arg1 + 104, (uint32_t)((uint32_t)(Arg3 + 1)), Arg3, a4);
    result = KeInitializeTimer2(Arg1 + 128, v_rip - 3201836, Arg1, Arg3 + 1 + 7);
    Arg3 = 0;
    result = KeQueryNodeActiveAffinity(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8)), v_stack_m18, Arg3, Arg3 + 1 + 7);
    Arg1 = 0;
    *(uint16_t *)(arg1 + 0x114) = 0;
    if ((uint32_t)(result) != 0) {
        a4 = 0;
        Arg2 = Arg1 + 276;
        Arg3 = 0;
        Arg1 = v_stack_m18;
        result = KeSelectIdealProcessor(Arg1, Arg2, Arg3, a4);
        *(uint16_t *)(arg1 + 0x114) = (uint16_t)(result);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg1` | `+ 0x80` | `64` | `R` |
| `Arg1` | `+ 0x114` | `16` | `W` |
| `Arg1` | `+ 0x114` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007D01D4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007D01D4[BB_007D01D4]
  bb_007D0279[BB_007D0279]
  bb_007D0297[BB_007D0297]
  bb_007D02A7[BB_007D02A7]
  bb_007D01D4 -->|branch| bb_007D0297
  bb_007D01D4 -->|fallthrough| bb_007D0279
  bb_007D0279 -->|flow| bb_007D0297
```
