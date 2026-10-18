# PopSleepstudyUlongFormatter

- RVA: `0x00AA3F30`–`0x00AA3F93` (길이 `99` bytes)
- VA: `0x0000000140AA3F30`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00088CDC`
- 디코드: `26`개 명령, `99/99` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00AA3F55` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AA3F8C` → [RtlUnicodeStringPrintf](../../text/48/RtlUnicodeStringPrintf_function_0048B984.md) (function, `0x0048B984`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00AA3F79` → RVA `0x00AFCAE0` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00AA3F55` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AA3F8C` → [RtlUnicodeStringPrintf](../../text/48/RtlUnicodeStringPrintf_function_0048B984.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AA3F30  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00AA3F35  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00AA3F3A  57                              push rdi
00AA3F3B  48 83 EC 20                     sub rsp, 0x20
00AA3F3F  48 8B DA                        mov rbx, rdx
00AA3F42  48 8B F9                        mov rdi, rcx
00AA3F45  BA 14 00 00 00                  mov edx, 0x14
00AA3F4A  B9 00 01 00 00                  mov ecx, 0x100
00AA3F4F  41 B8 53 53 4D 44               mov r8d, 0x444d5353
00AA3F55  E8 96 E1 0D 00                  call 0x140b820f0
00AA3F5A  48 85 C0                        test rax, rax
00AA3F5D  75 16                           jne 0x140aa3f75
00AA3F5F  B8 9A 00 00 C0                  mov eax, 0xc000009a
00AA3F64  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00AA3F69  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
00AA3F6E  48 83 C4 20                     add rsp, 0x20
00AA3F72  5F                              pop rdi
00AA3F73  C3                              ret
00AA3F74  CC                              int3
00AA3F75  48 89 43 08                     mov qword ptr [rbx + 8], rax
00AA3F79  48 8D 15 60 8B 05 00            lea rdx, [rip + 0x58b60]
00AA3F80  C7 03 00 00 14 00               mov dword ptr [rbx], 0x140000
00AA3F86  48 8B CB                        mov rcx, rbx
00AA3F89  44 8B 07                        mov r8d, dword ptr [rdi]
00AA3F8C  E8 F3 79 9E FF                  call 0x14048b984
00AA3F91  EB D1                           jmp 0x140aa3f64
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopSleepstudyUlongFormatter(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = ExAllocatePool2(256, 20, (unsigned int)(0x444D5353ULL), a4);
    if (result != 0) goto loc_00AA3F75;
loc_00AA3F64:
    v_rsp = (v_rsp) + (32);
    return (unsigned int)(0xC000009AULL);
loc_00AA3F75:
    *(unsigned __int64 *)(v_stack_p8 + 8) = (unsigned int)(0xC000009AULL);
    *(unsigned int *)(v_stack_p8) = 0x140000ULL;
    result = RtlUnicodeStringPrintf(v_stack_p8, v_rip + 363360, (unsigned int)(*(unsigned int *)(a1)), a4);
    goto loc_00AA3F64;
}
```

## 5. (Beta) C Style

```c
int64_t PopSleepstudyUlongFormatter(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = ExAllocatePool2(256, 20, (uint32_t)(0x444D5353ULL), a4);
    if (result != 0) goto loc_00AA3F75;
loc_00AA3F64:
    local_rsp = (local_rsp) + (32);
    return (uint32_t)(0xC000009AULL);
loc_00AA3F75:
    *(uint64_t *)(v_stack_p8 + 0x8) = (uint32_t)(0xC000009AULL);
    *(uint32_t *)(v_stack_p8) = 0x140000ULL;
    result = RtlUnicodeStringPrintf(v_stack_p8, v_rip + 363360, (uint32_t)(*(uint32_t *)(arg1)), a4);
    goto loc_00AA3F64;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x0` | `32` | `W` |
| `Arg2` | `+ 0x8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AA3F30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AA3F30[BB_00AA3F30]
  bb_00AA3F5F[BB_00AA3F5F]
  bb_00AA3F64[BB_00AA3F64]
  bb_00AA3F74[BB_00AA3F74]
  bb_00AA3F75[BB_00AA3F75]
  bb_00AA3F30 -->|branch| bb_00AA3F75
  bb_00AA3F30 -->|fallthrough| bb_00AA3F5F
  bb_00AA3F5F -->|flow| bb_00AA3F64
  bb_00AA3F74 -->|flow| bb_00AA3F75
  bb_00AA3F75 -->|branch| bb_00AA3F64
```
